# Cat Wu (@_catwu)

| Field | Value |
|-------|-------|
| Profile | https://x.com/_catwu |
| Bio | claude code + cowork @anthropicai, prev: @dagster, @scale_ai |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 29 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Claude Code product support, in public. On Oct 9 she answers a long Projects complaint by listing fixes already in the latest app: folder caps per project or none, a per-project trust level for prod (deploys and SSH), errors that say where a thread runs and how to fix them, and keeping project chat plus threads as the remote view from phone or web. She says the rest is still under look. https://x.com/_catwu/status/2108415409816793141
- Projects as a coordinator. Asked for better thread management, she says a new version of Projects is rolling out: one Claude that coordinates and finds all your threads. https://x.com/_catwu/status/2108413432504729729
- Compaction is a cost tradeoff. She posts the exact switches to turn auto-compact off, and says an alternative that would break caching would cost a lot more than the current implementation. https://x.com/_catwu/status/2108411312095314410 https://x.com/_catwu/status/2108412661906211059
- Model launches she amplifies with Claude Code numbers. Sonnet 5.5: about 30% more tasks done than Sonnet 5 in Claude Code, fewer tokens for the same work, and a leaf-raking demo that is 24 seconds faster with 6K fewer tokens. Separately she points people who want to try Opus 5.5 and Claude Tag in Slack, and says Tag is on Claude Team and Claude Enterprise. https://x.com/_catwu/status/2104639552170377399 https://x.com/_catwu/status/2102569951974584612 https://x.com/_catwu/status/2102648730415735045
- PM workflow on top of Claude: ask who used a feature most last week, build an artifact of the top 10, and schedule 15-minute chats. Names are anonymized. Her question list is use cases, how the user would pitch it, what is frustrating, and what should be supported next. https://x.com/_catwu/status/2107967210467803152 https://x.com/_catwu/status/2108010848127967652

### Opinions and takes

- "In Claude Code, users get ~30% more tasks done compared to Sonnet 5. It's smarter, so it needs fewer tokens for the same work." https://x.com/_catwu/status/2104639552170377399
- "the other thing that’s tricky about this is that this breaks caching and so would cost a lot more than the current compaction implementation." https://x.com/_catwu/status/2108412661906211059
- Auto-compact off: `/config` and flip the Auto-compact toggle (writes `"autoCompactEnabled": false`), or launch one session with `DISABLE_AUTO_COMPACT=1` (manual `/compact` still works). https://x.com/_catwu/status/2108411312095314410
- "we're rolling out a new version of projects to help with this! it gives you one claude that coordinates and finds all your threads." https://x.com/_catwu/status/2108413432504729729
- "We're still rolling out the Chat + Cowork merge to our users so some folks still have the separate experience." https://x.com/_catwu/status/2102557202259271745
- "I would recommend switching back. I generally reset my configs for each new model." https://x.com/_catwu/status/2102556970473709717
- "Let me know what you’d like us to improve in Claude Code!" https://x.com/_catwu/status/2108056942858096721

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Projects fixes already in the latest app**

**链接：** https://x.com/_catwu/status/2108415409816793141
**时间 / 互动（如有）：** Fri, 09 Oct 2026 04:33:00 GMT; Likes=47 Replies=7 Views=3638

##### 主帖在说什么

Michael Wise posted a long writeup of walls he hit with Claude Projects: the coordinator and threads run in the cloud, local folders were unreachable ("no default computer set"), Remote Control failed with "folder limit reached," web research stalled, permissions locked when a thread started, prod deploys and SSH were treated as sacred, and it was hard to see where a thread was running. Cat replies that four of his asks are fixed in the latest app: folder caps per project or none; a per-project trust level for prod (deploys, SSH); showing where each thread runs, with errors that say how to fix them; and keeping the project chat and threads as the remote view so he can check in from other Claude app instances (phone, web). She says she is looking into the rest.

##### 要点

