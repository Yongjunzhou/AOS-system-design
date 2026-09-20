# podcast2md

播客音频 → 整合版 Markdown 文稿。一条命令跑完：

```
取源 → 下载 → 本地转写 → 缺口质检补转 → 补标点 → LLM 摘要 + 专有名词校正 → 组装 md/srt
```

产出的文稿体例与 `100-subprojects/05-投资工程研究/00-投资工程研究报告/` 下的既有材料一致：元信息表＋说明注＋目录＋第一部分要点摘要（一句话主旨／时间轴／核心观点／术语校正清单／值得记住的一段）＋第二部分完整逐字稿。

## 环境

Python ≥ 3.10。**转写后端按平台自动选**，装好依赖直接跑即可：

```bash
python3 -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` 里带了平台标记：Apple Silicon 装 `mlx-whisper`，其余平台装
`faster-whisper`。PyTorch 只在标点恢复这一步用得到，CPU 机器建议装 CPU 版省几个 GB：

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

模型下载走 HuggingFace；**官方域名在部分网络下不可达，用镜像**（Windows 用 `set` 代替 `export`）：

```bash
export HF_ENDPOINT=https://hf-mirror.com      # Windows: set HF_ENDPOINT=https://hf-mirror.com
```

首次运行会下载转写模型（large-v3 约 3 GB）与标点恢复模型（约 400 MB），之后走缓存。

## 跨平台

整条流水线是**纯 Python**——没有 subprocess、没有 shell 调用、没有平台专属命令，所以除转写引擎外都可以直接移植。实测（样本：154 分钟中文播客，`large-v3`，int8）：

| 平台 / 后端 | 相对速度 | 该期耗时 | 说明 |
|---|---|---|---|
| macOS + Apple Silicon，`mlx` | 1.93x 实时 | ~1.3 小时 | 最快，走 GPU |
| Windows / Linux + NVIDIA，`faster-whisper` + `cuda`/`float16` | 约 3~6x 实时 | ~0.5 小时 | 有独显时比 Mac 还快 |
| **Windows / Linux 纯 CPU，`faster-whisper` + `int8`** | **0.57x 实时** | **~4.5 小时** | 慢，但能跑完 |
| 同上但用 `small` 模型 | 2.27x 实时 | ~1.1 小时 | 快 4 倍，专有名词准确率明显下降 |

结论：**有没有 NVIDIA 独显，决定 Windows 上是半小时还是四个半小时**。没有独显时，要么接受 `large-v3` 跑一晚，要么退到 `small`／`medium`（代价是这本流水线最看重的专有名词更容易错）。

各环节的平台情况：

| 环节 | Apple Silicon | Windows x86 | Windows on ARM |
|---|---|---|---|
| `fetch` / `llm` / `enrich` / `compose` / `util` | ✅ | ✅ | ✅ |
| 标点恢复（CPU torch） | ✅ | ✅ | ⚠️ torch 轮子少 |
| 转写（`mlx`） | ✅ | ❌ | ❌ |
| 转写（`faster-whisper`） | ➖ | ✅ | ⚠️ CTranslate2 轮子少 |

**ARM 版 Windows（如部分信创机型）要小心**：PyTorch 与 CTranslate2 的 Windows-ARM64 轮子都不齐，这套栈可能装不起来。这种情况下更实际的分工是——转写在别的机器上做，只把后面几步（标点／摘要／组装）拿过来跑。

已经处理掉的 Windows 细节：日志输出强制 UTF-8（否则重定向到文件时中文与「—／≥」会抛 `UnicodeEncodeError`）；文件名过滤 `\ / : * ? " < > |` 并挡掉结尾的点／空格与 `CON`、`NUL` 这类保留名。仍需留意：Windows 传统路径长度上限 260 字符，仓库路径别放太深。

**转写在别的机器、后处理在这台机器**是可行的：中间产物按阶段落盘在同一 `--work` 目录，把它拷过去即可接着跑，已完成的阶段会自动跳过。

