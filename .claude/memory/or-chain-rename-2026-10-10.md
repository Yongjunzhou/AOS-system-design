---
name: or-chain-rename-2026-10-10
description: 2026-10-10：or 链四份指南文件名复原（or00-textualize／or01-chunk／or02-clarify／or03-norm）、头注版本续旧档（创建 2026-06-07、版本号＝旧版数＋新版数）、prose 昵称 ortNN 全链统一为 orNN
metadata:
  type: project
---

**2026-10-10**，人类令「对 or01 到 03 的四个 skill 指南的文件名及其版本历史进行修订」，并逐项裁定（四份／前缀 `or`／版本号两数相加）。

## 一、文件名复原（前缀留 `or`，动词复原为旧档名）

| 旧（五章重写后） | 新 |
|---|---|
| `eos-or00-x2md` | `eos-or00-textualize` |
| `eos-or01-x2docbiz` | `eos-or01-chunk` |
| `eos-or02-x2vv` | `eos-or02-clarify` |
| `eos-or03-x2norm` | `eos-or03-norm` |

目录＋`.md`＋`SKILL.md`（frontmatter `name`／标题／`SKILL 指南ID`／设计依据链接）三件套同改；跨文件引用（`00-presysdev-4-eos/README.md`、94 §2.0.1、91 §A.5、`01-pl4eos-spec`、状态文档、`01-eos-specified-requirements`、`agile-t01`）同轮落。前缀取 `or` 不取旧 `ort`——链已统一 `or`。

## 二、版本历史续旧档

头注改「创建 2026-06-07｜版本 第 N 版」，N＝旧档末版数＋五章重写后版数：textualize 37+1=38／chunk 63+1=64／clarify 40+2=42／norm 68+1=69。旧四档同出于 2026-06-07（提交 `d089563a`「预处理链三区模型重构：6 个旧 skill→4 个新 eos-ort skill」）。

## 三、prose 昵称 `ortNN` 全链统一为 `orNN`

人类裁「**全部改**」，清偿 [[pending-or01-chain-followups]] 第 7 项。落在 25 个现行文件（`01-pl4eos-spec` §2.6/§15、`91`、`00-doc-conventions` §12、wft 各 Skill、数据文件 21/22/25、`.scripts/ai-commit.sh` 等）；ASCII 图（§2.6.2／§2.6.4、§15.6、22 号资产图）按新名重对齐。裸 `ort`（无数字，如「ort 预处理链」）一并改 `or`；11 份 `ort*` 记忆文件名／slug 一并改 `or*`，正文同扫（唯「旧名→新名」的沿革句保留原名，以免自相矛盾）。

## 四、连带的旧口径

- `02-eos-sysdev-review.md`（登记簿）历史行的 `eos-ort0X-*` 改名——人类裁「全部改」，**推翻其原「存量评审材料不改」的规矩**（[[pending-or01-chain-followups]] 原第 5 项）。其 `subpd` 路径未动（另属 [[pending-subpd-subpl-naming]]）。
- 记忆：11 份 `ort*` 文件名／slug 改 `or*`（`or-review-style-pattern`、`or01-chunk-align-scene-business` 等），三份 rewrite 记忆名同复原（`or01-chunk-rewrite` 等）＋正文扫名——沿革句保留原名。

**Why:** 五章重写（9-30／10-08／10-09）时把文件名与版本历史都从旧档切断了，且 `x2YYY` 式名与 `ortNN` 昵称是同一场改名的两面；本轮回补。

**How to apply:** 引用本链四步一律写 `eos-or0N-<动词>`（textualize／chunk／clarify／norm），不写 `x2YYY`，也不写 `ortNN`。相关：[[or00-textualize-rewrite]]、[[or01-chunk-rewrite]]、[[or02-clarify-rewrite]]、[[or-chain-or03-rewrite-and-status-model]]。
