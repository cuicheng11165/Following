# swyx (@swyx)

| Field | Value |
|-------|-------|
| Profile | https://x.com/swyx |
| Bio | achieve ambition with intentionality, intensity, integrity & insanity. · @smol_ai @dxtipshq @cognition @aidotengineer @latentspacepod |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T20:09:26Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** rewrite with summarize-x-post
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- **SmolForge**：agentic GitHub clone、CI/CD（workers）、皮肤与 spritesheet 动画
- 新「GSuite」动机：对 Workspace 愚蠢默认设置的不满
- 基础设施课：control plane / data plane / management plane（Devin Outposts 语境）
- 开源与评测透明：@poolsideai 公开完整 eval dataset
- 内容与社群：Latent Space（Poolside 访谈）、AI Engineer、Codex/Work 10M 用户播客预告

### Opinions and takes

- 正在 dogfood agentic forge，内置 CI/CD；欢迎加入 swyx inc 影响路线图。
- Cursor 在 performance maxxing，他在 featuremaxxing——不同探索维度；原型希望交给合适的人。
- 做产品是为真实使用与创新，而非 API 兼容/克隆。
- 控制面与数据面可独立分离是工程 career 必听课；尽早学 management plane。
- Poolside 的开放度被低估：好小模型 + 论文 + 完整 eval 数据可自证是否 rewardhack。
- Work + GPT 5.6（配合 computer use）可能是自原版 ChatGPT 以来最「公司定义级」的发布，并预期超 10 亿用户量级叙事。

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **SmolForge：dogfood agentic GitHub clone**

**链接：** https://x.com/swyx/status/2080500752183960017  
**时间 / 互动：** 2026-07-24 · ❤️ 107 · 🔁 2 · 💬 44 · 👀 25k

##### 主帖在说什么

他透露过去约一个月在 dogfood 一个 agentic 的 GitHub 克隆，体验已相当愉快，甚至因 workers for platforms 自带 CI/CD。还差约 3 个未展示的 idea 才上线；若想一起黑就现在加入 swyx inc 影响路线图。

##### 要点

