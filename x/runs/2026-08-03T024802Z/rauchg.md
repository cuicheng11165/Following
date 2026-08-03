# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
| Source list | builders.md |
| Run ID | 2026-08-03T024802Z |
| Run dir | x/runs/2026-08-03T024802Z/ |

---

## Window: 2026-08-01 → 2026-08-03

- **Run ID:** 2026-08-03T024802Z
- **Fetched at:** 2026-08-03T02:48:02Z
- **Posts in window (fetched):** 10 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **@v — company-wide internal agent:** powers Vercel ops (finance, comms, docs, marketing, eng, analytics); exponential interactions/tokens.
- **Agent as router/monolith:** too many agents = bad UX; @v is default front door + sub-agent router (web analogy: company.com vs every agent’s own domain).
- **Own your agent stack:** control source → runtime → data → tokens vs BigAI Slack integration “their agent.”
- **Eve (@evedev_):** productized design inspired by internal @v; multi-channel goal; `useEveAgent()` for custom UIs.
- ROI of redesigning every pattern from scratch is negative even with AI.

### Opinions and takes

- Agents will run entire companies; every company should have a first-party ops agent.
- Skills-driven + continuous improvement + per-user memory/schedules already real at Vercel.
- Occasional purpose-built agents are fine (subdomains); don’t proliferate front doors.
- Economic: pick battles—don’t rebuild everything.

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **@v runs Vercel’s company ops**

**链接：** https://x.com/rauchg/status/2084042561690456157  
**时间 / 互动：** 2026-08-02 · ~841 likes · ~561 bookmarks · ~65k views

##### 主帖在说什么

Vercel built internal agent @v used in every day-to-day job; usage growing exponentially. Expert across functions; seeded with skills and improving; keeps per-user memories and scheduled workflows (e.g. reminding when skills.sh hit 1M). Basis for Eve product design. Argues owning the full agent stack matters if agents become synonymous with companies—vs renting a third-party Slack bot.

##### 要点

- Internal company agent as production reality, not demo
- Ownership thesis: source/runtime/data/token control
- Eve as external product mirror of internal practice
- Extrapolation: agents operating companies

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@rauchg** (self) | Too many agents = bad UX; @v is agent + router/monolith with network escape hatch | [post](https://x.com/rauchg/status/2084060157085143512) |
| **@sageasika** | Customer support agent quality justifies subscription | [post](https://x.com/sageasika/status/2084058257388118387) |

##### 一句话概括

Vercel dogfoods a company OS agent and argues ownership of that agent is strategic infrastructure.

#### 2. **@v as agent router (too many agents problem)**

**链接：** https://x.com/rauchg/status/2084060157085143512  
**时间 / 互动：** 2026-08-02 · ~38 likes · ~21 bookmarks

##### 主帖在说什么

Teams had built dozens of agents—like every agent owning a domain. @v is company.com: default entry, sub-agents, skills, delegation. Monorepo/monolith analogy with ability to proxy over network when needed. Some agents deserve subdomain front doors, but sparingly.

##### 要点

- Agent sprawl is a UX/architecture problem
- Hub-and-spoke routing as solution
- Internet routing history as metaphor

##### 一句话概括

Agent architecture is converging on a default company router, not a zoo of bots.

### Products, launches, people

- **@v** — Vercel internal ops agent
- **@evedev_ / Eve** — productized agent platform; `useEveAgent()`
- **skills.sh** — 1M skills milestone via agent reminder
- Mentions writing with @shardara @ericdodds

### Tone

CEO systems-thinker: architectural analogies (web, monorepo), ownership ideology, product foreshadowing—confident and technical without hype-empty.
