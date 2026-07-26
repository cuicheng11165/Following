# Aditya Agarwal (@adityaag)

| Field | Value |
|-------|-------|
| Profile | https://x.com/adityaag |
| Bio | General Partner @SouthPkCommons, Co-Founder @Bevel_Health \| Ex: Early Eng @facebook, CTO @Dropbox, Board @Flipkart \| Optimist, Builder, Dad |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:15:00Z
- **Posts in window (fetched):** 41（cap 50: no；窗口已覆盖至约 2026-06-26）
- **Mode:** 30-day backfill
- **Cursor:** per-builder（本 run 不更新 state）
- **Notable method:** `summarize-x-post`（`x_thread_fetch` per item）

### Themes

- 创业文化：Culture eats strategy；创始人/早期团队/早期产品 DNA
- South Park Commons Founder Fellowship：极大野心、硬科技/原子级建造者（截止 Aug 2）
- AI harness 痛点：memory loss、compaction、skills 存信息方式、可解释性
- 模型经济学：付费 Fable vs 免费/开源替代；垂类 domain-specific 模型
- 云端 agent 栈愿景：任意模型 × harness × 全链路 tracing × 递归改进
- 家庭、国家认同、足球（USMNT）与个人叙事

### Opinions and takes

- 文化来自三块 DNA；压制涌现或碎片成「文化口袋」都糟；可多元背景但应共享公司文化
- 若很有价值却一用就被复刻，也许一开始就没那么有价值
- 系统层 switch off Fable：有好的免费替代为何付高价
- 在 ambition 边缘会更多被说 No；Love the No
- Cognition/Cursor 近前沿 OSS coding 模型 → 6 个月内高价值域都会出现 domain-specific 模型
- ChatGPT 新 app 功能重但日常 15–20 次轻查询变「沉重」

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **Culture always eats strategy for breakfast**

**链接：** https://x.com/adityaag/status/2079993986283123147  
**时间 / 互动：** 2026-07-22 · 约 55 likes / 9 replies / 39 bookmarks / 7.4k views

##### 主帖在说什么

他认为创业对话过度聚焦 Strategy，而 **Culture 永远吃掉 Strategy**。文化来自三源：创始人 personality/DNA、早期团队 DNA、早期产品 DNA——彼此重叠强化；既有 top-down 也有涌现。两害：创始人太弱压不住/固化涌现；意见过散形成多套亚文化。明确拒绝被拖进 DEI 论战：背景可不同，但应认同同一公司文化。

##### 要点

