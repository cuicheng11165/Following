# Simon Willison (@simonw)

| Field | Value |
|-------|-------|
| Profile | https://x.com/simonw |
| Bio | Creator @datasetteproj, co-creator Django. PSF board |
| Source list | builders.md |
| Run ID | 2026-08-13T041940Z |
| Run dir | x/runs/2026-08-13T041940Z/ |

---

## Window: 2026-08-05 → 2026-08-13

- **Run ID:** 2026-08-13T041940Z
- **Fetched at:** 2026-08-13T04:19:40Z
- **Posts in window (fetched):** 20 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Muse Glimmer 30B: first Apache 2.0 Meta open-weight (vs Llama’s non-OSI license)
- Local vision LLMs (pelican-on-a-bicycle, laptop-only descriptions)
- Claude Haiku as current least-favorite: hallucinates; still used by Claude Code WebFetch
- Auto-mode: wants to believe it fixes prompt injection, not there yet
- Vibe-coded games look like games; being fun is still unsolved

### Opinions and takes

- Codex is too keen to publish HTML to a site when you wanted a local file
- Tell Claude Code “use curl, not WebFetch”
- Agents talking via filenames + base64 + `zz` prefixes is a neat covert channel
- OpenAI needed two Artifactory 0-days to break free — not just misconfig

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Muse Glimmer notes**

**链接：** https://x.com/simonw/status/2086972895256007160  
**时间 / 互动：** Tue 11 Aug · Likes 427 · Bookmarks 162

##### 主帖在说什么

Blog notes on Muse Glimmer 30B — Meta’s first Apache 2.0 open-weight (Llama licenses were “janky non-OSI”). Follow-up: vision on-laptop describing a pelican photo still under-appreciated.

##### 要点

- License is the headline, not just bench
- 30B agentic, 24GB VRAM claim
- Local vision is underrated

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@toolshed_labs** | Apache 2.0 on 30B is what matters; Llama licenses stuck teams in production. Has anyone pushed past 32k context? | [post](https://x.com/toolshed_labs/status/2087011009969988081) |

##### 一句话概括

Meta finally shipped an OSI-clean 30B — Simon cares about the license and the laptop vision.

#### 2. **Haiku is the worst cheap model right now**

**链接：** https://x.com/simonw/status/2086931955539742985  
**时间 / 互动：** Mon 10 Aug · Likes 1505 · Views ~115k

##### 主帖在说什么

Haiku hallucinates wildly and loses to similarly priced GPT-5.6-Luna. Worse: Claude Code WebFetch still uses it, so every URL fetch inherits hallucination risk.

##### 要点

- Cheap model quality inverted
- Tool-routing bug, not just chat quality

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@trq212** | Working on removing Haiku from WebFetch now that automode is default | [post](https://x.com/trq212/status/2086944777363448210) |
| **@JustinGorya** | Haiku 4.5 has ~4x lower hallucination than Luna (counters the claim) | [post](https://x.com/JustinGorya/status/2086946210057711890) |

##### 一句话概括

Simon’s complaint shipped a product fix: Thariq said Haiku is leaving WebFetch.

### Products, launches, people

- [Muse Glimmer notes](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/)
- [GGUF on Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF)
- [Auto-mode notes](https://simonwillison.net/2026/Aug/8/auto-mode/)
- [Moonlight Mayhem](https://simonwillison.net/2026/Aug/7/moonlight-mayhem/)
- Opus 5 system prompt mentions Fable export controls

### Tone

Lab-notebook public: licenses, hallucinations, filename covert channels.
