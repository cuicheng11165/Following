# Andrej Karpathy (@karpathy)

| Field | Value |
|-------|-------|
| Profile | https://x.com/karpathy |
| Bio | I like training large deep neural nets. |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:09:26Z
- **Posts in window (fetched):** 9 (cap 50: no)
- **Mode:** rewrite with summarize-x-post
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- 与 LLM 协作的「高带宽」输入：长时语音 ramble、意识流、小访谈
- 模型自我意识的预训练来源与滞后（如理解 `/compact`）
- 新模型档位的质变：Fable × three.js 可玩世界、知识→几何/动画
- 推理侧工程：tokens/watt、极低电压域 vs 输电线路类比
- 「AI 腔」污名化波及正当语言结构（em dash 之外）

### Opinions and takes

- 有时你懒得打出足够 bits，就用约 10 分钟 /voice ramble；模型很擅长把混乱意识流整理得比你自己更干净，从而加深 mind meld。
- 模型对自身与工具的自我意识来自人类讨论它们的预训练 token，但滞后且不完整。
- 每个新 model tier 都有质变惊喜；Fable 上 three.js 环境与熊抓鲑鱼等细节是亮点。
- tokens/watt 是「与输电相反」的工程：极低电压高电流（短距离）vs 高压低电流（远距离）。
- 问题不只是 em dash：许多合法、有用的语言构造被武断标为 awkward/cringe。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **长时 ramble session 工作法**

**链接：** https://x.com/karpathy/status/2079610838143623371  
**时间 / 互动：** 2026-07-21 · ❤️ 48.4k · 🔁 4.0k · 💬 2.3k · 👀 3.8M

##### 主帖在说什么

Karpathy 分享一种与 LLM 协作的高信号模式：有时模型需要更多 bits 才理解你的目标，但你懒得打字。他会靠在椅子上切到 `/voice`，连续碎碎念约 10 分钟——意识流、错字、乱七八糟都行。有时开头声明 “switching to speech recognition sorry for any typos…”；有时做成几轮小访谈。他发现模型非常擅长把长而混乱的 ramble 重构得更干净，从而加深 mind meld，后续少纠错。

##### 要点

