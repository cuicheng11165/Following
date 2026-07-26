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

1. <one-line paraphrase> — <url>
2. ...

### Products, launches, people

- ...

### Tone

<1 short paragraph>

---

## Window: <older range>

...
```

### Empty window

```markdown
## Window: <YYYY-MM-DD> → <YYYY-MM-DD>

- **Posts in window (fetched):** 0
- No public posts returned in this range (or tool returned none). Nothing to summarize.
```
