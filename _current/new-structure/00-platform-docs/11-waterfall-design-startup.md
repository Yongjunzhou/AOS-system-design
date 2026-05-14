# 新Session启动清单

**用途**：为新Session提供完整的文档加载清单，确保所有必需的文档都被加载到上下文中

**使用方式**：在新Session的第一条消息中说：
```
请按照 SESSION-STARTUP.md 加载所有文档
```

---

## 📋 必需文档清单

### 1. 项目指导文档
**文件**：`e:\mywork\AOS\CLAUDE.md`
**用途**：项目整体指导，包含四层映射模型、6个核心任务、9个AI Skill定义等
**加载优先级**：⭐⭐⭐ 最高

---

### 2. 系统设计准则
**文件**：`e:\mywork\AOS\_current\new-structure\00-platform-docs\01-design-standards\01-system-design-standards.md`
**用途**：系统设计的理论基础，包含5层结构、3个核心约束、质量指标
**加载优先级**：⭐⭐⭐ 最高

---

### 3. 设计指南（瀑布式）
**文件**：`e:\mywork\AOS\_current\new-structure\00-platform-docs\02-design-guidelines\01-waterfall-design-guide.md`
**用途**：完整系统设计的方法指南（30-48天流程）
**加载优先级**：⭐⭐⭐ 最高
**说明**：如果选择其他方法，替换为相应的指南文件

---

### 4. AI支持文档概览
**文件**：`e:\mywork\AOS\_current\new-structure\00-platform-docs\03-ai-support\README.md`
**用途**：AI支持文档的总体说明
**加载优先级**：⭐⭐ 高

---

### 5. 原始需求文档
**文件**：`e:\mywork\AOS\_current\new-structure\08-system-design-pipeline\01-original-requirements.md`
**用途**：系统设计流水线产品的原始需求（本次设计的起点）
**加载优先级**：⭐⭐⭐ 最高

---

## 🤖 AI支持文档（按需加载）

这些文档在执行具体任务时加载，不需要在Session启动时全部加载：

| 文档 | 位置 | 用途 | 何时加载 |
|------|------|------|--------|
| 业务模式库 | `07-shared-assets/patterns/business-patterns.md` | 业务模式识别和匹配 | 业务架构设计阶段 |
| 质量检查清单 | `07-shared-assets/quality-standards/quality-checklist.md` | 质量检查和验证 | 每个阶段完成后 |
| AI Skill定义 | `07-shared-assets/ai-skills/skill-definitions.md` | AI自动化处理规则 | 需要AI处理时 |
| 映射规则 | `07-shared-assets/mapping-rules/mapping-rules.md` | 映射验证和约束 | 映射设计阶段 |

---

## 📝 加载顺序建议

1. **第一步**：加载 CLAUDE.md（项目指导）
2. **第二步**：加载 01-system-design-standards.md（设计准则）
3. **第三步**：加载 01-waterfall-design-guide.md（设计指南）
4. **第四步**：加载 03-ai-support/README.md（AI支持概览）
5. **第五步**：加载 01-original-requirements.md（原始需求）

---

## 🎯 新Session的工作目标

基于这些文档，新Session的工作目标是：

**从原始需求分析开始，按照瀑布式设计指南，完成系统设计流水线产品的完整设计**

包括以下阶段：
1. 原始需求分析（3-5天）
2. 相关方需求架构设计（5-7天）
3. 业务架构设计（7-10天）
4. 系统需求设计（7-10天）
5. 产品架构设计（5-7天）
6. 端到端追溯分析（2-3天）

---

## ✅ 检查清单

在新Session启动前，确认：
- [ ] CLAUDE.md 已准备好
- [ ] 设计准则 v2.1 已准备好
- [ ] 瀑布式设计指南已准备好
- [ ] AI支持文档已准备好
- [ ] 原始需求文档已准备好
- [ ] 工作目录结构已创建（08-system-design-pipeline/）

---

**文档生成时间**：2026-05-14
**版本**：v1.0
**状态**：✅ 完成
