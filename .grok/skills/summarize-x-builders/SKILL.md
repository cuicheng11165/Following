---
name: summarize-x-builders
description: >
  Fetch recent X/Twitter posts for builders listed in builders.md, summarize each
  person's themes and opinions into a time-stamped run folder under x/runs/, and
  track incremental windows per builder in x-summary-state.json. Use when the user
  wants X builder digests, monthly post summaries, incremental builder updates, or
  runs /summarize-x-builders or /x-builders.
---

# Summarize X Builders

You produce **per-builder summaries** of recent X posts.

**Critical: time windows are per person, not per whole job.**

- Each builder has their own `last_fetched_at` in `x-summary-state.json`.
- A newly added handle has no cursor → backfill the **past 30 days**.
- If a previous run failed halfway, only successfully finished handles advance.
- Do **not** use a single global `last_run_at` as the fetch floor for everyone.

**Critical: each run writes into its own time-stamped folder.**

- Never append new windows into the same forever-growing `x/<handle>.md`.
- Never dump all runs as flat files in `x/` root (hard to read after many runs).
- One run → one directory named by **run start time (UTC)**.

## Absolute rules

1. **Do not invent posts.** Only summarize content returned by X tools.
2. **Every claim that refers to a post should keep a post URL** when the tool provides one.
3. Work in the **current workspace root** (contains `builders.md` and `x/`).
4. Prefer tools over guessing. Zero posts in-range → still write a short empty-window note.
5. **One run, one output folder.** Do not prepend historical windows into a single file.
6. **Only advance a handle’s `last_fetched_at` after that handle succeeds** (file written in this run’s folder). Failures leave that handle’s cursor unchanged.
7. Prefer **updating state after each successful builder** (or small batch).
8. Keep **`x/README.md` as a run index only** (list of runs + link to latest), not a wall of every handle forever.

## Paths (relative to workspace root)

| Path | Purpose |
|------|---------|
| `builders.md` | Source list of builders (handles) |
| `x/runs/<run_id>/` | **This run’s** outputs only (one folder per run) |
| `x/runs/<run_id>/<handle>.md` | Per-builder summary for this run |
| `x/runs/<run_id>/README.md` | Index for this run only |
| `x/README.md` | Catalog of runs (latest first); not per-builder content |
| `x/latest` | Symlink (or text pointer) to the newest `x/runs/<run_id>/` |
| `x-summary-state.json` | Per-builder cursors + last run id |

### Run id format

At the **start** of each job, set:

```text
run_id = UTC now formatted as YYYY-MM-DDTHHMMSSZ
```

Examples: `2026-07-26T201500Z`, `2026-08-01T083012Z`

- Use **UTC**, zero-padded, **no colons** (filesystem-safe).
- Create the folder **once** at run start and write **all** this run’s files only there:

```bash
RUN_ID=$(date -u +"%Y-%m-%dT%H%M%SZ")
mkdir -p "x/runs/${RUN_ID}"
```

Optional deep post artifacts for this run only:

```text
x/runs/<run_id>/posts/<post_id>.md
```

### Layout goals (readability)

```text
x/
  README.md                 # run catalog only
  latest -> runs/2026-07-26T201500Z
  runs/
    2026-07-26T201500Z/     # one complete snapshot
      README.md
      karpathy.md
      swyx.md
      ...
    2026-07-20T090000Z/     # previous run (untouched)
      ...
```

**Do not** keep writing:

```text
x/karpathy.md   # accumulates forever — forbidden for new runs
```

### Migrating legacy flat layout

If you find old files like `x/karpathy.md`, `x/swyx.md` (not under `x/runs/`):

1. Create `x/runs/<legacy_run_id>/` using the best known time from those files’ meta
   (e.g. `Fetched at`) or from `x-summary-state.json` `last_run_at`.
2. Move all flat `x/*.md` **except** `x/README.md` into that run folder.
3. Rebuild `x/README.md` as a run catalog.
4. Point `x/latest` at that run folder.
5. Then start the new run in a **new** `run_id` folder.

### Retention (avoid pile-up)

After a successful run, **prune old run folders** so the tree stays readable:

| Setting | Default |
|---------|---------|
| Keep last **N** run directories under `x/runs/` | **N = 10** |

Rules:

