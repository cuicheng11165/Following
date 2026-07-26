# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude Code @anthropicai |
| Source list | builders.md |

---

## Window: 2026-06-26 → 2026-07-26

- **Fetched at:** 2026-07-26T19:28:25Z
- **Posts in window (fetched):** 50 (cap 50: yes — 窗口内可能更多)
- **Mode:** 30-day backfill (rewrite of existing window)

### Themes

- **AI 采用四步**：个人 10x → 组织追赶；token 不够，要破瓶颈 + 建护栏
- **领域知识基础设施化**：CLAUDE.md / REVIEW.md / skills / 文档；agent 零额外上下文可贡献
- **Opus 5**：编码/分析/设计/生物/知识工作；**最难 prompt inject**；叠 Auto Mode ≈ 0 成功率
- **Claude Code 产品**：/checkup、subagents 默认后台、Artifacts 扩至 Pro/Max、Desktop Linux
- 实践：用 Fable dynamic workflow 把 p95 压到 <300ms；避免无请求的代码注释
- 澄清误归因；科幻书单（Diamond Age、Permutation City 等）

### Opinions and takes

- 组织 AI 采用常见四步；更大回报是修复/维护在后台发生，团队专注构建——他自认到 step 4，Anthropic 在 3→4。
- 追踪 ROI 不看 usage dashboard  alone：问「没有 AI 你们会不会做、要多少 eng-hours」。
- 自动化乘以 agent 军团；把重复问题变成 lint/CI/routine 比每次用 token 修更好。
- 非工程师 day-one 能贡献代码的前提是：领域知识编码进 infra，而非只活在人头里。
- Opus 5 最兴奋的是抗 prompt injection；强对齐 + 探针 + Claude Code Auto Mode 可把攻击成功率压到 ~0。
- 优化代码的方式：告诉 Fable 用 dynamic workflow 把 p95 压到阈值以下，别停，用 profiler。

### Notable posts

1. **AI 采用四步长帖**  
   他每天和别的公司工程师聊天，常见画面：一个人用 Claude 10x 产出，组织其余人没跟上。他总结四步采用路径；强调每一步 token 都不够用，要拆掉下一层瓶颈并建护栏。更高阶需要端到端自验证、auto mode 权限、自动 code/security review、多 agent 界面（CLI Agent view、Desktop、iOS/Android、Tag），以及 /loop、/batch、dynamic workflows、worktree isolation。更大回报是维护在后台、团队去做以前够不着的事。他称 Anthropic 在 step 3 推向 4，自己刚到 level 4。  
   链接：https://x.com/bcherny/status/2077929379661844559

2. **把领域知识变成基础设施**  
   过去顶尖工程师用 vim 自动化、lint、e2e 测试乘以自身产出；agent 时代更重要：infra/DevX 加速每个 agent；把重复问题编码成 lint/CI/routine（「loops」）；最关键的是让 day-one 工程师与非工程师能贡献——障碍是人头里的领域知识。应写 CLAUDE.md、REVIEW.md、skills、docs，让 agent 零额外上下文即可工作；PR 因「没用对框架」被拒是自动化失败。  
   链接：https://x.com/bcherny/status/2077460395279692197

3. **Opus 5 与抗 prompt injection**  
   他肯定 Opus 5 适合 coding、数据分析、设计、生物、知识工作；但更兴奋的是：Opus 5 是迄今最难 prompt inject 的模型（system card 里 PI evals 与 red team 有体现）。叠加强模型对齐 + prompt injection probes + Claude Code Auto Mode，攻击成功率可到 ~0——「this is new and exciting」。  
   链接：https://x.com/bcherny/status/2080713091688583312

4. **/checkup 命令**  
   新功能 /checkup：清理未用 skills/MCPs/plugins 省上下文；本地 CLAUDE.md 与仓库版去重；把根 CLAUDE.md 拆成嵌套 + skills；关掉慢 hooks；升级 Claude Code；默认开 auto mode；预批准常被拒绝的只读命令等。任何改动前会确认。  
   链接：https://x.com/bcherny/status/2074997570317779038

5. **Subagents 默认后台运行**  
   下一版 Claude Code：subagents 默认在后台跑，你可继续与主 Claude 对话；若要前台，告诉 Claude 即可。权限请求会转发到主 agent；可用方向键 + enter「zoom in」给 subagent 发消息。  
   链接：https://x.com/bcherny/status/2071647677591466098

6. **Fable 动态工作流压 p95**  
   他描述当下优化代码的方式：对 Fable 说「用 dynamic workflow 把 p95 压到 300ms 以下，别停直到完成，用 profiler」——「pretty how I optimize code these days」。  
   链接：https://x.com/bcherny/status/2080172448314790016

7. **Artifacts 与 Claude Code 起源故事**  
   Artifacts 扩至 Pro/Max：他称 Artifacts「life changing」。另转发 Claude Code 起源故事（从 Anthropic 安全研究起步）：「So much more to do. We are 1% done.」Linux Desktop beta 上线时他也官宣下载链接。  
   链接：https://x.com/bcherny/status/2072777472970563995

8. **误归因澄清 + CLAUDE.md 反注释**  
   高赞帖澄清「I did not write this.. please don’t attribute stuff to me if it wasn’t me」。另建议：`echo "Avoid code comments unless you are explicitly asked…" >> CLAUDE.md`。  
   链接：https://x.com/bcherny/status/2081116450769731816

### Products, launches, people

- **Claude Code**：/checkup、subagents、Artifacts、Auto Mode、Tag、Desktop Linux
- **Opus 5**、**Fable**、Opus 4.8
- CLAUDE.md / REVIEW.md / skills / dynamic workflows
- 人物：Garry（活动）；科幻 Egan/Stephenson 等；Jarred Sumner（Bun in Rust）

### Tone

高信号工程师长文 + 大量产品答疑短帖；务实、可操作，偶有 meme 与书单。对误归因直接纠正，对用户反馈很在线。
