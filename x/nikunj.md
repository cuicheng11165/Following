# Nikunj Kothari (@nikunj)

| Field | Value |
|-------|-------|
| Profile | https://x.com/nikunj |
| Bio | partner @fpvventures - investing in seed/A. previous: early hire @meter, @opendoor, @atlassian & others. love @shimoleejhaveri + 👦👧 |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:15:00Z
- **Posts in window (fetched):** 50（cap 50: yes；本窗口更早帖子未纳入）
- **Mode:** 30-day backfill
- **Cursor:** per-builder（本 run 不更新 state）
- **Notable method:** `summarize-x-post`（`x_thread_fetch` per item）

### Themes

- AI agent / skill 工作流（Claude Code、Ramp 费用自动填报、模型路由、harness 防 slop）
- 投资人视角：科技圈职衔通胀与信号衰减；Series A 估值梗
- 治理与并购：Midjourney 收购 Co-Star 的「只有创始人完全控制才能做」观察
- 湾区生活：Burlingame 育儿与通勤、瑞士旅行、SF 社交密度
- 多巴胺式多任务：Slack × Claude Code × X

### Opinions and takes

- 「proof of prompt is soon going to replace proof of work」——可复现提示/工作流证据成为新信任层
- neo-、full stack、fellows、labs、partner、forward deployed、RL 等头衔因滥用而失信号（自嘲自己也是 partner / 跑 fellowship）
- Midjourney 收购占星 app 只有在 CEO 完全控制且极度野心时才可能
- 推荐用 harness 榨出模型能力；部署侧随口推荐 Railway
- 有小孩后对旅行/活动更克制；公开征询孩子何时开始 coding
- 调侃「tree fiddy M」热门 Series A 第二轮估值宿命

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **Proof of prompt 取代 proof of work**

**链接：** https://x.com/nikunj/status/2081383934928068619  
**时间 / 互动：** 2026-07-26 · 约 35 likes / 9 replies / 3.3k views

##### 主帖在说什么

他抛出一句极短判断：proof of prompt 很快会取代 proof of work。核心不是加密学 PoW，而是协作与招聘里的信任凭证：可复现的提示、agent 轨迹与工作流，正在比「我写了多少小时代码」更能证明能力与贡献。

##### 要点

