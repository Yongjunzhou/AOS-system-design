"""语音转写：PyAV 解码 + 可插拔 ASR 后端 + 缺口质检补转。

后端：
- `mlx`            Apple Silicon 专用（mlx-whisper），最快。
- `faster-whisper` 跨平台（CTranslate2），Windows / Linux / Intel Mac 走这条；
                  有 NVIDIA 卡时用 `--device cuda --compute-type float16` 才快，
                   纯 CPU 建议 `int8`（实测 M1 CPU 上 large-v3 约 0.57x 实时）。

分块产物落盘（chunks/NNNNNN.json），中断后重跑会自动跳过已完成的块。
"""
from __future__ import annotations

import os

from .util import log, read_json, ts, write_json

SR = 16000
MLX_MODEL = "mlx-community/whisper-large-v3-mlx"
FW_MODEL = "large-v3"

_MODELS = {}   # faster-whisper 的模型对象缓存：构造一次就要几百秒，绝不能每块重建


def resolve_backend(name: str = "auto") -> str:
    if name and name != "auto":
        return name
    try:
        import mlx_whisper  # noqa: F401
        return "mlx"
    except Exception:
        pass
    try:
        import faster_whisper  # noqa: F401
        return "faster-whisper"
    except Exception:
        raise RuntimeError("既没有 mlx-whisper 也没有 faster-whisper，请先装一个（见 README）")


def default_model(backend: str) -> str:
    return MLX_MODEL if backend == "mlx" else FW_MODEL


def _get_fw_model(name: str, device: str, compute_type: str, threads: int):
    key = (name, device, compute_type, threads)
    if key not in _MODELS:
        from faster_whisper import WhisperModel
        log(f"[asr] 加载 faster-whisper 模型 {name}（device={device}, compute={compute_type}）")
        _MODELS[key] = WhisperModel(name, device=device, compute_type=compute_type,
                                    cpu_threads=threads or 0)
    return _MODELS[key]


def _np():
    import numpy as np
    return np


def decode(path: str, limit: float = 0.0):
    """解码为 16k 单声道 float32。用 PyAV 直接解码，不依赖 ffmpeg CLI。"""
    import av

    np = _np()
    log("[asr] 解码音频…")
    container = av.open(path)
    stream = container.streams.audio[0]
    resampler = av.audio.resampler.AudioResampler(format="fltp", layout="mono", rate=SR)
    frames = []
    for frame in container.decode(stream):
        if frame is None:
            continue
        for f in resampler.resample(frame):
            arr = f.to_ndarray()
            if arr.ndim == 2:
                arr = arr.mean(axis=0)
            frames.append(arr.astype(np.float32))
    container.close()
    audio = np.concatenate(frames) if frames else np.zeros(0, dtype=np.float32)
    if limit:
        audio = audio[: int(limit * SR)]
    log(f"[asr] 解码完成 {len(audio)/SR:.0f}s")
    return audio


def _transcribe_segment(seg, backend: str, model: str, device: str = "cpu",
                        compute_type: str = "int8", threads: int = 0):
    """转写单个音频块。

    刻意不传 initial_prompt：提示词会被当成正文吐进静音段，且并不能可靠带来标点。
    """
    if backend == "mlx":
        import mlx_whisper
        return mlx_whisper.transcribe(
            seg,
            path_or_hf_repo=model,
            language="zh",
            condition_on_previous_text=False,
            no_speech_threshold=0.65,
            temperature=(0.0, 0.2, 0.4, 0.6, 0.8),
        )["segments"], "mlx"

    m = _get_fw_model(model, device, compute_type, threads)
    segments, _info = m.transcribe(
        seg,
        language="zh",
        condition_on_previous_text=False,
        no_speech_threshold=0.65,
        temperature=[0.0, 0.2, 0.4, 0.6, 0.8],
    )
    return list(segments), "fw"


def _norm(result, kind: str, offset: float):
    if kind == "mlx":
        return [[round(offset + s["start"], 2), round(offset + s["end"], 2), s["text"].strip()]
                for s in result if s["text"].strip()]
    return [[round(offset + s.start, 2), round(offset + s.end, 2), s.text.strip()]
            for s in result if s.text.strip()]