## 用法

```bash
export PODCAST2MD_API_KEY=sk-xxxx          # 摘要与校正需要；也可用 --api-key

python podcast2md.py "https://www.xiaoyuzhoufm.com/episode/xxxxxxxx" -o 输出目录
python podcast2md.py ./local.m4a -o 输出目录            # 也支持本地音频
python podcast2md.py <链接> -o 目录 --no-llm            # 只要逐字稿，不调 LLM
python podcast2md.py <链接> -o 目录 --limit 600         # 只处理前 10 分钟，调试用
```

产物：`<输出目录>/<NN>-<播客简称><期号>-<话题>.md` 与同名 `.srt`。编号 `NN-` 自动取该目录里下一个空位（已有 `00-`、`01-` 就出 `02-`），可用 `--num` / `--name` 覆盖。

### 主要参数

| 参数 | 说明 |
|---|---|
| `-o/--outdir` | 输出目录（默认当前目录） |
| `-w/--work` | 中间产物目录（默认 `<outdir>/.podcast2md/<slug>`） |
| `--limit N` | 只处理前 N 秒 |
| `--asr-backend` | `auto`（默认，按平台）／`mlx`／`faster-whisper` |
| `--asr-model` | 模型名；Apple Silicon 默认 `mlx-community/whisper-large-v3-mlx`，其余默认 `large-v3` |
| `--device` / `--compute-type` / `--threads` | faster-whisper 专用；CPU 用 `cpu`+`int8`，NVIDIA 用 `cuda`+`float16` |
| `--chunk N` | 转写分块秒数，默认 600 |
| `--gap-min N` | 判定"吞内容"的片段间隔阈值，默认 45 秒 |
| `--no-repair` | 跳过缺口补转 |
| `--no-llm` | 跳过摘要与校正 |
| `--no-verify` | 跳过校正表的 LLM 上下文复核 |
| `--model` / `--base-url` / `--api-key` | LLM 配置，默认 `deepseek-chat` @ `https://api.deepseek.com/v1` |
| `--window-chars N` | 分段理解的字数窗口，默认 6000 |
| `--corrections F.json` | 额外校正表 `{"识别":"应为"}`，人工补充用 |
| `--host` / `--guest` | 覆盖元信息里自动推断的主播／嘉宾 |
| `--num` / `--name` | 覆盖输出编号／文件名主干 |
| `--force` | 忽略中间产物，全部重跑 |

## 中间产物与续跑

每个阶段都落盘，重跑同一 `--work` 会跳过已完成的块，中断可续：

```
<work>/meta.json            单集元信息
<work>/audio.m4a            音频原件
<work>/chunks/NNNNNN.json   转写分块（按起始秒命名）
<work>/fix/*.json           缺口补转结果
<work>/segments_punct.json  补标点后的片段
<work>/llm_windows.json     分段理解结果（要点 + 校正候选）
<work>/llm_summary.json     汇总后的要点摘要
```

`--force` 才会重算；只换 LLM 的话删掉 `llm_windows.json` 即可。

## 哪些是代码，哪些靠 LLM

**确定性代码**：取源下载、转写、缺口检测与补转、补标点、规则清理、校正表套用、组装 md/srt。这部分给定输入必然得到同样结果。

**LLM（`--no-llm` 可关）**：
1. **分段理解**（map）——逐窗读稿，产出该段时间点要点，并指出可疑的专有名词误识别。提示词里会带上从标题与节目信息推出的真实人名（主播／嘉宾），否则容易漏掉「小骏→小珺」这类同音错写。
2. **校正复核**（verify）——把每条候选连同它在稿中的真实上下文再交给模型判一次（确认／驳回／改正）。分段理解与复核两步都会拿到从标题与节目信息推出的**权威人名**——复核若不知道「主持人叫张小珺」，就会因为"稿中查不到正确写法"而否掉「小骏→小珺」这类只能靠节目信息确认的修正。
3. **汇总**（reduce）——把分段要点合成一句话主旨／时间轴／核心观点／值得记住的一段。

