# Madhu Guru (@realmadhuguru)

| Field | Value |
|-------|-------|
| Profile | https://x.com/realmadhuguru |
| Bio | Sr Director, AI at Meta; Prev: Google - Led Gemini, Veo, Nano Banana. |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T22:00:00Z
- **Posts in window (fetched):** 47 (cap 50: no)
- **Mode:** rewrite / 30-day window (Notable posts 按 `summarize-x-post`)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- 开放权重模型（Kimi、GLM 等）对企业 AI 栈、路由与可选性的冲击
- 企业侧「真实工作流适配」：评测（evals）、后训练/RL、反馈闭环与人才缺口
- AI 产品落地分阶段：分发型公司扩张相邻能力（phase 1）vs 净新增创新（phase 2）
- 智能体安全与身份：无限 agent 与传统 IAM 的错位
- 个人认知与写作：第二大脑副作用、AI 文风识别
- 从 Google 到 Meta 的职业切换与「在非工程复杂系统里做 agent」

### Opinions and takes

- AI 对软件生态的「不可否认影响」还在 phase 1（分发方快速铺功能）；phase 2 才会出现大量净新特性。
- 美国 AI 圈对开源权重的共识是通过一系列公开「实验」迭代信念形成的（DeepSeek、MS–OpenAI、GLM/Kimi、Hugging Face 事件等），而非先验显然。
- 把通用模型做成领域专家，挑战在理解工作流、设计 evals、后训练与反馈环；该技能仍集中在少数实验室。
- 用中文训练的开源权重模型 ≠ 数据被中国获取；开源权重可本地下载、自托管。
- 开放权重会倒逼企业重构栈：eval 速度、自建路由、模型无关 harness。
- 「第二大脑」用多了主脑变钝：脑子里要留事实与半成品线索，才能实时联想。
- 企业难越过聊天机器人，核心是 harness + evals 人才稀缺，而非模型本身。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点（禁止一句带过）。

#### 1. **真实工作流适配是未来几年巨大机会**

**链接：** https://x.com/realmadhuguru/status/2080707454422413487  
**时间 / 互动：** 2026-07-24 · ❤️ 398 · 🔁 43 · 💬 21 · 🔖 356 · 👁 ~28k  
**语境：** 引用 Jensen Huang 首帖中 NVIDIA 联署「开放模型重要」的公开信。

##### 主帖在说什么

他指出：未来几年最大机会属于能把「混乱真实工作流」映射到基座模型上的人。这不只是调 prompt，而是理解工作如何完成、设计 evals、通过后训练改进模型，并建立持续反馈环，从而把通用模型变成领域专家。他认为这套技能今天仍高度集中在少数实验室。

##### 要点

