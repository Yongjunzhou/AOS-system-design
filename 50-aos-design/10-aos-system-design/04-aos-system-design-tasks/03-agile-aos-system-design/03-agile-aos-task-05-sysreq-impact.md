# task-05：系统需求影响分析

**对应场景**：03-agile · 第5步
**对应 AI 模板**：`03-aos-system-design-ai-support/03-agile-aos-system-design/workflow-prompts.md` 第5步

---

## 目标

将 BA IPO 增量映射到系统需求，更新 SysReq 架构定义。

## 输入

| 输入 | 说明 |
|------|------|
| BA 增量定义 | task-04 产出 |
| 现有 SysReq 文档（基线） | 基线中的 SysReq 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | SysReq 影响分析 | AI | 判断新增 5 级节点 / 修改 / 淘汰 |
| 2 | SysReq 增量定义 | AI | 更新 0-9 级层级结构 |
| 3 | 更新映射关系表 | AI | BA → SysReq 映射 |
| 4 | 结果审核 | 人类 | 确认 SysReq 更新 |

## 人类审核要点

- [ ] SysReq 5 级节点调整决策
- [ ] 9 级分解粒度是否合理

## 质量门禁

- [ ] SysReq 增量定义完成
- [ ] 映射关系表已更新
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 SysReq 文档 | `10-aos-system-product-data/05-system-requirements-architecture.md` |
