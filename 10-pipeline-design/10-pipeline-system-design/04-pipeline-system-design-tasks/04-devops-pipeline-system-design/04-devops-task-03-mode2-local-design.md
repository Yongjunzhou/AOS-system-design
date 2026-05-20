# task-03：模式2·局部设计

**对应场景**：04-devops · 第3步 · 模式2
**对应 AI 模板**：`03-pipeline-system-design-ai-support/04-pipeline-system-design-devops/workflow-prompts.md` 第3步（模式2部分）

---

## 目标

涉及 SysReq + PA 层的局部设计变更，1 天内完成。

## 适用条件

- 系统功能 bug
- 小功能需求
- 系统性能优化
- 需要修改 SysReq 和 PA，但不涉及 SR/BA 层

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 定位受影响的 SysReq 和 PA 节点 | AI | 定位到具体的末级节点 |
| 2 | SysReq 增量定义 | AI | 更新 SysReq 定义和详细分解 |
| 3 | PA 增量定义 | AI | 更新 PA 组件定义 |
| 4 | 更新映射关系 | AI | SysReq → PA 映射 |
| 5 | 回归验证 | AI | 不影响其他功能 |
| 6 | 结果审核 | 人类 | 确认局部设计 |

## 人类审核要点

- [ ] 局部设计是否影响其他功能
- [ ] SysReq 修改的准确性
- [ ] 是否需要升级为模式3

## 质量门禁

- [ ] SysReq + PA 增量定义已更新
- [ ] 映射关系已更新
- [ ] 回归验证通过
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 SysReq 文档 | `10-pipeline-system-product-data/05-*.md` + `06-*.md` |
| 更新后的 PA 文档 | `10-pipeline-system-product-data/07-product-architecture.md` |
