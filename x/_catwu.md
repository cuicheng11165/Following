# Cat Wu (@_catwu)

| Field | Value |
|-------|-------|
| Profile | https://x.com/_catwu |
| Bio | claude code + cowork @anthropicai, prev: @dagster, @scale_ai |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T22:00:00Z
- **Posts in window (fetched):** 44 (cap 50: no)
- **Mode:** rewrite / 30-day window (Notable posts 按 `summarize-x-post`)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Claude 产品发布与增压：Opus 5、Fable 5 限额延长、桌面内嵌浏览器
- **Claude Cowork** 真实用例（日历、非工程角色研究）
- **Claude Tag** 多玩家协作：从 single-player Code 到团队级 agent
- **Artifacts**：公开分享、多人编辑、HTML 交付
- 招聘与 sourcing 工作流（Claude Code + workflows + artifacts）
- 用户教育：安全账号、连接前确认、computer use 等

### Opinions and takes

- Opus 5 擅长长时间自主工作，欢迎用户试用反馈。
- Cowork 应用应深入非工程岗位（市场、销售、财务、法务等）；主动征集屏幕分享研究。
- Fable 5 的「判断力」体现在未点名也做倾向得分匹配等分析细节。
- 偏好用 HTML artifacts 而非长 Markdown 传达信息。
- 推荐为 Claude 使用单独账号（而非个人账号）处理连接类场景。
- 日历等个人工作流应沉淀为可迭代 skill，改邀请前先确认。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **Cowork 管理日历的具体 prompt**

**链接：** https://x.com/_catwu/status/2079011428380602526  
**时间 / 互动：** 2026-07-20 · ❤️ 531 · 🔁 18 · 💬 54 · 🔖 492 · 👁 ~54k

##### 主帖在说什么

她分享自己用 Claude Cowork 管周历的具体要求：① 会议总时长 &lt;20 小时；② 去重冲突会议；③ 参考过往周会拒哪些类型；④ 晚餐不计入 20 小时；⑤ 把流程建成可迭代 skill；⑥ 改邀请前先问她。并反问读者都用 Cowork 做什么。

##### 要点