- Fixed: per-project folder caps (or none).
- Fixed: per-project prod trust for deploys and SSH.
- Fixed: thread location plus actionable errors.
- Fixed: project chat and threads remain the remote view across phone and web.
- Not claimed as fixed: running the coordinator on a chosen local machine, project-wide permissions changeable mid-thread, and one-click move of a thread to a new environment.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@dusangran** | Per-project prod trust is the fix he was waiting on; he would still give the agent a read-only database user on prod. | [post](https://x.com/dusangran/status/2108425973947306138) |
| **@weezilla** | The original reporter calls the turnaround fast and thanks the team. | [post](https://x.com/weezilla/status/2108444738890141719) |

##### 一句话概括

Four of the loudest Projects complaints (folder caps, prod trust, thread location, remote view) are already in the latest app.

#### 2. **One Claude that finds your threads**

**链接：** https://x.com/_catwu/status/2108413432504729729
**时间 / 互动（如有）：** Fri, 09 Oct 2026 04:25:09 GMT; Likes=2 Replies=0 Views=151

##### 主帖在说什么

In a thread whose visible parent asks for better thread management, she says Anthropic is rolling out a new version of Projects so that one Claude coordinates and finds all of your threads. The post is one sentence; she does not describe scheduling, permissions, or how this differs from the cloud coordinator Wise had just criticized. The same hour she is also answering that critique with the fix list above.

##### 要点

- The product name she uses is Projects, not a new brand.
- The behavior she promises is coordination plus finding existing threads.
- She says it is rolling out, not that it is finished for everyone.
- No metrics, plan limits, or dates in this post.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies.

##### 一句话概括

The Projects rollout she is describing is one coordinating Claude that can find the threads, not a pile of separate chats.

#### 3. **PM shortcut: top users, then a 15-minute chat**

**链接：** https://x.com/_catwu/status/2107967210467803152
**时间 / 互动（如有）：** Wed, 07 Oct 2026 22:52:01 GMT; Likes=532 Replies=36 Views=58811

##### 主帖在说什么

She posts one of her favorite PM uses of Claude, with a screenshot: ask who used a given feature the most last week, have Claude make an artifact of the top 10 by usage, then reach out and schedule 15 minutes. She calls it the fastest way to get user feedback. In the same thread she says names are anonymized, that any cut of the data is one prompt away, and that she typically asks for top workflows, how the user would pitch the feature to a teammate, what is frustrating, and what they would want supported next. https://x.com/_catwu/status/2108010190641541304 https://x.com/_catwu/status/2108010063763849660 https://x.com/_catwu/status/2108010848127967652

##### 要点

- The workflow is usage ranking, an artifact, outreach, and a 15-minute conversation.
- She says names in that artifact are anonymized.
- The interview script is four prompts: workflows, pitch, frustration, next support.
- She frames this as a PM practice, not as a shipped Claude Code feature.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bcherny** | He does the same thing: Claude DMs people on Slack, watches for replies, and charts the results. | [post](https://x.com/bcherny/status/2107980284813787225) |
| **@ian_finlay** | Also talk to people who used the feature once and never came back; power users have already survived the confusing parts. | [post](https://x.com/ian_finlay/status/2107970977770639646) |

##### 一句话概括

Her research loop is a prompt that ranks last week's users and books the conversations.

#### 4. **Sonnet 5.5 in Claude Code**

**链接：** https://x.com/_catwu/status/2104639552170377399
**时间 / 互动（如有）：** Mon, 28 Sep 2026 18:29:06 GMT; Likes=504 Replies=50 Views=47658

##### 主帖在说什么

Quote-posting Claude's launch of Sonnet 5.5 (described there as a clear upgrade over Sonnet 5, more than 30% faster, and up to 30% cheaper for most work), she adds Claude Code specifics and a video. In Claude Code, users get about 30% more tasks done than on Sonnet 5, because the model is smarter and needs fewer tokens for the same work. The demo she attaches is the model raking a yard of leaves with tool calls: 24 seconds faster than Sonnet 5, with 6K fewer tokens, leaving "her" extra time to read.

##### 要点

- Her number, distinct from the launch post's speed and price claims: about 30% more tasks completed in Claude Code versus Sonnet 5.
- Mechanism she gives: fewer tokens for the same work, not only a faster decoder.
- Demo delta: 24 seconds and 6K tokens on the leaf-raking tool-call video.
- She does not restate API prices in her own text.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@SPAC89** | Says Sonnet 5.5 is better and cheaper than they expected, and claims that on their own 3D Cerebras-chip benchmark it outperforms GPT-6 Astra. That benchmark claim is theirs, not Cat's. | [post](https://x.com/SPAC89/status/2104640995627593730) |
| **@aronprins** | Says it is exceeding expectations and posts a one-shot Three.js scene made with Sonnet 5.5. | [post](https://x.com/aronprins/status/2104650651707793626) |

##### 一句话概括

Her Claude Code claim for Sonnet 5.5 is more finished tasks and fewer tokens, illustrated by a 24-second, 6K-token demo gap.

#### 5. **Opus 5.5 and Claude Tag in Slack**

**链接：** https://x.com/_catwu/status/2102569951974584612
**时间 / 互动（如有）：** Wed, 23 Sep 2026 01:25:15 GMT; Likes=172 Replies=14 Views=33987

##### 主帖在说什么

Boris Cherny posted that he used Opus 5.5 to formally verify the Claude Agent SDK in Lean, that a couple of short prompts produced 16 PRs fixing bugs and race conditions, and that TLA+ also works for data flow, concurrency, and state. Cat's post is a pointer: if you want to try Opus 5.5 and Claude Tag in Slack, this is a way in. The fetched text does not include a URL or setup steps. In the same conversation she later says it is available on Claude Team and Claude Enterprise. https://x.com/_catwu/status/2102648730415735045

##### 要点

- She is routing people to Opus 5.5 plus Claude Tag in Slack, not describing the Lean proof herself.
- The verification story (16 PRs, Lean, TLA+) is Boris's, which she is quote-posting.
- Availability she states: Claude Team and Claude Enterprise.
- No Teams support is promised. A reply asks for MS Teams and she does not answer that in the fetched thread.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@jasonchen3636** | Asks when Claude Tag is coming to Microsoft Teams. | [post](https://x.com/jasonchen3636/status/2102770617326125209) |

##### 一句话概括

She points Slack users on Team and Enterprise plans at Opus 5.5 and Claude Tag, using Boris's formal-verification post as the example.

### Products, launches, people

- Claude Sonnet 5.5, Claude Opus 5.5, Claude Code, Claude Projects, Cowork, Claude Tag (Slack; Team and Enterprise), Chat + Cowork merge still rolling out.
- Auto-compact setting `autoCompactEnabled` and `DISABLE_AUTO_COMPACT=1`.
- People in the threads: Boris Cherny, Michael Wise, Dan-style product feedback rather than a new Cat-owned product.

### Tone

Operator voice. The high-engagement posts are a model launch and a PM recipe; the rest of the window is her answering bug reports in the same hour they arrive, including the exact config key for auto-compact and a direct statement that a nicer compaction design would blow the cache budget. Almost no jokes, and very little that is not Claude Code or Cowork.
