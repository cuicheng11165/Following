# Output template for `X/<handle>.md`

Use this shape. Prepend new windows above older ones.

```markdown
# <Display Name> (@<handle>)

| Field | Value |
|-------|-------|
| Profile | https://x.com/<handle> |
| Bio | <from x_user_search if fetched> |
| Source list | builders.md |

---

## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

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

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **<短标题>**

**链接：** https://x.com/<handle>/status/<id>  
**时间 / 互动（如有）：** ...

##### 主帖在说什么

<2–6 句：该帖主张 / 发布 / 观察；含产品名、数字、限定条件>

##### 要点

- ...
- ...
- ...

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@handle** (Name) | <1–4 句实质观点> | [post](url) |

（无回复：写「未获取到回复上下文」。低信号：写「其余回复多为附和/表情」。）

##### 一句话概括

<一句>

#### 2. **...**

...

### Products, launches, people

- ...

### Tone

<1 short paragraph>

---

## Window: <older range>

...
```

### Notable posts checklist (must use `summarize-x-post`)

| Must | Must not |
|------|----------|
| `x_thread_fetch` for each notable `post_id` | Summarize only from search list snippet |
| Main post 2–6 sentences + 要点 | One vague phrase + URL |
| High-signal replies with who + take + link | Invent discussion |
| 3–5 notables per window (or all if &lt;3) | 8× shallow one-liners |
| Label thread-fetch failures honestly | Pretend replies were fetched |

Optional: also save `X/posts/<post_id>.md` using summarize-x-post’s full template.

### Empty window

```markdown
## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

- **Posts in window (fetched):** 0
- No public posts returned in this range (or tool returned none). Nothing to summarize.
```
