---
name: preprocessing-chain-unified-model
description: 预处理链统一模型 - 不切分统一 + chunk→sub 重命名 + clarify 合并已完成
metadata:
  type: project
---

# 预处理链统一模型

## 已完成的变更

### 第一批（2026-06-06，ort01-ort02 合并到 master）
- **不切分统一**：不切分文档在 ort01 中输出单一切分文件（total=1），不再被跳过
- **生命周期新增"已切分"**：原始文档行在 ort01 后标记为"已切分"，不再被 ort02 匹配
- **ort02 扫描简化**：统一处理所有 `-sub-*.md` 文件，不再区分来源

### 第二批（2026-06-06，本会话完成）
#### 变更一：`-chunk-` → `-sub-` 重命名
输出切分文件命名模式从 `{file}-chunk-{seq}.md` 改为 `{file}-sub-{seq}.md`。涉及 ort01~ort04 及登记表中的命名规则、示例、质检项等约 30 处文本替换。Skill ID（`ort01-chunk-execute` 等）和字段名（`chunk_batch`/`chunk_label`）保持不变。

#### 变更二：`-clarified.md` 合并到 sub 文件
消除衍生标注文件，标注记录直接写入切分文件自身：
- sub 文件 YAML frontmatter 追加 `status` 字段（raw → annotated → clarified）
- ort01：frontmatter 模板追加 `status: raw`
- ort02：不再创建 `-clarified.md`，改为在 sub 文件末尾追加 `## 模糊标注记录` 区块，更新 status→annotated；扫描条件从文件存在性改为检查 `frontmatter.status`
- ort03：扫描条件改为检查 status，[确认通过] 时更新 status→clarified
- ort04：读取路径从 `*-clarified.md` 改为 `-sub-{seq}.md (status=clarified)`
