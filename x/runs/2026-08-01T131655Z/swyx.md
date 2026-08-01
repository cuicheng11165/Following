# Swyx (@swyx)

| Field | Value |
|-------|-------|
| Profile | https://x.com/swyx |
| Bio | achieve ambition with intentionality… @smol_ai @aidotengineer @latentspacepod |
| Source list | builders.md |
| Run ID | 2026-08-01T131655Z |
| Run dir | x/runs/2026-08-01T131655Z/ |

---

## Window: 2026-07-29 → 2026-08-01

- **Run ID:** 2026-08-01T131655Z
- **Fetched at:** 2026-08-01T13:16:55Z
- **Posts in window (fetched):** 10 (cap 50: yes)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` floor `2026-07-29T03:32:35Z`)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **Agent loops still matter:** Defends active use of `/loop` and `/goal` when many AI leaders have abandoned them
- **Vibe coding mainstreamed:** Pejorative stigma gone as nontechnical and supertechnical both do it
- **Harness distillation / MITM:** Graduate-level reverse-engineering of agent harness prompts via proxies
- **Product gap:** Wondered aloud about a “Codex for batch mode” (cost-saving vs capability-maxing products)
- Casual engagement / memes mixed with loop engineering dinner quotes (Jerry Liu / Dex)

### Opinions and takes

- Minority among AI leaders still using `/loop` + `/goal`; believes people who stopped are *too early* in the g5.6/c5 era, not forever wrong
- Use loops when you want steerability + autonomy mix, or open-ended “loop that generates loops” without fully specifying the path
- Vibe coding’s social valence flipped: once pejorative, now ubiquitous
- MITM agent distillation “works” but is graduate-level; agrees with Ara’s breakdown that copying harness pieces is feasible

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Still using /loop and /goal**

**链接：** https://x.com/swyx/status/2083439562437673053  
**时间 / 互动：** Sat 01 Aug 2026 · ~46 likes · 28 replies · ~10k views

##### 主帖在说什么

Quoting Jerry Liu’s founder dinner notes (most attendees *not* using `/loop`), Swyx says he’s still actively using `/loop` and `/goal`. He argues peers who stopped are wrong for now—not forever—in the current model era. He lists when loops win: mix of steerability and autonomy, and open-ended end-states without a fully specified path. Shares a screenshot example where a saved goal rescued a long action-reasoning turn.

##### 要点

- Counter-signal to dinner consensus that loops are passé
- Goal/loop as product primitives, not just UI sugar
- Model era (g5.6/c5) still rewards structured looping

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@habibislop** | One chat for intent, then ask the agent to set up new chats with `/goals` and monitor via heartbeats; agent writes better goals than the user | [post](https://x.com/habibislop/status/2083451771649691849) |
| **@sidelined_cap** | Saved goal is the killer feature—long turns dying used to mean re-reading transcripts like archaeology | [post](https://x.com/sidelined_cap/status/2083448654686548132) |
| **@hshipit** | Goal files are “absolute magic”; loops stop when checkboxes clear | [post](https://x.com/hshipit/status/2083496917527630104) |

##### 一句话概括

Swyx is holding the line that structured agent loops still have alpha while many leaders have moved on.

#### 2. **“Vibe coding” lost its pejorative charge**

**链接：** https://x.com/swyx/status/2083294839186260385  
**时间 / 互动：** Fri 31 Jul 2026 · ~131 likes · 51 replies · ~9.9k views

##### 主帖在说什么

Observes that the negative connotation around “vibe coding” has disappeared because essentially everyone—from nontechnical to supertechnical—now does it.

##### 要点

- Cultural shift, not just tooling shift
- Mainstream adoption dissolves stigma

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@nabu_lines** | Jokes the trajectory mirrors other stigmatized-then-normalized careers | [post](https://x.com/nabu_lines/status/2083295765611373008) |
| **@jonnygravity** | Prefers “Katana Method”—fold, inspect, hammer—argues “vibes” never captured the real craft process | [post](https://x.com/jonnygravity/status/2083295260935946630) |

##### 一句话概括

When everyone vibes, “vibe coding” stops being an insult and becomes a default work mode.

#### 3. **MITM agent harness distillation**

**链接：** https://x.com/swyx/status/2083237045720465504  
**时间 / 互动：** Fri 31 Jul 2026 · ~9 likes · quote of Ara’s long distillation recipe

##### 主帖在说什么

Quotes Ara’s step-by-step on distilling harness subparts (computer use / search) via MITM proxies that force tools to reveal prompts—even with safety-tested models. Swyx replies: “MITM agent distillation is graduate level but yeah ofc this works.”

##### 要点

- Harness IP is more extractable than model weights for some subsystems
- Acknowledges technique works; implies taste still matters over pure copying

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@arafatkatze** (quoted) | Full 5-step recipe: pick subpart → stress debug → MITM for prompts → rebuild mental model → add to pi harness + evals | [post](https://x.com/arafatkatze/status/2083236726676615535) |

##### 一句话概括

Agent harnesses can be reverse-engineered at the prompt/tool layer—powerful, advanced, and already practiced.

### Products, launches, people

- Jerry Liu (@jerryjliu0) / Dex dinner on agent loops
- Mentions of Codex / Claude Code `/loop` culture
- Ara (@arafatkatze) on harness distillation into “pi harness”

### Tone

Practitioner-insider and contrarian-friendly: short takes, dinner discourse engagement, plus meme energy—argues for loops while the room has already moved on.
