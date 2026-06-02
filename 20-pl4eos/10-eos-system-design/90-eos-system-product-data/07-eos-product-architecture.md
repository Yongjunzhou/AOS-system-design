# EOS 产品架构定义
**EOS Product Architecture Definition**

**文档版本**：v1.0（模板）
**创建日期**：2026-05-20
**状态**：待填充

---

## 架构设计结果（树形结构）

<!-- EOS 是软件产品型系统，按四层分类组织：前端层、后端层、数据层、基础设施层 -->

```
EOS 企业运营体系 — 产品架构
├── 前端层
│   ├── PA-001: 运营门户
│   ├── PA-002: 管理仪表盘
│   ├── PA-FE-003: 产品详情页面          ← 范例节点
│   └── ...
│
├── 后端层
│   ├── 流程管理组件
│   │   ├── PA-00X: 流程引擎
│   │   ├── PA-00X: [组件]
│   │   └── ...
│   │
│   ├── 绩效管理组件
│   │   ├── PA-00X: 绩效计算引擎
│   │   ├── PA-00X: [组件]
│   │   └── ...
│   │
│   ├── 产品管理组件
│   │   ├── PA-BE-005: 获取产品详情      ← 范例节点
│   │   └── ...
│   │
│   └── ...
│
├── 数据层
│   ├── PA-00X: 运营数据仓库
│   ├── PA-00X: 指标库
│   ├── PA-00X: [数据组件]
│   └── ...
│
└── 基础设施层
    ├── PA-00X: API 网关
    ├── PA-00X: 统一认证
    ├── PA-00X: [基础设施组件]
    └── ...
```

---

## 架构末级节点定义

### 前端层（PA-001 ~ PA-00X）

| PA 节点 | 名称 | 承接 SysReq 场景活动 | 职责 |
|---------|------|---------------------|------|
| PA-001 | 运营门户 | <!-- SA-XXX.X.X.X --> | <!-- 职责描述 --> |
| PA-002 | 管理仪表盘 | <!-- SA-XXX.X.X.X --> | <!-- 职责描述 --> |
| PA-FE-003 | 产品详情页面 | [范例] SysReq-QUERY-003, SysReq-DATA-001, SysReq-UI-005 | 加载并展示产品详情 |

### 后端层（PA-00X ~ PA-00X）

| PA 节点 | 名称 | 承接 SysReq 场景活动 | 职责 |
|---------|------|---------------------|------|
| PA-BE-005 | 获取产品详情 | [范例] SysReq-QUERY-003, SysReq-DATA-001, SysReq-NFR-QUERY-001 | 根据产品 ID 返回完整 Product 数据 |

### 数据层（PA-00X ~ PA-00X）

| PA 节点 | 名称 | 承接 SysReq 场景活动 | 职责 |
|---------|------|---------------------|------|
| PA-00X | <!-- 组件名称 --> | <!-- SA-XXX.X.X.X --> | <!-- 职责描述 --> |

### 基础设施层（PA-00X ~ PA-00X）

| PA 节点 | 名称 | 承接 SysReq 场景活动 | 职责 |
|---------|------|---------------------|------|
| PA-00X | <!-- 组件名称 --> | <!-- SA-XXX.X.X.X --> | <!-- 职责描述 --> |

---

## 非功能约束

### 非功能需求对产品架构的约束

| SysReq-NFR | 约束 | 受影响的 PA 组件 |
|-----------|------|----------------|
| NFR-001 | <!-- 约束描述 --> | <!-- 受影响组件 --> |

---

## 架构统计

| 层级 | PA 节点数 | 说明 |
|------|----------|------|
| 前端层 | <!-- N --> | 运营门户、管理仪表盘、配置界面等 |
| 后端层 | <!-- N --> | 流程引擎、绩效计算、业务服务等 |
| 数据层 | <!-- N --> | 数据仓库、指标库、数据同步等 |
| 基础设施层 | <!-- N --> | API 网关、认证授权、监控日志等 |
| **合计** | <!-- N --> | |

