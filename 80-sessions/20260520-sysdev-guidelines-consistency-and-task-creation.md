# 2026-05-20 设计决策与重构：Skill、任务目录、命名对齐

## 一、Check 脚本与 Skill 的关系

### 发现

`00-general/20-conformance-review-tools/` 下的 3 个 check 脚本（编号检查、链接检查、版本检查）与 `.claude/skills/conformance-review/SKILL.md` 存在协作关系：
- SKILL.md（AI 执行引擎）定义审查流程 Step 0~7
- `01-conformance-review.md`（人类参考的方法论文档+模板）内容和 SKILL.md 大量重叠
- 3 个 check 脚本（机械检查工具）被 SKILL.md 在 Step 2 中调用

### 决策

- check 脚本移入 `.claude/skills/conformance-review/scripts/`，作为 skill 的配件
- SKILL.md 中引用脚本的路径从 `00-general/20-conformance-review-tools/` 更新为 `.claude/skills/conformance-review/scripts/`
- `01-conformance-review.md` 的功能已被 SKILL.md 完整替代，删除该文件及空目录 `20-conformance-review-tools/`

### 讨论过程的发现

通过符号链接机制，skill 可跨项目复用：
- 中心仓库 `aos-skills/`（独立的 git 仓库）——存放所有 SKILL.md 及其配件
- 各项目创建符号链接到中心仓库
- 文件系统级操作，对 Claude Code 透明
- 适合多项目协作场景

同时讨论了 **`.claude/` 的归属**——它是项目级的配置目录，可进 git 版本控制，不是跨项目的独立实体。

## 二、01-conformance-review.md 的清理

### 发现

该文档包含三部分：核心方法论、审查模板、入口指引。方法论在 SKILL.md 中已有完整继承，模板由 AI 直接输出替代，只有"告知开发者有此功能"的信息需要保留。

### 决策

该文档删除，信息分置两处：
- 审查方法论 → SKILL.md（AI 执行用）
- 何时触发审查 → 06-tasks 任务文档的质量门禁中标注
- 该信息纳入对应的文档（如 06-tasks README 中注明）

**AI 何时知道要触发 conformance-review？**
在 CLAUDE.md 或任务定义中说明触发条件（如"完成某一设计步骤后，建议用户执行符合性审查"）。

## 三、03-ai-support 流水线内容的真实定位

### 发现

`10-pipeline-design/.../03-pipeline-system-design-ai-support/` 下的文档究竟是支持 AI 开发哪个产品的？

检查发现：
- `00-ai-document-requirements-understanding.md` 明确写"在开发运营体系开发之系统设计流水线这个产品的过程中"
- 各场景 README.md 声明"本目录下的文档是产品L的AI辅助文档模板构件"
- 但瀑布式和敏捷式的 `workflow-prompts.md` 中有误导性表述"AI在使用本模板为产品M生成设计文档时"

### 决策

- 这些文档是**产品L的通用模板构件**，支持 AI 开发 Pipeline（产品L）本身
- AOS 的 03-ai-support 是这些模板的实例层（定制版）
- 修正了瀑布式和敏捷式 workflow-prompts.md 中的"依据B说明"话术，改为明确模板定位

## 四、06-pipeline-system-design-tasks 创建

### 讨论背景

先确定几个前置问题：
1. **06-tasks 给谁用？** → 人类开发者（团队L）
2. **Pipeline 是否需要？** → 未来多人协作需要
3. **给 AOS 还是 Pipeline？** → Pipeline 需要，AOS 已有但为空占位
4. **与场景的关系？** → 决定了 06-tasks 的组织方式

### 开发场景确认

Pipeline 的开发经历三个阶段：
- **瀑布式（已走完）**：产品已具雏形，但未正式化
- **逆向工程（当前）**：从现有产物逆向推导五层设计文档，补充追溯链
- **敏捷式 + DevOps（后续）**：基线建立后，日常增量开发和紧急修复**并行**运行

### 任务清单

四种场景共 26 个任务文档：

| 场景 | 任务数 | 步骤 |
|------|--------|------|
| 01-waterfall-pipeline-system-design | 6 | 6步法 |
| 02-reverse-engineering-pipeline-system-design | 8 | 逆向8步 |
| 03-agile-pipeline-system-design | 8 | 敏捷8步 |
| 04-devops-pipeline-system-design | 4 | 3种模式 |

每个任务文档结构：目标 → 输入 → 操作流程 → 人类审核要点 → 质量门禁（含 conformance-review 触发）→ 产出

## 五、目录和文件命名统一

### 决策

采用**场景前置、`-pipeline-system-design`后缀**的统一命名模式：

| 变更项 | 旧名 | 新名 |
|--------|------|------|
| 01 目录内文件名 | `01-pipeline-system-design-standards.md` | `01-pipeline-design-standards.md` |
| 01 目录内文件名 | `07-pipeline-system-design-terminology-glossary.md` | `07-pipeline-terminology-glossary.md` |
| 02 目录名 | `02-pipeline-system-4modes-design-guidelines` | `02-pipeline-system-design-guidelines` |
| 03 子目录 | `01-pipeline-system-design-waterfall/` | `01-waterfall-pipeline-system-design/` |
| 03 子目录 | `02-pipeline-system-design-agile/` | `02-agile-pipeline-system-design/` |
| 03 子目录 | `03-pipeline-system-design-reverse-engineering/` | `03-reverse-engineering-pipeline-system-design/` |
| 03 子目录 | `04-pipeline-system-design-devops/` | `04-devops-pipeline-system-design/` |

所有内部引用（超链接、路径引用）同步更新。CLAUDE.md 中的目录树也一并更新（删除 20-conformance-review-tools、新增 06-tasks、更新 03 子目录名）。

## 六、Skill 跨项目复用方案（知识性记录）

### 整体结构

```
workspace/
├── AOS-system-design/                    ← git 仓库 1
│   └── .claude/skills/
│       └── conformance-review/           ← 符号链接
├── another-project/                      ← git 仓库 2
│   └── .claude/skills/
│       └── conformance-review/           ← 符号链接
└── aos-skills/                           ← git 仓库 3（独立远程仓库）
    └── conformance-review/
        ├── SKILL.md
        └── scripts/
```

### 关键要点

- `aos-skills/` 是独立的 git 仓库，有独立的远程仓库（如 `org/aos-skills.git`）
- 各项目通过 `ln -s` 将 `.claude/skills/conformance-review` 指向 `aos-skills/conformance-review`
- 升版时只需修改 `aos-skills/` 中的源文件 → git push → 各项目 pull 后符号链接自动生效
- 符号链接对 Claude Code 透明，skill 的自动扫描和注册正常工作
- VSCode 多根工作区可同时显示两个项目的 git 状态，各自独立操作
- 新成员入职流程：clone 项目 → clone aos-skills → 创建符号链接 → 就绪
- 适合 3 个以上项目共享 skill 的场景；少量项目用复制更省事

### 符号链接的本质

- 符号链接是一个文件系统层面的"路牌"文件，存的是目标路径字符串（几十字节）
- 对应用程序（Claude Code）完全透明，读写操作自动转发到真实文件
- 在 git 中存储为特殊类型（120000），内容是路径字符串
- 删除符号链接只删"路牌"，不影响真实文件
