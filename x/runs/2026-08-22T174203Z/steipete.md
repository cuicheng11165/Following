# Peter Steinberger (@steipete)

| Field | Value |
|-------|-------|
| Profile | https://x.com/steipete |
| Bio | Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw + @OpenAI |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 20 (cap 50: yes)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- “No Doors for Agents” talk at Berkeley Agentic AI Summit
- iMessage CLI (`openclaw/imsg`) — anything a user sees, an agent can see
- Privacy framing: opt-in feature vs “privacy violation”; sharing contacts worse than inference providers
- OpenClaw sqlite migration / main-branch dogfood
- New skill drop after Linus used AI to find a kernel GPU bug
- Designer hire; Microsoft team; debug by pointing Claude/Codex at your config from your phone

### Opinions and takes

- Computer use made “doors” for agents a solved-ish interface problem (email, WhatsApp, Telegram, Slack)
- That has always been possible; it’s just a tad easier now
- Inference providers delete content; companies that store your contacts are the worse leak

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **“No Doors for Agents” at Berkeley**

**链接：** https://x.com/steipete/status/2090898421108605078  
**时间 / 互动：** Fri 21 Aug · Likes 250 · Views ~66k

##### 主帖在说什么

Spoke at Agentic AI Summit 2026 (~5k in person, ~100k online). Dawn Song’s recap quotes him: “The text box is AI’s radio-on-TV phase…. Every new medium starts by imitating the old one.” Talk: “No Doors for Agents” (YouTube). Follow-up: like email/WhatsApp/Telegram/Slack — anything a user sees, an agent can see; game over once computer use got good.

##### 要点

- Chat box is a transitional UI, not the medium
- Agents should not need special doors if they can use the same surfaces as humans
- Computer-use quality was the phase change

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Secondmindsys** | Once you add doors, each door needs a contract: action, authority, state change, evidence, what happens on no | [post](https://x.com/Secondmindsys/status/2090922843953676772) |
| **@_BMW_** | Ending on “building doors is the fun part” | [post](https://x.com/_BMW_/status/2090905555569123547) |

##### 一句话概括

Steinberger’s interface thesis: stop inventing agent APIs and let agents sit in the same rooms as users.

#### 2. **imsg CLI — and the privacy pile-on**

**链接：** https://x.com/steipete/status/2090676615986725196  
**时间 / 互动：** Fri 21 Aug · Likes 3 · Views ~772 （仅列表摘要，thread 拉取失败）

##### 主帖在说什么

Can’t comment on OpenAI; here’s his take: https://github.com/openclaw/imsg. Nearby replies: sharing contacts is worse because companies store that while inference providers delete content; “framing this as privacy violation when it’s a feature people specifically have to enable is a choice”; beauty of imsg CLI is you can run it with local models on your claw.

##### 要点

- Opt-in iMessage bridge for OpenClaw
- Local-model path as the privacy answer
- Contacts graph > message content as the scary permission

##### 回复中的有价值观点

Same conversation cluster; no extra high-signal third parties in the keyword fetch.

##### 一句话概括

The lobster wants your iMessage — as an explicit, preferably local, feature, not a silent harvest.

#### 3. **Dropping a new skill after Linus+AI kernel debug**

**链接：** https://x.com/steipete/status/2090946181564440727  
**时间 / 互动：** Fri 21 Aug · Likes 283 · Views ~64k （仅列表摘要，thread 拉取失败）

##### 主帖在说什么

Quotes a writeup of Linus using AI to grind 24 debug patches / 18 boots to a one-line `round_up→round_down` Xe GPU bug, then letting AI write the commit message (AI kept saying the bug was unsolvable). Steinberger: “dropping new skill brb.”

##### 要点

- Real-world agent debugging as the prompt for a new OpenClaw skill
- Human persistence vs model “give up” prior

##### 回复中的有价值观点

Quoted Mark Kretschmann post is the story; Peter’s tweet is a product tease.

##### 一句话概括

If Linus can bully an agent through a kernel heisenbug, that’s a skill-shaped product.

### Products, launches, people

- OpenClaw, `openclaw/imsg`, `openclaw/spogo`
- Agentic AI Summit / Dawn Song recap
- Microsoft team for OpenClaw
- Sqlite migration off main (dogfooding next release)

### Tone

Lobster-meme founder. Half conference keynote, half GitHub link, half “that’s a choice.”
