# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | Vercel CEO |
| Source list | builders.md |
| Run ID | 2026-09-06T143124Z |
| Run dir | x/runs/2026-09-06T143124Z/ |

---

## Window: 2026-08-29 → 2026-09-06

- **Run ID:** 2026-09-06T143124Z
- **Fetched at:** 2026-09-06T14:31:24Z
- **Posts in window (fetched):** 20 (cap 50: paginated, stopped ~20)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Intelligence revolution: AI workers are working the hardest they ever have
- WebMCP: agents should ride the existing WWW
- Astra #1 on Vercel DeepsecBench (49 min vs Sol ~4 hours)
- Open source winning because models train on it (Blender)
- Vercel build-machine / spend-control / deploy-speed product notes

### Opinions and takes

- “Anyone that works in AI is working the hardest they've ever worked”
- Agents *need* to ride existing WWW infrastructure; WebMCP makes it efficient
- fx + agent-browser = complete web dev stack with no debug-depth loss
- Open source ftw: models get better at Blender than proprietary 3D tools

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **The intelligence revolution**

**链接：** https://x.com/rauchg/status/2096375803714138437  
**时间 / 互动：** Sat 05 Sep · Likes 4.7k · Replies 253 · Views ~419k

##### 主帖在说什么

AI people are working the hardest they ever have. Ironic if AI was supposed to give time back. Reality: most fun, fascinating, empowering epoch. The intelligence revolution.

##### 要点

- Time-back narrative is fake; the bar moves
- Framed as fun, not burnout-only

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@davemagne** | Building has never felt more like a video game | [post](https://x.com/davemagne/status/2096376096384237686) |
| **@doodlestein** | Doesn’t feel like work because drudgery is gone; now thinking/creating | [post](https://x.com/doodlestein/status/2096431175078219968) |
| **@Little_K_Story** | Time-back was always fake; if the tool is this good you run harder | [post](https://x.com/Little_K_Story/status/2096381301674701146) |

##### 一句话概括

The Vercel take is: harder work, better game.

#### 2. **Bullish on WebMCP**

**链接：** https://x.com/rauchg/status/2096065378598441431  
**时间 / 互动：** Sat 05 Sep · Likes 1.5k · Replies 132 · Bookmarks 850 · Views ~135k

##### 主帖在说什么

Tesla FSD analogy: meet the world as it is. Agents must ride WWW. Unique win: Next.js dev pages expose debugging tools to the agent in the tab under test, with page context, no separate MCP server. fx + agent-browser is a complete stack.

##### 要点

- Page-native agent tools, not a sidecar MCP
- Debugging depth is the non-obvious win

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@0xidanlevin** | First WebMCP benchmark: 3–5x speed, up to 23x cheaper, 10–15% better vs computer-use/DOM | [post](https://x.com/0xidanlevin/status/2096081109989618033) |
| **@steren** | Easy to add to existing pages; asks to bake into Next.js on by default | [post](https://x.com/steren/status/2096069085624938517) |

##### 一句话概括

WebMCP is Rauch’s bet that the open web beats a parallel agent internet.

#### 3. **Astra on DeepsecBench**

**链接：** https://x.com/rauchg/status/2096285043094405491  
**时间 / 互动：** Sat 05 Sep · Likes 1.3k · Replies 77 · Views ~107k

##### 主帖在说什么

Astra is the best cybersecurity model on Vercel DeepsecBench: 49 minutes vs Sol ~4 hours, better score, nearly same cost; more effective and 50% cheaper than Claude Opus 5 max.

##### 要点

- https://vercel.com/ai-gateway/leaderboards/deepsecbench
- Time, not just accuracy

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@pilvar222** | Aikido Security: Astra rediscovered 29/32 CVEs at pass@3; three runs cost almost $4k | [post](https://x.com/pilvar222/status/2096313431829708898) |

##### 一句话概括

Astra wins cyber benches on latency; the footnote is the bill.

### Products, launches, people

- WebMCP
- Vercel DeepsecBench / AI Gateway
- Basic build machines changelog
- eve agents as AI-orchestrated SDLC
- Next.js deploy speed vs Cloud Run (QT これ)

### Tone

CEO-as-platform-theorist: one manifesto, one protocol bet, one leaderboard.