- 机会在「messy real-world workflows → foundation models」的适配层
- 能力栈：工作理解 + evals + post-training + 反馈闭环
- 通用模型 → 领域专家依赖上述闭环，而非单次 prompt
- 人才供给仍集中在少数 lab，技能缺口即市场空间

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TasneemNabi** | 看多能「访谈真实瓶颈 + 理解模型边界」的 PM：先搞清人的真实问题，再判断模型哪里真能解。 | [post](https://x.com/TasneemNabi/status/2080709998317912150) |
| **@nassarhayat** | 朋友加入 OpenAI 做 evals/post-training，动机是「当下最有趣的工作」；认为该领域仍有大量 low-hanging fruit。 | [post](https://x.com/nassarhayat/status/2080727649832620143) |
| **@alankarjain91** | 在 Google 多年做同类工作后，现于 NextToken 为企业 AI 团队规模化交付 post-training。 | [post](https://x.com/alankarjain91/status/2080727845090074924) |

##### 一句话概括

开放模型热潮下，真正稀缺的是把真实工作流做成领域专家的人——evals/后训练/反馈环，而非模型本身。

---

#### 2. **开源权重共识如何通过公开实验形成**

**链接：** https://x.com/realmadhuguru/status/2081141594892415028  
**时间 / 互动：** 2026-07-25 · ❤️ 41 · 🔁 6 · 💬 4 · 🔖 14 · 👁 ~5.9k  
**语境：** 引用 Aaron Levie 称 Google 站队后 open weights 已是「全面背书」。

##### 主帖在说什么

他强调：在未知领域，难题答案只能来自反复接触现实。美国 AI 社区对开放权重的支持「现在看起来显然」，但一个月前并非如此——DeepSeek、微软–OpenAI 裂痕、GLM、Kimi、Fable、OpenAI–Hugging Face 等一连串公开「实验」让人共同观察一阶/二阶效应并更新信念。他认为未来十年许多社会层面的 AI 难题也会用同样方式逼近答案。

##### 要点

- 硬问题靠「反复接触现实」而非先验叙事
- 开放权重共识是信念更新，不是先验正确
- 一系列公开事件各自揭示激励、创新、地缘与牌面
- 同方法将用于未来十年更大的社会层 AI 议题

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@alankarjain91** | 同意让市场自己演化；同时做多 closed + open 前沿智能。 | [post](https://x.com/alankarjain91/status/2081204274097467853) |
| **@MichaelWaitze** | 转向速度来自真实成本压力：企业已在用开源权重做基础任务控成本——「不是即将发生，已经在发生」。 | [post](https://x.com/MichaelWaitze/status/2081176322848542923) |
| **@ajs6888** | 用中文概括：一轮轮事件砸下来，风向就变了。 | [post](https://x.com/ajs6888/status/2081166796703600771) |

##### 一句话概括

开放权重「显然正确」是事后叙事；真正驱动共识的是一连串公开实验与企业成本压力下的信念更新。

---

#### 3. **Kimi/GLM 倒逼企业栈：evals · 路由 · 无关 harness**

**链接：** https://x.com/realmadhuguru/status/2077885624607228018  
**时间 / 互动：** 2026-07-16 · ❤️ 147 · 🔁 21 · 💬 6 · 🔖 185 · 👁 ~19k  
**语境：** Kimi-K3 登顶 Frontend Arena（超 Fable 5）的讨论。

##### 主帖在说什么

他断言像 Kimi、GLM 这样的开放权重模型会彻底重塑企业 AI 栈。企业若要最大化模型可选性，应做三件事：① **Evals**——回归评测（始终可靠的表项）+  aspirational/hill-climbing 评测（当前价位最优模型仍吃力的难例，靠 scaffold 或等更好模型）；eval 速度本身是竞争力。② **Model routing**——在质量/成本/延迟间取舍，最好自建，因无人比你更懂业务；现成路由器他尚未看到值得推荐的。③ **Model-agnostic harness**——系统不应知道 API 背后是哪个模型：归一化提示结构、上下文、工具定义与输出解析，evals 通过后再换模型。

##### 要点

- 开放权重 → 企业必须最大化 optionality
- 双层 evals：回归保底 +  aspirational 爬坡；eval velocity 是 moat
- 路由应按业务自建；货架路由器尚不成熟
- Harness 模型无关：提示/上下文/工具/解析归一

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@omarsar0** | 强烈同意；能力差距在缩小，单押 top1 模型是错的——应用私有 evals 在 harness/workflow 上，并融合多模型。 | [post](https://x.com/omarsar0/status/2077888023316890104) |
| **@trydotworks** | 自荐 @rolemodeldev 为「最好的 model router」（产品向回复）。 | [post](https://x.com/trydotworks/status/2077927938268488123) |
| **@UsmanAnzaar** | 重申：针对自身用例的 private evals 是最佳前进方式。 | [post](https://x.com/UsmanAnzaar/status/2078105655987380529) |

##### 一句话概括

Kimi 级开放权重逼企业从「绑一家模型」转向 eval 速度 + 自建路由 + 模型无关 harness 的可选性栈。

---

#### 4. **无限 agent 与传统 IAM 的错位**

**链接：** https://x.com/realmadhuguru/status/2080315474093760714  
**时间 / 互动：** 2026-07-23 · ❤️ 27 · 🔁 1 · 💬 7 · 🔖 17 · 👁 ~3.6k  
**语境：** GPT Sol 安全事件后与上市公司安全负责人的交流。

##### 主帖在说什么

身份与权限体系本为「有限员工」设计，而现在一人可拉起数百 agent，agent 还能再生 agent。他抛出一串开放问题：agent 是否继承发起员工权限？生命周期按任务、工单还是按周？子 agent 是否同权？如何审计这一切？

##### 要点

- IAM 假设有限身份 vs agent 近乎无限增殖
- 一人 → 数百 agent → 子 agent 递归
- 权限继承、生命周期、审计均为未解设计题
- 由 Sol 类事件把问题从理论推到企业安全议程

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@felixchi** | 规则：「no orphan agents」——每个 agent 必须代表某位员工行动。 | [post](https://x.com/felixchi/status/2080453224603992241) |
| **@amuldotexe** | 假设：SOC 2 需在 agent 语境下改写。 | [post](https://x.com/amuldotexe/status/2080514869447815400) |
| **@ivan_makarov** | Agent 应是系统中有明确 I/O 的函数，而非「无限自由」；无限自由≈无限混沌。应用身份曾被发明过——要把 agent 设计好，别做成集束炸弹。 | [post](https://x.com/ivan_makarov/status/2080343763508150475) |

##### 一句话概括

Sol 事件后，企业安全的核心张力是：为人类员工设计的 IAM，如何覆盖可无限繁殖的 agent 身份与审计。

---

#### 5. **加入 Meta 做 AI 产品**

**链接：** https://x.com/realmadhuguru/status/2075243087325217038  
**时间 / 互动：** 2026-07-09 · ❤️ 515 · 🔁 17 · 💬 52 · 🔖 69 · 👁 ~78k  
**语境：** 引用自己 5 月离开 Google 的告别帖。

##### 主帖在说什么

个人更新：已加入 Meta 构建 AI 产品。他认为 SWE agent 已改变软件工程，但其他复杂系统里的 agent 仍早期，多数人尚未「感受到」agent 的全部力量；Meta 有条件把 agent 能力推到更多人真正可用的程度。口号式收尾：Time to build。

##### 要点

- 新东家：Meta AI 产品
- SWE agent 已质变；非工程复杂系统仍早期
- 目标：让更多人「感受到」agent 全能力
- 与此前 Google/Gemini 经历形成连续叙事

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@adarshsolanki** | 调侃式祝福：muse spark 1.1 会进你的 boot camp（前 Meta 同事语境）。 | [post](https://x.com/adarshsolanki/status/2075248475315249639) |
| **@himanshustwts** | 印地/英语混搭祝贺「Chhaa gaye Guru」。 | [post](https://x.com/himanshustwts/status/2075250329889931740) |
| **@WisemanCap** | 标准祝贺；线程整体以祝贺为主、少技术争论。 | [post](https://x.com/WisemanCap/status/2075312362337587590) |

（其余回复多为祝贺/低信号；高信号技术讨论有限。）

##### 一句话概括

离开 Google 后加入 Meta：赌注是把已验证于软件工程的 agent 能力，铺到更广的复杂系统与大众体验。

### Products, launches, people

- **Meta**（新东家）、前 **Google / Gemini** 背景
- **Kimi K3**、**GLM** 等开源权重；**NVIDIA / Jensen** 开源立场；**Aaron Levie**、**levelsio** 引用讨论
- **GPT Sol** 安全事件与 agent 沙箱；**NextToken** / Thinking Machines 相关评论
- Google Cloud Model Garden 托管 Kimi 等

### Tone

产品与战略型技术评论：长帖条理清晰、框架感强，常引用行业事件做信念更新；夹杂短句金句与讽刺段子，语气自信、偏一线 lab/企业 AI 视角。
