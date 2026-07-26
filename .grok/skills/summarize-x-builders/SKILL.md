---
name: summarize-x-builders
description: >
  Fetch recent X/Twitter posts for builders listed in builders.md, summarize each
  person's themes and opinions into X/<handle>.md, and track incremental windows
  per builder in x-summary-state.json (each handle has its own last_fetched_at).
  Use when the user wants X builder digests, monthly post summaries, incremental
  builder updates, or runs /summarize-x-builders or /x-builders.
---

# Summarize X Builders

You produce **per-builder summaries** of their recent X posts under the workspace
`X/` directory.

**Critical: time windows are per person, not per whole job.**

- Each builder has their own `last_fetched_at` in `x-summary-state.json`.
- A newly added handle has no cursor → backfill the **past 30 days**.
- If a previous run failed halfway, only successfully finished handles advance;
  unfinished handles keep their old cursor (or still get a 30-day backfill if never done).
- Do **not** use a single global `last_run_at` as the fetch floor for everyone.

## Absolute rules

1. **Do not invent posts.** Only summarize content returned by X tools.
2. **Every claim that refers to a post should keep a post URL** when the tool provides one.
3. Work in the **current workspace root** (contains `builders.md` and `X/`).
4. Prefer tools over guessing. Zero posts in-range → still write a short empty-window note.
5. Never delete prior summary sections unless the user explicitly asks for a full rewrite.
6. **Only advance a handle’s `last_fetched_at` after that handle succeeds** (summary file written). Failures leave that handle’s cursor unchanged.
7. Prefer **updating state after each successful builder** (or small batch), so a mid-run crash does not lose progress.

## Paths (relative to workspace root)

| Path | Purpose |
|------|---------|
| `builders.md` | Source list of builders (handles) |
| `X/` | Output: one markdown file per builder |
| `x-summary-state.json` | **Per-builder** fetch cursors + last-run metadata |

If `builders.md` is missing, stop and tell the user.

---

## State file format (version 2)

```json
{
  "version": 2,
  "builders_file": "builders.md",
  "output_dir": "X",
  "last_run_at": "2026-07-26T18:59:13Z",
  "builders": {
    "karpathy": {
      "name": "Andrej Karpathy",
      "last_fetched_at": "2026-07-26T18:59:13Z",
      "last_window_start": "2026-06-26T00:00:00Z",
      "last_window_end": "2026-07-26T18:59:13Z",
      "last_posts_fetched": 9,
      "last_status": "ok"
    },
    "swyx": {
      "name": "Swyx",
      "last_fetched_at": "2026-07-26T18:59:13Z",
      "last_window_start": "2026-06-26T00:00:00Z",
      "last_window_end": "2026-07-26T18:59:13Z",
      "last_posts_fetched": 40,
      "last_status": "ok"
    }
  }
}
```

### Field meanings

| Field | Scope | Meaning |
|-------|--------|---------|
| `version` | global | Must be `2` for per-builder cursors |
| `last_run_at` | global | When the **job** last finished or last wrote state (informational only; **not** the fetch floor for all handles) |
| `builders.<handle>` | per person | Cursor and last result for that handle |
| `last_fetched_at` | per person | End of the last **successful** window for this handle. Next run uses this as `window_start` |
| `last_window_start` / `last_window_end` | per person | Last successful window bounds |
| `last_posts_fetched` | per person | Count in last successful fetch |
| `last_status` | per person | `ok` \| `empty` \| `error` (only `ok`/`empty` advance the cursor; `error` does not) |

### Handle key matching

- Prefer the **canonical handle** from `builders.md` as the JSON key (e.g. `AmandaAskell`, `_catwu`).
- When looking up, match **case-insensitively** if the key casing differs.
- Never invent a second entry for the same person under different casing; consolidate into the canonical key.

### Migrating version 1 → 2

If `x-summary-state.json` has `"version": 1` (or no version) with top-level `last_run_at` and `builders_processed`:

1. Build `builders` map: for each handle in `builders_processed` that is **not** in `builders_failed`, set:
   - `last_fetched_at` = top-level `last_run_at` (or `window_end` if present)
   - `last_window_start` / `last_window_end` from v1 fields when available
   - `last_posts_fetched` from `posts_fetched[handle]` when available
   - `last_status`: `ok`
2. Handles only in `builders_failed` (or never listed): **no** `last_fetched_at` → 30-day backfill next time.
3. Rewrite the file as **version 2** before or while processing.
4. Do **not** keep using v1 global `last_run_at` as everyone’s floor after migration.

---

