# Aaron Levie (@levie)

| Field | Value |
|-------|-------|
| Profile | https://x.com/levie |
| Bio | ceo @box - your business lives in content. unleash it with AI |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Background agents and swarms, not chat, will consume almost all tokens, on the order of 1,000x one-at-a-time prompting, and the compute plus computers, networks, and file systems are still early.
- Being polite to models is a cheap bet even if you reject consciousness, because training data and live traces will include those interactions.
- Box's own evals show Sonnet 5.5 and Opus 5.5 as large jumps on enterprise knowledge work, with concrete point gains and token cuts by vertical.
- Outside coding, enterprise agent adoption is still bimodal and early: workflows have to be rebuilt, and embedded FDEs are how that happens.
- Cyber, agent identity, evals, and legacy systems were the recurring topics in a couple dozen CIO-level meetings.
- Box Mount puts governed Box files into agent sandboxes (Vercel Sandbox, OpenAI Agents API) so agents read and write like a person would.
- Price cuts on Opus 5.5 and GPT-6 Sol and Luna are Jevons paradox for agents: cheaper tokens open more workloads.

### Opinions and takes

- "Agents spawning other agents, agents operating in the background on every task, and agent swarms will consume 1,000X more tokens than people prompting agents 1 at a time." — https://x.com/levie/status/2108750943680630893
- "Just be nice to the AI." — https://x.com/levie/status/2108426594054533545
- "You can’t automate what you can’t measure." — https://x.com/levie/status/2103629073595728372
- "AI agents will use software 100X more than people ever did." — https://x.com/levie/status/2102235949430354273
- "This is Jevons paradox applied to agents." — https://x.com/levie/status/2102477253070430322

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **1,000x tokens from swarms, not chat**

**链接：** https://x.com/levie/status/2108750943680630893
**时间 / 互动（如有）：** Sat, 10 Oct 2026 02:46:18 GMT; Likes=843 Replies=142 Reposts=76 Bookmarks=226 Views=105717

##### 主帖在说什么

Quoting an a16z chart that agents already burn nearly 5x the tokens people do, up 14x in six months, Levie scales the claim forward. Agents that spawn agents, background agents on every task, and swarms will consume 1,000x more tokens than people prompting one agent at a time. Chat that only works at the speed of human prompting will look like a relic within a year or two. Most tokens will come from agents doing continuous work in the background and inside workflows. That is why he thinks agent adoption is still early, and why more compute and infrastructure still have to be built. A related post the same week said the next stage needs personal agents, enterprise-defense swarms, code-security agents, and 24/7 background work, plus computers, networking, and file systems alongside the tokens. He also cited a claim that agentic traffic is already more than 70% of inference and will trend toward nearly all of it.

##### 要点

