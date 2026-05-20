# task-04：业务架构逆向推导

**对应场景**：02-reverse-engineering · 第4步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第4步
**对应设计指南**：[AOS 逆向工程系统设计指南 第4步](../../02-aos-system-design-guidelines/02-reverse-engineering-aos-system-design-guide.md#第4步业务架构反向推导)

---

## 目标

从 SysReq 反向推导业务架构 IPO，建立 BA 定义。

## 上下文继承

```
来源：第3步产出
产出：BA IPO 定义（含 SysReq→BA 追溯映射表）
```

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 架构定义 | task-03 产出 |
| 现有业务描述文档 | 仓库中已有的业务过程描述 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：SysReq→BA 追溯验证 | 人类+AI | 两类分析：(1) SysReq→BA 映射完整性分析——验证每个 SysReq 场景活动是否对应到至少一个 BA IPO；(2) BA 语义合理性分析——评估反向推导的 BA IPO 是否符合业务实际 |
| 2 | 同步建立相关方需求骨架 | AI | 在推导 BA IPO 的同时，标记各业务活动所服务的相关方角色，为后续 SR 反向推导建立骨架 |
| 3 | IPO 定义推导 | AI | 为每个 IPO 推导 I/P/O 定义 |
| 4 | 去重处理 | AI | 识别推导结果中的重复 IPO |
| 5 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] BA IPO 的业务语义是否正确
- [ ] SysReq → BA 的推导逻辑是否合理
- [ ] 是否有遗漏的业务过程
- [ ] 同步建立的相关方需求骨架是否合理——相关方角色划分能否支撑后续 SR 反向推导
- [ ] BA IPO 去重后是否还有语义相近但实际不同的业务活动被错误合并

## 质量门禁

- [ ] BA IPO 定义完整（I/P/O）
- [ ] SysReq → BA 映射关系建立且无单向断链
- [ ] 相关方需求骨架已同步建立
- [ ] BA IPO 去重完成，无重复项
- [ ] 运行 conformance-review 进行符合性审查
- [ ] 已按审查修复流程处理发现的问题

## 产出

| 文件 | 说明 |
|------|------|
| 业务架构定义文档 | `10-aos-system-product-data/04-business-architecture.md` |