1. List `x/runs/*/` sorted by name descending (ISO-like `run_id` sorts chronologically).
2. Keep the newest **10** (or N if the user specified another number).
3. **Delete** older run directories (entire folder).
4. Never delete the run folder you just wrote in this job until pruning runs after success.
5. If the user says “keep all history” or “do not prune”, skip deletion.
6. Report what was pruned in the final summary.

`x/latest` must always point at the newest remaining run after prune.

---

## State file format (version 2+)

```json
{
  "version": 2,
  "builders_file": "builders.md",
  "output_dir": "x/runs",
  "last_run_at": "2026-07-26T20:15:00Z",
  "last_run_id": "2026-07-26T201500Z",
  "last_run_dir": "x/runs/2026-07-26T201500Z",
  "retain_runs": 10,
  "builders": {
    "karpathy": {
      "name": "Andrej Karpathy",
      "last_fetched_at": "2026-07-26T20:15:00Z",
      "last_window_start": "2026-06-26T00:00:00Z",
      "last_window_end": "2026-07-26T20:15:00Z",
      "last_posts_fetched": 9,
      "last_status": "ok",
      "last_run_id": "2026-07-26T201500Z"
    }
  }
}
```

### Field meanings

| Field | Scope | Meaning |
|-------|--------|---------|
| `version` | global | `2` = per-builder cursors |
| `last_run_at` | global | Job heartbeat (not everyone’s fetch floor) |
| `last_run_id` / `last_run_dir` | global | Newest completed run folder |
| `retain_runs` | global | How many run folders to keep (default 10) |
| `builders.<handle>.last_fetched_at` | per person | Next run’s `window_start` for this handle |
| `builders.<handle>.last_run_id` | per person | Which run last successfully wrote this handle |

### Handle key matching

- Prefer the **canonical handle** from `builders.md` as the JSON key.
- Lookup is **case-insensitive**; consolidate casing to canonical.

### Migrating version 1 → 2

If top-level `last_run_at` + `builders_processed` (v1):

1. For each successful processed handle, set `last_fetched_at` from v1 `last_run_at` / `window_end`.
2. Failed / never-run handles: no cursor → 30-day backfill.
3. Rewrite as version 2; do not use global `last_run_at` as everyone’s floor after migration.

---

## Workflow

### Step 0 — Confirm workspace + create run folder

```bash
pwd
ls -la builders.md x-summary-state.json x 2>/dev/null
```

```bash
RUN_ID=$(date -u +"%Y-%m-%dT%H%M%SZ")
mkdir -p "x/runs/${RUN_ID}"
echo "$RUN_ID"
```

Remember `run_id` and `run_dir=x/runs/<run_id>` for the whole job.

If legacy flat `x/<handle>.md` files exist outside `runs/`, migrate them first (see above).

### Step 1 — Parse builders

```bash
python3 .grok/skills/summarize-x-builders/scripts/parse_builders.py builders.md
```

Produce `{ name, handle, profile_url }[]`. Deduplicate by case-insensitive handle.

### Step 2 — Load state and resolve **per-builder** windows

1. Load `x-summary-state.json` if present; migrate v1 → v2 if needed.
2. `run_now` = current UTC ISO-8601 (align with `run_id`).
3. For **each** builder:

| Condition | `window_start` | Mode |
|-----------|----------------|------|
| Valid `last_fetched_at` | that timestamp | `incremental` |
| Missing / never succeeded | `run_now − 30 days` | `30-day backfill` |

- `window_end` = `run_now`.
- X operators: `since:YYYY-MM-DD`, `until:` = day after end date.

Tell the user:

> Run folder: `x/runs/<run_id>/`  
> Per-builder windows: N incremental, M backfill  

### Step 3 — Fetch posts per builder

Same as before: `x_keyword_search` with each builder’s window, Latest, limit 10, paginate, cap 50.

Empty → write empty file in **this run folder** still counts as success for cursor.

### Step 4 — Summarize each builder into **this run folder only**

Write:

```text
x/runs/<run_id>/<handle>.md
```

Canonical handle for filename (e.g. `AmandaAskell.md`, `_catwu.md`).

Follow `references/output-template.md`.

**Each file is a single-run snapshot** (one window only). Do **not** prepend older windows into the same file. Historical content lives in older `x/runs/<other_id>/` folders.

#### Summary quality bar

