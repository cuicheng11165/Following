# Andrej Karpathy (@karpathy)

| Field | Value |
|-------|-------|
| Profile | https://x.com/karpathy |
| Bio | I like training large deep neural nets. |
| Source list | builders.md |
| Run ID | 2026-08-03T024802Z |
| Run dir | x/runs/2026-08-03T024802Z/ |

---

## Window: 2026-08-01 → 2026-08-03

- **Run ID:** 2026-08-03T024802Z
- **Fetched at:** 2026-08-03T02:48:02Z
- **Posts in window (fetched):** 8 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **LLM long-horizon creative coding:** Opus 5 + ~1M token budget / ~$10 / ~2 hours → 5500 lines of procedural LoTR Three.js animation.
- **Beyond “pelican on a bicycle”:** richer evals of generative capability (worlds, games, storyboarding).
- **Ephemeral custom worlds / “GTA of X on demand”:** hyper-custom interactive experiences that no human would hand-author.
- **Multimodal / gameplay audit gap:** models still weak at natively perceiving video or playing in the worlds they generate.
- **Pipeline taste:** procedural code for structure/control; video-to-video for texturing/looks; ElevenLabs for audio.

### Opinions and takes

- LLMs’ stamina turns “no one would ever do this” into “sure, why not, it’s ~free.”
- World/game domains expose a concrete capability hole: slow screenshot-based self-audit → jank.
- N-gram tables / decision trees as a fun research question for best val loss under a tiny (e.g. 25KB) user-space budget.
- Agrees procedural storyboarding + v2v looksmaxxing is a compelling split.

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Opus 5 renders LoTR as procedural Three.js movie**

**链接：** https://x.com/karpathy/status/2083749667410727319  
**时间 / 互动：** 2026-08-02 · ~23.8k likes · ~1.8k reposts · ~2.97M views

##### 主帖在说什么

Karpathy argues we’ve outgrown simple LLM demos like “SVG of a pelican on a bicycle.” He gave Opus 5 the first paragraph of *Lord of the Rings*, a ~1M token budget (~$10), and asked for a Three.js render. After ~2 hours the model wrote ~5500 lines that procedurally placed polygons, orchestrated animation, and produced a janky-but-real story render. He frames this as the new economics of custom software: humans wouldn’t bother; models have infinite patience. He also flags a hard limit—models can’t efficiently perceive video or play the games they generate, so self-audit is painful and error-prone. Excited about ephemeral custom worlds (spectator NPC / character in LoTR-like experiences—“GTA of X on demand”).

##### 要点

- New capability frontier: long-running autonomous code generation for custom 3D worlds
- Cost/stamina flip: bespoke interactive media becomes near-free
- Weakness: multimodal/gameplay loop for self-correction still lagging
- Follow-ups: published playable source at karpathy.ai/lotr-movie/; ElevenLabs for audio

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@elonmusk** | Short affirmation (“Yah”) on the demo’s significance | [post](https://x.com/elonmusk/status/2083761408932458568) |
| **@karpathy** (self) | Points to Simon Willison’s pelican-on-bicycle writeup; ships forkable browser version; jokes about “GTA Hobbiton before GTA VI” | [post](https://x.com/karpathy/status/2083948654377996480) |

##### 一句话概括

Long-horizon coding models can already author one-off interactive worlds cheaply—but can’t yet properly see or play what they make.

#### 2. **Playable LoTR source + pelican benchmark context**

**链接：** https://x.com/karpathy/status/2083948654377996480  
**时间 / 互动：** 2026-08-02 · ~338 likes · ~85k views

##### 主帖在说什么

Follow-up pointing to Simon Willison’s “pelican on a bicycle” history, plus hosting the LoTR render source so it’s browser-playable and forkable.

##### 要点

- Ties the viral demo back to an evolving public eval culture
- Makes the artifact reproducible, not just a screenshot/video flex

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| — | Thread mostly engagement around the demo site | — |

##### 一句话概括

He closed the loop from viral clip → public, forkable artifact.

### Products, launches, people

- **Opus 5** (Anthropic) as the long-running coding agent in the demo
- **karpathy.ai/lotr-movie/** — playable Three.js LoTR procedural render
- **ElevenLabs** for voice/audio
- **Simon Willison** — pelican-on-bicycle LLM test writeup
- Mentions video-to-video models for looks; procedural code for control

### Tone

Excited, slightly awe-struck builder energy—sharing a mind-bending demo while being precise about remaining capability gaps (perception/gameplay). Playful (“GTA Hobbiton”) and research-curious (tiny-program val-loss n-grams).
