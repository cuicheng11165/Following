# Jim Fan (@DrJimFan)

| Field | Value |
|-------|-------|
| Profile | https://x.com/DrJimFan |
| Bio | NVIDIA Director of Robotics & Distinguished Scientist. Co-Lead of GEAR lab. Solving Physical AGI, one motor at a time. Stanford Ph.D. OpenAI's 1st intern. |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 8 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Touch as the under-explored robotics modality (T-Rex open-source)
- Dual-clock mixture-of-transformers: slow vision, fast tactile
- GEN-1.5 hype: in-context improvement from *not* sanitizing recovery/symmetry in human data
- Teleop is dying; UMI (human wearing the gripper) keeps physical intuition
- Physical AGI timelines: no later than 2040, likely 2035

### Opinions and takes

- Pixels run out of steam at the moment of contact; the next scaling curve is hours of touch
- Keep the fumble in the dataset or the robot will not learn recovery
- Demos for in-context robot learning are still too simple to call it ICL

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **T-Rex: tactile as a first-class citizen**

**链接：** https://x.com/DrJimFan/status/2090832821036470626  
**时间 / 互动：** Fri 21 Aug · Likes 677 · Views ~108k

##### 主帖在说什么

Robots today are doing sleight of hand in oven mitts: snap-fit magnets, peeling a paper cup, seating a USB are invisible to cameras. T-Rex (NVIDIA × Berkeley) is a full-stack methodology: (1) mixture-of-transformer with two async clocks — slow visuomotor planner, fast tactile expert at 4 touch ticks per vision tick; (2) open 50-hour / ~5,500-episode tactile play dataset on a 22-DoF SOTA hand (HuggingFace); (3) EgoScale recipe — human egocentric video pretrain, tactile robot play mid-train. “The next scaling curve will be measured in hours of touch.”

##### 要点

- Architecture change because force dynamics are faster than frames
- Largest tactile dataset they know of, fully open
- Bridges contact-free pretraining to contact-rich manipulation

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@DrJimFan** | Led by @Dantong_Niu, co-advised by @trevordarrell; site + HF dataset | [post](https://x.com/DrJimFan/status/2090832822525403481) |
| **@Grady_Booch** | Human fingertip ~3,000 neurons/cm with Meissner/Merkel/Pacinian stack; evolution’s tactile vocabulary still far beyond engineered sensors | [post](https://x.com/Grady_Booch/status/2090899815723053492) |

##### 一句话概括

Vision got us to the object; touch has to finish the last millimeter.

#### 2. **GEN-1.5: keep the fumble, kill teleop**

**链接：** https://x.com/DrJimFan/status/2090465981240086992  
**时间 / 互动：** Thu 20 Aug · Likes 1.1k · Views ~70k

##### 主帖在说什么

Respect to Pete & Andy on GEN-1.5. Secret is repetitive structure in human data: (1) symmetric tasks (IKEA bolts) where the second instance is a free in-context prompt; (2) recovery — don’t trim the drop, keep fumble→catch. UMI (human wearing the gripper) beats teleop because teleop bleeds out physical intuition. Many behaviors can be zero-shot once you have enough similar scenes. Current demos still a bit too simple to conclude ICL. Cautiously optimistic.

##### 要点

- In-context improvement from *not* over-sanitizing data
- Teleop is a lossy codec for human motor skill
- Zero-shot pickup is distributional, not magic

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bluequbit** | Asks if Jim is still on his published timeline | [post](https://x.com/bluequbit/status/2090480870440497275) |
| **@WeihaoTan64** | Longer-horizon tasks rarely have two consecutive trajectories from the same start | [post](https://x.com/WeihaoTan64/status/2090535669936660785) |
| **@DrJimFan** | Timeline reply elsewhere: no later than 2040, likely 2035 | [post](https://x.com/DrJimFan/status/2090489100419858576) |

##### 一句话概括

Robot ICL is a data-hygiene story: leave in the repeats and the mistakes.

### Products, launches, people

- T-Rex (NVIDIA GEAR × Berkeley): https://tactile-reactive-dexterous.github.io/
- HuggingFace dataset `zekaiwang/trex_dataset`
- GEN-1.5 / UMI
- Dantong Niu, Trevor Darrell, Pete & Andy

### Tone

Research-explainer. Metaphors (oven mitts, IKEA, USB) then architecture. Cautious on hype, aggressive on open data.
