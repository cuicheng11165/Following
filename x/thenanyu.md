# Nan Yu (@thenanyu)

| Field | Value |
|-------|-------|
| Profile | https://x.com/thenanyu |
| Bio | head of product @linear |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:09:26Z
- **Posts in window (fetched):** 40 (cap 50: no)
- **Mode:** rewrite with summarize-x-post
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **Systems thinking** 定义战争：工程 + 行为经济学；或成继 “taste” 后的下一 meme
- Agent 时代的 **code review**：运行中的 review guide / agent memory，新模式升级给人
- **SoftwareFactory** 元梗：FactoryFactory、Java vibe code 缺位
- Linear 产品观：Projects 是重心而非 tickets；审慎自动回复
- 轻松文化帖：享受工作 vs 无意义内卷

### Opinions and takes

- Systems thinking（产品语境）= 工程 + 行为经济学：功能如何被用/滥用、用户是否理解、与其他功能/产品如何交互。
- 可推广到公卫、法律等「被设计并实施的意图」，但仍需 intention/design，本质是工程概念。
- 代码评审不会消失，而是变成：给 review agent 一份持续更新的架构意图目录（更像 agent memory）；新模式或指南变更时升级给人。
- 若能做 SoftwareFactory，就能做 SoftwareFactoryFactory。
- 「没人自愿 vibe code Java」= 我们还没有真正 SoftwareFactory 的原因之一。
- Linear 的重心是 Projects，不是 tickets。
- 丢客户若只因缺某功能，说明本就没抓住该客户。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Systems thinking 是什么？（征集定义）**

**链接：** https://x.com/thenanyu/status/2079996178687459693  
**时间 / 互动：** 2026-07-22 · ❤️ 86 · 🔁 4 · 💬 105 · 🔖 70 · 👀 32k

##### 主帖在说什么

抛出开放问题：当你听到或说出 “systems thinking” 时，脑子里的精确定义是什么？自评论预感：这会是继 “taste” 之后的下一个大 meme。三天后给出自己在产品语境下的答案（见下条）。

##### 要点

