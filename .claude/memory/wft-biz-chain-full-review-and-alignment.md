---
name: wft-biz-chain-full-review-and-alignment
description: 2026-06-28 业务链(wft01~05-biz)全链路一致性审查——三个空隙填补+入口/出口/Step3结构对齐完成
metadata:
  type: project
---

## 修改摘要

对 wft01→wft02→wft03→wft05 全业务链执行了全局一致性审查，包括三个空隙填补和三轮结构对齐。

### 已完成 — 三个空隙填补（commit 19c9fd8）

| 空隙 | 内容 | 涉及文件 |
|------|------|---------|
| 空隙1: 引擎判定准则 | wft02-biz 新增 wft01→wft02 引擎差异处理规则；补充按BA对象类型判定的具体流程；§一新增与上游wft01-biz衔接说明 | wft02-biz |
| 空隙2: 产出模板字段 | wft03-biz 流1/流2/流3产出清单模板补充支撑引擎和主CU能力类型标注；Step End新增分解总览 | wft03-biz |
| 空隙3: 映射失败追踪 | wft05-biz 新增PA映射状态四态(待映射/已映射/映射失败/待重试)；重入逻辑只处理失败条目 | wft05-biz |

### 已完成 — 入口/出口/Step3 结构对齐（commit 695e2ef）

- wft02-biz 第四层命名统一为"同次运行顺序约束"
- wft01-biz 新增OR条目状态检查（入口容错）
- wft05-biz Step End C选项"进入下游"→"进入下游开发线/配置线"
- wft01-biz Step End B选项「修改：…」→"局部修改"
- wft05-biz "到位粒度"从Step3末尾前移到设计姿态后

### 待办（明天到另一终端继续）

1. **wft01-biz 遗留**：v1.38 平台治理类角色识别口径已补完，但需确认治理对象类型在 wft02-biz 中的实际承接情况是否完整
2. **wft05-biz 知识重载**：另一终端可能没有本次对话的上下文，首次启动时先 `git pull` 获取全部变更，再加载任意一个最新文件即可
3. **91规范**：全Skill自闭环(v2.6)已完成，但映射表的wft03/wft05 biz行需要验证是否与最新文件一致

### 关键文档清单

| 文件 | 版本 | 定位 |
|------|------|------|
| eos-wft01-biz-or2str.md | v1.38 | OR→场景业务识别 |
| eos-wft02-biz-str2ba.md | v2.27 | STR-F→BA展开+引擎支撑判定 |
| eos-wft03-biz-ba2sr.md | v1.2 | BA→三流SR-F末级分解 |
| eos-wft05-biz-sr2pa.md | v3.2 | SR-F汇聚→配置单元需求 |
| eos-wft04-nfr-str2sr.md | v2.0 | STR-NFR→NFR量化约束(自闭环) |
| 91-doc-paired-skill-spec.md | v2.6 | 全Skill自闭环规范 |

### 业务链一句话定位

```
wft01: 需求方的业务期望是什么？
wft02: 这个场景在EOS上怎么运转？（+每个对象由哪个引擎支撑）
wft03: 系统必须提供哪些功能来支撑这个运转？（按引擎CU结构分解）
wft05: 这些功能配置哪些既有引擎CU来实现？（汇聚+规范化为配置需求）
```

### 记忆关联

- [[wft05-biz-engine-cu-requirement-redefinition]] — PA本质重定义
- [[wft04-nfr-self-closed-merge]] — 自闭环合并
- [[wft05-biz-eng-restructure-v2]] — 之前的四源分流重构
