# Madhu Guru (@realmadhuguru)

| Field | Value |
|-------|-------|
| Profile | https://x.com/realmadhuguru |
| Bio | Sr Director, AI at Meta; Prev: Google — Led Gemini, Veo, Nano Banana. |
| Source list | builders.md |
| Run ID | 2026-08-29T145528Z |
| Run dir | x/runs/2026-08-29T145528Z/ |

---

## Window: 2026-08-22 → 2026-08-29

- **Run ID:** 2026-08-29T145528Z
- **Fetched at:** 2026-08-29T14:55:28Z
- **Posts in window (fetched):** 8 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- AI product playbooks have a ~3-month half-life; invent, don’t milk
- Enterprises: own evals, own (post-trained) models
- Eval series parts 7–9: Goldilocks granularity, discriminatory power, eval roadmap

### Opinions and takes

- Traditional PM orgs discover a playbook and milk it for 5 years; labs throw playbooks away every few months
- Highest-leverage enterprise AI move: model-agnostic stack
- Evals that don’t separate known-better systems are useless (PhDs taking a 5th-grade test)
- If evals stay in week-1 while users are in week-3, churn shows it

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **AI product building has a ~3-month playbook half-life**

**链接：** https://x.com/realmadhuguru/status/2093562783627620456  
**时间 / 互动：** Sat 29 Aug · Likes 99 · Bookmarks 91 · Views ~6.2k

##### 主帖在说什么

Quote-tweeting Jack Altman on opinion-reversals every three months: trad teams milk a playbook for years; labs throw them away when returns diminish. Builders should define *meta*-principles for (1) learning what the market wants now and in 3 months, and (2) executing with extreme urgency. Legacy teams optimize for milking; AI teams for inventing.

##### 要点

- Playbook half-life ≈ 3 months
- Meta-principles > frozen process
- Team design is the actual product decision

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ryanedkins** | Throwing playbooks away feels wasteful until the alternative is optimizing a landscape that already moved | [post](https://x.com/ryanedkins/status/2093596134807625853) |

##### 一句话概括

In AI, the durable asset is a team that can throw the playbook away — not the playbook.

#### 2. **Own the evals, own the models**

**链接：** https://x.com/realmadhuguru/status/2093143877087879377  
**时间 / 互动：** Fri 28 Aug · Likes 231 · Bookmarks 199 · Views ~11k

##### 主帖在说什么

If you lead enterprise AI, make the stack model-agnostic. Invest (1) today in an eval suite that captures use cases and business outcomes (most companies don’t), (2) within a year in post-training open models (talent gap is acute). Then you can switch, customize, and optimize quality/cost/latency.

##### 要点

- Evals first, post-train second
- Portability is the strategy, not a vendor feature
- Talent for post-training is the scarce input

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@GilFeig** | Built an internal portable “company brain” with evals + ACLs; launching it in Workforce | [post](https://x.com/GilFeig/status/2093372730020417956) |
| **@AriHeljakka** | (1) is not an R&D side project — it’s strategic codification if you want to be alive in 2028 | [post](https://x.com/AriHeljakka/status/2093162906649346379) |

##### 一句话概括

Vendor models are rented intelligence; evals + post-train are owned intelligence.

#### 3. **Eval series part 9 — the eval roadmap problem**

**链接：** https://x.com/realmadhuguru/status/2092426017118028266  
**时间 / 互动：** Wed 26 Aug · Likes 128 · Bookmarks 143 · Views ~7.5k

##### 主帖在说什么

Most evals fail as static artifacts while usage evolves. Financial-research agent example: summarize 5 pages → 5 earnings → 15 filings into a thesis → proactive portfolio alerts. Dimensions: short→long context, single→multi-turn, citations, QA→synthesis, reactive→proactive. Practical: map dimensions, prioritize, mine traces, build P0 evals for the *next* stage, hill-climb. Also recaps parts 1–8.

##### 要点

- Evals need a product roadmap
- Stay ahead of usage, not behind it
- Production traces are the early-warning system

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@jurlycat** | Production traces are the earliest warning that an eval suite is falling behind real usage | [post](https://x.com/jurlycat/status/2092455179757158889) |

##### 一句话概括

An eval suite that still tests week-1 tasks is a churn dashboard with extra steps.

### Products, launches, people

- Eval series parts 7–9 (Goldilocks, discriminatory power, roadmap)
- Jack Altman / Benchmark as the quoted frame
- Post-training talent (Prime Intellect called out in replies)

### Tone

Teacher-operator: numbered lists, series cadence, “share with your teammates.” The most systematic builder voice this window.
