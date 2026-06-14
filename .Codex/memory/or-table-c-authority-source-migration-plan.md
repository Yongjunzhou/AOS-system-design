---
name: or-table-c-authority-source-migration-plan
description: OR 基线表C权威源反转的待办决策，记录目标方向、理由和迁移影响范围
metadata:
  type: project-todo
---

# OR 表C权威源反转计划

## 当前结论

暂不在本轮执行 OR 表C 权威源反转。

当前实现继续保持：
- `01-eos-sysdev-status.md` 中的表C为当前权威源
- `01-eos-original-requirements.md` 中的表C为同步/派生视图

## 拟定目标

后续择机统一反转为：
- `01-eos-original-requirements.md` 内嵌表C为权威源
- `01-eos-sysdev-status.md` 中的表C改为集中查阅/汇总视图

## 反转理由

1. 表C与表D在方法论上同属“对象本体上的交接状态表”。
2. OR 条目正文、反馈、分析建议都位于 `01-eos-original-requirements.md`。
3. `ort03`、`wft01`、`wft06` 在消费表C时，不只读取状态，也依赖 OR 条目本体内容。
4. 统一为“状态跟着对象走，状态文档做汇总视图”后，OR / STR / BA / SysReq / PA 的规则会更一致。

## 本轮不执行的原因

当前剩余可用上下文/用量不足，不适合执行“权威源迁移”这类高影响改造，避免出现“两边都像权威源”的过渡状态。

## 后续迁移影响范围

后续正式迁移时，至少需要一并检查和修改：

- `20-pl4eos/80-pl4eos-2-eosdata/00-origin-requirement-materials/01-eos-sysdev-status.md`
- `20-pl4eos/80-pl4eos-2-eosdata/01-eos-original-requirements.md`
- `20-pl4eos/10-pl4eos-subpl-sysdev/00-presysdev-4-eos/eos-ort03-norm.md`
- `20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft01-or2str.md`
- `20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft06-trace.md`
- 上层规范与本仓库记忆文件中关于表C权威源的表述

## 迁移执行原则

1. 不做局部单点改动，必须按“权威源声明 + 同步契约 + 读写顺序 + skill 文档 + 复扫”整体迁移。
2. 完成迁移后，必须明确标注：
   - OR 文档内嵌表C：权威源
   - 状态文档表C：派生视图，不直接编辑
3. 迁移完成后需做一次仓库级残留词与同步契约复扫。
