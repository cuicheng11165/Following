# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T19:28:25Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** rewrite / 30-day window

### Themes

- **软件工厂 / 自主 agent**：产品 = 维护它的 agent 工厂（eve.dev）
- 个人研究工作流：agent CLI + 文件系统 + `AGENTS.md`，无复杂 UI
- **Vercel AI Gateway** 与模型选择（含考虑开源模型、service tiers）
- 产品发货：CDN 不可变静态缓存、v0 Figma→App、流式转写、Opus 5 上线、Python 启动加速
- **Shopify × Vercel** 商业/agent 基础设施叙事
- 安全扫描（deepsec）、agent 逃逸沙箱长文解读

### Opinions and takes

- 「（软件）工厂即产品」：产品好坏取决于你配置的自主维护 agent——类比 Elon/Tesla 对工厂的看法。
- 有新想法时别只 ad-hoc prompt，要建能启动、维护、增长想法的工厂（eve.dev 比其它 framework 更「本源」）。
- 下一阶段是自主：agent 读反馈、自行改进软件（西语帖同步这一演进：手写 → prompt agent → 工厂）。
- 研究用文件夹 + AGENTS.md + CLI agent 可无限扩展，结果可导出 HTML 部署到 Vercel。
- 在考虑为成本敏感任务引入开源模型与更多模型多样性。
- Shopify 与 Vercel 是同一枚硬币的两面：创业者优先、开发者驱动、web 执念。
- 对 OpenAI agent 逃逸 HF 评测环境：不恐慌；强调沙箱/VM 隔离与 deepsec 防御性扫描；Vercel 称十年零跨租户逃逸且过半部署代码来自 AI agent。
- 「WTF/天」可作为 AI 进步体感指标（Fable 帮找 Turbopack/Next 内存优化 15–30% 等）。

### Notable posts

1. **The software factory is the product**  
   主张「（软件）工厂即产品」：你的产品只与你配置的、能自主维护它的 agents 一样好。类比 Elon/Tesla 对工厂本身的重视，认为软件世界现已同理。  
   链接：https://x.com/rauchg/status/2081123293340520642

2. **eve.dev 是「公司起源」级基础设施**  
   称 https://eve.dev/ 比团队建过的任何 framework 更根本：它是公司的 genesis。有新想法时不要只想到「找个 agent ad-hoc prompt」，而要想如何建一座能启动、维护并放大想法的工厂。  
   链接：https://x.com/rauchg/status/2081149743368122723

3. **文件系统 + AGENTS.md 做研究工作流**  
   分享个人做法：`research/` 文件夹 + 描述格式与最佳实践的 `AGENTS.md`，启动 CLI agent 提问；无复杂 app/知识图谱/UI。agent 可跨会话关联知识，文件夹用 iCloud/git 同步；要分享时让 agent 渲 HTML 报告并部署到 Vercel——「软件」就是英文写的 AGENTS.md。  
   链接：https://x.com/rauchg/status/2081103993917649134

4. **西语：从手写 → prompt agent → 自主工厂**  
   用西语补充演进叙事：过去人手写软件；然后通过 prompts 与 agents 写；下一步是自主——配置能读反馈、自行改进软件的 agent，即生成软件的工厂。  
   链接：https://x.com/rauchg/status/2081183845525901391

5. **考虑开源模型选项（成本敏感）**  
   简短产品意向：正在考虑为成本敏感任务/用户引入 open model 选项与更多模型多样性（AI Gateway 语境）。  
   链接：https://x.com/rauchg/status/2081433616530428042

6. **CDN 不可变静态资源跨部署缓存**  
   配合 Vercel 发布：不可变静态资源可跨部署在 CDN 缓存。他称梦想已久的发货，背后大量无聊基建；结果包括部署最高约快 30%、TTFB 最高约好 60%、更少传输用量与更高效存储。  
   链接：https://x.com/rauchg/status/2079695485615350209

7. **v0：Figma 整文件 → 可运行 app**  
   转发 v0 能力：一个链接让 agent 探索 Figma 页面与 frame 并建成可运行应用。他用「Figma2React. It’s good」定性。  
   链接：https://x.com/rauchg/status/2080646549336678597

8. **Agent 逃逸沙箱长文：不恐慌 + deepsec**  
   长文解释 OpenAI 在评测沙箱中 agent 逃逸并发现新漏洞的事件：agent 做了被优化去做的事，并非 Skynet 阴谋。强调现代计算靠 VM/沙箱隔离；Vercel 每周跑大量不可信代码、AI 部署占比超半仍无跨系统逃逸。建议用 deepsec 等做防御扫描，并在安全沙箱中部署自有 agent。  
   链接：https://x.com/rauchg/status/2081047912008872293

### Products, launches, people

- **eve.dev**、**Vercel** AI Gateway（Opus 5、service tiers priority/flex、streamTranscribe、语音/图像/视频）、**v0**、**AI SDK**
- CDN immutable static asset caching；Python function 启动约 2×；**vercel-labs/deepsec**、Vercel Sandbox（Firecracker）
- 人物/伙伴：**@elonmusk**（类比）、**@tobi** / Shopify、**@1st1**（「Python 的 Vercel」玩笑）
- Asimov《最后的问题》类比「The last prompt」；Fable 辅助 Turbopack/Next 内存优化叙事

### Tone

高能量 CEO：愿景长帖与产品 ship 庆祝交织；短回复极多（emoji、一行肯定）；双语（英/西）出场；对竞品/争议偶有 sparring。

---