- 主张：prompt/工作流证据即将成为默认信任层
- 语境：agent 时代审计、面试与协作
- 形式：单句金句，留给讨论补全机制

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ananthmv** | 团队已把 prompts（叫 skills）全部 commit 进 git 复用；不同 Agentic CLI/TUI 处理方式不同 | [post](https://x.com/ananthmv/status/2081405653030191151) |
| **@PravinTiwariX** | 面试已要求展示如何 steer 模型；「show me your prompt」比传统题更能看出思维范式 | [post](https://x.com/PravinTiwariX/status/2081403332820971758) |
| **@martimC11** | 反方：认为是 nonsensical slop | [post](https://x.com/martimC11/status/2081395137247158392) |

##### 一句话概括

投资人把「可复现提示」抬成新 PoW，讨论立刻落到 git skills 与面试考 prompt。

---

#### 2. **科技头衔已失信号**

**链接：** https://x.com/nikunj/status/2080293627784212933  
**时间 / 互动：** 2026-07-23 · 约 59 likes / 10 replies / 5.9k views

##### 主帖在说什么

他列出一批「因为用得太滥而失去筛选功能」的科技头衔：neo-something、full stack、fellows、labs、partner、forward deployed，以及「慢慢通胀」的 RL。脚注自嘲：自己既是 partner，又在跑 fellowship——讽刺的自觉写进主帖。

##### 要点

- 信号衰减对象：neo / full stack / fellows / labs / partner / FDE / RL
- 机制：标签滥发 → 招聘与社交筛选失效
- 姿态：点名自己也在「通胀名单」里

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@animesh_garg** | 希望 RL 别丢语义——那是整个学术领域的名字，不能轻易变成头衔 buzzword | [post](https://x.com/animesh_garg/status/2080313216211530129) |
| **@chinmay185** | 主张回归旧称：software engineer、sysadmin、dba | [post](https://x.com/chinmay185/status/2080309906289385778) |
| **@davidhoang** | 一句话合成梗：Forward Deployed Partner | [post](https://x.com/davidhoang/status/2080504291421569429) |

##### 一句话概括

职衔通胀清单引发「把旧工种名找回来」与「别把 RL 玩坏」的共鸣。

---

#### 3. **开源 Ramp-Autofill skill（Claude Code）**

**链接：** https://x.com/nikunj/status/2076775924650107151  
**时间 / 互动：** 2026-07-13 · 约 27 likes / 7 replies / 24 bookmarks / 7.9k views

##### 主帖在说什么

他写 Ramp 使命是省钱+省时间，自己却仍在手工分类与贴票据——直到用了 Ramp CLI。于是开源 **Ramp-Autofill skill**：从 iMessage/Gmail 找收据（链接则用 Playwright 转 PDF）、用 Google Calendar 填 memo、根据历史交易学分类与文风、校验并支持 scheduled job。面向 Claude Code 的 drop-in，周末清完 60 天费用。

##### 要点

- 产品：Ramp CLI + 自研 skill，仓库开源
- 能力：收据发现、日历 memo、风格/分类学习、定时跑
- 运行时：Claude Code / Fable 语境

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@nikunj**（自跟） | 用 @tryramp CLI（谢 @zack_field）与 Claude Fable 构建；repo：github.com/kothari-nikunj/ramp-autofill | [post](https://x.com/nikunj/status/2076776777884811671) |
| **@teddy_riker**（Ramp agents） | 希望发到 agents.ramp.com/playbooks | [post](https://x.com/teddy_riker/status/2076798964691542228) |

##### 一句话概括

投资人把个人费用流做成可复用 Claude skill，并被 Ramp 官方侧邀请进 playbooks。

---

#### 4. **Midjourney 买 Co-Star：只有创始人完全控制才做得出**

**链接：** https://x.com/nikunj/status/2081017328137916426  
**时间 / 互动：** 2026-07-25 · 约 171 likes / 11 replies / 51 bookmarks / 28.7k views

##### 主帖在说什么

引用 Midjourney 收购占星 app Co-Star、Banu 任 CDO 的公告后，他给出治理结构观察：这类「离谱并购」只有在 (a) CEO 对公司有完全控制（盈利、无典型董事会/VC）且 (b) 像 @DavidSHolz 一样野心到「crazy」时才可能。否则无法向团队解释生成媒体公司为何买占星 app。PS：第一秒以为买的是房地产 CoStar。

##### 要点

- 条件 a：控制权 / 盈利 / 无强董事会约束
- 条件 b：创始人野心与品味
- 幽默：Co-Star vs CoStar 混淆

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TanyaaCJain** | 好奇促成交易的多层愿景 | [post](https://x.com/TanyaaCJain/status/2081267357423640660) |
| **@sharozjavaid** | 猜测本质是 data play | [post](https://x.com/sharozjavaid/status/2081137925312688209) |

##### 一句话概括

用并购案例讲清：战略自由度是治理结构的函数，不是「idea 够酷」就行。

---

#### 5. **Slack × Claude Code × X 多巴胺三角**

**链接：** https://x.com/nikunj/status/2081128318598881336  
**时间 / 互动：** 2026-07-25 · 约 16 likes · 父帖关于 Slack 多巴胺机

##### 主帖在说什么

在 Brian Lovin 讨论「Slack 是工作版多巴胺机」的语境下，他补刀一句群体画像：CMD+Tab 在 Slack、Claude Code 与 X 之间切换，多巴胺停不下来——通讯、agent 编程与信息流三端同时在线。

##### 要点

- 三端：Slack / Claude Code / X
- 机制：工具链本身劫持注意力
- 语气：自嘲式 builder 状态

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@brian_lovin** | 直接命名「The trifecta!」 | [post](https://x.com/brian_lovin/status/2081161568713335016) |

（其余低信号附和略。）

##### 一句话概括

一句话钉死 2026 builder 默认多任务栈：协作软件 + coding agent + 公域信息流。

### Products, launches, people

- **FPV Ventures**；**Claude Code** / Fable；**@tryramp** CLI / Ramp-Autofill skill
- **@Railway**、**@midjourney** / Co-Star / **@DavidSHolz**、**@banu__guler**
- 生活：Burlingame、瑞士列车/风景；育儿 coding 时间点征询

### Tone

轻松吐槽 + 投资人观察；大量回复与生活片段；技术判断偏实用，夹杂育儿与湾区生活方式，幽默自嘲多过严肃长文。

---
