---
name: feedback-claude-role
description: CLAUDE.md 文件定位：仅包含项目导航和文件引用，不包含方法论摘要
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7106660b-eaf8-4d11-b833-2ac34ea08ad4
---

CLAUDE.md 的职责限定为项目上下文导航——目录结构说明、关键文件引用、工作约定。不应包含系统设计方法论内容的摘要或复述（如四原则、五层链路、设计活动、六步法），这些内容的完整定义在通用设计准则 v2.4 中。

**Why:** 复述引出一致性风险——准则更新后 CLAUDE.md 的摘要未同步即产生矛盾，本次会话中的多次修正（指标分解描述、N:1 范围、六步法层级、缺失的术语概念、不应存在的独立小节）均由此产生。

**How to apply:** 需要引用方法论时，在 CLAUDE.md 中只放指向通用设计准则的链接（如 `[通用设计准则 v2.4](path)`）即可。不展开、不摘要、不复述。
