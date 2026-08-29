# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
| Source list | builders.md |
| Run ID | 2026-08-29T145528Z |
| Run dir | x/runs/2026-08-29T145528Z/ |

---

## Window: 2026-08-22 → 2026-08-29

- **Run ID:** 2026-08-29T145528Z
- **Fetched at:** 2026-08-29T14:55:28Z
- **Posts in window (fetched):** 19 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- The web splits: ultra-fancy human experiences vs agent-centric markdown/MCP; the middle becomes JIT UI
- MCP usage exploding (Vercel MCP +564% in 3 months; mcp-handler npm)
- Eve: one-minute agents with a Git repo you own
- Cursor → Origin → deploy to Vercel

### Opinions and takes

- Agent as the new browser for utilitarian content
- Easy agent builders are common; owning the whole intelligence stack (runtime, models, skills, tools, sandbox) is not
- Models getting more performant → UI getting more generative
- Embrace all deploy paths: Claude Code, fx.sh, Cursor, open platforms

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Web in two extremes; the middle is JIT UI**

**链接：** https://x.com/rauchg/status/2093482695838007318  
**时间 / 互动：** Fri 28 Aug · Likes 805 · Bookmarks 556 · Views ~51k

##### 主帖在说什么

The web evolves toward (1) ultra-fancy human experiences (vgpu.sh / threejs / typegpu) and (2) agent-centric lossless signal (markdown, MCP). The in-between is subsumed by agents producing just-in-time UI. When you need utilitarian content, it will be generated for you. Agent as the new browser.

##### 要点

- Delight vs machine-readable as the two surviving poles
- Utilitarian pages become generated, not designed
- MCP/markdown as the agent-facing web

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ricmac** | Or human experience *augmented* by agents — Engelbart was right | [post](https://x.com/ricmac/status/2093487340572360791) |
| **@purrrealist** | Wants both ends: lovely for people, legible for agents — does one eat the other? | [post](https://x.com/purrrealist/status/2093485977822179568) |

##### 一句话概括

Rauch’s web thesis: beauty and machine-signal survive; CRUD websites get eaten by agents.

#### 2. **MCP is growing explosively**

**链接：** https://x.com/rauchg/status/2093463771071336497  
**时间 / 互动：** Fri 28 Aug · Likes 324 · Bookmarks 163 · Views ~68k

##### 主帖在说什么

Quotes Vercel eng: Vercel MCP tool calls +564% in 3 months (Jun +43, Jul +117, Aug +114). Not just Vercel — look at `mcp-handler` npm downloads for implementing MCP servers.

##### 要点

- First-party usage + ecosystem package as dual charts
- MCP as infrastructure, not a demo protocol

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@mxstbr** | Should I look up Chat/Codex MCP gateway traffic? | [post](https://x.com/mxstbr/status/2093477925790048661) |
| **@SlimAssiliX** | mcp-handler downloads = more tool calls; the cost chart lags npm ~30 days | [post](https://x.com/SlimAssiliX/status/2093484121804681608) |

##### 一句话概括

MCP crossed from blog-post protocol to something whose npm and tool-call charts both go vertical.

#### 3. **Eve: an agent with a Git repo you own**

**链接：** https://x.com/rauchg/status/2093387887668814214  
**时间 / 互动：** Fri 28 Aug · Likes 413 · Bookmarks 306 · Views ~59k

##### 主帖在说什么

Many easy ways to create agents. How many give you a Git repo where you own the whole intelligence stack — runtime, model choice, skills, tools, connectivity, sandbox? Start: https://vercel.com/new/agent

##### 要点

- Ownership of the stack is the differentiator vs toy agent builders
- Prompt → models/MCP → deploy, backed by git

##### 回复中的有价值观点

Light product replies (Stripe? shipping is easy). The thesis is in the post.

##### 一句话概括

Vercel’s agent play is “you own the repo,” not “we host a chatbot.”

### Products, launches, people

- eve — https://vercel.com/new/agent
- Vercel MCP; mcp-handler
- vgpu.sh / typegpu / threejs
- Cursor + Origin + Vercel deploy
- AI Gateway (personal onboarding offer)

### Tone

Thesis-plus-ship: one architectural essay, then charts and product links. Highest-signal web-futures post of the window.
