# Nan Yu (@thenanyu)

| Field | Value |
|-------|-------|
| Profile | https://x.com/thenanyu |
| Bio | head of product @linear |
| Source list | builders.md |
| Run ID | 2026-08-01T131655Z |
| Run dir | x/runs/2026-08-01T131655Z/ |

---

## Window: 2026-07-29 → 2026-08-01

- **Run ID:** 2026-08-01T131655Z
- **Fetched at:** 2026-08-01T13:16:55Z
- **Posts in window (fetched):** 10 (cap 50: yes)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` floor `2026-07-29T03:32:35Z`)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **Agentic software factory loop at Linear:** Issue → Agent → PR → Release; ~30% of bugs fully automatic
- Agent hygiene: root-cause research, Datadog/Sentry MCPs, high-certainty gate before fixing, comment-back for more evidence
- Product craft: “Just Do Normal Things” (quoting design discourse)
- Light office / culture chatter

### Opinions and takes

- Linear’s most common automation loop matches Rauch’s agentic-factory thesis
- Agents need the same good practices as people—research first, don’t burn tokens on low-certainty fixes
- When blocked, agents should leave issue comments with full context and resume when unblocked
- Design permission structure: normal patterns over snowflake UI

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Linear’s Issue → Agent → PR → Release loop (~30%)**

**链接：** https://x.com/thenanyu/status/2083230295206121807  
**时间 / 互动：** Fri 31 Jul 2026 · ~111 likes · 8 replies · ~16k views · 107 bookmarks

##### 主帖在说什么

Quotes Guillermo Rauch on agentic software factories. Nan says Linear’s most common loop is some variant of Issue → Agent → PR → Release, with ~30% of bugs making it fully through. Nuances: instruct agents to deep-research root cause via Datadog/Sentry MCPs; only fix with high certainty; otherwise leave comments requesting repros. Agents need good practices “just like people.”

##### 要点

- Real production hit-rate (~30%), not a demo claim
- Observability MCPs as agent research tools
- Human-in-the-loop via issue comments when evidence is thin

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@RabnoorSingh10** (quoted in Nan’s follow-up) | Asks what happens when the fix needs a *decision* not a change—how much of the other 70% is ambiguity of “correct”? | [post](https://x.com/RabnoorSingh10/status/2083330431190213108) |
| **@thenanyu** (self) | Loop leaves a comment + full context; when you answer, the agent continues | [post](https://x.com/thenanyu/status/2083534333428580501) |
| **@__lepton__** | Prefers RCA *before* Issue so implementer agent only implements; asks if research+implement together works | [post](https://x.com/__lepton__/status/2083541186074026069) |

##### 一句话概括

Linear is running agent factories in production—with a 30% end-to-end rate and explicit rules against reckless token burns.

#### 2. **Permission to Just Do Normal Things**

**链接：** https://x.com/thenanyu/status/2083340761488126101  
**时间 / 互动：** Fri 31 Jul 2026 · ~34 likes · ~5k views

##### 主帖在说什么

Quotes joshpuckett that 90% of software should look/work the same. Nan: “You have permission from Josh to Just Do Normal Things.”

##### 要点

- Anti-snowflake product design stance
- Taste as constraint, not maximal novelty

##### 回复中的有价值观点

（thread 信号偏低；主帖本身是 pithy endorsement）

##### 一句话概括

Linear’s HoP blesses boring, shared patterns over UI uniqueness cosplay.

### Products, launches, people

- Linear agent loops; Datadog & Sentry MCP integrations
- Dialogue with @rauchg on agentic factories
- Design discourse with @joshpuckett

### Tone

Calm, operator-dense product leadership: concrete percentages, MCP names, and process rules over hype.