---

**文档版本**：v1.0（模板）
**最后更新**：2026-05-20

---

## 范例附录：产品详情场景的 SysReq ↔ PA 完整链路

> 本附录展示一个完整的设计链路——从 SysReq 数据模型定义开始，到 PA 前后端组件的详细定义结束。
> 这里的 SysReq 节点编号为便于理解而简化；实际 EOS 项目中的 SysReq 编号遵循 SysReq 规范。

---

### A1. SysReq 层：产品实体数据模型

```
SysReq-DATA-001: 产品实体模型（Product Entity Model）
│
├─ 1. 概述
│   └─ 本节点定义"产品"实体的完整数据结构和字段约束。
│      所有涉及产品数据的 PA 节点均以本定义为数据契约。
│
├─ 2. 实体定义
│   ├─ 实体名称: Product（产品）
│   ├─ 标识: id: string (UUID v4)，系统自动生成
│   └─ 字段清单:
│       ├─ name: string (1..64)               ← 产品名称，必填，最大 64 字符
│       ├─ code: string (1..32) [unique]       ← 产品编码，全系统唯一
│       ├─ category: enum { RAW, FINISHED, SEMI, SERVICE }
│       ├─ status: enum { ACTIVE, DISCONTINUED, ARCHIVED }
│       ├─ specification: map<string, string>  ← 规格参数，KV 对
│       ├─ unit: string (1..8)                 ← 计量单位
│       ├─ unitPrice: decimal(18,2)            ← 标准单价
│       ├─ bomId: string?                      ← 关联 BOM（可选）
│       ├─ categoryId: string (FK → ProductCategory)
│       ├─ description: text?                  ← 产品描述（可选）
│       ├─ attachements: Attachment[]          ← 附件列表
│       ├─ createdAt: datetime
│       └─ updatedAt: datetime
│
├─ 3. 值对象定义
│   └─ Attachment:
│       ├─ fileName: string
│       ├─ fileUrl: string
│       ├─ fileSize: int (bytes)
│       └─ uploadTime: datetime
│
├─ 4. 业务约束
│   ├─ BC-01: 同一租户下 code 不可重复
│   ├─ BC-02: ARCHIVED 状态不可逆（归档后不可重新激活）
│   ├─ BC-03: DISCONTINUED 状态的产品不可用于新建订单
│   └─ BC-04: 产品描述最大 2000 字符
│
└─ 5. 关联关系
    ├─ belongsTo → ProductCategory（多对一）
    ├─ hasParts  → Product（可选，一对多，仅 BOM 场景）
    └─ referencedBy → OrderItem（被引用，不在本节点定义）
```

### A2. SysReq 层：查询功能（引用数据模型）

```
SysReq-QUERY-003: 查询产品详情
├─ 1. 功能描述: 系统应支持根据产品 ID 查询产品的完整信息
├─ 2. 输入: productId (string)
├─ 3. 输出: Product（字段定义见 SysReq-DATA-001）
├─ 4. 性能指标: P99 < 500ms, 并发 ≥ 100 TPS
└─ 5. 映射 SysReq-NFR: SysReq-NFR-QUERY-001
```

### A3. SysReq-NFR：查询类 API 非功能需求

```
SysReq-NFR-QUERY-001: 查询类 API 非功能需求
├─ 缓存策略: 产品基础信息可缓存 300s，价格/状态变更后失效
├─ 数据权限: 按组织层级控制产品可见范围
└─ 审计要求: 所有产品详情查询记录审计日志
```

### A4. PA 后端组件详细定义

