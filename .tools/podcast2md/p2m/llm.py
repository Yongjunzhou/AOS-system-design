"""LLM 客户端：任意 OpenAI 兼容 /chat/completions 端点，只用标准库。"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

from .util import extract_json, log

DEFAULT_BASE_URL = "https://api.deepseek.com/v1"
DEFAULT_MODEL = "deepseek-chat"
KEY_ENVS = ("PODCAST2MD_API_KEY", "DEEPSEEK_API_KEY", "OPENAI_API_KEY")


def resolve_api_key(explicit: str | None = None) -> str:
    if explicit:
        return explicit
    for name in KEY_ENVS:
        v = os.environ.get(name)
        if v:
            return v.strip()
    raise RuntimeError(
        "没有找到 API key。请设置 PODCAST2MD_API_KEY（或 DEEPSEEK_API_KEY / OPENAI_API_KEY），"
        "或用 --api-key、--no-llm。"
    )


class LLM:
    def __init__(self, model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL,
                 api_key: str | None = None, timeout: int = 600, retries: int = 3):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = resolve_api_key(api_key)
        self.timeout = timeout
        self.retries = retries

    def chat(self, system: str, user: str, json_mode: bool = False,
             max_tokens: int = 8192, temperature: float = 0.3) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        body = json.dumps(payload).encode("utf-8")
        last = None
        for attempt in range(1, self.retries + 1):
            req = urllib.request.Request(
                f"{self.base_url}/chat/completions", data=body,
                headers={"Content-Type": "application/json",
                         "Authorization": f"Bearer {self.api_key}"})
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    data = json.loads(r.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
            except Exception as exc:  # 网络抖动 / 限流 / 超时
                last = exc
                log(f"[llm] 第 {attempt} 次调用失败：{exc}")
                if attempt < self.retries:
                    time.sleep(2 * attempt)
        raise RuntimeError(f"LLM 调用失败：{last}")

    def chat_json(self, system: str, user: str, **kw):
        return extract_json(self.chat(system, user, json_mode=True, **kw))