def transcribe(audio, work: str, backend: str, model: str, chunk: float = 600.0,
               device: str = "cpu", compute_type: str = "int8", threads: int = 0,
               force: bool = False):
    """按 chunk 秒切块转写，逐块落盘。返回 [[start, end, text], ...]。"""
    chunk_dir = os.path.join(work, "chunks")
    os.makedirs(chunk_dir, exist_ok=True)
    total = len(audio) / SR
    starts = [float(s) for s in range(0, int(total), int(chunk))]
    log(f"[asr] 后端 {backend} / 模型 {model}；共 {ts(total)}，切 {len(starts)} 块（{chunk:.0f}s/块）")

    for i, pos in enumerate(starts, 1):
        path = os.path.join(chunk_dir, f"{int(pos):06d}.json")
        end = min(pos + chunk, total)
        if os.path.exists(path) and not force:
            log(f"[asr] 跳过 {i}/{len(starts)} {ts(pos)}–{ts(end)}（已有）")
            continue
        result, kind = _transcribe_segment(audio[int(pos * SR): int(end * SR)], backend,
                                           model, device, compute_type, threads)
        segs = _norm(result, kind, pos)
        write_json(path, segs)
        log(f"[asr] {i}/{len(starts)} {ts(pos)}–{ts(end)} → {len(segs)} 段")

    return merge_chunks(work)


def merge_chunks(work: str, fix: bool = True):
    """合并 chunks/ 与 fix/，fix 区间优先。"""
    segs = []
    chunk_dir = os.path.join(work, "chunks")
    for name in sorted(os.listdir(chunk_dir)):
        if name.endswith(".json"):
            segs.extend(read_json(os.path.join(chunk_dir, name), []))
    if fix:
        fix_dir = os.path.join(work, "fix")
        if os.path.isdir(fix_dir):
            for name in sorted(os.listdir(fix_dir)):
                if not name.endswith(".json"):
                    continue
                obj = read_json(os.path.join(fix_dir, name), {})
                a, b = obj["range"]
                segs = [s for s in segs if not (a <= s[0] < b)]
                segs.extend(obj["segments"])
    segs.sort(key=lambda x: x[0])
    return segs


def find_gaps(segments, gap_min: float = 45.0):
    """相邻片段间隔过大 → 疑似吞掉了内容。"""
    gaps = []
    for i in range(1, len(segments)):
        d = segments[i][0] - segments[i - 1][1]
        if d > gap_min:
            gaps.append((segments[i - 1][1], segments[i][0], d))
    return gaps


def repair_gaps(audio, work: str, backend: str, model: str, gap_min: float = 45.0,
                pad: float = 15.0, sub: float = 300.0, device: str = "cpu",
                compute_type: str = "int8", threads: int = 0, force: bool = False):
    """对所有 >gap_min 的缺口定点补转，结果写入 fix/。"""
    segs = merge_chunks(work, fix=False)
    gaps = find_gaps(segs, gap_min)
    log(f"[qc] 检出缺口 {len(gaps)} 处（阈值 {gap_min:.0f}s）")
    if not gaps:
        return merge_chunks(work)

    fix_dir = os.path.join(work, "fix")
    os.makedirs(fix_dir, exist_ok=True)
    total_s = len(audio) / SR
    for gs, ge, d in gaps:
        a, b = max(0.0, gs - pad), min(total_s, ge + pad)
        path = os.path.join(fix_dir, f"{int(a):06d}.json")
        if os.path.exists(path) and not force:
            log(f"[qc] 跳过 {ts(a)}–{ts(b)}（已有）")
            continue
        log(f"[qc] 补转 {ts(gs)}→{ts(ge)}（{d:.0f}s 缺口）")
        out, pos = [], a
        while pos < b:
            end = min(pos + sub, b)
            result, kind = _transcribe_segment(audio[int(pos * SR): int(end * SR)], backend,
                                               model, device, compute_type, threads)
            out.extend(_norm(result, kind, pos))
            pos = end
        write_json(path, {"range": [a, b], "gap": [gs, ge], "segments": out})
    return merge_chunks(work)
