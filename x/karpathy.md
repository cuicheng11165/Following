# Andrej Karpathy (@karpathy)

| Field | Value |
|-------|-------|
| Profile | https://x.com/karpathy |
| Bio | I like training large deep neural nets. |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T19:28:25Z
- **Posts in window (fetched):** 9 (cap 50: no)
- **Mode:** 30-day backfill (rewrite of existing window)

### Themes

- 与 LLM 协作的工作流：长时「碎碎念」语音输入、上下文压缩（/compact）与模型元认知的滞后
- 模型能力跃迁：Fable 等在 three.js 可玩世界、知识→代码→动画上的质变
- 语言风格与「AI 腔」：破折号等正当表达被污名化、显得尴尬
- 推理侧工程：tokens/watt、极低电压域与集群级内存
- 社群噪音：澄清推特误信息、调侃用改 bio 代替长文官宣

### Opinions and takes

- 认为「长时间 ramble + 语音」能与 LLM 建立 mind meld：模型擅长把杂乱意识流整理得比你自己更干净。
- 模型对自身与工具的自我意识来自预训练中人类讨论它们的文本，但滞后且不完整。
- Fable 级模型能把互联网知识转成可交互 three.js 小世界（熊抓鲑鱼等细节）令人惊叹，并期待更高档次。
- 不仅是 em dash，许多合法、有用的语言结构正被武断地标为 cringe。
- 对「swear meter」作为 eval 信号很感兴趣，并追问是否基于字符串 grep。

### Notable posts

1. **长时 ramble session 工作法**  
   他分享一种与 LLM 协作的模式：有时你懒得打出足够多的 bits 让模型理解目标，就靠在椅子上切到 /voice，连续碎碎念大约 10 分钟，意识流、错字、乱七八糟都行。有时会先声明「switching to speech recognition sorry for any typos…」，有时做成几轮小访谈。他发现模型非常擅长把长而混乱的 ramble 重构得更干净，从而加深 mind meld、后续少纠错。  
   链接：https://x.com/karpathy/status/2079610838143623371

2. **模型对 /compact 的「自我意识」**  
   他评论模型的自我意识如何从预训练中逐渐渗出：来自大量人类讨论模型自身的 token，但滞后且不完整。举例说，当他告诉模型准备 /compact 其上下文时，模型开始「懂」他在说什么，觉得有趣又好笑。  
   链接：https://x.com/karpathy/status/2079645572047548608

3. **Fable 生成可玩 three.js 世界**  
   他惊叹模型能创造出融合知识与代码的丰富可玩世界；特别提到约 43 分钟处熊抓鲑鱼的细节。后续又说每个新 model tier 都有质变惊喜，Fable 上 three.js 环境与熊/鱼的物理细节是亮点，并想象 +1/+2/+3 档模型还能做出什么。  
   链接：https://x.com/karpathy/status/2073499112876761166

4. **tokens/watt 推理工程**  
   祝贺并点评 LLM 服务侧工程：极低电压域、集群级内存等为在 interactive tokens/sec/user 下 max tokens/watt。他觉得特别好玩的是：这是与输电线路「相反」的工程体制——极低电压高电流（极短距离）vs 高压低电流（远距离）。  
   链接：https://x.com/karpathy/status/2072061140943921550

5. **合法语言结构被标成 cringe**  
   他指出问题不只是 em dashes：许多正当且有用的语言构造突然、有些武断地变得 awkward 和 cringe，反映「AI 腔」污名化波及真实写作习惯。  
   链接：https://x.com/karpathy/status/2077433347085930882

6. **辟谣与官宣方式吐槽**  
   他否认推特上流传的误信息（「weird misinformation… no」）。另帖调侃：宣布大事的正确方式不该是改 bio，而应发那篇他刚和团队分享的 10 段长文。  
   链接：https://x.com/karpathy/status/2081193667529003247  
   链接：https://x.com/karpathy/status/2081195664479068350

7. **swear meter 作 eval**  
   他喜欢「swear meter」的想法，认为可能是很强的 eval 信号，并追问这些是不是基于字符串的 grep。  
   链接：https://x.com/karpathy/status/2074951886969725413

### Products, launches, people

- **Fable** 模型与 three.js 可玩环境演示
- 推理/服务侧工程（tokens per watt、集群内存）
- 语音与 LLM 交互模式（/voice、/compact）

### Tone

克制、好奇、略带戏谑；偏第一性原理的技术观察，偶尔辟谣。高赞帖多为可复用的工作流洞见。