顺序上**先定校正表，再把校正回灌进分段要点，最后汇总**。否则摘要会基于未校正的文本生成，出现正文写「曾鸣」而摘要写「曾敏」的割裂。

校正候选要过三道闸才落地：识别串必须在原文真实出现、同一错串在不同窗口给出冲突答案则拒绝、出现次数超过 30 次的疑似常见词一律拒绝（避免把「成绩」这类语境词全局替换坏掉）。被拒条目会打在日志里。

**verify 这一步不是装饰**。实测中 map 阶段把「红历史」猜成「人类历史」，而稿中同一句在片头预告里出现过正确写法「从历史」；复核环节带着上下文重判，才把它改对。**LLM 产出的摘要与校正仍建议人工过一遍**——脚本只能保证不越界，保证不了判断正确。

## 几个已经踩过的坑

- **不要给 Whisper 传 `initial_prompt`**：提示词文字会被当成正文吐在静音段（表现为整段样板幻觉），且并不能可靠带来标点。代码里刻意不传。
- **Whisper 可能整篇不出标点**：本仓库实测某期 154 分钟全稿只有 3 处标点，加提示词也只到约 1 处/110 字。故外挂标点恢复模型 `p208p2002/zh-wiki-punctuation-restore`，再用规则清掉两类误标——夹在拉丁字母/数字之间的标点（`C，EO`、`2.8。T`）、虚词后不可能断句的逗号。**换后端也逃不掉这一步**：`faster-whisper` 在同样音频上同样一个标点都不出。
- **繁体输出**：`language="zh"` 并不保证简体。实测同一段音频 MLX `large-v3` 出简体，`faster-whisper` `small` 整段出繁体，所以无脑过一道 `opencc t2s`。
- **分块会丢内容**：按时间戳查相邻片段间隔，超过 `--gap-min` 的区间定点补转。
- **片头预告会造成"复读"假象**：很多播客片头是金句剪辑，与正文逐字重合，全文查重复会误报，不是识别故障。

## 实测

以 `100-subprojects/05-投资工程研究/00-投资工程研究报告/01-张小珺商业访谈录153-和曾鸣聊产业史观.md` 那一期（154 分钟）为样本：

| 环节 | 结果 |
|---|---|
| 转写（16 块，600s/块） | 79.8 分钟，约 1.9x 实时，4639 段 |
| 缺口质检 | 0 处（阈值 45s） |
| 补标点 | 标点密度约 10 字/处，全角 |
| LLM 分段理解 | 8 窗，280 条分段要点 |
| 分层压缩 | 280 → 61 条（两轮） |
| 校正表 | 123 词条落地；拒绝 3 条（拿不准） |
| 纯 LLM 阶段耗时 | 约 2 分 16 秒（转写走缓存） |
| 正文与人工整理稿对照 | 346 段、相似度 99.67% |

机器跑出的校正表里出现了人工整理时漏掉的条目（例如 `路口→入口` 全稿 10 处），也有判断分歧的条目（人工作 `垂垒→垂类`，机器作 `垂垒→垂直`）。这说明两件事：**机器更适合穷举，人更适合裁决**。

## 局限

- 转写是 GPU 重活：2.5 小时音频约 80 分钟（约 1.9x 实时），只能后台跑，快不了。
- 中间产物含整段音频与分块 JSON，体积可观；输出目录若在仓库内，建议给 `--work` 指到仓库外，或把 `.podcast2md/` 加进 ignore。
- 目前只支持小宇宙单集页与本地音频；Apple Podcasts 等其它源需另加 `fetch` 分支。
- 摘要质量取决于所用模型；换模型用 `--model` / `--base-url`，任何 OpenAI 兼容端点均可。
- 校正的 verify 环节偏保守（宁可放过也不改错），会拒掉一些本可成立的候选；被拒条目会打在日志里，可用 `--corrections` 手工补回。