- 概念澄清优先于口号
- 预期 meme 化
- 用问题帖收集高信噪定义

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@clairevo** (claire vo) | 产品/业务 taxonomy（名词/动词）→ 用例工作流 → 体验连贯 → 何时扩展 taxonomy → 从产品 ladder 到收入与企业价值。 | [post](https://x.com/clairevo/status/2080020868592468039) |
| **@thenanyu**（自续） | 预感这是 taste 之后的下一 meme。 | [post](https://x.com/thenanyu/status/2079996354340782090) |

##### 一句话概括

用公开征集把含糊的 “systems thinking” 逼成可讨论的定义，并预感其 meme 化。

---

#### 2. **他的定义：工程 + 行为经济学**

**链接：** https://x.com/thenanyu/status/2081139836342145412  
**时间 / 互动：** 2026-07-25 · ❤️ 95 · 🔁 4 · 💬 9 · 👀 6.7k

##### 主帖在说什么

给出自己的答案：systems thinking 一半是工程，一半是行为经济学。建功能 X 时：可能如何被用、误用、滥用？用户能否理解目的、会嫌缺什么？如何与其他功能与产品交互？后续澄清：此处谈软件，但可推广到公卫/法律等「被设计的意图」；即使一般化，仍需要 intention/design，本质是工程概念。

##### 要点

- 三问：用/滥用、理解与缺口、系统交互
- 行为侧 + 结构侧
- 可跨域，但不丢「设计意图」

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@pdotcv** (Paul Macgregor) | 若谈软件设计 OK；更一般地是 zoom out、放进更广语境——可及品牌、政策、医学。 | [post](https://x.com/pdotcv/status/2081151940432482404) |
| **@thenanyu**（自续） | 软件可推广到公卫/法律；意图仍是被设计与实施的。 | [post](https://x.com/thenanyu/status/2081183178568405171) |

##### 一句话概括

Systems thinking = 预演功能的社会技术后果与系统交互，而不只是画架构图。

---

#### 3. **Code review → agent memory 式 review guide**

**链接：** https://x.com/thenanyu/status/2081121226265633159  
**时间 / 互动：** 2026-07-25 · ❤️ 83 · 🔁 4 · 💬 5 · 🔖 64 · 👀 55k  
**上下文：** 回复 @GergelyOrosz「Fable 后资深工程师不再审 AI 代码」

##### 主帖在说什么

当前正确平衡：给 code review agent 一份**运行中的 review guide**，编目代码架构的模式与意图。它更像 **agent memory** 而非静态人写文档；并指导：引入新模式或指南本身需改时，**升级给人类评审**。另回复：开箱主要抓硬 bug/逻辑错；风格偏好可另加；最好靠定期人工复盘逐步 bootstrap 编码指南。

##### 要点

- 人审不全丢，边界上收
- living guide / memory > 静态 checklist
- 新模式 = 人机交接触发器
- Linear guided review UX 被用户点名表扬

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@amir_mehrabi_** | 有用的 agent memory 是意图/模式/例外的活模型；知道何时交给人，才配信任。 | [post](https://x.com/amir_mehrabi_/status/2081126852433678485) |
| **@Jordi_Up** | 感谢 Linear guided reviews：4 个月 19k LOC 功能分支切 3 个 PR 飞过，微调后 merge。 | [post](https://x.com/Jordi_Up/status/2081231963206385730) |

##### 一句话概括

AI 时代 code review 应变成「可进化的架构记忆 + 新模式升级人」，而非全盘放弃。

---

#### 4. **SoftwareFactoryFactory**

**链接：** https://x.com/thenanyu/status/2081187979024797858  
**时间 / 互动：** 2026-07-26 · ❤️ 21 · 🔁 0 · 💬 7 · 👀 2.4k

##### 主帖在说什么

一句元层级玩笑/论断：如果你能做 SoftwareFactory，你就能做 SoftwareFactoryFactory——工厂的工厂，递归放大软件生产。

##### 要点

- 元生产 / 递归工业化叙事
- 与当周 Software Factory 讨论互文
- 短帖高概念密度

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@MattRoth** | 递归加码：FactoryFactoryFactory… | [post](https://x.com/MattRoth/status/2081189675361018040) |
| **@_buggles** | 先做「能做出你想做之物的东西」。 | [post](https://x.com/_buggles/status/2081262080137798072) |
| **@techwraith** | 物理世界类比：产品工厂的工厂？🤔 | [post](https://x.com/techwraith/status/2081191111801155916) |

##### 一句话概括

软件工厂叙事的下一跳是「造工厂的工厂」——元工具链递归。

---

#### 5. **Java vibe code 与真·SoftwareFactory 的缺失**

**链接：** https://x.com/thenanyu/status/2081195994499133820  
**时间 / 互动：** 2026-07-26 · ❤️ 19 · 🔁 0 · 💬 2 · 👀 4.4k  
**引用：** @jasoki「没见过有人自愿 vibe code Java」

##### 主帖在说什么

把该观察收成结论：**这就是我们还没有真正 SoftwareFactory 的真实原因**——当「自愿、愉快地用 AI 写」尚未覆盖企业主流语言/栈时，工厂化生产仍不完整。

##### 要点

- 文化/栈意愿是工厂化瓶颈
- 不止模型能力，还有语言生态与趣味
- 与 Factory 元讨论闭合

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@petewilz** (Peter Wilczynski) | 甩出 Spring 式地狱名：`AbstractBeanFactoryCreatingFactoryBean`——工厂套娃梗拉满。 | [post](https://x.com/petewilz/status/2081202290212426053) |

##### 一句话概括

没有人愿意 vibe code 的栈，就撑不起「真·软件工厂」——意愿与栈覆盖是隐藏约束。

---

### Products, launches, people

- **Linear**：Projects 重心、guided code review、集成边界（如 Google Chat 非官方）
- 讨论对象：@GergelyOrosz、@clairevo、@rauchg 系 Software Factory 话语
- 文化：@vboykis 论享受工作

### Tone

产品负责人式短帖：概念精确、略干幽默、少发长 thread；用问题帖与一句收束推动定义战。对 meme（taste → systems thinking）有自觉。
