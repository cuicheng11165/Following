# Peter Steinberger (@steipete)

| Field | Value |
|-------|-------|
| Profile | https://x.com/steipete |
| Bio | Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T19:28:25Z
- **Posts in window (fetched):** 50（cap 50: yes；高频发帖，抓取多为窗口后半段）
- **Mode:** 30-day backfill

### Themes

- OpenClaw 产品工程：并行 QA、subagents、release 准备、Linux app
- Codex / GPT-5.6 Sol 与 harness 实战（意图理解、compaction 边界）
- open weights / 生态竞争与 OpenAI 署名支持
- agent skills（autoreview 等）与成本优化（Terra 等高性价比路由）
- 对 hype→唱衰钟摆的反应：忽略噪音，继续做 dream harness
- 旅行与社区（Boston、luminary talk、Slack/Discord 用户反馈）

### Opinions and takes

- 竞争对生态有好处；大规模 serving 很难；为 OpenAI 签署 open weights 信函骄傲，并点名 Ant 沉默
- 分享实操 tip 而非当 eval framework；「我 review 的是 PR，不是 subagents」
- Terra underrated：部分工作流上 Terra high 可降成本约 80%
- 过去并行 QA 会在 compaction 边界崩或模型“作弊”，现在 Sol 意图理解与找复杂行为 bug 能力显著提升
- hype 后的 boo 阶段像摆锤过猛——选择忽略并继续做 harness
- 部分模型/工具链问题会绕过：直接走 claude CLI code path
- OpenClaw Mac 仍是 AppKit 壳、核心偏 web；Linux app 将随下版发布
- 邮箱已“破产”，别等他回邮件；Slack 用户会在不对时大声抱怨——他接受这种反馈回路

### Notable posts

1. 他全天用 Codex 做大规模并行 QA，为下一版 release 备战，并配图展示现场。判断是 Sol 对意图的理解“离谱地好”，还能揪出复杂行为问题；过去同类流程常在 compaction 边界崩溃，或模型开始作弊。这是 builder 第一手 harness 演进报告，而非榜单截图。

   链接：https://x.com/steipete/status/2081169373784633552

2. 公开了那条超长 QA prompt：用 12 个 subagents 拆功能、多端口 dev gateway 压测、自主 worktree/PR、目标找 200 bugs、修根因禁止创可贴、可 refactor 但不碰 plugin SDK 边界、桌面 markdown 测试报告持续更新。这是可复制的“agent 军团做 QA”操作手册，也解释了为何他强调 review PR 而非盯着每个 subagent。

   链接：https://x.com/steipete/status/2081169376317932017

3. 转发 OpenClaw 签署微软 open weights 相关信函，并提炼两点：竞争对生态好、规模化 serving 很难；Proud 于 OpenAI 也签了，同时点名 Ant 沉默。把产品立场、lab 政治与基础设施现实压进三条短句。

   链接：https://x.com/steipete/status/2081175795587072421

4. 在讨论用量/额度的语境下回了一句高传播吐槽：「You have limits for employees at Google?」把大厂内部配额与“无限 agent 野心”之间的荒谬感一针戳破，互动量远超多数产品帖。

   链接：https://x.com/steipete/status/2081196406854050071

5. 宣布 autoreview skill 新纪录：在一场难 refactor 上跑了 66 轮，并贴出 openclaw/agent-skills 仓库链接。信号是 agent skill 不只是 demo，而是能扛长时间、多轮、硬工程任务的生产工具。

   链接：https://x.com/steipete/status/2080899298838098034

6. 引用 Alex 的 “graph-max with Codex” 教程（画图→让 Codex 写成 code mode 脚本→跑输入），配图自嘲 “am I a graph engineer now”。表达的是：工作流可视化 + Sol/Codex 已把“图即程序”变成默认动作，角色边界在被工具抹平。

   链接：https://x.com/steipete/status/2080779917130858598

7. 对“狂 hype 之后的狂 boo”感到像摆锤过猛；选择 mostly ignore，把噪音期用来 build dream harness。这是他在舆论周期里的稳定策略：不跟风唱衰，也不被热度绑架。

   链接：https://x.com/steipete/status/2080431240520384760

8. 直言 Terra 被低估：连 @clawsweeper 相关工作流也跑在 Terra high 上，自己降本约 80%。在 frontier 模型军备竞赛中，他持续强调路由与性价比是 harness 的一部分，而不只是“永远上最贵模型”。

   链接：https://x.com/steipete/status/2081184939719213127

### Products, launches, people

- **OpenClaw**（Mac AppKit + web 内核、Linux app 将随下版发布、session summaries、VibeTunnel 历史功能）
- **autoreview skill**（openclaw/agent-skills）
- **Codex / GPT-5.6 Sol**、**Terra**、**Claude CLI**
- **@OpenAI**、**@openclaw**、**@clawsweeper**、**@alex_frantic**、**@theo**、**@mitsuhiko**
- 组织形态：501(c)(3) non-profit、小团队、Slack/Discord 社区

### Tone

高密度 builder 现场感：实用、直率、偶带德语吐槽与龙虾 meme；对模型与 harness 极具体，对 hype 循环保持防御性乐观。

---
