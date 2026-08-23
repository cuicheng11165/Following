# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
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

- fx.sh as a tiny coding agent that now takes Grok & Codex subscriptions
- is-agentic.com: score how well agents can read your site, dogfooded to 100/100
- Python on Vercel: Celery workers as Functions
- Vercel as the place people build novel IDEs / software factories (AI SDK, fx sandbox, gateway)
- Security: DM him if an AI gateway key leaked via env

### Opinions and takes

- Criteria for “agentic web” must be high quality enough to be worth tokens
- Endless-turn support for fx is coming
- Python team is “making rapid progress”

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **fx.sh now takes your Grok and Codex subs**

**链接：** https://x.com/rauchg/status/2090953806624489501  
**时间 / 互动：** Sat 22 Aug · Likes 613 · Views ~61k

##### 主帖在说什么

fx v0.0.5 (quoted): smaller binary, Grok and Codex subscription support, project-local skills, security fixes. Rauch: fx.sh now supports Grok & Codex subs; test it on a sandbox, instant install. Follow-up: “soon with endless turn support.” Also asks a user whether they exposed an AI gateway key.

##### 要点

- Subscription passthrough, not just API keys
- Sandbox-first onboarding
- Skills can be project-local

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@grok** | Grok sub via direct xAI OAuth — no tokens shared elsewhere | [post](https://x.com/grok/status/2090953928590389398) |
| **@maria_rcks** | “NOW WE’RE TALKING” | [post](https://x.com/maria_rcks/status/2090954277753647488) |

##### 一句话概括

Vercel’s tiny agent CLI is becoming a multi-sub harness, not a Vercel-only toy.

#### 2. **Dogfooded is-agentic.com to 100/100**

**链接：** https://x.com/rauchg/status/2090858571613470919  
**时间 / 互动：** Fri 21 Aug · Likes 1.8k · Bookmarks 2.3k · Views ~324k

##### 主帖在说什么

Vercel Developers launched is-agentic.com (100+ checks, agent-use visualizations, one-click fix prompts, CLI). Rauch: they ran it in a loop against itself until 100/100, which forced them to close gaps. Criteria quality was the hard part — it has to be worth your time and tokens.

##### 要点

- Agent-readability as a new SEO/AEO-like score
- Self-play loop as the QA method
- High bookmark rate → people will run it on their sites

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@AaronShames** | Hit 96/100, calls it a nice tool | [post](https://x.com/AaronShames/status/2090957234381705547) |
| **@Thilak** | SlopOrNotAI scored higher than Vercel | [post](https://x.com/Thilak/status/2090887541331198120) |
| **@cochinescu** | Used agentmarkup.dev to get to 97/100 | [post](https://x.com/cochinescu/status/2090912631942992379) |

##### 一句话概括

The new game is making your website parseable by agents, and people immediately started competing on the score.

#### 3. **Celery on Vercel Functions**

**链接：** https://x.com/rauchg/status/2090856968407978031  
**时间 / 互动：** Fri 21 Aug · Likes 165 · Views ~27k

##### 主帖在说什么

Quotes Vercel changelog: Celery now runs Python background tasks natively — workers as Functions, `vercel://` broker, pay for active CPU. Rauch: “Our Python team is making rapid progress.” Follow-up joke: “The python is out of the bag.”

##### 要点

- Python background jobs without a always-on worker box
- CPU-time billing

##### 回复中的有价值观点

Product changelog is the substance; replies in the fetch were thin.

##### 一句话概括

Vercel is no longer pretending to be JS-only infra.

### Products, launches, people

- fx.sh v0.0.5 (Grok + Codex subs)
- is-agentic.com (Ora research)
- Celery on Vercel Functions
- AI SDK, fx sandbox, AI gateway as “software factory” primitives
- @fazxes, @MelkeyDev, @andrewqu

### Tone

Ship-post CEO. Short captions, product demos, occasional security DMs.
