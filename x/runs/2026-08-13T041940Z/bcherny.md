# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude Code @anthropicai |
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

- LLM bugs shifted from off-by-ones to system design / UX / missing context
- Adversarial `/code-review` (low/medium; low uses no agents, higher up to 10)
- Token cost falling as models improve (Pareto frontier shifts left)
- Worktree cleanup; billing-UI bug refunds (196 Fable overage purchases)

### Opinions and takes

- Some kinds of coding are solved; not all
- `/code-review low` beats other models at <$0.01 in their evals
- Each generation needs fewer tokens for the same task
- Hands-on support: refunds, usage debugging, “keep the feedback coming”

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Bugs changed shape; adversarial review is the tool**

**链接：** https://x.com/bcherny/status/2087284684103537011  
**时间 / 互动：** Tue 11 Aug · Likes 3810 · Bookmarks 2056 · Views ~487k

##### 主帖在说什么

Quoting Jarred Sumner’s “doesn’t happen anymore,” Boris argues LLM bugs are now design/UX/context failures, not off-by-ones. Adversarial review (one-line prompt or `/code-review`) catches many of them.

##### 要点

- Class of remaining bugs is higher-level
- Review can be a one-liner or built-in command
- Effort knobs: low sips tokens; higher effort uses up to 10 agents

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@PawelHuryn** | Best adversarial review is a *different model family*, not more of the same | [post](https://x.com/PawelHuryn/status/2087290193552474145) |
| **@jadenitripp** | Wishes the answer weren’t “throw more tokens at it” | [post](https://x.com/jadenitripp/status/2087297360120721902) |
| **@backnotprop** | Asking for “adversarial” review gets the chat flagged | [post](https://x.com/backnotprop/status/2087286171638612429) |

##### 一句话概括

Coding agents still fail — just at architecture now — and the fix is a hostile second reader.

#### 2. **Should Claude Code clean stale worktrees?**

**链接：** https://x.com/bcherny/status/2087024157196489117  
**时间 / 互动：** Tue 11 Aug · Likes 2125 · Replies 290

##### 主帖在说什么

Worktrees pile up. He uses a loop to clean stale ones and asks if this should be built into Claude Code. High engagement as a product-probe.

##### 要点

- Worktree hygiene is a real agent-coding pain
- Productizing personal loops

##### 回复中的有价值观点

Thread replies were mostly +1 / usage reports; not listed individually.

##### 一句话概括

The next Claude Code primitive may be janitorial: delete the worktrees agents leave behind.

### Products, launches, people

- `/code-review` (low/medium; forked agent since 2.1.218)
- Fable overage UI bug: refunds + extra credits for 196 users
- Jarred Sumner (quoted)

### Tone

Founder-support mode: ship, refund, debug `/usage` with users, then drop a 400k-view thesis.