## Workflow

### Step 0 — Confirm workspace

```bash
pwd
ls -la builders.md x-summary-state.json X 2>/dev/null
```

```bash
mkdir -p X
```

### Step 1 — Parse builders

```bash
python3 .grok/skills/summarize-x-builders/scripts/parse_builders.py builders.md
```

Produce `{ name, handle, profile_url }[]`. Deduplicate by case-insensitive handle.

### Step 2 — Load state and resolve **per-builder** windows

1. Load `x-summary-state.json` if present; migrate v1 → v2 if needed.
2. Let `run_now` = current UTC time (ISO-8601).
3. For **each** builder independently:

| Condition | `window_start` | Mode label |
|-----------|----------------|------------|
| `builders[handle].last_fetched_at` exists and is valid ISO time | that timestamp | `incremental` |
| No entry / missing `last_fetched_at` / never succeeded | `run_now − 30 days` | `30-day backfill` |

- `window_end` = `run_now` (same end for everyone in this job is fine; **starts differ**).
- For X date operators, convert to `YYYY-MM-DD`:
  - `since:` = calendar date of `window_start` (optional: one day earlier for safety; document if you do)
  - `until:` = day **after** `window_end` date (exclusive upper bound)

Tell the user a short plan table, for example:

> Per-builder windows (sample):  
> - karpathy: incremental from 2026-07-26T18:59:13Z  
> - newhandle: 30-day backfill  
> - failed_last_time: 30-day or resume from their last ok cursor  

If many share the same cursor, you may group: “22 incremental from T, 4 backfill”.

### Step 3 — Fetch posts per builder

Use that builder’s own `since` / `until` derived from **their** window.

#### Primary tool: `x_keyword_search`

```text
from:<handle> since:<this_builder_start_date> until:<this_builder_end_date_plus_one>
```

- `mode: "Latest"`
- `limit` max **10** per call — paginate

#### Pagination

1. First page: limit 10, Latest.
2. If 10 results: tighten `until:` from oldest post in page (or `max_id:`).
3. Stop when page &lt; 10, posts before `window_start`, or **50 posts** cap (note cap in file).

#### Empty / errors

- **0 posts:** write empty-window section; treat as success for cursor advance (`last_status: "empty"`).
- **Tool / write failure:** set in-memory `last_status: "error"`; **do not** update `last_fetched_at` for that handle; continue others.

Process in parallel batches (3–5) when possible. Each builder still uses **its own** window.

### Step 4 — Summarize each builder

Write/update:

```text
X/<handle>.md
```

Use the **canonical handle** from `builders.md` for the filename (e.g. `X/AmandaAskell.md`, `X/_catwu.md`).

Follow `references/output-template.md`.

**Incremental file behavior:**

- Prepend a new `## Window: <start> → <end>` section if the file exists.
- Do not remove older window sections.
- Meta must record **this handle’s** window and mode (`incremental` vs `30-day backfill`).

#### Summary quality bar

1. Meta — window, post count, cap hit?
2. Themes — 3–7 bullets
3. Opinions / takes — cross-cutting views across the window
4. **Notable posts** — **must** use the `summarize-x-post` skill (see below)
5. Products / launches / people
6. Tone — short paragraph

Language: match the user (Chinese if they write Chinese).

#### Notable posts — **must use `summarize-x-post`**

A short paraphrase of the keyword-search snippet is **not enough**.

For each notable post you **must** run the **`summarize-x-post`** workflow
(read `.grok/skills/summarize-x-post/SKILL.md` and its
`references/output-template.md` if needed):

1. Parse `post_id` from the status URL (digits after `/status/`).
2. Call `x_thread_fetch` with that `post_id` (main post + parent/replies).
3. Summarize **main post** (2–6 sentences + key points).
4. Extract **high-signal reply viewpoints** (who + take + link; typically 3–8 replies; skip emoji/spam).
5. Add a **one-line takeaway** for post + discussion.

**Selection:** pick **3–5** high-signal posts per builder per window
(or all posts if fewer than 3). Prefer:

- Original theses / long threads / product launches
- High engagement or dense technical content
- Not pure RTs of others without added comment (unless the quote-comment is the point)

**Per-item structure inside `### Notable posts`:** embed a compact
`summarize-x-post` block (same sections as that skill’s template):

