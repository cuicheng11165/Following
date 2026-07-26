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
- **Cursor:** per-builder (`last_fetched_at` for this handle only; not a global job cursor)

### Themes

- ...

### Opinions and takes

- ...

### Notable posts

Each item = **that post’s viewpoint summary** (2–5 sentences) + **URL**. Never link-only or one vague phrase + link.

1. **<optional short title>**  
   <What this post claims, announces, or argues — concrete details from the post text.>  
   链接：https://x.com/<handle>/status/<id>

2. **<optional short title>**  
   <...>  
   链接：https://x.com/<handle>/status/<id>

### Products, launches, people

- ...

### Tone

<1 short paragraph>

---

## Window: <older range>

...
```

### Notable posts checklist

| Must | Must not |
|------|----------|
| Summarize **this** post’s argument / news / observation | Only “谈到了 X — url” |
| Keep numbers, product names, caveats from the post | Invent quotes or details |
| Include URL when available | Link-only lines |
| 3–8 items (or all if fewer posts) | Paste full raw tweets as the whole entry |

### Empty window

```markdown
## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

- **Posts in window (fetched):** 0
- No public posts returned in this range (or tool returned none). Nothing to summarize.
```
