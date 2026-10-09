---
name: pending-or-chain-batch2-migration
description: 挂账 2026-10-09：or 链本轮只落到 or00~or03＋状态文档＋README；下游 wft 指南/SKILL、脚本、91 §A.1 仍停在旧布局，且 91 §11.1 与 §A.1 自相抵，待批 2 收
metadata:
  type: project
---

**挂账（2026-10-09）**：原始需求处理链逻辑收口，本轮只落 **or00~or03 自身 ＋ 状态文档 ＋ README**（提交 `8631136f`，两仓已推）。以下属**批 2**，未动：

1. **下游 wft 全批仍停在最老一代布局**（`## AI可以处理节点` ＋ `## AI最近变更`）：wft01~wf05 的 10 份指南/SKILL、`comformed-2-91spec/`、`eos-biz01abr-stfr2rbpl.md`，以及脚本 [`read-section.sh`](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/scripts/read-section.sh)（按 `## AI最近变更` 定位分节）／[`update-meta.sh`](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/scripts/update-meta.sh)（在 `AI可以处理节点` 中移动节点条目）。
2. **91 自身未收口**：§11.1 明写「不另设状态与处理队列区、也不设 `## AI可以处理节点` 节」，附录 §A.1 R1 又要求「必须先读 AI可以处理节点」——**自相抵**。
3. **91 旧名未扫**：`ort00~ort03`、`eos-ort03-norm`（§七/§十/§A 多处）；链已统一 `or`、`eos-or03-x2norm`。
4. **01 数据文件已按 §十四 重建**（`0.4 全景层——条目行表`，无独立队列区），是本批迁移的**目标形态**；or03 指南本轮已跟上，02/03/05 停在中间代（`## 1. 状态与处理队列`），其余未跟。
5. **改名的残留（勿误改）**：`业务输出文档` 在 02／24／25 数据文件与旧 wft 里是**「文档物」义**——新口径是「节点名 `文档级任务`、其产出的那份文档即 `业务输出文档`」（94 §2.1.1 的别称注），故**保留不动**；旧 wft 里的节点义随退役消失。改名已落活链（`or00~or03`＋README＋94＋91＋01 数据文件，提交 `a913d92e`）。

**第二批已收（不在批 2）**：or03↔biz01abr 的**退回通道**（`待退回重切` 落状态文档表 B `处置标记`，91 §11.7 加需求侧一族）与**承接记录体例**（or03 §3.3＋biz01abr）——均随 `a913d92e` 落。

**判据**：这批是「依据文档与下游读者落后于链」的**同步缺口**，判对错不依赖「谁是权威」；见 [[feedback-work-style]] 2026-10-09。启动须人类点头。

关联 [[channel-single-track-ruling]]、[[eos-design-landing-spec-93-refactor]]、[[feedback-work-style]]。
