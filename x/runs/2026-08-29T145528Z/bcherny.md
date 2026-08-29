# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude Code @anthropicai |
| Source list | builders.md |
| Run ID | 2026-08-29T145528Z |
| Run dir | x/runs/2026-08-29T145528Z/ |

---

## Window: 2026-08-22 → 2026-08-29

- **Run ID:** 2026-08-29T145528Z
- **Fetched at:** 2026-08-29T14:55:28Z
- **Posts in window (fetched):** 20 (cap 50: yes, paginated)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Coding vs engineering: coding is solved *for him*; engineering is not
- Opus 5 is a hill-climb monster, and also too verbose — `outputStyle=concise` as a bandage
- Unified Claude memory across Chat and Cowork
- Prompt injection as a solvable research problem (alignment + mech interp)

### Opinions and takes

- He stopped writing code by hand in Nov 2025; still codes every day via agents
- “Coding/programming = writing code; engineering = everything else”
- Strategic coding is starting to automate (Anthropic auto-maintains apps)
- Cybersecurity refusals suck; same Fable; more to come
- Remote-from-phone sessions are hard to make secure by default; more updates soon

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Coding is solved for average programmers; engineering is not**

**链接：** https://x.com/bcherny/status/2091589188298891264  
**时间 / 互动：** Sun 23 Aug · Likes 1484 · Bookmarks 625 · Views ~157k

##### 主帖在说什么

Reply to Matt Pocock’s dunk on “coding is solved, bugs are not.” Boris treats it as a real debate and gives a three-step timeline: (1) models code better than him, (2) coding-adjacent engineering (debug, profile, design), (3) most computer work better than most people. Claude has 1 and some of 2, early signs of 3 — not yet for Anders Hejlsberg-class compiler work. He considers himself an average programmer; Opus 4.8 was the first model that coded better than him; Fable now finds optimizations he couldn’t.

##### 要点

- Capability tracks the distribution of human ability, not a binary “solved”
- Coding ≠ engineering; bugs and architecture remain
- Stopped writing code by hand Nov 2025

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@mattpocockuk** | AI ate tactical programming; no evidence of strategic (Ousterhout). Agents feel like “tactical tornadoes” | [post](https://x.com/mattpocockuk/status/2091620519376544153) |

##### 一句话概括

“Coding is solved” is true for his distribution and false as a general claim — engineering is the remaining job.

#### 2. **Opus verbosity: we hear you; `claude /config outputStyle=concise`**

**链接：** https://x.com/bcherny/status/2091591570982371454  
**时间 / 互动：** Sun 23 Aug · Likes 1147 · Bookmarks 654 · Views ~481k

##### 主帖在说什么

After being called dismissive for highlighting Opus hill-climb use cases while users complain Opus 5 is lazy/sloppy/verbose: he uses Opus for lots of work; every model has quirks; verbosity is top of mind and a team priority. Short-term bandage: `claude /config outputStyle=concise`.

##### 要点

- Acknowledges the complaint instead of “you’re holding it wrong”
- Concise output style is a stopgap, not the long-term fix
- Opus still framed as best at long-running coding

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@kimmonismus** | Appreciates the reply; wants a modern version of beloved 4.6 with better capabilities than Opus 5.1 | [post](https://x.com/kimmonismus/status/2091636397379596462) |
| **@snjwieiiwidje** | Fable is better at talking to Opus than humans are — maybe models were designed with Fable as orchestrator | [post](https://x.com/snjwieiiwidje/status/2091598659888480725) |

##### 一句话概括

Anthropic is treating Opus verbosity as a product bug with a config patch while the model team works on the real fix.

#### 3. **People are sleeping on Opus hill-climb**

**链接：** https://x.com/bcherny/status/2091308045284585724  
**时间 / 互动：** Sat 22 Aug · Likes 1670 · Bookmarks 894 · Views ~964k

##### 主帖在说什么

Agrees that Opus 5 is a monster if you give it a target. Internally they use it to optimize CPU/memory, CI times, frame rates, latency — any “iterate on X with a profiler and dataset until it hits Y” loop.

##### 要点

- Hill-climb / profiler loops are the hidden Opus 5 skill
- This is how Anthropic itself uses it

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@AliZahid000** | Personal use: hallucinates, marks work done when it isn’t, forgets instructions — worse than Opus 4.8 | [post](https://x.com/AliZahid000/status/2091502214204534908) |
| **@Loster** | “Chatty bastard. Outputs a War and Peace to every prompt.” | [post](https://x.com/Loster/status/2091340951830602162) |

##### 一句话概括

Opus 5 shines as an optimizer-with-a-metric and frustrates as a general chat/coding partner.

### Products, launches, people

- Unified Claude memory (quotes @claudeai)
- `claude /config outputStyle=concise`
- Fable (internal/orchestrator model) as the thing that finds optimizations
- Prompt injection: “combo of alignment training and mechanistic interpretability… solvable… took many years”

### Tone

Engineering-dense and unusually willing to debate critics. Mix of framework posts (coding vs engineering) and product support (concise mode, memory). Not dismissive this week — more “fair, here’s the timeline.”
