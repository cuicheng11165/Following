# Peter Steinberger (@steipete)

| Field | Value |
|-------|-------|
| Profile | https://x.com/steipete |
| Bio | Polyagentmorous ClawFather. OpenClaw + OpenAI |
| Source list | builders.md |
| Run ID | 2026-09-06T143124Z |
| Run dir | x/runs/2026-09-06T143124Z/ |

---

## Window: 2026-08-29 → 2026-09-06

- **Run ID:** 2026-09-06T143124Z
- **Fetched at:** 2026-09-06T14:31:24Z
- **Posts in window (fetched):** 20 (cap 50: paginated, stopped ~20)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- OpenClaw: sessions vs subagents, nesting cap at two levels
- Bottleneck is CI and GitHub API calls, not the model
- App server is open source so he one-shotted a UI (slop, but it does the job)
- crabbox for ~40+ providers
- Grok Bot probably doesn’t show subagents

### Opinions and takes

- Sessions are steerable and stay; subagents disappear and are readonly
- You don’t need the fancy UI: iMessage agent is enough, ask for more power when needed
- Focus is performance and reliability (2026.9.2 / dev channel)
- Limited by compute, then CI/GitHub

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Limited by CI and GitHub API**

**链接：** https://x.com/steipete/status/2096465112685273169  
**时间 / 互动：** Sun 06 Sep · Likes 320 · Replies 27 · Views ~19k

##### 主帖在说什么

Reply to Theo’s “Fable 5.1 and Astra changed how much we ship”: he’s limited by CI and GitHub API calls at this stage. Related: multi-nesting exists but subagent generation is capped at two levels.

##### 要点

- Model is no longer the bottleneck
- Infra/quotas are

##### 回复中的有价值观点

Lives on Theo’s thread. See theo.md.

##### 一句话概括

The lobster is GPU-rich and GitHub-poor.

#### 2. **Sessions vs subagents**

**链接：** https://x.com/steipete/status/2096477729663377679  
**时间 / 互动：** Sun 06 Sep · Likes 8 · Replies 3 · Views ~1.7k

##### 主帖在说什么

Are these sessions or subagents? Difference is blurry: sessions are steerable and stay; subagents disappear and are readonly. Grok Bot showing subagents: he doubts it.

##### 要点

- Taxonomy for harness UIs
- OpenClaw vs Grok Bot comparison

##### 回复中的有价值观点

Short technical back-and-forth, not a long thesis thread.

##### 一句话概括

He’s drawing the session/subagent line in public because the UIs are blurring it.

### Products, launches, people

- OpenClaw (open source + his prompt)
- crabbox (~40 providers)
- Grok Bot (comparison)
- 2026.9.2 / dev channel

### Tone

High-volume product-debug tweets. Most of the 20 are replies in two conversations.