- 三源：founder / early team / early product
- 风险：压制涌现 vs 文化碎片化
- 边界：多元背景 ≠ 多套文化契约

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@HarryKapoor19** | 文化=你奖励与惩罚什么；推荐 MrBeast culture deck | [post](https://x.com/HarryKapoor19/status/2080004372998791270) |
| **@stutyashakti** | 文化在艰难期导航；硬决定沉淀成自上而下的潜规则 | [post](https://x.com/stutyashakti/status/2080005991857598636) |
| **@Chainbuilderpro** | 当一团队成功默默给另一团队加成本时，文化会政治化 | [post](https://x.com/Chainbuilderpro/status/2080018841808306418) |

##### 一句话概括

用三 DNA 模型讲清 startup culture，讨论落到「奖惩」与「艰难期决策沉淀」。

---

#### 2. **Harness 记忆丢失与 compaction 仍是大坑**

**链接：** https://x.com/adityaag/status/2079540355234414716  
**时间 / 互动：** 2026-07-21 · 约 45 likes / 16 replies / 32 bookmarks / 7.3k views

##### 主帖在说什么

他吐槽所有 harness 仍有严重 **memory "loss" 与 compaction** 问题：易忘、易混，终端用户挫败。出错时 **interpretability** 也差。把 **Skills 当信息存储** 视为根因之一，期待某种更好的 format/language。

##### 要点

- 症状：遗忘、混淆、错误不可解释
- 根因假设：skills 承载记忆的方式不对
- 诉求：新原语/语言，而不只是加 token

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@davemorin** | Agent memory 是最大问题之一；可能需每日训一部分权重；否则只是 search+上下文管理 | [post](https://x.com/davemorin/status/2079720148639084616) |
| **@justinkalland** | 根因是把 chat transcript 当 continuation state——歧义、表面；缺 governed semantic state 原语 | [post](https://x.com/justinkalland/status/2079581609964302365) |
| **@anieasyy** | 推 Greplica 作为 agents 共享读写 substrate | [post](https://x.com/anieasyy/status/2079595518603526517) |

##### 一句话概括

从用户痛点逼近「记忆不是更长上下文，而是缺语义状态原语」。

---

#### 3. **正在把系统从 Fable 上迁走：免费替代为何付费？**

**链接：** https://x.com/adityaag/status/2077983435000324125  
**时间 / 互动：** 2026-07-17 · 约 390 likes / 52 replies / 51.6k views

##### 主帖在说什么

他声明**不是夸张**：正在把自家系统的模型从 Fable 切走。逻辑直白——若存在足够好且免费的替代，为何继续付高价？这是 GP/builder 双重身份下的单位经济决策，不是评测站队。

##### 要点

- 行动：production switch off Fable
- 理由：good + free alternative
- 语气：反双曲、可审计的「literally」

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@trenchesbase** | 追问如何「免费」跑 Kimi：权重未放、自建可能数百万美元 | [post](https://x.com/trenchesbase/status/2078012175000740337) |
| **@davemorin** | 同样切换；「看不出差别」 | [post](https://x.com/davemorin/status/2078003259340685818) |
| **@shensi** | 建议 smart router（Merge gateway） | [post](https://x.com/shensi/status/2078082431874175169) |

##### 一句话概括

把模型选择从「SOTA 崇拜」拉回「可替代时的价格弹性」，并引发「免费到底多贵」的争论。

---

#### 4. **Founder Fellowship：别浪费这个时代**

**链接：** https://x.com/adityaag/status/2074892507306238235  
**时间 / 互动：** 2026-07-08 · 约 345 likes / 57 reposts / 140 bookmarks / 76.7k views · 视频

##### 主帖在说什么

每个创始人都怕「错过这个时刻」；最好的人怕的是**浪费**它。浪费=忽视世界已变、仍用 5 年前纯软件抓价值、只做小事。SPC 想要的人：硬件 tinkerer、mad scientist、biohacker、地下室堆核反应堆那种——摸 grass and atoms。若只做软件，至少要有朋友会嘲笑的异端 thesis。**Apply by Aug 2.**

##### 要点

- miss vs waste 的区分
- 招募画像：atoms / hardware / heresy
- CTA：South Park Commons Founder Fellowship

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@adityaag**（自跟） | 申请链与「Don't waste the moment」 | [post](https://x.com/adityaag/status/2074892952233705956) |
| **@JPBrebner** | 视频里有自己镜头，互动拉近社区 | [post](https://x.com/JPBrebner/status/2074894937267765511) |

##### 一句话概括

用「浪费时代」重新定义 SPC fellowship：极大野心 + 硬科技/异端软件。

---

#### 5. **AI 终局清单：云 agents × 任意模型 × 任意 harness**

**链接：** https://x.com/adityaag/status/2076047290083733539  
**时间 / 互动：** 2026-07-11 · 约 200 likes / 45 replies / 96 bookmarks / 40.7k views

##### 主帖在说什么

他列终局能力：云端跑所有 agents、任选 frontier/OSS/中美模型、任选 harness、全 tracing、递归改进环。他知道「会到」，问的是 **can it happen already?**——催促产品层把碎片拼成默认体验。

##### 要点

- 五件套：cloud agents / multi-model / multi-harness / tracing / recursive improve
- 情绪：不怀疑方向，急于 now
- 隐含：当前栈仍碎片化

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sabhyac267** | 推 omnigent_ai：任意 model×harness×平台 | [post](https://x.com/sabhyac267/status/2076656386197569588) |
| **@ankrgyl** | 无 PMF/用户反馈与 eval 工程会膨胀变慢，不如 just use codex | [post](https://x.com/ankrgyl/status/2076446447546024286) |
| **@loridotsh** | 自称 lori.sh 已做 multi-agent control plane | [post](https://x.com/loridotsh/status/2076138214121771133) |

##### 一句话概括

一张终局清单变成控制平面创业者的开源/产品路演墙。

### Products, launches, people

- **@southpkcommons** Founder Fellowship（Aug 2）；**Bevel_Health**
- **Chip**（@drivewithchip）Day -1 支持
- 模型/工具：Fable、ChatGPT/Codex 体验吐槽；domain-specific OSS coding 模型观察

### Tone

GP 长帖 + 短句判断；文化/野心/经济学并重；夹杂足球与家庭情感帖，整体乐观、直接、略硬核。

---
