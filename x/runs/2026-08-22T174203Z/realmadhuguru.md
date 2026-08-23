# Madhu Guru (@realmadhuguru)

| Field | Value |
|-------|-------|
| Profile | https://x.com/realmadhuguru |
| Bio | Sr Director, AI at Meta; Prev: Google - Led Gemini, Veo, Nano Banana. |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 8 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Daily “how to build great evals” series (parts 3–5 this window)
- Laddered eval strategy: hill-climb / regression / smoke / launch
- Tyranny of the average: don’t collapse a suite into one score
- Quality-first then cost-down (treat evals like frontier models)
- Failure-mode taxonomy from production traces

### Opinions and takes

- Enterprises fail at AI for lack of eval strategy, not models
- Weighted scores fake mathematical precision around a judgment call
- People who can look at details beat abstracted dashboards
- Get the trusted signal first (expensive judge, humans), then cheapen

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Part 5 — stop dumbing evals into one score**

**链接：** https://x.com/realmadhuguru/status/2090930137885774324  
**时间 / 互动：** Fri 21 Aug · Likes 217 · Bookmarks 311 · Views ~21k

##### 主帖在说什么

Don’t collapse a complex eval suite into one number because a senior wants a simplified decision. Happened in early Gemini. “Tyranny of the average.” Example: summarization 85→89, basic QA 80→85, complex financial analysis 70→63 — a single score hides that the frontier use case got worse. Weighted scores just launder a judgment call. Instead: keep a prioritized ladder (from part 4); staff who can read details; understand where each eval fails/shines; decide if the *system* is better for users.

##### 要点

- Multi-dimensional quality, no “one number”
- Weighted averages are fake rigor
- Decision-makers must sit with the failures

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bhi5hmaraj** | Wants more posts on hill climbing | [post](https://x.com/bhi5hmaraj/status/2091185436354036033) |

##### 一句话概括

If your dashboard is one number, you will ship a model that got worse at the thing you actually care about.

#### 2. **Part 4 — laddered eval strategy**

**链接：** https://x.com/realmadhuguru/status/2090595384905113939  
**时间 / 互动：** Fri 21 Aug · Likes 239 · Bookmarks 367 · Views ~33k （仅列表摘要，thread 拉取失败）

##### 主帖在说什么

Enterprises struggle because they lack an eval strategy. You need a ladder on the cost/realism spectrum: hill-climb evals (push the frontier, refresh continually); regression (did we break today while climbing); smoke (safety/basics, e.g. product identity); launch (near-online, real-ish traffic). Correction: “hill climbing evals,” not “hill-climb long.”

##### 要点

- Different evals have different jobs
- Realism vs control is a spectrum, not a single test
- Unique use cases, not generic HELM

##### 回复中的有价值观点

Self-thread plus part 5; no dense third-party debate in the keyword set.

##### 一句话概括

One eval is not a strategy; four kinds of evals are.

#### 3. **Part 3 — name the failure, then you can test it**

**链接：** https://x.com/realmadhuguru/status/2090242427944833047  
**时间 / 互动：** Thu 20 Aug · Likes 128 · Bookmarks 197 · Views ~7k （仅列表摘要，thread 拉取失败）

##### 主帖在说什么

First thing after v1 evals: a failure-mode taxonomy. Study last 500–1,000 production traces, cluster, *name* them specifically — not “bad answer.” Wrong doc retrieved vs right doc / wrong section vs ungrounded hallucination vs failed to punt vs assumed instead of clarifying. Named failures become targeted tests. That’s the bridge from evals to an improvement flywheel. Earlier in the series: quality-first then cost (expensive judges first).

##### 要点

- Taxonomy before more metrics
- Production traces, not synthetic-only
- Precision of the cluster name is the whole game

##### 回复中的有价值观点

Series is mostly one-way teaching; he asks for eval questions in comments.

##### 一句话概括

If you can’t name the failure, you can’t write the eval that catches it.

### Products, launches, people

- Gemini (early-days average-score war story)
- Daily eval series (parts 1–5)

### Tone

Practitioner-teacher. Bookmark-heavy, low-ratio replies. Written for teammates and managers who “run from complexity.”