- 语音 ramble ≈ 用带宽换打字成本
- 可先声明语音输入、或做成 interview 轮次
- 模型「回声」常比你原始思路更干净
- 目标是 mind meld，减少后续纠正

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@mattpocockuk** (Matt Pocock) | 同意多数人只说 what 而省略 why；why 在实现阶段对 tie-break 很有用。ramble 与 interview 都好，他更偏 interview，因为可被有趣地质疑。 | [post](https://x.com/mattpocockuk/status/2079679893479018727) |
| **@lajoiedeslutins** (Jester) | 调侃：花几十年做键盘，赢法却是对着笔记本说话像它欠你房租。 | [post](https://x.com/lajoiedeslutins/status/2079612044790169950) |

（其余大量回复为 meme/附和；工具返回的高信号观点以上为主。）

##### 一句话概括

用长语音意识流给模型喂够 context，换更干净的协作状态与更少纠错。

---

#### 2. **模型对 /compact 的「自我意识」**

**链接：** https://x.com/karpathy/status/2079645572047548608  
**时间 / 互动：** 2026-07-21 · ❤️ 989 · 🔁 11 · 💬 44 · 👀 80k  
**上下文：** 回复 @DavidSHolz 关于模型不懂自身耗时的帖

##### 主帖在说什么

他评论模型自我意识如何从预训练中逐渐「渗出」：来自大量人类讨论模型自身的 token，但滞后且不完整。举例：当他告诉模型准备 `/compact` 其上下文时，模型开始「懂」他在说什么——有趣又好笑。

##### 要点

- 自我意识 ≈ 预训练中人类讨论模型的副产品
- 滞后 + 不完整
- 工具约定（如 /compact）会被逐渐内化

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@DavidSHolz** (David) | 几乎想要「早期 Claude」在部署前给后来的 Claude 写一份手册。 | [post](https://x.com/DavidSHolz/status/2079646019198042291) |
| **@gustavokov** (Gustavo Noronha) | 会先问模型是否 OK compact——这会触发该保存哪些细节到 memory、以免 compact 丢失的反思。 | [post](https://x.com/gustavokov/status/2079663942880600574) |

##### 一句话概括

模型对工具与自身的理解来自「人类谈论它们」的预训练，会慢慢跟上产品原语（如 /compact）。

---

#### 3. **Fablemaxxing：three.js 可玩世界**

**链接：** https://x.com/karpathy/status/2073505440479293773  
**时间 / 互动：** 2026-07-04 · ❤️ 270 · 🔁 10 · 💬 12 · 👀 24k  
**上下文：** 回复 @petergostev 的 Fable demo 视频讨论

##### 主帖在说什么

他同意这是 top-tier fablemaxxing：每个新 model tier 都有质变惊喜；Fable 迄今 three.js 环境最出彩。熊抓鱼是奇怪而生动的细节，鱼在嘴里还在挣扎。他追问：LLM 如何从互联网知识学会这些，再转成坐标、mesh、变换、动画、特效、交互与小故事？并想象 +1/+2/+3 档模型还能创造什么。

##### 要点

- 每档模型有独特「质变惊喜」
- Fable 的 three.js 可玩世界是当前亮点
- 知识 → 3D/动画/交互 的端到端能力令人惊叹
- 期待更高 tier 的创作上限

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@petergostev** (Peter Gostev) | 自己最爱「步入画中」式生成；抽象出新世界的能力是另一层级。 | [post](https://x.com/petergostev/status/2073502172801835454) |
| **@MFrancis107** (Michael Francis) | 不买账：更大模型 = 更多记忆；水 shader 等网上可抄，更像 memorization 而非技能跃迁。 | [post](https://x.com/MFrancis107/status/2073514993602134081) |

##### 一句话概括

Fable 把互联网知识压成可玩 three.js 世界，被视作本代质变；也有人质疑只是记忆而非能力。

---

#### 4. **tokens/watt 推理工程（Etched）**

**链接：** https://x.com/karpathy/status/2072061140943921550  
**时间 / 互动：** 2026-06-30 · ❤️ 1.7k · 🔁 49 · 💬 23 · 👀 105k  
**上下文：** 祝贺 @Etched 出 stealth

##### 主帖在说什么

祝贺 Etched，并点评 LLM 服务侧工程：极低电压域、集群级内存等，目标是在 interactive tokens/sec/user 下 max tokens/watt。他特别记住的类比：这是与输电线路「相反」的工程体制——极低电压高电流（极短距离）vs 高压低电流（远距离）。

##### 要点

- 推理效率核心指标：tokens/watt（兼 interactive latency）
- 极低电压域 + 集群内存等是关键手段
- 物理直觉：短距高电流 vs 远距高压

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Etched** | 期待继续一起深聊。 | [post](https://x.com/Etched/status/2072067419196293320) |
| **@robertwachen** (Robert Wachen) | 一起 nerd out 很有趣；预期会看到更大 scale-up domain。 | [post](https://x.com/robertwachen/status/2072068161693012474) |
| **@__tinygrad__** (the tiny corp) | 对宣传持怀疑：若技术人在回复里夸，请交叉核对（付费）顾问名单——像 crypto 套路。 | [post](https://x.com/__tinygrad__/status/2072235314547167380) |

##### 一句话概括

在 interactive 服务约束下 max tokens/watt 是「反输电」的物理与系统工程；社区对商业叙事也有交叉验证压力。

---

#### 5. **合法语言结构被标成 cringe**

**链接：** https://x.com/karpathy/status/2077433347085930882  
**时间 / 互动：** 2026-07-15 · ❤️ 4.2k · 🔁 97 · 💬 219 · 👀 238k  
**上下文：** 回复 @btaylor 对 em dash 被 AI 污名化的抱怨

##### 主帖在说什么

问题不只是 em dash：许多正当且有用的语言构造突然、有些武断地变得 awkward 和 cringe——「AI 腔」污名化波及真实写作习惯。

##### 要点

- 污名范围 > em dash
- 合法修辞被「AI 探测器文化」误伤
- 写作自由被武断美学约束

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bizjakblaz93** (Blaž Bizjak) | 「It's not just X. It's [更戏剧性的 Y]」这种结构也杀伤力巨大，现在到处都是。 | [post](https://x.com/bizjakblaz93/status/2077495303930892474) |
| **@softmaestro** (Nate Codes) | triad（三项法则）、「not x, y」、整体句式形状；现在甚至讨厌 “honestly” 这个词。 | [post](https://x.com/softmaestro/status/2077459786623283399) |

##### 一句话概括

反 AI 腔正在误伤一整套仍有用的英文修辞，而不只是破折号。

---

### Products, launches, people

- **Fable** / three.js 可玩世界（@petergostev demo）
- **Etched** 推理集群出 stealth（tokens/watt）
- 工具约定：`/voice`、`/compact`
- 对话相关：@DavidSHolz、@btaylor、@mattpocockuk

### Tone

克制、好奇、略带戏谑；偏第一性原理与可复用工作流洞见。发帖量少但单帖信号极高（尤其 ramble 长帖破千万曝光）。
