---
name: nfr-chain-deep-review-round1
description: NFR 链深审第一轮已完成（2026-08-22，7 项发现全修复未提交）——SKILL 版本错位（wft01/wft04 落后 v5.7、wft06 落后 v3.5）+ 02/05 数据模板重写 + 22 契约更新
metadata:
  node_type: memory
  type: project
  modified: 2026-08-22
---

**NFR 链深审第一轮（2026-08-22）已执行并修复**。审视范围：wft01-nfr/wft04-nfr 人类方案（v5.7）+ SKILL（v1.4）+ 22 资产（v1.2）+ 11 约束包（v1.0）+ 91 规范（v5.36）+ 下游 wft05-eng（v10.5/v1.8）+ wft06（v3.5/v1.0）+ 02/05 数据模板。

**发现 7 项并全部修复（F1~F7）**：

- **F1 wft01-nfr SKILL 未同步 v5.7（M6 归组锚点）**：附录A.1 适用对象线索仍含页面类型/具体页面 ID（与附录A.5 五种对象自相矛盾）→ 收敛回五种对象 + 页面降适用范围备注
- **F2 wft04-nfr SKILL 未同步 v5.7（NFR 分解设计）**：无分解规则/分解子指标独立装配/消费状态回写 → Step 3 Phase C 补分解、Step 4 补独立装配+单写者、Step 6 补消费状态回写、附录A.9 新增分解判据
- **F3 wft06 SKILL v1.0 落后 v3.5**：无守恒核对/消费状态回写核对/三可/追溯态推进模型 → 全量同步 v3.4+v3.5（eng 链两层、PA/SysReq-NFR 追溯态、加载清单补 10/11+23、矩阵列补 FR-BIZ指标行ID/承接组件/消费版本）
- **F4 02 STR-NFR-TEMPLATE 是 STR-F 模板复制**：含「量化指标/测量方法」（wft01 不产量化指标，错位）→ 按 wft01-nfr §2.1.2 重写（22 分类路径/需求清单/适用对象/完备性/变更声明）
- **F5 05 SysReq-NFR-TEMPLATE 旧术语 SR-NF** → 按 wft04-nfr §2.1 重写 + 修 4 处 SR-NF 陈旧引用（索引 108/读取说明 124/模板 178/追溯 198）
- **F6 22 §6.3 迁移期契约陈旧**：Step 6 汇聚→Step 5 写回（删「从 STR-NFR 节点量化指标」错位）、阶段一/三→Step 1/3/6、SR-NFR→SysReq-NFR、落账补 06；22 升 v1.3
- **F7 wft01-nfr SKILL 输入校验表缺「边界混杂」行 + 硬退出/软提示标注** → 补齐对齐人类方案 §3.1.1

**涉及版本**：wft01-nfr SKILL v1.4→v1.5、wft04-nfr SKILL v1.4→v1.5、wft06 SKILL v1.0→v1.1、22 v1.2→v1.3、02/05 模板重写（数据文件不 bump 版本，模板为 AI 写节点参照）。

**挂账/下轮**：
- 修复未提交 git（待人类审阅后提交）
- 22 §3.2 契约摘要「STR/SR-NFR」→「STR-NFR」顺带修正
- 21 角色资产「wft01」引用为旧泛称（未区分 biz/eng/nfr），非 NFR 链阻塞，留待角色资产专项清理
- NFR 链无真实 STR-NFR/SysReq-NFR 节点（仅 OR-008 一个 NFR 型 OR + 模板块），模板重写后 AI 写节点时验证模板可用性
