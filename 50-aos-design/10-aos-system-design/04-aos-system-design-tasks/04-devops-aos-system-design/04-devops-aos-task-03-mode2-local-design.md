# task-03：模式2·局部设计

**对应场景**：04-devops · 第3步 · 模式2
**对应 AI 模板**：`03-aos-system-design-ai-support/04-devops-aos-system-design/workflow-prompts.md` 第3步（模式2部分）

---

## 目标

局部设计变更，影响 SysReq 和 PA 两层，1 天内完成。

## 适用条件

- 新增系统功能（影响 SysReq 和 PA）
- 非功能需求调整
- 不影响 SR/BA 层

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 定位受影响的 SysReq 节点 | AI | 从问题追踪到 SysReq 9 级节点 |
| 2 | SysReq 增量定义 | AI | 更新 9 级场景活动定义 |
| 3 | PA 增量定义 | AI | 更新相关 PA 组件的定义和映射 |
| 4 | 回归验证 | AI | 确保修改不影响其他功能 |
| 5 | 结果审核 | 人类 | 确认局部设计 |

## 人类审核要点

- [ ] SysReq 变更是否准确
- [ ] PA 定义是否同步更新
- [ ] 是否需要升级为模式3

## 质量门禁

- [ ] SysReq 增量定义完成
- [ ] PA 增量定义完成
- [ ] 回归验证通过
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 SysReq + PA 文档 | `10-aos-system-product-data/05`~`07` |
