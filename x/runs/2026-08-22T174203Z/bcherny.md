# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude Code @anthropicai |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 20 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Mythos-class models need extra safety *and* customer-owned data (ZDR coming fall)
- “Coding is solved, bugs are not”
- As models improve, maybe we won’t need code review
- Claude Code usage explosions: parallelism, runaway loops, inefficient skills
- Electron vs native: push Electron first
- Hands-on bug triage in public

### Opinions and takes

- Hand-written code had bugs too — agent bugs are not a unique moral failure
- `/usage` is how you diagnose quota burn
- Desktop quality of Electron has been “really good lately”; native prototypes have downsides

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Mythos-class ZDR: customers own the data, Anthropic retains none**

**链接：** https://x.com/bcherny/status/2090537902912815536  
**时间 / 互动：** Thu 20 Aug · Likes 2.2k · Views ~484k

##### 主帖在说什么

Quotes Bloomberg on Anthropic changing data-retention for advanced AI. Boris: they’ve been working on this with customers for a while. Mythos-class models need extra safety; enterprises need privacy/compliance. Customers can own and control their data; Anthropic retains none. Coming this fall.

##### 要点

- ZDR as a fall ship, not a rumor-only policy
- Safety measures *and* customer-owned data are both required for Mythos
- Timed against OpenAI’s same-week ZDR post

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ShaunStewart** | Anthropic staff on X dodge the complaints customers actually have; people are being forced to cancel | [post](https://x.com/ShaunStewart/status/2090541504787878370) |
| **@reach_vb** | Congrats — and links OpenAI’s ZDR post | [post](https://x.com/reach_vb/status/2090580171183018465) |
| **@vibecodeguild** | Enterprises get safety; “peasants” are stuck on older security settings because Fable won’t do a basic audit | [post](https://x.com/vibecodeguild/status/2090551436954546437) |

##### 一句话概括

Anthropic’s Mythos answer is zero retention — the replies are still about product quality for non-enterprise users.

#### 2. **Coding is solved, bugs are not yet solved**

**链接：** https://x.com/bcherny/status/2090649326032945591  
**时间 / 互动：** Fri 21 Aug · Likes 985 · Views ~192k

##### 主帖在说什么

Reply to a screenshot of “Coding is solved” vs an agent that still can’t hot-reload: “Coding is solved, bugs are not yet solved. Fix incoming.” Later: “When I wrote code by hand it had bugs too.” And: “As models improve, I suspect we won’t need code review.”

##### 要点

- Splits generation (solved) from correctness (not)
- Fix incoming — this is a product bug thread, not a philosophy paper
- Extra take: code review itself may atrophy as models improve

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@GaryKildal** | If there are still bugs, coding isn’t solved — bugs *are* the problem coding is supposed to solve | [post](https://x.com/GaryKildal/status/2090655290387730584) |
| **@dedene** | Solving coding was the easy part (parent: still can’t hot-reload the 24/7 agent) | [post](https://x.com/dedene/status/2090690754129559639) |

##### 一句话概括

Boris treats “coding solved” as generation being cheap; the crowd treats unfixed bugs as the refutation.

#### 3. **Run /usage — parallelism, runaway loops, bad skills**

**链接：** https://x.com/bcherny/status/2090490321893499335  
**时间 / 互动：** Thu 20 Aug · Likes 196 · Views ~42k

##### 主帖在说什么

People burning Claude Code quota should run `/usage` for a breakdown. Most often: extreme parallelism, a runaway loop, or a very inefficient skill/plugin.

##### 要点

- Quota issues are often user harness, not silent server-side cuts
- Skills/plugins can be cost bugs
- `/usage` is the diagnostic

##### 回复中的有价值观点

Mostly support-thread follow-ups (“looking”, “fix landed”) rather than a thesis debate.

##### 一句话概括

Before you blame Anthropic billing, inspect whether your agent is looping.

### Products, launches, people

- Mythos-class ZDR (fall)
- Claude Code `/usage`
- Claude Code desktop on Electron
- Phone → local session, session-to-session communication (some of this already works)

### Tone

Support engineer-in-chief. Short, concrete, slightly provocative on “coding is solved.”
