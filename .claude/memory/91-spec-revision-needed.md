---
name: 91-spec-revision-needed
description: 91-doc-paired-skill-spec.md 需根据 wft01a Step 3 修订同步更新
metadata: 
  node_type: memory
  type: project
  originSessionId: 83d2889b-87d7-4951-88b9-f7b9105378b0
---

wft01a Step 3 两轮深度修订完成后，91-doc-paired-skill-spec.md（文档结对设计 Skill 设计规范，v1.16）需要修订以下内容：

**1. 核心原则 #1（第55行）**：
   - 当前："Skill A 每次仅处理一个上游架构末级节点"
   - 问题：wft01a 现在一次处理同一角色的多条 OR（≤10 条），可能同时修订多个已有 STR 节点或新建多个 STR 节点
   - 建议：增加例外说明，或者将"一个节点"改为"一批同类 OR 条目（同角色）"

**2. 全链路映射 wft01 行（第101行）**：
   - 当前：wft01a 流程描述较概括，未反映 Phase A/B/C 结构
   - 建议：补充多 OR 积累收敛机制（Phase A 分组、Phase B 四关系检测+边界检查、Phase C 三步判断法+十链扫描）

**3. 端到端定义（第60行）**：
   - 当前："角色的端到端职责闭环"
   - 建议：补充用户-EOS 交互闭环视角，明确"OR 语义为终端边界"

**4. 增量标记扩展**：
   - 当前：五类标记（新增/改进/确认/矛盾/删除）
   - 问题：wft01a 现用八类标记（新增推断/边界扩展/跨场景）
   - 建议：91 规范引用八类标记，或说明不同 Skill 可按需扩展

**Why**：wft01a 是 91 规范的重要实例化实现，其 Step 3 的 Phase A/B/C 结构、多 OR 收敛机制、端到端约束等新设计应反馈到 91 规范中。
**How to apply**：下一轮工作时打开 91-doc-paired-skill-spec.md，逐条修订上述内容。
