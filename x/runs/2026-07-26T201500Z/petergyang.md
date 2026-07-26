# Peter Yang (@petergyang)

| Field | Value |
|-------|-------|
| Profile | https://x.com/petergyang |
| Bio | Practical AI tutorials and interviews for busy people |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:09:26Z
- **Posts in window (fetched):** 40 (cap 50: no)
- **Mode:** rewrite with summarize-x-post
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **Jason Liu（@jxnlco）× Codex 工作系统**访谈：chief of staff、skills、heartbeat、可验证目标
- **ChatGPT Voice × Codex**：床上语音编排多 thread；多 Voice 线程「团队」愿景
- 模型评论转发：@kunchenguid 论 Opus 5 / benchmark 失效 / RLHF 淡化
- Indie 软件变现难：纯软件需 + 服务等；求反例
- 产品反馈：ChatGPT 长会话卡顿、Voice 在 Codex 的线程管理与中文发音

### Opinions and takes

- 引用金句：「唯一剩下的工作是理解你不喜欢什么，说清楚，告诉 AI。」
- Codex 用例：从 Slack 学说话方式做 skill；thread→heartbeat 扫邮件/Slack/Linear；订票值机发登机牌。
- 躺床上用 Voice 指挥 Codex 很爽；关键是记住长跑 thread 名字。
- 同意「做产品 10x 容易、赚钱 100x 难」：纯软件对 indie 很难 monetize，常需 software + services。
- 转发 Kun：公共 benchmark 近乎无用；应信私有域评测；「好不好用」维度 Claude 不再领先。
- 预测一年内语音控电脑成主流，键鼠「去牧场」。
- 下一进化：多 Voice 线程组成互相说话的「全团队」。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **访谈：Jason Liu 的 Codex 全工作系统**

**链接：** https://x.com/petergyang/status/2081382827548148091  
**时间 / 互动：** 2026-07-26 · ❤️ 134 · 🔁 5 · 💬 15 · 🔖 107 · 👀 15k

##### 主帖在说什么

发布与 OpenAI DevEx **@jxnlco** 的新一集：他如何在工作日全天使用 Codex——搭 Slack/邮件首席参谋、把过往 session 变成 skills、给长跑项目可验证目标。示例 prompt：读一周自己的 Slack 学说话方式；把 thread 变成 heartbeat 查邮件/Slack/Linear 做优先级；找机票值机并把登机牌发到手机。强调 Jason 写了官方 Codex 工作手册。并附 Spotify/Apple/Newsletter 链接。

##### 要点

