---
name: pending-subpd-subpl-naming
description: 待决——子线目录名到底是 subpl 还是 subpd，39 个文档文件与磁盘目录不一致
metadata: 
  node_type: memory
  type: project
  originSessionId: 5ff7b330-61c6-4f82-a69e-77b676f52e87
  modified: 2026-09-19T13:43:35.944Z
---

**待决**，2026-09-19 发现。定名之前**不要扫**——方向可能扫反。

## 现象

- 磁盘与 git 里只有 `subpl`：`20-pl4eos/10-pl4eos-subpl-sysdev/` 等 9 个目录，`subpd` 目录**从未存在于 git**。
- 但 **39 个文档文件写 `subpd`**，含根 `CLAUDE.md`（目录树 12 行）、`README.md`、`AGENTS.md`、两份讲解材料、13 个现行规范／SKILL，以及 20 个记忆文件。
- 其中 **135 处处在相对链接里**，点了 404；转 PDF 也是死链。

## 证据冲突（这正是不能擅自扫的原因）

| 证据 | 指向 |
|------|------|
| 磁盘与 git 只有 `subpl`，`subpd` 从未存在 | `subpl` 是实在的名字 |
| `4b1803c2`、`b491289a`（2026-09-17「三形态命名体系」）把文档里的 `subpl` 改成 `subpd`（同段文字 `-` 行 subpl、`+` 行 subpd） | 那轮是**主动改成 subpd** |
| 同一天最新的 `27ce333d` 又改回 `subpl`，提交说明写「subpd→subpl」，只动 3 份文件 | 又往回改，没改完 |

判断：9-17 那次命名体系把 `subpl` 改名成 `subpd`（只改文档没改目录），随后往回改、改到一半停了，39 个文件卡在中间态。

## 处置建议

定名之后再动，且只扫「导航文档 + 现行规范／SKILL」约 19 个文件；**20 个记忆文件不动**——记忆是当时的事实快照，改它们等于篡改历史。
若裁定 `subpd` 才是新名，则相反：要动的是 9 个目录（`git mv`），39 个文档反而不动。

实例代价：2026-09-19 查 worktree 时按根 `CLAUDE.md` 的路径 `find` 空手而归，绕了几个弯才弄清是文件改了名。

相关：[[chain-form-three-tiers-naming]]、[[biz-chain-renumbering-2026-09-16]]
