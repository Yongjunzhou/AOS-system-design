---
name: progress-93-skill-guide
description: 进行中的工作：93 SKILL 指南编制规范与三份试点（abr／abp／cr）的真实进度、记忆落后的三处、以及编排类术语正名与路径名挂账
metadata: 
  node_type: memory
  type: progress
  originSessionId: d9d470f3-bb34-43d0-9c31-85ebd491b29e
  modified: 2026-09-22T13:50:01.357Z
---

# 进行中的工作：SKILL 指南规范（93）与三份试点

**当前状态**（2026-09-22 实查磁盘，非转述）：

| 对象 | 文件 | 实际版次 |
|------|------|---------|
| 93 SKILL 指南编制规范 | `93-eos-skill-guide-spec.md` | 第 **80** 版 |
| 试点一 相关方需求 → 职责视角业务流程概要 | `eos-biz01abr-stfr2rbpl.md` | 第 **99** 版 |
| 试点二 R 树 → P 树 | `eos-biz01abp-rbpl2pbpl.md` | 第 **36** 版 |
| 试点三 R 树 → 职责视角业务流程定义 | `eos-biz01cr-rbpl2rbpd.md` | 第 **13** 版 |

文件位置：`20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/`。最近一轮改动：abp **第 31~36 版**（第二~四章定点修订九条 ＋ 第四章「过程／规则」两次归位 ＋ 第五章按二三四章重写 ＋ 文档级E2E任务加「P 树归位记录」＋ 子块标题改名）与 abr **第 96~99 版**（第 96＝第四章按同一风格重构；第 97＝第五章对上 ch4 引规则名 ＋ 收 abr 自己的五条相抵；第 98＝表3-7 加 P 树归位记录；第 99＝子块标题改名），一次提交 `c32df554`；此前 `a7fab8c5`（abp 第 28~30 版：第五章重写、第四章各步提级、§4.5 整节删）、`98a64f45`（93 第 80 版：§2.4 第十二条「标题与引子写足限定」）、`e5deaac4`（删本目录 PDF 六份）；此前另有 `dceb4998`（目标表补全、§1.2 对齐、工位更名、复述清理）、`67686451`（链级术语正名"任务位 → 工位"）、`1e7ec407`（占位与合并、处理单位改批次、定位版式重排、表达风格全篇扫改）、`5e6ebf44`（占位节点机制落定 ＋ 表达规则三条 ＋ 阶段／环节正位）。

## 下一轮从哪继续

**版次以本表为唯一现状源。** 挂账文件里写的版次（`pending-biz01abr-ch5` 的「abr 第 88 版／93 第 74 版」、`pending-abr-cleanup-open` 的「93 第 75 版 ＋ abr 第 89 版」、`asset23-retired-and-perspective-renamed` 的「93 第 76 版／abr 第 90 版」）都是**当轮记录**，记的是那一轮改到哪一版，不是现状——**不改它们**（改了反而把当轮历史写错），已各自加「当轮」二字标明。查现状只读上表。

**`asset23-retired-and-perspective-renamed` 还写着"三处外围未落"**（`01-pl4eos-spec §2.6` 整节、`ort03` 的 23 匹配基准约 60 处、8 份 wft 指南旧名），是否已随手落掉要核。

**顺手核一条术语。** 这几处版次跳变与提交 `67686451`（"任务位 → 工位"）同时发生，说明**编排类术语又正了一轮名**；核对 `93` §2.4 规则七的词例与三份试点正文是否已全数换过，未换的按 `[[feedback-93-principles-over-terms]]` 的裁决依据（**以 91／94 里找不找得到为准**）处理。

## 待裁与阻塞

- **路径名 `subpl` 与 `subpd` 仍不一致**（见 `[[pending-subpd-subpl-naming]]`）：本目录实查为 `20-pl4eos/10-pl4eos-subpl-sysdev/`，而 `AGENTS.md`／`CLAUDE.md` 的目录结构与多份规范写的是 `subpd`。该挂账原记"磁盘与 git 只有 `subpl`、39 个文档写 `subpd`、135 处链接 404"，**两轮改动方向相反，是改到一半的中间态，证据冲突不能擅自扫**——定名后再统一。
- **`90-hold/` 与 `80-sessions/` 未被纳入本进度**：`80-sessions/` 停在 2026-05-30（7 份），是旧"按会话存档"的做法，本轮起由 `progress-*` 取代；是否清理旧档待人类定。

## 本轮改动的文件与提交号

本轮**未改动**上述任何一份 SKILL 指南或 93 规范；本文件只做状态记录。改动仅限记忆与规程：`AGENTS.md`、`CLAUDE.md` §八、新增 `progress-*` 两份、`MEMORY.md` 索引。

## 关联记忆

[[pending-biz01abr-ch5]]、[[pending-abr-cleanup-open]]、[[pending-biz01abp-revision]]、[[pending-biz01abp-rewrite]]、[[asset23-retired-and-perspective-renamed]]、[[feedback-93-principles-over-terms]]、[[feedback-abr-only-scope]]、[[pending-subpd-subpl-naming]]、[[progress-dsh-memory-mechanism]]。
