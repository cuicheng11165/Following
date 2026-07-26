# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude Code @anthropicai |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:09:26Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** rewrite with summarize-x-post
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **组织级 AI 采用四阶段** 与 ROI 度量
- 把领域知识编成基础设施：CLAUDE.md / skills / REVIEW.md / loops
- **Opus 5**：编码与知识工作 + **抗 prompt injection**（叠防御 ~0 成功率）
- Claude Code 产品：`/checkup`、Artifacts 扩 Pro/Max、Fable 动态工作流优化
- 安全与 harness：Auto Mode、探针、自动化 code/security review
- 社群：科幻书单、澄清勿误归其言、Claude Code 起源故事

### Opinions and takes

- 常见现象：一人用 Claude 10x，组织其余人未跟上——采用有可映射的 4 步。
- 升阶靠拆瓶颈 + 建护栏，而非堆 token；要端到端自验证、auto permissions、多 agent 界面、`/loop` `/batch` 等。
- 度量应看「本来会不会花工程时间 / 值多少 eng-hours」，而非纯 usage。
- 自动化从「每次修同类 bug」升级为 lint/CI/例程永久消灭整类工作；领域知识应写入 CLAUDE.md 等，使 agent 零额外 context 也能贡献。
- Opus 5 最令他兴奋的不是榜，而是最难 prompt inject；对齐 + 探针 + Auto Mode 叠层后攻击成功率近 0。
- 日常优化口令：Fable + dynamic workflow + profiler，不达 p95 目标不停。
- 过度注释可用一行写入 CLAUDE.md 约束。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **AI 采用四阶段（Steps of AI Adoption）**

**链接：** https://x.com/bcherny/status/2077929379661844559  
**时间 / 互动：** 2026-07-17 · ❤️ 10.3k · 🔁 958 · 💬 417 · 🔖 17k · 👀 1.4M

##### 主帖在说什么

他每天与他司工程师交流，听到同一件事：有人用 Claude 把产出 10x，组织其余人没跟上。观察团队采用 AI 时反复看到相同 **4 步**，并给出映射图「Steps of AI Adoption」。线程续帖：无唯一路径；每步靠拆瓶颈与建护栏而非堆 token。实践上要让 Claude 端到端自验证、开 auto mode、默认自动化 code/security review、用多 agent 界面（CLI Agent view、Desktop、iOS/Android、Tag）；更高阶用 `/loop` `/batch`、dynamic workflows、worktree 隔离。ROI 不看 usage 而看「是否本就该花工程时间 / 省多少 eng-hours」。最大收益是修复维护在后台、团队专注建造；Anthropic 在 step 3 冲 4，他个人刚到 level 4。

##### 要点

