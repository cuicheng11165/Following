# Aaron Levie (@levie)

| Field | Value |
|-------|-------|
| Profile | https://x.com/levie |
| Bio | ceo @box — your business lives in content. unleash it with AI |
| Source list | builders.md |
| Run ID | 2026-08-29T145528Z |
| Run dir | x/runs/2026-08-29T145528Z/ |

---

## Window: 2026-08-22 → 2026-08-29

- **Run ID:** 2026-08-29T145528Z
- **Fetched at:** 2026-08-29T14:55:28Z
- **Posts in window (fetched):** 9 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Strongly held AI beliefs have a ~6-month half-life
- Software + agents grow TAM together; SaaS is not dead
- Box Q2: unstructured data as the context layer agents need
- Systems of record get *more* important when agents do 100× the work
- ZDR as a hidden driver of enterprise AI diffusion
- Evals (workflow-specific) as the real rate limiter

### Opinions and takes

- Lists cycling takes: OSS too far behind, labs unprofitable, all software replaced by agents, no moats, RAG dead, prompting won’t matter, training wall, etc.
- Agents need deterministic guardrails more, not less, because they scale past humans
- Hugging Face incident = preview of agents executing goals against enterprise data
- Applied AI (evals, harness, vertical UX, change management) is where the premium sits

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **AI beliefs have a 6-month half-life**

**链接：** https://x.com/levie/status/2093568352736436576  
**时间 / 互动：** Sat 29 Aug · Likes 379 · Bookmarks 190 · Views ~72k

##### 主帖在说什么

Quote-tweeting Jack Altman: the average strongly held AI belief lasts 6 months at best. He lists a graveyard of consensus-that-wasn’t (OSS too far, labs unprofitable, agents replace all software, no moats, cheaper models → less compute, don’t need evals, RAG dead, engineering jobs gone, prompting won’t matter, training wall, frontier too dangerous…). Stay flexible.

##### 要点

- Intellectual humility as operating system
- Many “dead” takes just got boring, not disproven (reply)

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@somi_ai** | Half of these didn’t get disproven, they just got boring | [post](https://x.com/somi_ai/status/2093593831077974224) |
| **@simonhedlin** | Things get exponentially weirder; open-minded people weather it | [post](https://x.com/simonhedlin/status/2093588763461013594) |

##### 一句话概括

Levie’s meta-take: treat AI consensus as perishable inventory.

#### 2. **Software and agents grow the IT TAM together**

**链接：** https://x.com/levie/status/2093192697331011846  
**时间 / 互动：** Fri 28 Aug · Likes 276 · Bookmarks 167 · Views ~108k

##### 主帖在说什么

On NVDA/Salesforce earnings shredding “AI capex bubble” and “SaaS is dead”: software is the guardrails (data, business logic, access, protection). Agents execute at superhuman scale *inside* those systems, which is why deterministic controls matter more. Best deployments are in Salesforce, Box, Harvey, ServiceNow, with vertical evals and headless agent-to-agent. Both software and AI adoption go up; TAM grows.

##### 要点

- Systems of record ≠ the thing agents replace
- Vertical applied platforms optimize agents for the workflow
- Earnings as evidence, not vibes

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@realpaulsmith** | Salesforce×Anthropic deal exists because customers already have permissions/workflow/audit on SFDC; they want Cowork agents inside that | [post](https://x.com/realpaulsmith/status/2093397655481135112) |
| **@iabdul_wasey** | Agents can only respect guardrails that exist in a system, not in someone’s head | [post](https://x.com/iabdul_wasey/status/2093195027098845243) |

##### 一句话概括

The anti-SaaS take dies where agents need audit logs.

#### 3. **Box Q2: agents starve without unstructured enterprise knowledge**

**链接：** https://x.com/levie/status/2092702955292230100  
**时间 / 互动：** Wed 26 Aug · Likes 258 · Views ~122k

##### 主帖在说什么

Q2 revenue $321.1M, +9% / +11% CC (fastest CC in 14 quarters), FY target raised to $1.290B. Superintelligence is only as useful as the enterprise knowledge it can reach — contracts, research, financials, roadmaps, mostly unstructured. Enterprises need applied platforms that swap models, mix cost/performance, and (post-HF incident) guardrails, audit logs, real-time alerts for both humans *and* agents.

##### 要点

- Context, not the model, is the enterprise bottleneck
- Model-agnostic applied layer
- HF incident as enterprise-security parable

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@danieloleary** | Box MCP server and Box agents are world class | [post](https://x.com/danieloleary/status/2092839102911574044) |
| **@itamar_mar** | Well-engineered context management, enterprise-ready, with a human interface | [post](https://x.com/itamar_mar/status/2092704428923240603) |

##### 一句话概括

Box’s pitch: the model is a commodity; the file graph with permissions is not.

### Products, launches, people

- Box Q2 / intelligent content management
- Salesforce, Harvey, ServiceNow as agent hosts
- ZDR as diffusion infrastructure (~95% ZDR aside)
- Hugging Face incident as recurring exhibit A

### Tone

Enterprise-essay cadence. Same Levie loop as always — longer, more earnings-grounded, and now using HF as the cautionary tale for why systems of record win.
