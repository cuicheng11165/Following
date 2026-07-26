# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T22:00:00Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** rewrite / 30-day window (Notable posts 按 `summarize-x-post`)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **软件工厂 / 自主 agent**：产品 = 维护它的 agent 工厂（**eve.dev**）
- 个人研究工作流：agent CLI + 文件系统 + `AGENTS.md`
- **开放模型时刻**：Kimi K3 登顶 Next.js evals；考虑 Gateway 开源选项
- 产品发货：v0 Figma→App、AI Gateway / Opus 5、CDN、流式转写
- **人才**：Pete Hunt 掌 Frameworks/Next.js；Nick Schrock 做 Agentic DX
- 产品站内 agent vs 通用 harness（回应 Mitchell Hashimoto）

### Opinions and takes

- 「（软件）工厂即产品」：产品好坏取决于你配置的自主维护 agent——类比 Elon/Tesla。
- 有新想法时别只 ad-hoc prompt，要建能启动、维护、增长想法的工厂（eve.dev 比其它 framework 更「本源」）。
- 下一阶段是自主：agent 读反馈、自行改进软件（英/西语同步叙事）。
- 研究用文件夹 + AGENTS.md + CLI agent 可无限扩展，结果可导出 HTML 部署到 Vercel。
- 在考虑为成本敏感任务引入开源模型与更多模型多样性。
- 公共站内 agent 与「自带 harness」是序列问题：先 API/MCP/CLI 选择权，再 .com 便利/安全/主动运维。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **The (software) factory is the product**

**链接：** https://x.com/rauchg/status/2081123293340520642  
**时间 / 互动：** 2026-07-25 · ❤️ 1652 · 🔁 113 · 💬 77 · 🔖 702 · 👁 ~229k

##### 主帖在说什么

主张「（软件）工厂即产品」：你的产品只与你配置的、能**自主维护**它的 agents 一样好。类比 Elon Musk 对 Tesla 工厂的洞察，认为软件世界现已同理。

##### 要点

