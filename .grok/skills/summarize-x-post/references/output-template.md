# Output template for a single X post summary

Use this shape in chat (and in any saved file). Match the user’s language.

```markdown
## 总结：@<handle> 的帖子

**作者：** <Display Name> (@<handle>)  
**时间：** <timestamp if available>  
**链接：** https://x.com/<handle>/status/<id>  
**互动（如有）：** likes / reposts / replies / views

### 主帖在说什么

<2–6 sentences or dense bullets: the core claim, complaint, announcement, or question.
Include concrete product names, numbers, and caveats from the post text.>

### 要点

- ...
- ...
- ...

### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@handle** (Name) | <1–4 sentences: distinct thesis, disagreement, product, or mechanism — not “agree”> | [post](url) |
| ... | ... | ... |

（若高信号回复很少：写“仅以下 N 条有实质内容”；若工具未返回回复：写“未获取到回复上下文”。）

### 一句话概括

<One sentence: what the post + discussion is really about.>
```

### English variant (when user writes in English)

```markdown
## Summary: @<handle>’s post

**Author:** ...  
**When:** ...  
**Link:** ...  
**Engagement (if any):** ...

### What the main post says

...

### Key points

- ...

### High-signal viewpoints from replies

| Who | Take | Link |
|-----|------|------|
| **@handle** | ... | [post](url) |

### One-line takeaway

...
```

---

## Quality checklist

| Must | Must not |
|------|----------|
| Summarize main post’s argument from tool text | Invent quotes or missing replies |
| Attribute each reply take to a person | “Someone said interesting things — url” only |
| Prefer insight / disagreement / product / mechanism | Dump every emoji reply |
| Include status URLs when tools provide them | Link-only lines with no paraphrase |
| Note empty reply context honestly | Pretend there was a rich discussion |

## Optional file save

If the user asks to save:

```text
X/posts/<post_id>.md
```

or a path they specify. Create parent dirs if needed. Prepend a short YAML or meta header only if useful; body stays the template above.
