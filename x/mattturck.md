# Matt Turck (@mattturck)

| Field | Value |
|-------|-------|
| Profile | https://x.com/mattturck |
| Bio | VC at @FirstMarkCap. Host: MAD Podcast; Organizer: Data Driven NYC, Author: MAD Landscape. |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:15:00Z
- **Posts in window (fetched):** 50（cap 50: **yes**，窗口内实际更多）
- **Mode:** 30-day backfill (full rewrite; Notable = summarize-x-post)
- **Cursor:** per-builder（本 handle 独立窗口；非全局 job cursor）
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **Cerebras / 快速推理长访谈**：从 wafer 讲到芯片业围绕 inference speed 重组
- **Model routing 一周**：OpenRouter 传闻、Cursor/Runway Router、各云/数据平台的「router」同名异物
- VC 文化吐槽：bootstrapped 盈利 vs 烧算力 neo-lab；Anthropic SPV 诱惑；recursive auto-research 的讽刺

### Opinions and takes

- 推理速度与 tokens/sec/user 成为新瓶颈叙事（对标宽带/Netflix 类比）
- Routing 层正在成为横跨工具、创意与 infra 的默认组件
- 顶级研究者在「递归自动研究」中研究掉自己的工作——被低估的反讽
- 用 meme 与短视频消化 VC 圈荒诞

### Notable posts

> 以下每条均按 skill **`summarize-x-post`**：`x_thread_fetch` 主帖 + 高信号回复。

#### 1. **Cerebras 长谈：芯片业为推理速度重组**

**链接：** https://x.com/mattturck/status/2080333707483725876  
**时间 / 互动（如有）：** Thu, 23 Jul 2026 · Likes≈39, Bookmarks≈39, Views≈1.2万 · ~73min 视频

##### 主帖在说什么

发布与 Cerebras CEO **Andrew Feldman** 的 MAD 对话：从「什么是 wafer」铺到整个芯片业为何围绕 **inference speed** 重组。目录覆盖 tokens/sec/user、ASIC vs GPU/TPU/Trainium、Nvidia/Groq 快推理战、主权 AI 与电力、HBM/CoWoS/3nm 瓶颈、agent 带来的 CPU 需求、SRAM vs HBM、wafer-scale、prefill/decode、「100 部高清电影」式上下文问题、推理如何改变 RL、OpenAI 750MW 交易、CUDA 护城河、以及「今天的模型将是你用过最差的」等。

##### 要点