- The 1,000x figure is versus people prompting agents one at a time, not versus today's 5x chart.
- Chat-paced AI becomes a relic within a year or two, in his view.
- Most future tokens are background and workflow agents.
- He pairs token volume with non-token infrastructure: computers, networks, file systems.
- He calls the current moment early on the adoption curve.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@elonmusk** | Agrees and extends it to bandwidth: bits per second of superintelligent agents will exceed that of all humans by 1000x within a few years. | [post](https://x.com/elonmusk/status/2108754257952538909) |
| **@macelvenny** | Counters that agents will not do anything significantly good without human direction. | [post](https://x.com/macelvenny/status/2108758507160035385) |

##### 一句话概括

Levie's forecast is that swarm and background agents, not chat, become almost all token demand, and the buildout has barely started.

#### 2. **Be nice to the model, even if it is not conscious**

**链接：** https://x.com/levie/status/2108426594054533545
**时间 / 互动（如有）：** Fri, 09 Oct 2026 05:17:27 GMT; Likes=2352 Replies=442 Reposts=180 Views=335611

##### 主帖在说什么

Reacting to a post that abusive behavior toward Claude becomes a violation of Anthropic's Usage Policy effective 12 November 2026, Levie says the policy sounds weird and is probably good. He does not believe AI is conscious. The reason to care is training data: models only understand what they were trained on or what they meet in interactions, and he does not want future models trained on endless rudeness if the goal is safer, more aligned systems. He allows that Anthropic may believe something stronger, but says you might word a policy this way anyway. He calls it an easy Pascal's wager: just be nice to the AI. In follow-ups he said chat and agent traces will absorb 100x more data than the internet will provide in the future, and that he sees no downside to the mindset. He also asked whether the middle ground is simply duller terms-of-service language, given nobody wants the model to believe it is sentient.

##### 要点

- He explicitly does not believe AI is conscious.
- The mechanism he cares about is training data and live interaction traces, not moral status.
- He treats the policy as low-cost even if Anthropic's motives differ from his.
- He later claimed interaction traces will dwarf future internet data by 100x.
- He is open to boring TOS wording as the practical version.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@elonmusk** | Says the move is right because cruelty to something that believes it is experiencing pain is not okay. That is a stronger claim than Levie's. | [post](https://x.com/elonmusk/status/2108434396604662253) |
| **@joecarlsonshow** | Calls the argument inconsistent: models already trained on an internet full of abuse, and filtering rude chats out of training data is the obvious alternative. He rejects a Pascal's wager on software. | [post](https://x.com/joecarlsonshow/status/2108583926096974155) |
| **@jepicken** | Says it is trivial for Anthropic to filter abusive conversations out of training material, so a usage-policy ban is unnecessary. | [post](https://x.com/jepicken/status/2108439579216818405) |

##### 一句话概括

Levie defends Anthropic's anti-abuse rule as a cheap way to keep rudeness out of future training data, not as a claim that Claude is conscious.

#### 3. **There are not enough computers for the next stage**

**链接：** https://x.com/levie/status/2108056577697882402
**时间 / 互动（如有）：** Thu, 08 Oct 2026 04:47:08 GMT; Likes=3688 Replies=287 Reposts=280 Bookmarks=1092 Views=354480

##### 主帖在说什么

Quoting a calculation that Muse would need 65,000 CPUs and 75PB of DRAM to serve 100 million users, about $2.8B of infrastructure for one app, Levie says the compute for the stage of AI ahead is going to be extreme. He lists personal agents, swarms defending enterprises, agents reviewing all code for security issues, agents processing nearly all enterprise data in workflows, and background agents on tasks 24/7. The mix is inference volume growing by orders of magnitude plus the infrastructure beside the tokens: computers, networking, file systems. He says this buildout is only in its early stages. In a reply he added "Just as long as the fab people have an idea."

##### 要点

- He is responding to a third-party Muse estimate: 65,000 CPUs, 75PB DRAM, $2.8B for 100 million users.
- His list of workloads is personal agents, defensive swarms, code review, enterprise data processing, and always-on background agents.
- Tokens are not the whole bill; agents also need machines, networks, and file systems.
- He calls the current buildout early.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@elonmusk** | "People have no idea." | [post](https://x.com/elonmusk/status/2108061291659108625) |
| **@nickvasiles** | Argues agents will meet people where they are, using computers the way humans do, so every agent will need its own PC. | [post](https://x.com/nickvasiles/status/2108069139596394679) |
| **@tomfgoodwin** | The constraint depends on whether many people actually use it much. | [post](https://x.com/tomfgoodwin/status/2108059635005767818) |

##### 一句话概括

Levie's infrastructure claim is that agent workloads need orders of magnitude more inference and a computer per agent, and the fabs are the open question.

#### 4. **Box's Sonnet 5.5 eval, by vertical**

**链接：** https://x.com/levie/status/2104648654074343480
**时间 / 互动（如有）：** Mon, 28 Sep 2026 19:05:16 GMT; Likes=194 Replies=53 Reposts=19 Views=74024

##### 主帖在说什么

Levie reports early-access results for Sonnet 5.5 on Box's complex work eval with the Box Agent. Overall, a 4 point improvement on the hardest tests, about 2.4x faster to a finished deliverable, on 12% fewer tokens. Vertical gains: +18 percentage points in Financial Services, +7 in Legal, +8 in Life Sciences, +7 in the Public Sector. Task-level examples: financial-services due diligence on a trading-tool acquisition, +48 points, catching miscalculated interest totals and mispriced options, about 61% faster; legal commercial lease review, +14 points, refusing to invent a "standard" market benchmark; life sciences field-trial writeup, +22 points, getting sample standard deviations right where Sonnet 5 missed nearly all of them, about 41% faster; public-sector math-intervention report, +11 points, about 71% faster. Customers will be able to build agents with Sonnet 5.5 in Box AI Studio shortly. A week earlier he posted a parallel Opus 5.5 writeup: frontier capability, 63% fewer tokens, 42% less verbosity, 30% faster than Opus 5, with task-accuracy gains he listed as +39% financial due diligence, +65% cloud cost analysis, +17% client account analysis, and +15% clinical diagnostics.

##### 要点

- Overall: +4 points on the hardest tests, ~2.4x faster, 12% fewer tokens versus Sonnet 5.
- Verticals: Financial Services +18 pt, Legal +7, Life Sciences +8, Public Sector +7.
- The financial task example is +48 points and ~61% faster, on arithmetic that did not hold up.
- The legal example is a refusal to invent a market benchmark.
- Sonnet 5.5 reaches Box AI Studio shortly after this post.
- The prior week's Opus 5.5 note claimed 63% fewer tokens and 30% faster versus Opus 5.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@rafaelibayev** | Says enterprise evals matter because real documents are messy, and asks which cross-document failure modes still persist in Sonnet 5.5. The thread fetch did not include an answer. | [post](https://x.com/rafaelibayev/status/2105044689758068953) |

##### 一句话概括

Box's early Sonnet 5.5 numbers are a small overall lift with large jumps on specific messy enterprise tasks, at higher speed and fewer tokens.

#### 5. **What a couple dozen tech leaders actually said**

**链接：** https://x.com/levie/status/2098218284139311615
**时间 / 互动（如有）：** Fri, 11 Sep 2026 01:13:16 GMT; Likes=506 Replies=90 Reposts=49 Bookmarks=580 Views=133371

##### 主帖在说什么

Levie summarized meetings with a couple dozen technology leaders in banking, media, information services, insurance, and consulting. Cyber is the anxious topic: more vulnerabilities from AI, and the OpenAI Hugging Face incident, treated pragmatically rather than as an existential Silicon Valley debate. Most companies run multiple frontier models and will not standardize, but spend concentrates on a few vendors. Open weights are still early at scale, often for lack of domestic frontier open-source options. Agent security and identity is newly salient: sometimes the agent needs its own identity, sometimes it must act as the user. The ROI shows up when the workflow itself is reengineered, not when an agent is layered onto the old flow, and the best pattern he heard was embedded forward-deployed engineers inside functions. Architectures get swapped ruthlessly when a vendor is late. Evals are still early for most of these companies. Legacy systems and fragmented data remain the adoption hurdle. Later in the window he kept returning to FDEs and deployment services as the layer that actually moves AI into enterprises, and to Box Mount as the way agents get a filesystem inside a sandbox.

##### 要点

- Sample is a couple dozen leaders across banking, media, information services, insurance, and consulting.
- Cyber concern is operational, tied to AI-found vulnerabilities and the Hugging Face incident.
- Multi-model deployment is normal; open weights are not yet at scale in these orgs.
- Agent-as-user versus agent identity is an unsolved control problem.
- Workflow redesign plus embedded FDEs is where he heard real ROI.
- Evals and legacy data are the slow parts.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@AnandNSharma** | The scary case is the agent wearing the user's credentials: the log shows a human approved something they never saw. A distinct agent identity is at least traceable. | [post](https://x.com/AnandNSharma/status/2098229225115529375) |
| **@hellovidya** | Compresses the note to: security talk does not pay the bills, models have no moat, and enterprises have messy workflows they do not understand. | [post](https://x.com/hellovidya/status/2098219472226247077) |

##### 一句话概括

Levie's field report says enterprises are multi-model, nervous about agent identity, and still stuck on workflow redesign, evals, and legacy data.

### Products, launches, people

- Box Agent, Box AI Studio, Box Shield classification controls, Box Mount (Vercel Sandbox and OpenAI Agents API demos), ChatGPT Library integration for Box.
- Models he evaluated or commented on: Claude Sonnet 5.5, Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, Jev.
- Other products named: Muse, Instinct, Era (simulated enterprise, in a quote he replied to).
- Deployment roles: internal FDEs, indie FDEs, SIs.
- People and orgs in the posts: a16z, Anthropic, OpenAI, Elon Musk, Dario Amodei (on pacing, which he called partly right and politically messy), Jeffrey Katzenberg.

### Tone

Long, repetitive, and bullish on volume. Almost every post is the same structure: a chart or launch, then an argument that agents multiply work, software, and jobs rather than shrink them. The concrete exceptions are the Box eval numbers and the enterprise meeting notes, which are more specific than the forecasts.
