# Output template for one builder in **one run folder**

Path (only when **posts &gt; 0**):

```text
x/runs/<run_id>/<handle>.md
```

Each file is a **single-run snapshot** (one window). Do not stack multiple historical windows in the same file.

## Zero posts — no file

If the fetch window returned **0 posts**:

- **Do not** write `x/runs/<run_id>/<handle>.md`
- **Do not** create empty placeholders (“Nothing to summarize”)
- Still update `x-summary-state.json` for that handle (`last_status: empty`, advance `last_fetched_at`)
- List the handle under **No updates** in the run `README.md` and the user-facing final report

---

## With posts — full summary

```markdown
# <Display Name> (@<handle>)

| Field | Value |
|-------|-------|
| Profile | https://x.com/<handle> |
| Bio | <from x_user_search if fetched> |
| Source list | builders.md |
| Run ID | <run_id> |
| Run dir | x/runs/<run_id>/ |

---

## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

- **Run ID:** <run_id>
- **Fetched at:** <ISO timestamp>
- **Posts in window (fetched):** <n> (cap 50: yes/no)
- **Mode:** incremental | 30-day backfill
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- ...

### Opinions and takes

- ...

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **<短标题>**

**链接：** https://x.com/<handle>/status/<id>  
**时间 / 互动（如有）：** ...

##### 主帖在说什么

<2–6 句>

##### 要点

- ...

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@handle** | <1–4 句> | [post](url) |

##### 一句话概括

<一句>

#### 2. **...**

...

### Products, launches, people

- ...

### Tone

<1 short paragraph>
```

---

# Run folder index: `x/runs/<run_id>/README.md`

```markdown
# Run <run_id>

| Field | Value |
|-------|-------|
| **Fetched at** | ... |
| **With reports** | n (posts &gt; 0, file written) |
| **No updates** | m (zero posts, state only — no file) |
| **Failed** | k (cursor not advanced) |

## With updates

| Handle | Name | Posts | Notables | Headline | File |
|--------|------|-------|----------|----------|------|
| karpathy | ... | 9 | 5 | ... | [karpathy.md](./karpathy.md) |

## No updates (cursor advanced, no report)

| Handle | Name | last_fetched_at |
|--------|------|-----------------|
| claudeai | Claude | 2026-08-03T02:48:02Z |
| _catwu | Cat Wu | 2026-08-03T02:48:02Z |
```

Only list handles that were successfully processed with zero posts. Failed handles go in a separate **Failed** section (or the final user report), and their cursors stay unchanged.

---

# Root catalog: `x/README.md` (runs only)

```markdown
# X Builders 运行目录

每次 `/summarize-x-builders` 写入独立文件夹 `x/runs/<运行时间UTC>/`，避免单文件无限追加。

仅有新帖的 builder 会生成 `<handle>.md`；无更新的人只推进 `x-summary-state.json` 游标。

| 最新 | [./latest](./latest) → `runs/<run_id>/` |
|------|----------------------------------------|

## 历史运行（新 → 旧）

| Run ID | 路径 |
|--------|------|
| 2026-07-26T201500Z | [runs/2026-07-26T201500Z/](./runs/2026-07-26T201500Z/) |
```

Default retention: keep last **10** run folders; older runs may be deleted after a successful job.
