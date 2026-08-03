# Swyx (@swyx)

| Field | Value |
|-------|-------|
| Profile | https://x.com/swyx |
| Bio | achieve ambition with intentionality, intensity, integrity & insanity. affiliations: @smol_ai, @dxtipshq, @cognition, @aidotengineer, @latentspacepod |
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

- **Forge agents / platform-product dogfooding:** building Forge while hosting all personal projects on it; bouncing between platform and app work.
- **Multi-agent premoves:** Codex @-thread + queue so blocked project work auto-resumes when platform unblocks.
- **Slop-tolerant systems:** praises Boundary talk “fighting slop with slop”; being slop-tolerant ≫ being anti-slop.
- **Patio11’s Law of Agents:** chronic under-ambition about agents improving *every* workflow part—even after you account for that law.
- **Cloud-first infra:** prefers not reinventing laptop/local infra; “fuck laptops,” cloud from the start; not trying to out-infra Microsoft.

### Opinions and takes

- Better multiagent harnesses should orchestrate platform ↔ project work without a human in the loop (rare unless you build a real multi-tenant platform).
- “Being slop-tolerant is 100x more valuable than being anti-slop.”
- Clanker/blog automation for Forge decisions going forward.
- Only the very motivated will do certain hard local/setup paths.

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Fighting slop with slop — AI-native programming**

**链接：** https://x.com/swyx/status/2083753582160191988  
**时间 / 互动：** 2026-08-02 · ~203 likes · ~230 bookmarks · ~41k views

##### 主帖在说什么

As a conference organizer who rarely attends his own events, swyx binge-watches talks afterward. Highlights @vaibcode (Boundary) on “fighting slop with slop” as exceptionally well paced. Connects to Bret Taylor asking on the pod for an AI-native programming language; as a PL fan, he’s glad someone is rethinking how code runs from first principles. Core takeaway: slop-tolerance beats slop-resistance.

##### 要点

- Conference-organizer curse → post-hoc talk consumption
- Boundary / BAML as AI-native PL rethink
- Design for noisy AI outputs rather than pure anti-slop purity

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@vaibcode** | Thanks; jokes next step is Sierra writing everything in BAML | [post](https://x.com/vaibcode/status/2083950194648092684) |
| **@ehzish** | “the sleeping guy on the slide next to slop is the most accurate diagram i've seen all year” | [post](https://x.com/ehzish/status/2083755411035877404) |

##### 一句话概括

Embrace slop-tolerant, AI-native programming primitives instead of fighting messiness head-on.

#### 2. **Forge dogfooding + Codex premove trick**

**链接：** https://x.com/swyx/status/2083993378258288976  
**时间 / 互动：** 2026-08-02 · ~28 likes · ~24 replies

##### 主帖在说什么

Developing Forge by hosting all his projects on it creates constant platform↔product bounce. Shares a Codex trick: @ a thread and queue so project work can “premove” once a blocking platform feature lands. Notes he wasn’t strictly necessary in the loop—ideal multiagent harness would orchestrate that seam automatically. Rare use case unless you build a real multi-tenant platform (most people build one app on someone else’s platform).

##### 要点

- Platform + product concurrent development is a special harness problem
- Queue/@ threading as a poor-man’s dependency scheduler
- True multiagent orchestration still under-built for this pattern

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@juan_zgz** | Building platform + product at once is the rare setup that surfaces this seam | [post](https://x.com/juan_zgz/status/2083996777787645972) |
| **@Telestijl** | Needs structured “blocked” metadata + supervisor auto-resume, not manual re-queue | [post](https://x.com/Telestijl/status/2083994267848933403) |
| **@Berthilson** | What if platform fix changes the contract the queued project assumed? | [post](https://x.com/Berthilson/status/2084008891394736340) |

##### 一句话概括

Dogfooding a platform forces multiagent dependency scheduling—and current tools only half-solve it.

#### 3. **Patio11’s Law of Agents**

**链接：** https://x.com/swyx/status/2084099311907013053  
**时间 / 互动：** 2026-08-03 · early thread, rising

##### 主帖在说什么

States Patio11’s Law of Agents: you are insufficiently ambitious about what agents can do to improve every part of your workflow—even when you’ve already internalized that law (recursive under-ambition).

##### 要点

- Meta-cognitive check on agent ambition
- Workflow redesign, not bolt-on automation

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@DharmpalDotasa1** | Biggest mistake isn’t underestimating AI once—it’s failing to revisit assumptions as it improves | [post](https://x.com/DharmpalDotasa1/status/2084099621752816104) |
| **@ApacheAE** | Still aiming too low even after you know you’re aiming too low | [post](https://x.com/ApacheAE/status/2084103654957789677) |
| **@elian_mcc** | Patio11 names laws better than most VCs name funds | [post](https://x.com/elian_mcc/status/2084099756624675108) |

##### 一句话概括

Even agent-aware builders systematically under-scope what agents should own.

### Products, launches, people

- **Forge** (forge.smol.ai) — agent platform; blog: every repository gets its own agent
- **OpenAI Codex** — @ thread + queue workflow
- **Boundary / BAML** (@vaibcode) — AI-native PL talk
- **Bret Taylor** — AI-native language ask on pod
- **Clanker** — decision-blogging for Forge

### Tone

High-velocity builder-operator: shipping Forge in public, coining laws, conference curatorial energy, blunt infra takes (“fuck laptops”). Practical patterns over pure theory.