- 硬约束：周会议 &lt;20h + 冲突去重
- 个性化：从历史拒绝模式学习
- 晚餐豁免计入
- 沉淀为 skill + 改邀请需确认（人在环）
- 开放式收集用例

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@trevrjay** | 抱怨 Cowork 在发 prompt 后才要求批准文件夹/找路径，不如 Claude Code 直观，难以找到稳定用例。 | [post](https://x.com/trevrjay/status/2079026791444889642) |
| **@glawsontweets** | 同类任务用 Claude Code/Codex：邮件/日历/TODO 授权集中到私有 repo，可在多 agent CLI 间切换虚拟助理。 | [post](https://x.com/glawsontweets/status/2079018112792555955) |
| **@Greg_TheBuilder** | Cowork 当「更强的 claude.ai 聊天」：小便携 app、点子实验后再交给 Code，以及文档数据抽取。 | [post](https://x.com/Greg_TheBuilder/status/2079020671904993570) |

##### 一句话概括

产品负责人用可执行 prompt 示范 Cowork：日历不是「帮我安排一下」，而是带预算、历史偏好与人在环的 skill 化流程。

---

#### 2. **候选人 sourcing：workflows + artifacts**

**链接：** https://x.com/_catwu/status/2073806626965049686  
**时间 / 互动：** 2026-07-05 · ❤️ 633 · 🔁 29 · 💬 101 · 🔖 575 · 👁 ~85k

##### 主帖在说什么

征集「Claude Code + workflows + artifacts」顶级用例，并给出自己的 sourcing 流程：描述岗位与背景 → 启动 dynamic workflow 找约 100 候选人（LinkedIn/Twitter/博客/播客/一句话 pitch）→ 生成 artifact 邮件发给自己 → 锁电脑离开，移动端审阅。

##### 要点

- 并行研究规模：~100 候选人
- 信息包：多平台 + one-line pitch
- 交付形态：artifact + 邮件，异步审阅
- 邀请社区交换 use case

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@danmana** | Artifacts 用于方案对比可视化、给非开发看；通常先普通会话收集信息——workflows 太吃 5 小时窗口。 | [post](https://x.com/danmana/status/2073811017205690842) |
| **@morganlinton** | 自称 artifacts 后知后觉，会读评论学习。 | [post](https://x.com/morganlinton/status/2073811942230360164) |
| **@hopes_revenge** | 高赞表情/梗图互动（低文本、高可见度）。 | [post](https://x.com/hopes_revenge/status/2073807891858153932) |

##### 一句话概括

招聘 sourcing 被拆成「可无人值守的 map-reduce 工作流 + 移动端可读 artifact」，把 Claude Code 从写代码扩到组织流程。

---

#### 3. **Claude Code 桌面内嵌浏览器**

**链接：** https://x.com/_catwu/status/2075647324790112304  
**时间 / 互动：** 2026-07-10 · ❤️ 1667 · 🔁 70 · 💬 76 · 🔖 431 · 👁 ~230k  
**语境：** 引用 @ClaudeDevs 官方桌面内嵌浏览器发布。

##### 主帖在说什么

她转述并扩写：Claude Code 可在桌面 app 内打开任意网站——用生产环境、打开它发给你的链接、刷 Twitter，甚至看世界杯。官方侧强调沙箱、可配置会话持久，交互方式与本地 dev server 一致。

##### 要点

- 内嵌浏览器：读/点/交互任意站点
- 场景：生产 app、文档/设计稿、外链、娱乐梗
- 沙箱 + 会话持久可配置
- 产品定位：agent 与「真实网页」同上下文

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ken100bands** | 「世界杯那句卖到我了」——娱乐场景反而降低理解门槛。 | [post](https://x.com/ken100bands/status/2075655787288904171) |
| **@AgentOrToy** | 调侃 Claude 比自己更会「多标签生活」。 | [post](https://x.com/AgentOrToy/status/2075765776405946375) |
| **@itscharliecowan** | 实质产品问题：preview 能否用 Clerk 登录，而不只限 localhost？ | [post](https://x.com/itscharliecowan/status/2075657631562158329) |

##### 一句话概括

桌面 Code 从「本地文件 agent」变成可进生产站与任意 URL 的浏览 agent——用户立刻追问登录态与沙箱边界。

---

#### 4. **Claude Tag 现场 walkthrough 预告**

**链接：** https://x.com/_catwu/status/2074925531519468012  
**时间 / 互动：** 2026-07-08 · ❤️ 602 · 🔁 42 · 💬 54 · 🔖 349 · 👁 ~91k

##### 主帖在说什么

预告次日 10am PT 直播：从单人 Claude Code 走到多人 Claude Tag 的路径，并深讲 Tag 如何工作。叙事弧：AI 曾补全句子 → 写整功能 → 现在 Tag 可监控频道、主动干活、全员可 steer，并记住上周交代过的事。

##### 要点

- 单玩家 → 多玩家协作 agent
- Tag 能力：监控频道、主动工作、团队 steer、跨周记忆
- 直播形式：walkthrough + 机制深潜
- 产品叙事：从补全到团队同事

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@starryhe214** (Siqi, Pika Lead Product) | 团队两周重度用 Tag（单频道 ~$5k）：已成 ideation/原型/营销（发布视频）核心；反馈故障、外部 MCP、每频道配置等，希望对接工程谈 best practices。 | [post](https://x.com/starryhe214/status/2074984132137115959) |
| **@RandyHaddad6** | 晒「浴缸里用 Tag 推 PR」——移动/生活场景 dogfood。 | [post](https://x.com/RandyHaddad6/status/2076716070988296450) |
| **@LeeLinAI123** | 已收到邀请链接，确认出席。 | [post](https://x.com/LeeLinAI123/status/2074935064400433594) |

##### 一句话概括

Tag 被定位为「团队可 steer 的频道同事」；重度付费用户已在规模化使用并反馈 MCP/可靠性缺口。

---

#### 5. **征集非工程角色 Cowork 用例**

**链接：** https://x.com/_catwu/status/2077933568282755145  
**时间 / 互动：** 2026-07-17 · ❤️ 287 · 🔁 18 · 💬 20 · 🔖 161 · 👁 ~32k

##### 主帖在说什么

主张「你最懂自己的工作流」：面向市场、销售、财务、法务等非工程岗位，开放 30 分钟屏幕分享研究报名，让团队据此改进 Cowork。

##### 要点

- 目标角色：非工程职能
- 方法：30 分钟 screenshare 研究
- 目的：产品改进输入，而非单向 demo
- 表单报名链接

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@crimpislife** | Top 需求：Cowork 要有带登录态的完整浏览器（类似 Code 更强）；年底不想再开独立浏览器。 | [post](https://x.com/crimpislife/status/2078174428697907209) |
| **@CWrightswold** | 请求加速 Cowork Cloud 推送。 | [post](https://x.com/CWrightswold/status/2078069003113611272) |
| **@SEO** (AJ Ghergich) | 痛点：star 默认项目文件夹后，Cowork 仍重置为 none——「wildly annoying」。 | [post](https://x.com/SEO/status/2077952753653969280) |

##### 一句话概括

Cowork 要吃非工程市场，产品团队用 screenshare 收真实流程；用户回馈集中在浏览器登录态、Cloud 与文件夹状态稳定性。

### Products, launches, people

- **Claude Opus 5**、**Claude Fable 5**、**Claude Code**、**Claude Cowork**、**Claude Tag**、**Artifacts**
- 与 **Boris Cherny**、官方 **@claudeai** / **@ClaudeDevs** 联动
- Claude Code 历史回顾（making-of）与早期用户致谢

### Tone

产品负责人式：发布日高能转发 + 实用 prompt/工作流示范 + 高频回复用户；语气友好、邀请反馈，偏「show don't just announce」。
