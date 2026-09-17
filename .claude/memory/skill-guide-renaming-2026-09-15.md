---
name: skill-guide-renaming-2026-09-15
description: 2026-09-15 链级更名：「人类方案」→「SKILL 指南」（93 §1.4 定名；在用 590 处／86 文件；字段名 人类方案ID → SKILL 指南ID）
metadata:
  type: project
---

2026-09-15 人类定名：**「人类方案」改称「SKILL 指南」**。人类原话：「人类方案其实就是对应 SKILL 的指南」。

**定义**（落在 93 §1.4 术语表）：SKILL 指南 = EOS 设计线某任务位的操作规程文档，文件名形如 `eos-wftNN-xxx.md`；它是**该任务 SKILL 的权威源**，SKILL 由它提取。§1.4 同处写明与 91 附录A 第二部分「编写 Skill 文档」的分工——那一节讲 SKILL.md 自身怎么写，与本词不是一回事（两者字面易混，故就地划界）。

**改面（在用 590 处／86 文件）**：
- 15 个 SKILL.md，447 处——头部字段「设计依据 = SKILL 指南（权威源）」+ 正文；
- 93，35 处（含 §二 章名「SKILL 指南总骨架」）；
- 各文档本体（三试点／旧版 wft／ort 链），54 处；
- 91 + 01-pl4eos-spec + 00-doc-conventions + 04 数据文件，6 处；
- EOS 侧逆向／敏捷／DevOps 任务文档，20 处；元流水线侧（`10-pl4pleos`），28 处。
- 字段名 `**人类方案ID**` → `**SKILL 指南ID**`（约 40 个文件第 2 行）。

**不改**：`00-origin-requirement-materials/02-eos-sysdev-review.md`（存量评审材料，173 处）、`90-hold`（7 处）、`.claude/` 记忆正文（79 处）——记忆记的是当时状态，不机械改写。

**不做**：**文件不更名**（`eos-wftNN-xxx.md` 照旧，文件名里本无"人类方案"三字，改文件名是另一轮的事）；旧版 `wft0?-*.md` 不借机重写（退役规则：只作单向内容源）。

**版本**：93 v0.32、91 v5.61。

**类名同轮落定**：§2.1 由「每份 wft 类 SKILL 指南」改「每份**系统或构件设计类** SKILL 指南」（人类定）；93 其余 6 处 `wft 类`／`wft` 按人类指示**直接删去、不换类名**——§一 头注「wft 类操作规程」→「操作规程」、§1.2「EOS 设计线 wft 类」→「EOS 设计线」、§2.2「旧版 wft」→「旧版」、§4.1 理由段「91/wft 双写」→「与 91 的双写」、§4.2「并非 wft」→「并非」、§5.2 两处。**只留文件名 `eos-wftNN-xxx.md` 不动**（那是实际文件名，不是类名）。

**标书与文件名同轮改**（人类 2026-09-15 定）：
- 93 标题：`设计与开发落地方案编制规范（93 规范）` → **`设计与开发 SKILL 指南编制规范—93 号规范`**；英文副标题 `EOS Design-Development Landing Plan Authoring Spec` → `EOS Design-Development SKILL Guide Authoring Spec`。旧全称在整仓只此一处，别处一律引短称「93 规范」，故未牵动其他文档。
- 93 文件名：`93-eos-sysdev-landing-spec.md` → **`93-eos-skill-guide-spec.md`**（`git mv`）；引用只 2 个文档（biz01cr 3 处、biz03 2 处）+ 记忆 2 处，已全部跟改，无残留。
- 版本：93 **v0.33**。

关联 [[eos-design-landing-spec-93-refactor]]、[[feedback-changelog-concise]]。