```
PA-BE-005: 获取产品详情（Get Product Details）
│
├─ 1. 构件定义
│   ├─ 职责: 根据产品 ID 从产品主表查询并返回完整的 Product 数据
│   ├─ 所属架构节点: 产品服务 · 查询模块
│   └─ 本构件是: 软件模块（后端服务）
│
├─ 2. 所映射的上层需求（SysReq 第 9 级）
│   ├─ [SysReq-QUERY-003]      → 查询产品详情          ← 功能性需求
│   ├─ [SysReq-DATA-001]       → 产品实体模型           ← 数据契约引用
│   └─ [SysReq-NFR-QUERY-001]  → 查询类 NFR             ← 非功能需求
│
├─ 3. 符合性分析
│   ├─ 功能: 通过 RESTful GET API 返回完整 Product 数据，
│   │       字段完全对齐 SysReq-DATA-001，满足 SysReq-QUERY-003
│   ├─ 性能: 只读查询 + Redis 缓存（key: product:{id}, TTL=300s），
│   │       命中缓存 P99 < 50ms，穿透 < 300ms，满足 NFR
│   ├─ 权限: 在网关层解析 Token 获取组织范围，
│   │       数据层按 tenantId + 组织层级过滤
│   └─ 审计: 在 API 网关层统一记录，本组件不单独处理
│
├─ 4. API 契约
│   ├─ 端点: GET /api/v1/products/{productId}
│   ├─ 请求参数: productId: string (UUID)
│   ├─ 成功响应 (200):
│   │   └─ body: Product
│   │       └─ 字段定义: 见 SysReq-DATA-001 §2
│   │           即完整返回 Product 实体的所有字段
│   ├─ 错误响应:
│   │   ├─ 404: { code: "PRODUCT_NOT_FOUND", message: "产品不存在" }
│   │   └─ 403: { code: "ACCESS_DENIED", message: "无权限" }
│   └─ 幂等性: 是（只读查询）
│
├─ 5. 非功能设计
│   ├─ 缓存: Redis, key=product:{id}, TTL=300s；
│   │        状态/价格变更时主动失效；布隆过滤器防穿透
│   ├─ 限流: 单用户 60 次/分钟
│   └─ 数据权限: 按组织树向上可见
│
├─ 6. 数据依赖
│   └─ 产品主表: product（字段映射 = SysReq-DATA-001 + tenantId）
│
├─ 7. 测试要求
│   ├─ 单元测试: 覆盖 200/404/403 三种响应
│   ├─ 性能测试: P99 < 500ms（命中缓存/穿透两种场景）
│   └─ 安全测试: 验证组织越权查询被拒绝
│
└─ 8. 下游指导
    ├─ 实现框架: Java 21 + Spring Boot 3.x
    ├─ 数据库: PostgreSQL 15
    ├─ 查询方式: Spring Data JPA + QueryDSL
    └─ 联调对象: PA-FE-003
```

### A5. PA 前端组件详细定义

