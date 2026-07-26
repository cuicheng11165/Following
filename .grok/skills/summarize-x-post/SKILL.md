---
name: summarize-x-post
description: >
  Fetch a specified X/Twitter post and its thread replies, then summarize the main post
  and extract high-signal viewpoints from the discussion. Use when the user pastes an
  x.com/twitter.com status URL, asks to summarize a tweet and replies, digests a thread
  discussion, or runs /summarize-x-post or /x-post.
---

# Summarize X Post

Summarize **one** X post (and its discussion): the main take, plus **high-signal**
viewpoints from replies / thread context. Default output is in the **user’s language**
(Chinese if they write Chinese).

## Absolute rules

1. **Do not invent posts or quotes.** Only use content returned by X tools.
2. **Prefer tools over scraping.** Primary: `x_thread_fetch`. Do not scrape x.com HTML as the main method.
3. Keep **post URLs** for the main post and for every cited reply when available.
4. Filter replies: surface **valuable** takes (insight, disagreement, product, technical depth), not pure emoji/“this”/spam.
5. If the tool returns little or no reply context, say so — do not pad with invented discussion.

---

## Input

Accept any of:

| Form | Example |
|------|---------|
| Status URL | `https://x.com/user/status/123` or `https://twitter.com/user/status/123` |
| Status ID | `1234567890` |
| Handle + ID (if both given) | `@user` + id |

**Parse `post_id`:** the numeric id after `/status/` (or the bare numeric id).

If the user gives no id/URL, ask once for a link or status id, then stop until provided.

Optional flags (apply when the user asks):

- **More depth / longer:** include more replies, longer bullets
- **Save to file:** write under workspace (e.g. `X/posts/<id>.md` or path they name)
- **English only / Chinese only:** force output language

---

## Workflow

### Step 1 — Fetch the post + context

Use:

```text
x_thread_fetch
  post_id: <numeric id>
```

Capture:

- Main post: author name, `@handle`, time, text, engagement if present
- Parent posts (if this is a reply)
- Replies / thread context returned by the tool

If fetch fails or returns empty: report the error; do not invent content. Optionally retry once.

### Step 2 — Optional enrichment (only if useful)

- Author bio / identity: `x_user_search` with the author’s handle (1 result) when context helps.
- If the main post is a thin pointer (“see this”, single link) and the user wants the article: you may open the linked page with browse tools **in addition to** summarizing the post itself — label external content separately from the X text.
- Do **not** start a full `summarize-x-builders` run.

### Step 3 — Select high-signal replies

From replies / thread context, keep replies that do at least one of:

- Add a **distinct thesis** or mechanism (not just “agree”)
- **Disagree** with a reason
- Share **product / repo / paper** relevant to the topic
- Give **concrete numbers, experience, or architecture**
- Reframe the problem (root cause, missing primitive, etc.)

Drop or collapse:

- Single-emoji / “lol” / “this” / pure tags
- Spam, promo spam, empty quotes
- Near-duplicates (merge into one bullet; name one representative)

Prefer **quality over quantity**: typically **3–8** reply takes. If fewer high-signal replies exist, use all of them. If many, pick the strongest and note “other replies were low-signal.”

### Step 4 — Write the summary

Follow `references/output-template.md`. Structure:

1. **Meta** — author, handle, time, link, light engagement if available  
2. **Main post summary** — 2–6 sentences (or dense bullets): claim, argument, ask  
3. **Key points** — 3–7 bullets from the main post only  
4. **Valuable viewpoints from replies** — table or numbered list: who, take, link  
5. **One-line takeaway** — what the discussion is really about  

**Quality bar for the main post:**

- Paraphrase structure; do not dump raw tweet as the whole summary  
- Keep product names, numbers, caveats from the text  
- If it is a short complaint/question, state the frustration and the desired direction  

**Quality bar for replies:**

- Each item = **who** + **viewpoint summary** (1–4 sentences) + **URL** when available  
- Not “某人回复了 — url”  
- Attribute clearly (`@handle` or display name)  

### Step 5 — Deliver

- Default: reply in chat with the full summary markdown.  
- If user asked to save: write the file, confirm path.  
- Offer nothing extra unless useful (e.g. “I can dig into reply author X”).

---

## Tool cheat sheet

```text
x_thread_fetch
  post_id: 2079540355234414716

x_user_search
  query: adityaag
  count: 1
```

URL form: `https://x.com/<handle>/status/<post_id>`

---

## Failure modes

| Situation | Action |
|-----------|--------|
| No URL / id | Ask once |
| Invalid id | Say so; ask for a correct link |
| Tool error / empty | Report; no invented posts |
| No replies returned | Summarize main post only; note missing reply context |
| Post is non-English | Summarize in user’s language; keep key terms if needed |
| User wants builders batch digest | Hand off to `summarize-x-builders`, not this skill |

---

## Done checklist

- [ ] `post_id` parsed from URL or bare id  
- [ ] `x_thread_fetch` used for main + context  
- [ ] Main post summarized without invention  
- [ ] High-signal replies selected and attributed  
- [ ] Links included when available  
- [ ] Output language matches user (or their override)  
- [ ] File written only if requested  
---

## Related

- Batch / per-builder digests → skill `summarize-x-builders`  
- This skill is **single post + discussion**, not a monthly builder rollup  