1. Meta — run_id, window, post count, cap, mode  
2. Themes — 3–7 bullets  
3. Opinions / takes  
4. **Notable posts** — must use `summarize-x-post`  
5. Products / launches / people  
6. Tone  

Language: match the user.

#### Notable posts — must use `summarize-x-post`

For each of **3–5** high-signal posts (or all if fewer than 3):

1. Parse `post_id` from URL.  
2. `x_thread_fetch` with that id.  
3. Main post summary (2–6 sentences) + 要点.  
4. High-signal replies (who + take + link).  
5. One-line takeaway.

Structure: see `references/output-template.md`.

Optional: `x/runs/<run_id>/posts/<post_id>.md`.

Fallback if thread fetch fails twice: label `（仅列表摘要，thread 拉取失败）`.

### Step 5 — Update state **per successful handle**

After each success:

```json
{
  "name": "<display name>",
  "last_fetched_at": "<window_end ISO UTC>",
  "last_window_start": "<window_start ISO>",
  "last_window_end": "<window_end ISO>",
  "last_posts_fetched": <n>,
  "last_status": "ok",
  "last_run_id": "<run_id>"
}
```

Also set global `last_run_id`, `last_run_dir`, `last_run_at` as you go or at end.  
`last_status`: `empty` for zero posts. **Do not** advance cursor on error.

### Step 6 — Run index + root catalog + latest pointer

#### A) `x/runs/<run_id>/README.md`

Only this run:

- run_id, fetched at, mode notes  
- Table: handle | posts | notables | headline | file link  

#### B) `x/README.md` (run catalog)

Rewrite as a **list of runs**, newest first — **not** a full dump of every builder every time:

```markdown
# X Builders 运行目录

| 最新运行 | [x/runs/<run_id>/](./runs/<run_id>/) |
|----------|--------------------------------------|
| 快捷入口 | [x/latest](./latest) |

## 历史运行

| Run ID | 路径 | 说明 |
|--------|------|------|
| 2026-07-26T201500Z | [runs/...](./runs/...) | ... |
```

#### C) `x/latest`

```bash
cd x && rm -f latest && ln -s "runs/${RUN_ID}" latest
```

If symlink is undesirable on the platform, write `x/latest` as a one-line text file containing the path `runs/<run_id>`.

### Step 7 — Prune old runs

Unless user disabled retention:

```bash
# Keep newest retain_runs (default 10); delete the rest under x/runs/
```

Update `x/README.md` catalog after prune. Fix `x/latest` if needed.

### Step 8 — Report to user

- `run_id` and path `x/runs/<run_id>/`
- Incremental vs backfill counts
- Success / empty / failed
- Failed handles (cursor not advanced)
- How many old runs pruned
- Point to `x/latest` for reading

---

## Single-handle or custom window

- Still create (or reuse current job’s) `run_id` folder if this is part of a full run.
- One-off single handle: `x/runs/<run_id>/<handle>.md` is fine; advance only that handle’s cursor.
- Do not write back into a shared forever file.

---

## Tool cheat sheet

```text
x_keyword_search
  query: from:karpathy since:2026-07-26 until:2026-07-28
  limit: 10
  mode: Latest

x_thread_fetch
  post_id: 2079610838143623371

x_user_search
  query: karpathy
  count: 1
```

Related: **`summarize-x-post`** for every Notable item.

---

## Failure modes

| Situation | Action |
|-----------|--------|
| `builders.md` missing | Stop |
| No X tools | Stop |
| Cannot create `x/runs/<run_id>/` | Stop |
| New handle | 30-day backfill for that handle only |
| Partial crash | Finished handles keep cursors + files in run folder |
| Rate limits | Smaller batches; failed handles keep old cursors |
| Legacy flat `x/*.md` | Migrate into one historical run folder first |

---

## Done checklist

- [ ] `run_id` created; all outputs under `x/runs/<run_id>/` only  
- [ ] Builders parsed; per-builder windows resolved  
- [ ] Posts listed (cap 50); notables via `summarize-x-post` / `x_thread_fetch`  
- [ ] No flat forever-file under `x/<handle>.md` for this run  
- [ ] `x/runs/<run_id>/README.md` written  
- [ ] `x/README.md` is a **run catalog**  
- [ ] `x/latest` points at this run  
- [ ] Old runs pruned (default keep 10) unless disabled  
- [ ] Per-handle `last_fetched_at` updated only on success  
- [ ] User reported path + prune summary  
