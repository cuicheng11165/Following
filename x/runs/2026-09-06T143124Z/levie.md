# Aaron Levie (@levie)

| Field | Value |
|-------|-------|
| Profile | https://x.com/levie |
| Bio | ceo @box - your business lives in content. unleash it with AI |
| Source list | builders.md |
| Run ID | 2026-09-06T143124Z |
| Run dir | x/runs/2026-09-06T143124Z/ |

---

## Window: 2026-08-29 → 2026-09-06

- **Run ID:** 2026-09-06T143124Z
- **Fetched at:** 2026-09-06T14:31:24Z
- **Posts in window (fetched):** 10 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Box enterprise evals: Fable 5.1 then GPT-6 Astra
- Process redesign vs “faster shit”
- AI-for-cyber going vertical
- Open weights + vertical models (Thomson Reuters, Muse Spark, HF/NVIDIA)

### Opinions and takes

- No easy button: reengineer the process or you just accelerate the old 14-step workflow
- All roads lead to FDEs
- Cyber: triaging/fixing with more AI + humans is the only way; good time to be in security
- Data-rich companies can now train their own models instead of only licensing data

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Astra on Box’s hardest enterprise eval**

**链接：** https://x.com/levie/status/2095598710311067716  
**时间 / 互动：** Thu 03 Sep · Likes 1.1k · Replies 101 · Views ~263k

##### 主帖在说什么

GPT-6 Astra is the best model Box has tested on an expanded hard set: 77% vs 74% GPT-5.6 Sol overall, with huge task-type jumps (media +52, tech +28, legal +24, healthcare +23, energy +15). The interesting part is catching proxy metrics, citing policy language, grading radiology severity, and not calling a measurement glitch a missing record. Coming to Box AI Studio.

##### 要点

- Overall delta is small; per-industry deltas are the story
- Legal: verdict without citation is a critical error
- Coming as an agent option in Box AI Studio

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Avery_Coree** | 74→77 needed five bar charts to sell it | [post](https://x.com/Avery_Coree/status/2095599002813108345) |
| **@jasonlk** | Wants real-world speed + net cost per action/workflow, not just accuracy | [post](https://x.com/jasonlk/status/2095666955055399367) |

##### 一句话概括

Box is selling Astra as “the model that cites the clause,” not a 3-point overall bump.

#### 2. **Apply AI to a 14-step process and you get faster shit**

**链接：** https://x.com/levie/status/2096279756925026733  
**时间 / 互动：** Sat 05 Sep · Likes 774 · Replies 76 · Bookmarks 1.6k · Views ~206k

##### 主帖在说什么

Quote-tweeting Vas on enterprise process redesign. No easy button. Important workflows span functions; nobody is empowered to walk into finance and cut 14 steps to 5. So people “apply AI” to the current process. Opportunity for applied-AI companies and implementation teams. All roads lead to FDEs.

##### 要点

- Diffusion bottleneck is org design, not model IQ
- FDE as the delivery vehicle

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ponnappa** | AI transformation is a people problem | [post](https://x.com/ponnappa/status/2096448745307341191) |
| **@dimavollo** | Getting companies to admit 9 steps were redundant is the hard part | [post](https://x.com/dimavollo/status/2096279984432181609) |

##### 一句话概括

Enterprise AI fails when you automate the org chart instead of rewriting it.

### Products, launches, people

- GPT-6 Astra and Fable 5.1 in Box Agent / AI Studio
- NVIDIA acquiring Hugging Face (QT Jensen)
- Meta Muse Spark 1.3
- Thomson Reuters “Thomson” vertical LLM

### Tone

Enterprise-operator: long numbered evals, then a sharp one-liner about FDEs.
