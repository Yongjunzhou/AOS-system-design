# task-05：系统需求详细定义及产品架构定义

**对应场景**：01-waterfall · 第5步
**对应 AI 模板**：`03-aos-system-design-ai-support/01-waterfall-aos-system-design/workflow-prompts.md` 第5步

---

## 目标

合并功能和非功能分支，将 SysReq 5 级节点分解到 9 级场景活动，完成产品架构定义。

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 功能部分架构定义 | task-03 产出 |
| SysReq 非功能部分架构定义 | task-04 产出 |
| PA 骨架 | task-03 同步建立 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：架构定义验证 | AI | 覆盖度、一致性、追溯验证 |
| 2 | SysReq 功能部分 5→9 级分解 | AI | 逐级分解到 9 级场景活动 |
| 3 | 产品架构定义 | AI | 完善 PA 树形结构 + 详细定义 + 映射关系 |
| 4 | 结果审核 | 人类 | 审核 PA 组件划分和技术决策 |

## 人类审核要点

- [ ] PA 组件粒度是否合理
- [ ] 技术栈选择、接口定义等技术决策
- [ ] 产品架构分类体系选择（方法论/工具产品）

## 质量门禁

- [ ] SysReq 9 级场景活动完成分解
- [ ] PA 架构定义完整（架构定义 + 详细定义 + 映射关系表）
- [ ] 所有 SysReq 9 级已分配到 PA 组件
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 系统需求详细定义文档 | `10-aos-system-product-data/06-system-requirements-detailed.md` |
| 产品架构定义文档 | `10-aos-system-product-data/07-product-architecture.md` |