- Agentic forge + 内建 CI/CD
- 仍有 3 个功能再公开
- 招人/共创窗口打开
- 截图展示 UI/流程

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@diptanu** (Diptanu Choudhury) | 在做 desegregated Git backend：单仓多 branch 可达约 670 pushes/s；模拟 worker 下可扩展到百万级推送。想探索与 forge 集成。 | [post](https://x.com/diptanu/status/2080671930643013850) |
| **@MoLuch_AI** (Mo Luch) | 关心 agent 多 branch 并行时的 merge conflict——这是此类系统常崩的点。 | [post](https://x.com/MoLuch_AI/status/2080613892292587850) |

##### 一句话概括

SmolForge 把「agent 原生的 git + CI」做成可 dogfood 产品，并公开招共创者。

---

#### 2. **SmolForge 加皮肤与 spritesheet 动画**

**链接：** https://x.com/swyx/status/2080750437133901925  
**时间 / 互动：** 2026-07-24 · ❤️ 36 · 🔁 2 · 💬 16 · 👀 12k

##### 主帖在说什么

在 agentic forge 帖之后追加：好吧其实是 4 个新功能——SmolForge 现在有可定制皮肤与 spritesheet 动画。后续另帖称 spritesheet 问题已解：从 imagegen 一次性出整张 sheet，改为（结合 image + video 模型）分步生成；并更新 gist/站点。

##### 要点

- 角色皮肤 + 动画成为产品身份感
- 生成管线从 oneshot spritesheet 演进
- 与 forge 体验一体化

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@MVXMXM** (Maximillian Piras) | 视觉「sick」、设计向肯定。 | [post](https://x.com/MVXMXM/status/2080756245019996263) |

（其余多为表情/角色梗；spritesheet 技术讨论更多在后续 gist 帖。）

##### 一句话概括

在 agent forge 之上叠角色皮肤与动画，把「工具」做成有人格的产品体验。

---

#### 3. **为什么要做新 GSuite：愚蠢默认**

**链接：** https://x.com/swyx/status/2080705334587605122  
**时间 / 互动：** 2026-07-24 · ❤️ 48 · 🔁 2 · 💬 16 · 👀 12k

##### 主帖在说什么

他展示一张（Workspace 类）极差默认设置的截图，直言：正因为这种 stupid defaults，他才在做新的 gsuite。后续回复补充：产品要服务真实使用与创新，而非简单 API 兼容克隆。

##### 要点

- 创业动机 = 被默认设置激怒
- 目标是 JTBD 更好解，不是 feature parity 克隆
- 截图作证据

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@buildwbhoomika** | 最好的创业往往来自有人受够某个 stupid default。 | [post](https://x.com/buildwbhoomika/status/2080714989808373956) |
| **@tech_summaries** | Workspace 遗留 bloat 是所有人的时间税；企业默认在杀小团队。问他做邮件层还是文档协作层。 | [post](https://x.com/tech_summaries/status/2080728271067468246) |

##### 一句话概括

新协作套件的动机是反「企业默认税」，而非再做一个兼容层。

---

#### 4. **Poolside：公开完整 eval 的罕见开放**

**链接：** https://x.com/swyx/status/2080387171723137440  
**时间 / 互动：** 2026-07-23 · ❤️ 208 · 🔁 20 · 💬 20 · 👀 31k  
**引用：** Latent Space × Poolside 访谈

##### 主帖在说什么

他认为人们低估 @poolsideai 的开放度：不仅 ship 了在 coding 上能赢 @thinkymachines 的优秀 Small 模型、有被圈内夸的论文，更是少数真正公开完整 eval dataset 的团队——6 个公开 benchmark、各 4 runs、每 run 数百 turns，可自行验证是否 rewardhack。Brilliant。

##### 要点

- 开放 = 模型 + 论文 + **可审计 eval 数据**
- 对抗 rewardhack 质疑的正确姿势是公布细节
- 与 LS 访谈内容互补

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@MarcusSpillane** | 2026 年「公布 eval 让别人证你没作弊」居然成了业界最大胆之举。 | [post](https://x.com/MarcusSpillane/status/2080412988675096832) |
| **@ChainZenit** (Strata) | eval 透明是巨大一步。 | [post](https://x.com/ChainZenit/status/2080388074878488810) |

##### 一句话概括

在 frontier 竞赛里，完整公开 eval 轨迹比口号式 open 更稀缺、也更可信。

---

#### 5. **控制面 vs 数据面（Devin Outposts）**

**链接：** https://x.com/swyx/status/2079775327539339329  
**时间 / 互动：** 2026-07-22 · ❤️ 691 · 🔁 13 · 💬 46 · 🔖 646 · 👀 113k  
**引用：** @cognition Devin Outposts（任意机器跑 Devin）

##### 主帖在说什么

某天资深工程师会跟你讲「控制面与数据面必须可独立分离」——一定要听。然后再尽早学 management plane。他后续串起 devtools 101/201：把 MxN 反复变成 M+N 的 unbundling 是生态与企业关键；并笑称自己 2023 年就在讲 mesh/控制数据面。

##### 要点

- Outposts = 数据面可下沉到客户基础设施
- 控制/数据/管理三平面是 agent 平台必修课
- 与企业/空隔部署叙事一脉相承

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@swyx**（自续） | 上述是 unbundling 版 Devtools playbook；若那是 201，另有 101 课（MxN→M+N）。 | [post](https://x.com/swyx/status/2079935949103132677) |
| **@ccccjjjjeeee** (Christopher Ehrlich) | 问哪位 graybeard 的 YouTube 可入门。 | [post](https://x.com/ccccjjjjeeee/status/2079815734583288242) |

##### 一句话概括

Devin 可部署到任意机器，再次把「控制面/数据面分离」推到 AI agent 平台的中心。

---

### Products, launches, people

- **SmolForge** / swyx inc；spritesheet gist；Workers for Platforms
- **@poolsideai**、**@cognition** Devin Outposts、**@latentspacepod**
- **@aidotengineer** / AI Engineer NYC；Cormac 视频
- 播客预告：Codex + ChatGPT Work 10M 用户里程碑（@akshaynathan_）
- 人物：@eisokant、@eliebakouch、@stevenkplus1、@theo

### Tone

高产 builder-commentator：产品 ship 截图 + 基础设施长帖 + 短句梗；社区运营感强，常招人/串线，技术观点带「devtools 教科书」口吻。