```
PA-FE-003: 产品详情页面（Product Detail Page）
│
├─ 1. 构件定义
│   ├─ 职责: 加载并展示指定产品的完整详情页面
│   ├─ 所属架构节点: 产品管理模块 · 产品详情
│   └─ 本构件是: 软件模块（前端页面组件）
│
├─ 2. 所映射的上层需求（SysReq 第 9 级）
│   ├─ [SysReq-QUERY-003]      → 查询产品详情          ← 数据来源
│   ├─ [SysReq-DATA-001]       → 产品实体模型           ← 展示字段来源
│   └─ [SysReq-UI-005]         → 详情页支持关联跳转     ← UI 需求
│
├─ 3. 符合性分析
│   ├─ 数据: 调用 PA-BE-005 获取 Product 数据，
│   │       字段渲染对齐 SysReq-DATA-001
│   ├─ 关联跳转: categoryId 渲染为可点击分类标签，
│   │           bomId 渲染为"查看 BOM"链接
│   └─ 状态覆盖: loading / empty / error / success
│
├─ 4. UI 规范
│   ├─ 路由: /products/:productId
│   ├─ 页面布局（从上到下分区渲染）:
│   │   ├─ ① 标题栏
│   │   │   ├─ 面包屑: 产品管理 > 产品详情
│   │   │   ├─ 产品名称（name，大字标题）
│   │   │   └─ 操作按钮组: [编辑] [停用/启用] [归档]
│   │   │
│   │   ├─ ② 基本信息卡片
│   │   │   └─ 展示字段（来源: SysReq-DATA-001）:
│   │   │       ├─ 产品编码: {code}
│   │   │       ├─ 分类: {category} → 标签
│   │   │       ├─ 状态: {status}   → 彩色徽章
│   │   │       ├─ 规格参数: {specification} → KV 表格
│   │   │       ├─ 计量单位: {unit}
│   │   │       ├─ 标准单价: {unitPrice}
│   │   │       ├─ 所属分类: {categoryId} → 可点击链接
│   │   │       └─ 时间: {createdAt} / {updatedAt}
│   │   │
│   │   ├─ ③ 关联产品区域
│   │   │   ├─ 标题: "BOM 组成"（仅 bomId 不为空时展示）
│   │   │   └─ 卡片列表: 调用 BOM 服务获取子件列表
│   │   │
│   │   └─ ④ 附件区域
│   │       ├─ 标题: "附件（{attachements.length}）"
│   │       └─ 文件列表: 文件名 + 大小 + 下载链接
│   │
│   └─ 交互行为:
│       ├─ 加载中: Skeleton 骨架屏
│       ├─ 404: 全页提示"产品不存在" + [返回列表]按钮
│       ├─ 403: Toast "无查看权限"
│       └─ 网络错误: 错误提示 + [重试]按钮
│
├─ 5. 状态管理
│   ├─ 组件状态: loading | notFound | denied | error | success
│   ├─ 数据源: GET /api/v1/products/{productId}
│   └─ 请求时机: 组件挂载时自动发起
│
├─ 6. 非功能设计
│   ├─ 首屏渲染: FCP < 1s
│   ├─ 页面切换: React.lazy + Suspense
│   └─ 可访问性: 语义化 HTML + 键盘 Tab 导航
│
├─ 7. 测试要求
│   ├─ 单元测试: 覆盖 4 种渲染状态
│   ├─ E2E 测试: 从列表页点击 → 详情页渲染 → 关联跳转
│   └─ 可访问性测试: axe-core 扫描
│
└─ 8. 下游指导
    ├─ 框架: React 18 + TypeScript, Ant Design 5.x
    ├─ 状态管理: React Query + 组件级状态
    ├─ 路由: React Router v6
    └─ 联调对象: PA-BE-005
```

### A6. 追溯关系一览

```
SysReq-DATA-001（产品实体模型）      SysReq-NFR-QUERY-001（NFR）
  ├─ 被 PA-BE-005 引用为 API 响应体      └─ 被 PA-BE-005 映射为缓存策略
  └─ 被 PA-FE-003 引用为 UI 字段来源
        ↑
SysReq-QUERY-003（查询产品详情）──→ N:1 ──→ PA-BE-005 ──→ 联调 ──→ PA-FE-003
                                              ↑                          ↑
                                         SysReq-NFR-QUERY-001      SysReq-UI-005
```

| 节点 | 层 | 角色 | 不负责 |
|------|----|------|--------|
| SysReq-DATA-001 | SysReq | 定义实体有什么字段、什么类型 | 不定义如何获取、如何渲染 |
| SysReq-QUERY-003 | SysReq | 定义查询功能需求 | 不定义实现方式 |
| SysReq-NFR-QUERY-001 | SysReq-NFR | 定义非功能约束 | 不定义技术选型 |
| PA-BE-005 | PA | 定义如何提供数据（API + 缓存 + 权限） | 不定义字段语义 |
| PA-FE-003 | PA | 定义如何展示数据（UI + 交互 + 状态） | 不定义数据来源 |
