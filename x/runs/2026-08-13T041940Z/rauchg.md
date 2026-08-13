# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | Vercel CEO |
| Source list | builders.md |
| Run ID | 2026-08-13T041940Z |
| Run dir | x/runs/2026-08-13T041940Z/ |

---

## Window: 2026-08-05 → 2026-08-13

- **Run ID:** 2026-08-13T041940Z
- **Fetched at:** 2026-08-13T04:19:40Z
- **Posts in window (fetched):** 20 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Self-maintaining software / AI SDK “software factory”
- Vercel Sandbox managed images (`npx sandbox@latest sh`)
- Agent-priced sandbox (charge active CPU + baseline memory)
- Digg’s agent-native reboot on Vercel
- Seedance 2.5 on AI Gateway

### Opinions and takes

- Toward self-maintaining software, with humans still merging
- Sandbox feels faster than local
- Pricing should match agent workloads (active CPU, not idle)

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Software factory for AI SDK**

**链接：** https://x.com/rauchg/status/2087574374706761892  
**时间 / 互动：** Wed 12 Aug · Likes 315 · Bookmarks 252

##### 主帖在说什么

Vercel built a software factory for AI SDK: each step is an agent, humans merge. Four weeks: factory authors up to 35% of merged PRs, closed 70% of July issues, open bugs down 25%. “Towards a future of self-maintaining software.”

##### 要点

- Humans still merge (quality gate)
- Concrete OSS metrics, not vibes
- Balance autonomy vs quality

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@udohjeremiah_** | Self-maintaining codebases change how we think about software teams | [post](https://x.com/udohjeremiah_/status/2087606111658557850) |
| **@GabiiAH11** | Curious what the unclosed 30% of issues look like | [post](https://x.com/GabiiAH11/status/2087575614957990071) |
| **@benshipssolo** | Still need someone to define “quality” | [post](https://x.com/benshipssolo/status/2087633702591283236) |

##### 一句话概括

Vercel is dogfooding agent factories on its own most-popular AI library — with humans still holding merge.

#### 2. **Sandbox managed images**

**链接：** https://x.com/rauchg/status/2087698195120116064  
**时间 / 互动：** Thu 13 Aug · Likes 150

##### 主帖在说什么

Vercel Managed Images: Ubuntu default, preinstalled coding agents (codex, claude…), customizable OSS base images. `npx sandbox@latest sh` “feels faster than your local machine.”

##### 要点

- Cloud sandbox as default agent runtime
- Agents preinstalled
- Agent-optimal pricing (active CPU)

##### 回复中的有价值观点

Mostly product praise; pricing calculator called out separately: https://vercel.com/sandbox

##### 一句话概括

The new localhost is a billed sandbox with Codex already installed.

### Products, launches, people

- [Software factory for AI SDK](https://vercel.com/blog/building-a-software-factory-for-ai-sdk)
- Vercel Managed Images / Sandbox
- Seedance 2.5 on AI Gateway
- Digg.com/tech on Vercel (Kevin Rose)

### Tone

CEO-as-demo: ship infra, post metrics, reply “fixing!” to every customer ping.