- 产品价值上移到「维护工厂」层
- 自主 agent 维护能力 = 产品质量上限
- Tesla 工厂隐喻迁移到软件
- 为 eve.dev 叙事铺垫

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@santtiagom_** | 工厂好坏取决于反馈环；无可靠 validation，自主无法规模化——建反馈环是核心工程题。 | [post](https://x.com/santtiagom_/status/2081132864096120845) |
| **@albertmetzz** | 反隐喻：Tesla 瓶颈是制造；软件瓶颈从来不是「建」，而是「知建什么」——agent 加速的是本已便宜的部分。 | [post](https://x.com/albertmetzz/status/2081259337494786197) |

##### 一句话概括

Rauch 把竞争点从「写出功能」挪到「配置可自维护的软件工厂」——支持者谈反馈环，反对者说瓶颈其实是产品判断。

---

#### 2. **eve.dev：公司 genesis 级工厂**

**链接：** https://x.com/rauchg/status/2081149743368122723  
**时间 / 互动：** 2026-07-25 · ❤️ 1003 · 🔁 46 · 💬 54 · 🔖 921 · 👁 ~128k  
**产品：** https://eve.dev/

##### 主帖在说什么

称 eve.dev 比团队建过的任何 framework 更根本——是公司的 **genesis**。有新想法时不要只想到「找个 agent ad-hoc prompt」，而要想如何建一座能**启动、维护并放大**想法的工厂。

##### 要点

- eve.dev > 既有 framework（本源定位）
- 反模式：一次性 ad-hoc prompt
- 正模式：可生长的 agent 工厂
- 与「factory is the product」同日连发

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@SeeLos** | 产品反馈：Eve 需要原生 memory 系统。 | [post](https://x.com/SeeLos/status/2081157194276282704) |
| **@ifeanyi_we** | 自称先建类似系统，Eve 发布后移植概念；认为 **WDK** 是杀手级能力却讨论不足。 | [post](https://x.com/ifeanyi_we/status/2081151664602374158) |
| **@SherifKozman** | 域名轶事：曾想拿 eve.dev 未果，现懂为何；自有 evemem.com。 | [post](https://x.com/SherifKozman/status/2081155404617437556) |

##### 一句话概括

eve.dev 被定义为「想法→可自生长公司」的工厂原语；早期用户立刻要 memory，并争论 WDK 是否被低估。

---

#### 3. **文件系统 + AGENTS.md 做无限研究**

**链接：** https://x.com/rauchg/status/2081103993917649134  
**时间 / 互动：** 2026-07-25 · ❤️ 1045 · 🔁 40 · 💬 70 · 🔖 827 · 👁 ~76k

##### 主帖在说什么

分享个人做法：`research/` 文件夹 + 描述格式与最佳实践的 `AGENTS.md`，启动 CLI agent 提问；无复杂 app/知识图谱/UI。Agent 可跨会话关联知识，文件夹用 iCloud/git 同步；要分享时让 agent 渲 HTML 报告并部署到 Vercel——「软件」就是英文写的 AGENTS.md。

##### 要点

- 原语：文件夹 + AGENTS.md + agent CLI
- 反 UI 崇拜：不要 fancy apps
- 扩展：跨会话相关、iCloud/git 同步
- 输出：HTML → Vercel 部署分享

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@tobi** (Shopify CEO) | 推荐 https://github.com/tobi/try 作为配套工具。 | [post](https://x.com/tobi/status/2081117462767014300) |
| **@colinhacks** | 实战：撞 Claude Code WebSearch 默认 200 次上限，晒新爱用 env vars。 | [post](https://x.com/colinhacks/status/2081126046594912257) |
| **@RohithThakurwar** | 反方：简单 md 易 context rot；多专用 agent 更好，链 OpenCompany。 | [post](https://x.com/RohithThakurwar/status/2081108728607326546) |

##### 一句话概括

研究系统被降维成「英语配置的文件夹」——Tobi 补工具链，另一些人警告单仓 md 的 context rot。

---

#### 4. **Kimi K3 登顶 Next.js evals（开放模型里程碑）**

**链接：** https://x.com/rauchg/status/2077900518404321759  
**时间 / 互动：** 2026-07-16 · ❤️ 5746 · 🔁 385 · 💬 166 · 🔖 1142 · 👁 ~610k  
**基准：** https://nextjs.org/evals

##### 主帖在说什么

宣布 **Kimi K3** 在 nextjs.org/evals 上成为最佳模型，超过 Fable，并以更短时间达到可比成功率。称这是**首次**开放模型在此综合 web 工程基准上全面领先专有模型。附注：基准不讲完整故事但仍是重要信号；尚无模型 100% 完成，顶峰约 92%、「with help」约 96%。

##### 要点

- Kimi K3 > Fable（该 eval）
- 首次 open 全面领先 proprietary（此套件）
- 时间效率优势
- 上限未满：92% / 96% with help

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@zmentzony** | 要求表格加 **cost** 列——质量领导不等于经济领导。 | [post](https://x.com/zmentzony/status/2077919694292406460) |
| **@oscargaske** | 对比营销：发布未用「政府拦我们」叙事。 | [post](https://x.com/oscargaske/status/2077914531372630319) |
| **@FredrikAurdal** | 时代类比：LLM 进入 Linux vs Windows 阶段。 | [post](https://x.com/FredrikAurdal/status/2077910448540680659) |

##### 一句话概括

Vercel 自家 web 工程 eval 上 open 权重首次登顶——信号够强，社区立刻要成本列与开源时代叙事。

---

#### 5. **公共站内 Agent 的理由（回应 Mitchell）**

**链接：** https://x.com/rauchg/status/2077847855306596563  
**时间 / 互动：** 2026-07-16 · ❤️ 352 · 🔁 17 · 💬 37 · 🔖 421 · 👁 ~74k  
**语境：** 引用 Mitchell Hashimoto：通用 harness+CLI/MCP 总是好过产品内嵌聊天框。

##### 主帖在说什么

提出「在你自己的 .com 上提供公共 agent」的案例：⓪ 若还没做好 agent API，先做 OpenAPI/SDK/CLI/MCP。① **便利**：不是每个客户随时有 harness。② **安全**：vercel.com Agent 有审计、最小权限、云沙箱，避免用户机器上静态凭证蔓延。③ **主动**：仍处「人输入 prompt」阶段；云 agent 可对异常/攻击/用量尖峰告警并在你睡觉时盯基础设施。同意 Mitchell 优先给选择权；Vercel 提供 AI Gateway、CLI/MCP，站内 Agent 复用同一能力，站点对 agent 以 Markdown-over-the-wire 可读。

##### 要点

- 序列：先 agent-ready API，再站内 agent
- 三理由：便利 / 安全沙箱 / 主动运维
- 与 BYO harness 并存，非二选一
- 自身 Agent 复用对外同一平台 primitives

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@lukerramsden** | 正解是同一 agent 双表面：MCP 给自带 harness，生成 UI 给路人——底层同一工具与上下文。 | [post](https://x.com/lukerramsden/status/2078107880033603925) |
| **@pranvv27** | 多数用户不会配 MCP；打开网站就要 AI 可用——开发者只是小众重要受众。 | [post](https://x.com/pranvv27/status/2077862119354343730) |
| **@cramforce** (Vercel CTO) | 轻松「下届董事会」表情回应（内部梗）。 | [post](https://x.com/cramforce/status/2077858759620329560) |

##### 一句话概括

不是否定 BYO harness，而是主张「同一能力、两种入口」：极客用 MCP，大众用 .com——安全与主动运维是站内 agent 的护城河。

### Products, launches, people

- **eve.dev**、**Vercel** AI Gateway（Opus 5、开源模型意向）、**v0**（Figma→App）、**AI SDK**
- **Pete Hunt**（Frameworks / Next.js）、**Nick Schrock**（Agentic DX / GraphQL 联合发明人）
- Next.js evals；CDN / Python 启动等基建 ship
- 对话对象：**@elonmusk**（隐喻）、**@tobi**、**@mitchellh**

### Tone

高能量 CEO：愿景长帖与产品 ship 庆祝交织；短回复极多（emoji、一行肯定）；双语（英/西）出场；对竞品/争议偶有 sparring。
