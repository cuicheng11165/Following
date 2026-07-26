# Output template for one builder in **one run folder**

Path:

```text
x/runs/<run_id>/<handle>.md
```

Each file is a **single-run snapshot** (one window). Do not stack multiple historical windows in the same file.

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

### Empty window

```markdown
# <Display Name> (@<handle>)

| Field | Value |
|-------|-------|
| Run ID | <run_id> |

## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

- **Posts in window (fetched):** 0
- No public posts returned in this range. Nothing to summarize.
```

---

# Run folder index: `x/runs/<run_id>/README.md`

```markdown
# Run <run_id>

| Field | Value |
|-------|-------|
| **Fetched at** | ... |
| **Builders** | n success / m empty / k failed |

| Handle | Name | Posts | Notables | Headline | File |
|--------|------|-------|----------|----------|------|
| karpathy | ... | 9 | 5 | ... | [karpathy.md](./karpathy.md) |
```

---

# Root catalog: `x/README.md` (runs only)

```markdown
# X Builders 运行目录

每次 `/summarize-x-builders` 写入独立文件夹 `x/runs/<运行时间UTC>/`，避免单文件无限追加。

| 最新 | [./latest](./latest) → `runs/<run_id>/` |
|------|----------------------------------------|

## 历史运行（新 → 旧）

| Run ID | 路径 |
|--------|------|
| 2026-07-26T201500Z | [runs/2026-07-26T201500Z/](./runs/2026-07-26T201500Z/) |
```

Default retention: keep last **10** run folders; older runs may be deleted after a successful job.
