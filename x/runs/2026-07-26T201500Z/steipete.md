# Peter Steinberger (@steipete)

| Field | Value |
|-------|-------|
| Profile | https://x.com/steipete |
| Bio | Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:15:00Z
- **Posts in window (fetched):** 50（cap 50: yes；高频发帖，列表偏窗口后半段）
- **Mode:** 30-day backfill
- **Cursor:** per-builder（本 run 不更新 state）
- **Notable method:** `summarize-x-post`（`x_thread_fetch` per item）

### Themes

- OpenClaw 产品工程：并行 QA、subagents、release、品牌统一、招人
- Codex / GPT-5.6 Sol 与 harness 实战（graph 工作流、意图理解、compaction）
- agent skills：autoreview 长循环重构；CLI 直连绕过工具 schema 漂移
- 对 hype→唱衰钟摆的反应：忽略噪音，继续做 dream harness
- 社区：Slack 用户会「喊」、Discord clawtributors、Boston 旅行
- 架构碎片：agents 经 Tailscale SSH + tmux + presence 路由解锁提示

### Opinions and takes

- 竞争对生态有好处；「我 review 的是 PR，不是 subagents」
- 新模型可能让工具调用变差——OpenClaw 增加直接走 Claude CLI 的 code path
- hype 与 boo 都是钟摆过冲；用噪音时段建 dream harness
- 对 Google 员工是否有产品限额的玩笑式追问（对方答：周末用个人号真实体验）
- 邮件积压到「email bankruptcy」——别等他回邮件

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **Autoreview skill：66 轮啃难重构**

**链接：** https://x.com/steipete/status/2080899298838098034  
**时间 / 互动：** 2026-07-25 · 约 1.2k likes / 63 replies / 1.7k bookmarks / 147k views

##### 主帖在说什么

他公布 OpenClaw **autoreview** skill 的新纪录：在一次「gnarly refactor」上跑了 **66 轮**自动审查循环，并链到技能定义：`github.com/openclaw/agent-skills/.../autoreview/SKILL.md`。重点不是单次补丁，而是把 review 做成可持续、可配置的 agent skill。

##### 要点

