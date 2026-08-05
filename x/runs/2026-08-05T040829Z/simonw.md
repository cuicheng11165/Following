# Simon Willison (@simonw)

| Field | Value |
|-------|-------|
| Profile | https://x.com/simonw |
| Bio | Creator @datasetteproj, co-creator Django… |
| Source list | builders.md |
| Run ID | 2026-08-05T040829Z |
| Run dir | x/runs/2026-08-05T040829Z/ |

---

## Window: 2026-07-06 → 2026-08-05

- **Run ID:** 2026-08-05T040829Z
- **Fetched at:** 2026-08-05T04:08:33Z
- **Posts in window (fetched):** 10 (cap 50: no)
- **Mode:** 30-day backfill
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Major LLM CLI/library release (reasoning traces, Responses API, server-side tools, logging)
- Local MiniMax-H3 video gen on M5 Mac (~115GB, ~45 min)
- Anticipation for laptop-sized Qwen 3.8 models
- OAuth wish: bill LLM features to users’ existing OpenAI accounts
- Media-value fact-checking rabbit holes

### Opinions and takes

- Don’t get excited before weights drop—but Qwen 3.8 laptop sizes are an exception to that restraint
- Local video gen is fun if you accept prompt-guide discipline
- Wants OAuth so apps meter against user OpenAI accounts

### Notable posts

#### 1. **Big LLM CLI release**

**链接：** https://x.com/simonw/status/2084792341572001871  
**时间 / 互动：** Wed 05 Aug · Likes 139 · Bookmarks 76

##### 主帖在说什么

Announces major release of his LLM CLI + Python library for hundreds of models: reasoning traces, OpenAI Responses support, server-side tools, smarter logging. Links full write-up.

##### 要点

- Multi-model interface as infrastructure
- Observability (traces/logs) first-class
- Practitioner tooling culture

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@kaanbuildsai** | Model landscape is an infrastructure problem; consistent interface > reinventing adapters | [post](https://x.com/kaanbuildsai/status/2084792631322714147) |
| **@dushyantk** | Full logs beat pass/fail—like render dispatch | [post](https://x.com/dushyantk/status/2084797459621093754) |

##### 一句话概括

Simon ships the Swiss Army knife for multi-LLM work and treats traces as non-optional.

#### 2. **MiniMax-H3 local video**

**链接：** https://x.com/simonw/status/2084719238569435469  

##### 主帖在说什么

Rainbow skunk leaps mossy log in supermarket—generated on M5 Pro, ~115GB download, ~45 minutes; notes on MLX port and prompt guide for audio.

##### 一句话概括

Local video gen is a weekend project if you have RAM and patience.

#### 3. **Qwen 3.8 laptop models**

**链接：** https://x.com/simonw/status/2084667167212245170  
**时间 / 互动：** Likes ~1.2k

##### 主帖在说什么

Usually avoids pre-release hype; very much looking forward to upcoming laptop-sized Qwen 3.8 models.

##### 一句话概括

Even the skeptic of pre-hype is hyped for capable local Qwen sizes.

### Products, launches, people

- llm CLI, MiniMax-H3 MLX, Qwen 3.8, Datasette ecosystem implicit

### Tone

Reproducible tinkerer: links, hardware specs, caveats, zero vapor.