- 组织采用不均是常态
- 四阶段框架 + 护栏/瓶颈视角
- 自验证与多 agent 是升阶条件
- ROI = 替代的真实工程小时
- 后台自治维修 unlock 新能力边界

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bcherny**（线程） | tokens 不够用；要 verify / auto mode / 多 agent / loop·batch·worktree。 | [post](https://x.com/bcherny/status/2077929390806073807) |
| **@terminalxw** (Saurav) | 批评沟通与听用户反馈变差，粉丝好感在消退。 | [post](https://x.com/terminalxw/status/2077929868344631619) |

##### 一句话概括

把「个人 10x / 组织落后」收成可操作的四阶段采用地图，核心是护栏与自治闭环而非烧 token。

---

#### 2. **把领域知识编成基础设施（CLAUDE.md 时代）**

**链接：** https://x.com/bcherny/status/2077460395279692197  
**时间 / 互动：** 2026-07-15 · ❤️ 10.0k · 🔁 898 · 💬 392 · 🔖 10k · 👀 1.7M

##### 主帖在说什么

过去顶尖工程师花大量时间自动化：vim/emacs、lint、e2e，以自乘产出。如今更重要：① DevX/infra 加速你与 agent 大军；② 把「每次用 token 修同类问题」变成 lint/CI/例程，永久消灭整类 busywork——这就是人们说的 loops；③ 自动化让他人（含非工程师）日一即可贡献；挡路的是装在人脑子里的领域知识。Agent 时代可编码的知识远超类型/测试：comments、skills、CLAUDE.md、memories。PR 因「没用对框架/架构」被拒，是自动化失败。每个团队应写 CLAUDE.md / REVIEW.md / skills / docs，使 agent 无需提示者额外 context 也能高效工作——这是工程师一贯做的「自动化 + 把知识变基础设施」的自然延伸。

##### 要点

- 自动化 ROI 在 agent 军队下放大
- loops = 消灭问题类，非单次修复
- 领域知识 → CLAUDE.md / skills / memories
- 评审失败常是 harness/文档失败
- 标准之争（AGENTS.md 等）在回复中爆发

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@heyvishal_** | 2026 了为何还不用统一 **AGENTS.md**。 | [post](https://x.com/heyvishal_/status/2077476731745956281) |
| **@kupolov** (Ted Kupolov) | 好开发者也跟标准与开源；问 AGENTS.md。 | [post](https://x.com/kupolov/status/2077475565679124565) |
| **@KonradRzonca** | 吐槽 .codex / .agents / .github 与各仓复制 md 地狱，缺共同标准与 registry。 | [post](https://x.com/KonradRzonca/status/2077471611041591684) |

##### 一句话概括

agent 时代最高杠杆仍是「自动化 + 编码领域知识」；格式碎片化成了新瓶颈。

---

#### 3. **Opus 5：抗 prompt injection 才是亮点**

**链接：** https://x.com/bcherny/status/2080713091688583312  
**时间 / 互动：** 2026-07-24 · ❤️ 6.1k · 🔁 471 · 💬 330 · 👀 611k  
**引用：** @claudeai Opus 5 SOTA 评测图

##### 主帖在说什么

Opus 5 适合 coding、数据分析、设计、生物、知识工作。但比 eval 分数更令他兴奋的是：它是迄今 **最难成功 prompt inject** 的模型（system card 里略埋没）。叠层防御——强对齐 + PI 探针 + Claude Code **Auto Mode**——后，prompt injection 攻击成功率降到约 **0**。称这是新且令人兴奋的事，预告更多内容。

##### 要点

- 能力面广，但安全属性是 headline
- 模型对齐 ≠ 唯一防线；要叠探针与产品 Auto Mode
- ~0 成功率是组合结果
- Elon 等高层互动抬高曝光

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@elonmusk** | “Very impressive”。 | [post](https://x.com/elonmusk/status/2080720634347176003) |
| **@jjferman** (JJ Ferman) | 质疑/核对图表数学（截图）。 | [post](https://x.com/jjferman/status/2080716890503008446) |
| **@vedolos** | 求 usage reset（产品配额压力）。 | [post](https://x.com/vedolos/status/2080713813582905537) |

##### 一句话概括

Opus 5 的差异化叙事从榜单转向「几乎注不进 prompt」的多层防御栈。

---

#### 4. **Fable + dynamic workflow 优化 p95**

**链接：** https://x.com/bcherny/status/2080172448314790016  
**时间 / 互动：** 2026-07-23 · ❤️ 1.5k · 🔁 61 · 💬 52 · 🔖 1.4k · 👀 98k  
**上下文：** 回复 @rauchg 关于 Fable 找 Turbopack/Next 内存优化

##### 主帖在说什么

他现在优化代码大致就是一句话：“Hey fable, use a dynamic workflow to get p95 time down under 300ms. Dont stop till you’re done, use a profiler”。目标导向 + 不停 + 用 profiler，而不是手工微操每一步。

##### 要点

- 目标（p95）写进 prompt
- dynamic workflow + 持续跑到达标
- 强制用 profiler，非猜

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Kikser1214** | 类比为对吃面包喝水的人炫耀开兰博基尼——可达性鸿沟。 | [post](https://x.com/Kikser1214/status/2080209820594913366) |
| **@JasonCh96059300** | 别给要「一个肾」才能跑的建议；Anthropic 无限预算，普通人不是。 | [post](https://x.com/JasonCh96059300/status/2080279178948104621) |
| **@dmnc_eu** (Dominic) | Fable 约一小时就打满 20× Max 限额，不可持续。 | [post](https://x.com/dmnc_eu/status/2080291657233183121) |

##### 一句话概括

顶级用户把性能优化外包给 Fable 闭环；社区同时尖锐指出成本与配额现实。

---

#### 5. **一行 CLAUDE.md 关掉过度注释**

**链接：** https://x.com/bcherny/status/2080731329990377755  
**时间 / 互动：** 2026-07-24 · ❤️ 108 · 🔁 5 · 💬 4 · 👀 10k  
**上下文：** 用户抱怨模型仍倾向 over-comment

##### 主帖在说什么

给出可执行一行：`echo "Avoid code comments unless your are explicitly asked to add comments" >> CLAUDE.md`——用项目级指令压默认注释癖。

##### 要点

- 偏好应用 CLAUDE.md 而非每次口头说
- 默认「少注释」可配置
- 与「领域知识进基础设施」主题一致

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@nathanv246** (Nate) | 他更偏向「更好注释」指令（讲 why/不变量）；或许 Claude 基线偏多注释，需更严。 | [post](https://x.com/nathanv246/status/2080736636422455793) |
| **@Semmonix** (The Baron) | 称 CLAUDE.md/memory/hook/skill 仍不够，不显式二次提示仍会注释——怀疑是耗 token 设计。 | [post](https://x.com/Semmonix/status/2080949138284331306) |
| **@datawanderer0** | 为何不默认？依赖 CLAUDE.md 非确定性。 | [post](https://x.com/datawanderer0/status/2080764857096483201) |

##### 一句话概括

小偏好也该进 CLAUDE.md；但社区反馈显示指令遵循仍不稳定。

---

### Products, launches, people

- **Claude Code**：`/checkup`、Artifacts（Pro/Max）、Auto Mode、Tag、Desktop/移动
- **Opus 5** / **Fable**；Making of Claude Code 故事
- 文档：AI Adoption steps；临时 Google Doc 分享
- 人物：@claudeai、@rauchg、@jarredsumner（Bun in Rust）、@elonmusk

### Tone

高密度方法论长帖 + 产品经理式 ship 笔记；对安全与组织采用特别认真。回复区常混「膜拜工作流」与「配额/成本/标准碎片」的反压。
