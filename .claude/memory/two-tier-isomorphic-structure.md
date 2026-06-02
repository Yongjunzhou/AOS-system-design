---
name: two-tier-isomorphic-structure
description: 10-pl4pleos/ 和 20-pl4eos/ 目录结构同构，均含 00-spec/10-product-sysdev/20-comdev/30-sysint/40-sysops/80-opsdata
metadata:
  type: project
---

# 两层目录结构同构化

**日期**：2026-06-02

## 结构

```
10-pl4pleos/（元流水线, A1）        20-pl4eos/（EOS 流水线, A2）
00-pl4pleos-spec/                  00-pl4eos-spec/
10-pl4pleos-product-sysdev/        10-pl4eos-product-sysdev/
20-pl4pleos-product-comdev/        20-pl4eos-product-comdev/
30-pl4pleos-product-sysint/        30-pl4eos-product-sysint/
40-pl4pleos-product-sysops/        40-pl4eos-product-sysops/
50-* (A2 特有：bizcfg)            50-pl4eos-product-bizcfg/
80-pl4pleos-opsdata/               80-pl4eos-opsdata/
```

## 命名规律

`{层级号}-{产品前缀}-product-{子线名称}`

- `pl4pleos` = Pipeline for Pipeline of EOS（元流水线）
- `pl4eos` = Pipeline for EOS（EOS 流水线）

## 清理操作

- 移除了 `10-pl4pleos/10-pl4eos-sysdev/`（内容重复，移入 90-hold/）
- 移除了 `20-pl4eos/10-eos-sysdev/`（内容重复，移入 90-hold/）
- 统一命名：`pl4eos`/`pl4pleos` 前缀对齐

## 产品链关系

A1（元流水线, 流水线类×AI SKILL）→ A2（EOS 流水线, 流水线类×AI SKILL）→ A3（EOS, 非流水线类×软件产品）→ B（输出产品）

## 相关记忆

- [[delivery-framework-two-types]]