- 内容产品：可执行工作流 > 模型八卦
- Skills 从历史行为蒸馏
- Heartbeat = 定时上下文扫描
- 跨媒体分发（视频+播客+通讯）

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@petergyang**（自续） | Spotify / Apple / Newsletter 深度阅读入口。 | [post](https://x.com/petergyang/status/2081382839795560637) |
| **@DakshMalik47** | 轻松向：他终于有平台好好讲了。 | [post](https://x.com/DakshMalik47/status/2081384911685165537) |

##### 一句话概括

把 OpenAI 内部 Codex「工作操作系统」拆成可抄作业的 skills + heartbeat + 可验证目标。

---

#### 2. **Heartbeat 深挖：定时优先级 + 预起草回复**

**链接：** https://x.com/petergyang/status/2081462078758592947  
**时间 / 互动：** 2026-07-26 · ❤️ 11 · 🔁 2 · 💬 3 · 👀 3.6k

##### 主帖在说什么

从同一访谈抽出可执行句：把 thread 变成 heartbeat，在 9am/1pm/5pm 检查邮件、Slack、Linear，告诉你优先级。Jason 说：仅此就能对一天有不错概览；再叠偏好——先缺链接就补链接，再接 Linear，现在已预起草 Slack/邮件回复。

##### 要点

- 日程化 agent 检查点
- 渐进式偏好叠加
- 从摘要跨到预起草 = 真劳动替代

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@serxzsz** | 一天三次 check-in 并起草回复不是委派，是被 bot 管理。 | [post](https://x.com/serxzsz/status/2081463640452964650) |
| **@Cranefomo** | 预起草 Slack 是摘要工作流跨入真劳动；仅当模型学会语气后才不重写。 | [post](https://x.com/Cranefomo/status/2081462806872809769) |

##### 一句话概括

Heartbeat 把 Codex 从聊天变成日节奏 OS；边界是「辅助」还是「被管理」。

---

#### 3. **转发 Kun：Opus 5 与 benchmark 失效**

**链接：** https://x.com/petergyang/status/2081132101441823068  
**时间 / 互动：** 2026-07-25 · ❤️ 484 · 🔁 8 · 💬 7 · 🔖 377 · 👀 184k  
**引用：** @kunchenguid 长文

##### 主帖在说什么

Peter 背书：朋友 Kun 的模型分析是他见过最好的之一，请读原文。Kun 要点包括：公共 benchmark 几乎无用（Opus 榜高但实用远不如 Fable）；5 系疑似 mythos 蒸馏路径影响质量；「好不好用」Claude 不再强，Grok/Kimi 更愉快；lab 偏 machine-verifiable RL 轻 RLHF，模型更 jargon、更需 steering——甚至质疑 alignment 是否已在失败。

##### 要点

- 策展型影响力：放大高质量第三方分析
- 实践评测 > 公榜
- 「愉快度」成为选型维度

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@zhang_tom12103** | 最准分析来自天天用的人；X 上最火的常是零订阅观众。 | [post](https://x.com/zhang_tom12103/status/2081255060114149498) |
| **@SandorDardin** | Fable 后知识工作输出更「机器」、缺温度；硬加温度又成小说 slop。 | [post](https://x.com/SandorDardin/status/2081446022027399199) |

##### 一句话概括

用策展放大「公榜失效 / 蒸馏副作用 / 愉快度下降」的一线模型批评。

---

#### 4. **床上 Voice 指挥 Codex**

**链接：** https://x.com/petergyang/status/2080793867960643823  
**时间 / 互动：** 2026-07-24 · ❤️ 150 · 🔁 5 · 💬 41 · 👀 17k

##### 主帖在说什么

体验报告：躺床上对 ChatGPT Voice 说话、让它在 Codex 里干活很棒。要做好，你得记住所有长跑 thread 的名字。另帖补充 Voice 初印象：它是编排其他 thread 的 orchestrator；要明确 “start new thread” / “use thread A”，否则请求会糊进一个 thread；其他 thread 工作时语音静默，破坏沉浸。

##### 要点

- Voice = 多 agent 编排入口
- Thread 命名是关键 UX 技能
- 静默等待破坏对话感

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Entrepenulian** (Julian) | 把 thread 命名为 1–5；语音未来很上瘾。 | [post](https://x.com/Entrepenulian/status/2080799372284158270) |
| **@phorne96** (Patrick) | 给 thread 真人名，像带团队：「让 James 做财报，问 Sandra 度假计划」。 | [post](https://x.com/phorne96/status/2080833792093327870) |
| **@vthallam** (Venkatesh Thallam) | 可直接问「做 X 的是哪个 thread」，它会找到并更新。 | [post](https://x.com/vthallam/status/2080801530899489197) |

##### 一句话概括

Voice+Codex 把「躺着指挥 agent 团队」变成可行工作流，瓶颈是 thread 身份与反馈。

---

#### 5. **纯软件难 monetize？求反例**

**链接：** https://x.com/petergyang/status/2080669643577176573  
**时间 / 互动：** 2026-07-24 · ❤️ 99 · 🔁 4 · 💬 31 · 👀 19k  
**引用：** @damonchen「做产品 10x 易，赚钱 100x 难」

##### 主帖在说什么

倾向同意：对 indie 而言纯软件现在很难 monetize，往往需要 software + 别的（如服务）。求回复里的反例。后续也追问 channel-market-fit（消费/prosumer 在社交/SEO 之外是什么）。

##### 要点

- 供给爆炸 → 变现更难
- 捆绑服务作默认假设
- 开放征集反例与分发讨论

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@nurijanian** (George) | 分发一直比产品重要；现在更难因供给上升。分发 = 营销+广告+**channel market fit**，不是只会 SEO/社媒。Indie 常给其他 indie 做题，社区问题枯竭。 | [post](https://x.com/nurijanian/status/2080775422808322264) |
| **@ChiderArinze** | 反例：Pieter Levels、Caleb Porzio、Tony Dinh 等——特定受众 + 真分发 + 愿付费问题；泛化工具才难卖。 | [post](https://x.com/ChiderArinze/status/2080721293662450168) |

##### 一句话概括

AI 让造船变便宜后，indie 胜负手更在分发与「软件+X」，而非再做一个通用 SaaS。

---

### Products, launches, people

- 播客/通讯：**Behind the Craft** / creatoreconomy.so；赞助 Riverside、Google AI Studio
- **Codex**、**ChatGPT Voice**、**ChatGPT Work** 体验
- 人物：@jxnlco、@kunchenguid、@guinnesschen、@theteriyu、@damonchen
- 反馈对象：ChatGPT 移动长会话卡顿（@JustinBleuel 跟进）

### Tone

实践派创作者：访谈拆解 + 亲测工作流 + 转发高质量分析；语气轻松、爱用 🔥/😅，持续收集用户与变现反例。