- 指标：66 rounds on hard refactor
- 资产：开源 agent-skills 仓库中的 autoreview
- 隐含主张：长循环 QA 是 harness 竞争力

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@BenKraus** | 该 skill 是自己「少 slop」的最大贡献者，也是需要多账号的原因（配额/并行） | [post](https://x.com/BenKraus/status/2080902502653018458) |
| **@elshayib_** | 问 Hermes 出来后是否还有人用 autoreview | [post](https://x.com/elshayib_/status/2080903017784562174) |

（另有大量求邮件回复等低信号互动。）

##### 一句话概括

用 66 轮 autoreview 证明：防 slop 靠长循环 skill，不是靠一次「写完就过」。

---

#### 2. **「我现在是 graph engineer 了吗」**

**链接：** https://x.com/steipete/status/2080779917130858598  
**时间 / 互动：** 2026-07-24 · 约 4.9k likes / 223 replies / 5.8k bookmarks / 759k views

##### 主帖在说什么

引用 OpenAI harness 工程 **@alex_frantic** 的教程：用 Codex + 5.6 Sol「graph-max」——任意工具画图 → 让 Codex 写成 code-mode 脚本并跑通。Peter 配上自己的图，自嘲 **am I a graph engineer now**，把新工作流身份化、meme 化。

##### 要点

- 工作流：手绘/工具图 → Codex 实现 → 直接跑
- 模型栈：Codex + GPT-5.6 Sol
- 语气：高传播自嘲，推动社区跟做

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@luckeyfaraday** | 开源 athena-graphs 供人 tinkering graph engineering | [post](https://x.com/luckeyfaraday/status/2080800603945464083) |
| **@pdp** | 预言下周会被改名叫 topology orchestration | [post](https://x.com/pdp/status/2080781338634805568) |
| **@neoworldlife** | 「Graph engineer certification pending」 | [post](https://x.com/neoworldlife/status/2080845696534766006) |

##### 一句话概括

一张图 + 一句自嘲，把 Sol/Codex 的「画流程图即实现」推成全网 job title meme。

---

#### 3. **Hype 之后是 boo：钟摆过冲时建 dream harness**

**链接：** https://x.com/steipete/status/2080431240520384760  
**时间 / 互动：** 2026-07-23 · 约 401 likes / 46 replies · 回复 @maxmax 对 OpenClaw 被低估的辩护

##### 主帖在说什么

在有人问「为何大家都表现得好像 OpenClaw 不是巨大进步」之后，他回应：疯狂 hype 之后是疯狂唱衰，像钟摆甩过头。他选择**大体忽略**，把这段时间用来建 **dream harness**——情绪周期不进产品决策。

##### 要点

- 诊断：hype ↔ boo 过冲
- 策略：ignore noise → ship harness
- 上下文：OpenClaw 被 always-on agent 生态「偷走」的理念

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Ahsann_** | 从 1 月用到现在，更可靠；solo founder 最好工具之一 | [post](https://x.com/Ahsann_/status/2080477743871889842) |
| **@kevincodex** | 追问 dream harness 长什么样 | [post](https://x.com/kevincodex/status/2080467556448731247) |
| **@gladstein** | 强调对 freedom AI 的巨大进步 | [post](https://x.com/gladstein/status/2080462459765448813) |

##### 一句话概括

不接唱衰战，把注意力锁在 harness 工程上——这是他公开的情绪与产品策略。

---

#### 4. **「Google 员工也有额度？」**

**链接：** https://x.com/steipete/status/2081196406854050071  
**时间 / 互动：** 2026-07-26 · 约 1.2k likes / 25 replies / 112k views

##### 主帖在说什么

DeepMind / AI Studio 的 Dmitry 晒个人 Antigravity 订阅烧到限额（「71h 好太远」）。Peter 只回一句：**You have limits for employees at Google?**——用玩笑戳穿「大厂员工无限算力」的刻板印象。

##### 要点

- 触发：大厂员工晒个人订阅耗尽
- 一句话反问：公司是否仍限员工额度
- 传播：高 likes，讨论转向「真实用户体验」

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@LyalinDotCom** | 内部资源很多；周末用自己设备、个人号付费，才能发现「特权账号」看不到的问题 | [post](https://x.com/LyalinDotCom/status/2081201128172118169) |
| **@lastusername123** | 补充：对方已说明用个人号是为了感受真实产品 | [post](https://x.com/lastusername123/status/2081198220919636130) |

##### 一句话概括

一句吐槽引出产品人共识：要找 bug，得像普通付费用户一样被限流。

---

#### 5. **模型更好、工具更差：直接走 Claude CLI**

**链接：** https://x.com/steipete/status/2080318789980201224  
**时间 / 互动：** 2026-07-23 · 约 287 likes / 24 replies / 111k views

##### 主帖在说什么

引用 Armin Ronacher 文章：新 Opus/Sonnet 在 Pi 的 edit tool 上出现旧模型没有的 tool invocation 失败。Peter 确认 OpenClaw **也观察到**，并加了**直接调用 Claude CLI** 的 code path——「hard to fight the system」：与其跟模型偏好的 schema 硬刚，不如走官方 CLI 集成面。

##### 要点

- 现象：新模型 × 自定义工具 schema 更易失败
- 对策：CLI 直连旁路
- 哲学：不硬刚系统，绕过去

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@shoriful_dev** | 若模型对 Claude Code schema 强 RL，CLI 可避开 mismatch；问 strict mode 能否单独修好 | [post](https://x.com/shoriful_dev/status/2080359013234123228) |
| **@i_mika_el** | 迟早「直连 Claude CLI」会变成正式集成形态 | [post](https://x.com/i_mika_el/status/2080320763047882792) |
| **@lajoiedeslutins** | 金句：can't fight the system, can only cli around it | [post](https://x.com/lajoiedeslutins/status/2080319332123369520) |

##### 一句话概括

新模型可能破坏工具契约时，实用派答案是：CLI 旁路，而不是死磕 prompt。

### Products, launches, people

- **OpenClaw** / **OpenClaw agent-skills**（autoreview）；**Codex** / **GPT-5.6 Sol**；Claude CLI
- **@alex_frantic** graph-max；**@mitsuhiko** 工具退化文章；**@LyalinDotCom** 个人订阅故事
- 基建碎片：Tailscale + SSH + tmux + presence 路由

### Tone

高频、工程向、meme 与德/英语混用；对社区抱怨直接、对 hype 冷静；像「在 X 上 live 写 harness 日志」的 ClawFather。

---