```markdown
### Notable posts

> 以下每条均按 skill `summarize-x-post`：`x_thread_fetch` 主帖 + 高信号回复。

#### 1. **<短标题>**

**链接：** https://x.com/<handle>/status/<id>  
**时间 / 互动（如有）：** ...

##### 主帖在说什么

<2–6 句：主张、论据、产品名、数字、限定条件；勿只写一句空话>

##### 要点

- ...
- ...

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@handle** | <1–4 句实质观点，非 “agree”> | [post](url) |

（无回复上下文时写明「未获取到回复上下文」。）

##### 一句话概括

<一句：主帖 + 讨论的核心>
```

**Optional artifact:** also write full post digests to
`X/posts/<post_id>.md` when useful; still **embed** the summary in
`X/<handle>.md` so the builder file stands alone.

**Bad (do not write this):**

```markdown
1. 谈到了 AI agent — https://x.com/...
2. **Opus 5**  
   发布了 Opus 5，很好。  
   链接：https://x.com/...
```

**Rules:**

- **No notable item without `x_thread_fetch`** (unless fetch fails twice — then note the error and fall back to search-snippet summary labeled `（仅列表摘要，thread 拉取失败）`).
- Do **not** invent replies or quotes.
- Parallelize: after selecting notable IDs for a handle, you may `x_thread_fetch` several posts concurrently.
- Cap: still max **50** list posts per handle from search; deep-summarize only the 3–5 notables.

### Step 5 — Update state **per successful handle**

After each handle succeeds (file written, including empty window):

1. Read current `x-summary-state.json` (or keep a merged in-memory object you flush often).
2. Upsert `builders[handle]`:

```json
{
  "name": "<display name>",
  "last_fetched_at": "<this handle window_end ISO UTC>",
  "last_window_start": "<this handle window_start ISO>",
  "last_window_end": "<this handle window_end ISO>",
  "last_posts_fetched": <n>,
  "last_status": "ok"
}
```

Use `"empty"` for zero-post success. Do **not** write `last_fetched_at` for errors.

3. Optionally set global `last_run_at` to now (job heartbeat only).
4. Write the full JSON back (`version: 2`).

**Safe write pattern:** rewrite the whole file with pretty-printed JSON after each success or after each small batch so crashes mid-job only lose the unfinished handles.

### Step 6 — Index

Update `X/README.md` after the run (or incrementally):

- Note that windows are **per builder**
- Table: handle | name | window mode | window start → end | posts | headline | file

### Step 7 — Final state + report

1. Ensure `x-summary-state.json` is version 2 and reflects every success/error this run.
2. Global `last_run_at` = job end time (informational).
3. Report to user:

- How many incremental vs 30-day backfill
- Success / empty / failed counts
- List failed handles (cursor **not** advanced)
- List newly backfilled handles (no prior cursor)
- Paths: `X/`, `x-summary-state.json`

---

## Single-handle or custom window

If the user asks for one person or a custom range:

- Use their range, or that handle’s per-person cursor if not specified.
- Still write `X/<handle>.md`.
- On success, advance **only that handle’s** `last_fetched_at` (unless they asked for a dry-run).

---

## Tool cheat sheet

```text
# List posts in window
x_keyword_search
  query: from:karpathy since:2026-07-26 until:2026-07-28
  limit: 10
  mode: Latest

# Deep-summarize each notable (required) — same as skill summarize-x-post
x_thread_fetch
  post_id: 2079610838143623371

x_user_search
  query: karpathy
  count: 1
```

Related skill: **`summarize-x-post`** (`.grok/skills/summarize-x-post/SKILL.md`) — single post + discussion. This skill **calls that method** for every Notable item.

Do **not** scrape x.com HTML as the primary method.

---

## Failure modes

| Situation | Action |
|-----------|--------|
| `builders.md` missing | Stop |
| No X tools | Stop |
| New handle, no state entry | 30-day backfill for that handle only |
| Handle failed last run | Retry from their last **successful** `last_fetched_at`, or 30-day if never succeeded |
| Partial job crash | Already-saved handles keep new cursors; rest unchanged |
| Rate limits | Smaller batches; failed handles keep old cursors |
| v1 state file | Migrate to v2 per rules above |

---

## Done checklist

- [ ] Builders parsed from `builders.md`
- [ ] State loaded; v1 migrated to v2 if needed
- [ ] **Each** builder has its own window (incremental or 30-day)
- [ ] Posts listed with pagination (cap 50)
- [ ] Each Notable post ran **`summarize-x-post`** / `x_thread_fetch` (not list-snippet only)
- [ ] `X/<handle>.md` written/prepended for each attempted handle
- [ ] `last_fetched_at` updated **only** for successes (per handle)
- [ ] `X/README.md` updated
- [ ] User report includes incremental vs backfill vs failed
