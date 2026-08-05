# Jim Fan (@DrJimFan)

| Field | Value |
|-------|-------|
| Profile | https://x.com/DrJimFan |
| Bio | NVIDIA Director of Robotics… GEAR lab… |
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

- RoboTTT: 8K-timestep robot context via test-time training, constant inference cost
- One-shot imitate human video; mid-episode error recovery; context scaling curve
- Jensen’s open-models letter praise (“GOAT”, “Stay hungry…”)
- Real2sim2real / env scaling for physical RL

### Opinions and takes

- Robot policies must leave few-frame amnesia; context scaling belongs to robotics like LLMs
- TTT core compresses history into fixed-size weights—learning continues post-deploy
- Open models matter (endorses Jensen letter)
- RL is about environments; real2sim2real scales them

### Notable posts

#### 1. **RoboTTT launch**

**链接：** https://x.com/DrJimFan/status/2077414142340988962  
**时间 / 互动：** Wed 15 Jul 2026 · Likes ~1.3k · Bookmarks 765 · Views ~300k

##### 主帖在说什么

NVIDIA GEAR scaled robot model to 8,000 timesteps (~5 min muscle memory) with constant inference cost—orders of magnitude beyond SOTA. RoboTTT: tiny model inside model does a gradient step per sensor reading; fixed-size hidden state; indefinite post-deploy learning. Enables video-as-prompt one-shot imitation, on-the-fly self-improvement/error recovery. Context scaling curve: 8K beats 1K by 62%, no saturation. Blog/paper + Yunfan deep dive.

##### 要点

- Context scaling imported from LLM world to closed-loop robotics
- Constant compute despite long history is the hard trick
- Failure-to-correction as first-class skill

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@IamPranavJ** | Don’t only fixate on 8k steps—flat compute is the real surprise | [post](https://x.com/IamPranavJ/status/2077447036312703168) |
| **@DrJimFan** | Paper: research.nvidia.com/labs/gear/robottt/ | [post](https://x.com/DrJimFan/status/2077414143901188195) |

##### 一句话概括

RoboTTT is “long context for muscles”—test-time training gives robots minutes of memory without blowing inference cost.

#### 2. **Morning robot assembly ritual**

**链接：** https://x.com/DrJimFan/status/2078150032575082616  

##### 主帖在说什么

Coffee then watch robot assemble—uncut, no speedup, end-to-end policy; meditative quality of careful physical work.

##### 一句话概括

Physical AGI progress as daily aesthetic practice, not only benchmarks.

#### 3. **Jensen open models letter**

**链接：** https://x.com/DrJimFan/status/2080798306566045756  

##### 主帖在说什么

On Jensen’s first post / NVIDIA open-models letter: “Stay hungry, stay foolish. Absolute legend.”

##### 一句话概括

Full-throated support for open + closed frontier coexistence narrative.

### Products, launches, people

- RoboTTT / GEAR Lab, Yunfan Jiang, Jensen Huang, Marble/SceniX shoutouts

### Tone

Research storyteller: long technical posts + human awe for robots and legends.
