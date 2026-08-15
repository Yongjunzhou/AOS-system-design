---
name: chunk-file-three-segment-dual-track
description: 切分文件 = frontmatter + 管理区 + 正文区三段；全链双轨状态模型（表A/B/C 外部 + 文档内嵌内部）
metadata:
  type: project
---

切分文件（.chunk-{seq}.md）= **frontmatter + 管理区 + 正文区**三段（2026-08-13 裁决方向 A，人类方案 §2.1.2/§5.2）。管理区放状态摘要表（阶段/AI建议/待处理/操作指引），frontmatter.status 记机器状态（**raw→annotated→clarified→normalized→abandoned**；2026-08-13 审视裁决：已规范化时由 ort03 确认执行写 `normalized`，方案期 `待确认规范方案` 保持 `clarified`，值域权威定义见 ort01 §2.2.2）。

**全链双轨状态模型**：OR 预处理链所有文档都双轨——外部轨道（状态文档表 A/B/C，管"流程推进到哪一步"，AI 入口判断 + 人类批量选材）+ 内部轨道（文档内嵌状态，管"被处理到什么程度"；文本化文档 = 管理区状态摘要表，切分文件 = frontmatter.status + 管理区表）。同步契约：先更新状态文档表（权威），再推导写内嵌状态。

**Why:** ort01 v2.0 重构曾把切分文件简化为 frontmatter+正文（丢管理区），但 ort02/ort03 仍按"有管理区"建（"切分文件管理区状态表"）——链上结构认知分裂，ort01 创建的片在 ort02 面前是残缺文档。2026-08-13 裁决回归三段（方向 A）。

**How to apply:** 涉及切分文件结构/状态时，以三段模型 + 双轨为准。「切分文档」在链上是既定术语 = 切分文件（.chunk-*.md），不是文本化文档；ort01 第二章按文档对象聚拢（§2.1/§2.2 文本化文档，§2.3/§2.4 切分文件）。