- 结构：入门物理 → 产业地图 → Cerebras 深技术故事 → 商业模式
- 核心命题：速度成为 AI 瓶颈；解码/内存路径重塑架构选择
- 分发：YouTube / Spotify / Apple 全平台

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@mattturck**（自回） | 附跨平台收听链接，定位为「reference conversation」。 | [post](https://x.com/mattturck/status/2080333711640285549) |
| **@AGTPinsights** | 追问何种新设计让企业「用 AI 而不把数据交给云」——主权/本地部署视角。 | [post](https://x.com/AGTPinsights/status/2080365334473683041) |

##### 一句话概括

一档把 wafer-scale 与推理瓶颈做成系统课的参考访谈，配套全平台分发。

#### 2. **Model routing 大周**

**链接：** https://x.com/mattturck/status/2080645582209663049  
**时间 / 互动（如有）：** Fri, 24 Jul 2026 · Likes≈42, Bookmarks≈30, Views≈1.7万

##### 主帖在说什么

盘点「routing 大周」：Stripe 传闻 **100 亿美元收购 OpenRouter**；**Cursor Router** 周三发布；**Runway Router** 昨天发布；并点名 Databricks、Vercel、Cloudflare、Dataiku、AWS、Google 都有「router」——括号强调 **同词异物**。

##### 要点

- 资本事件（传闻）+ 产品发布同周共振
- 命名泛滥：router 不等于同一产品类别
- 暗示：多模型编排成为默认中间层

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sonicaghi** | 指向 Kong 更早的开源 AI gateway——「谁才是 OG」的品类溯源。 | [post](https://x.com/sonicaghi/status/2081010000147652803) |
| **@kurt** | 以反讽帖接龙「居然找不到 router」——市场噪音 vs 真实需求。 | [post](https://x.com/kurt/status/2080661117760680256) |
| **@mmurph** | 「对某些人是大周，对 OG OpenRouter 是日常」——先发者心态。 | [post](https://x.com/mmurph/status/2081017870373499250) |

##### 一句话概括

一周内收购传闻 + 多产品同名 Router，Matt 提醒：词同、栈不同。

#### 3. **递归自动研究：研究者研究掉自己的工作**

**链接：** https://x.com/mattturck/status/2080738638065729741  
**时间 / 互动（如有）：** Fri, 24 Jul 2026 · Likes≈23, Replies≈12

##### 主帖在说什么

一句观察：被低估的反讽——世界顶级 AI 研究者在建造 **recursive auto-research** 时，正研究着让自己岗位消失的路径。

##### 要点

- 主题：自动化科研 / RSI 对研究者劳动的含义
- 语气：冷静指出 irony，非煽情末日论

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@jeremyjordan** | 若把职业看成无限问题集，自动化当前工作是满足感而非讽刺；只有「不会再有重要问题」才讽刺——成长心态 + 无限游戏。 | [post](https://x.com/jeremyjordan/status/2080774167230636168) |
| **@DoggyCapital** | 股权会在不再被需要时提供安慰——资本缓冲视角。 | [post](https://x.com/DoggyCapital/status/2080739463416717634) |
| **@jon3k** | 从不「保护岗位」；要做酷东西、去能创造价值的地方。 | [post](https://x.com/jon3k/status/2080795389091869045) |

##### 一句话概括

一句 irony 触发「无限游戏 vs 岗位保护 vs 股权缓冲」的职业哲学讨论。

#### 4. **Chip landscape 101 短片**

**链接：** https://x.com/mattturck/status/2081131761686184333  
**时间 / 互动（如有）：** Sat, 25 Jul 2026 · Likes≈17, Views≈4.3k

##### 主帖在说什么

从 Cerebras 长谈中剪出 **Chip landscape 101** 短视频：CPU、GPU、NVIDIA、AMD、TPU、Trainium、Cerebras 等地图式导览，降低长访谈门槛。

##### 要点

- 内容策略：长内容 → 短切入口
- 受众：需要地图而非全文的从业者/投资者

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@subramanya** | 追问何种 workload 会让答案从 GPU 翻转到 **wafer-scale first**——架构选型阈值。 | [post](https://x.com/subramanya/status/2081136440466165875) |

##### 一句话概括

用 101 短片导流长访谈；评论直接问 workload 切换条件。

#### 5. **VC 看到盈利 bootstrapped：迷之表情**

**链接：** https://x.com/mattturck/status/2080451010439352711  
**时间 / 互动（如有）：** Fri, 24 Jul 2026 · Likes≈38 · 短视频 meme

##### 主帖在说什么

Meme 视频标题：**当创始人为盈利的 bootstrapped 生意融资，而不是烧几亿美元算力做 neo-lab 时，VC 的反应**——自嘲圈内激励偏向烧钱训练故事。

##### 要点

- 讽刺：盈利被当成异类，算力烧钱才是默认叙事
- 身份：FirstMark VC 自嘲，增强可信

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@zeeg** | 「那些（盈利 bootstrapped）还存在吗？」——夸张确认荒诞。 | [post](https://x.com/zeeg/status/2080451159094165749) |
| **@MarcusSpillane** | 「没有什么比留存收益更能吓到 Series B deck review」——会计健康 vs 增长故事。 | [post](https://x.com/MarcusSpillane/status/2080484855477916039) |

##### 一句话概括

VC 自嘲：圈内更懂「烧算力叙事」而不是「盈利无聊」。

### Products, launches, people

- **MAD Podcast** × Cerebras / Andrew Feldman
- Model routing：OpenRouter、Cursor Router、Runway Router 及云厂同名品
- FirstMark / Data Driven NYC / MAD Landscape 身份背景

### Tone

VC-播客主：长内容 + 产业地图 + meme；短回复多，高信号集中在播客与周观察帖。

---
