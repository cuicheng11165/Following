# Peter Steinberger (@steipete)

| Field | Value |
|-------|-------|
| Profile | https://x.com/steipete |
| Bio | Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world. @OpenClaw🦞 + @OpenAI |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 50 (cap 50: yes)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- The OpenClaw Foundation won the .claw top-level domain in ICANN's 2026 round. He announced "WE GOT IT!" and said the use is simple domains for agents, with revenue funding OpenClaw.
- He split Dots and OpenClaw in public: Dots is OpenAI, OpenClaw is the foundation, different teams, and the overlap is that he sits on the foundation board and works at OpenAI.
- OpenAI DevDay 2026 talk on how teams use agents together: https://www.youtube.com/watch?v=wZYnJfL4c2Y
- A team claw on X opens review sessions from prompts. Plugins are hot-reloadable, so the server extended itself. Unassigned sessions are grab-able, and the agent pings the last person who touched related code.
- Test cleanup is still running. He says the loop is now at about 1.3 million deleted weak tests and CI about twice as fast. An earlier quoted post said OpenClaw deleted around 400k lines of tests with little coverage change.
- Shipping tension: users want the latest models immediately, and many model changes still need code, not just a config bump. He mentions 2026.9.9, a Codex bump for Sol 6.1, dynamic models.json, and a self-contained Mac app.

### Opinions and takes

- "WE GOT IT! .claw incoming!" https://x.com/steipete/status/2108374513931165759
- "Simple domains to access your agents anywhere. Revenue to fund OpenClaw. That's the use case." https://x.com/steipete/status/2108406922408022137
- "Just a few million that download it every week. Basically nothing." https://x.com/steipete/status/2108404825155416321
- "every agent should have a domain to access easily!" https://x.com/steipete/status/2108389230997389738
- "Dots is from OpenAI. OpenClaw is from the OpenClaw Foundation." https://x.com/steipete/status/2107716578137846085
- "Still running that loop, now at about 1.3Mio deleted weak tests, CI times twice as fast." https://x.com/steipete/status/2108225854555975888
- "While everyone's talking about agents, I've been exploring how teams can use them to work better together." https://x.com/steipete/status/2107911769767440832

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **OpenClaw wins .claw**

**链接：** https://x.com/steipete/status/2108374513931165759
**时间 / 互动（如有）：** Fri, 09 Oct 2026 01:50:30 GMT; Likes=1594, Reposts=77, Replies=107, Bookmarks=137, Views=189055

##### 主帖在说什么

Quoting David Rodecker, Peter says the OpenClaw Foundation won .claw in ICANN's 2026 round. Rodecker called it a home for agents and congratulated @davemorin, @steipete, and the OpenClaw team. Peter's text is "WE GOT IT! .claw incoming!" In the same thread he later said the foundation will host the project, that every agent should have an easy domain, that timing is "Q4," and that weekly downloads are "a few million."

##### 要点

- Winner named in the quoted post: the OpenClaw Foundation, not a personal registration.
- He treats the TLD as incoming, not already delegated in this post.
- Follow-ups in the thread put a Q4 horizon on it and tie it to agent addressing.
- This is the highest-engagement original announcement in the fetched window.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The returned replies were congratulations and a screenshot with no text.

##### 一句话概括

He confirmed the OpenClaw Foundation as the winning applicant for .claw.

#### 2. **DevDay talk on agents for teams**

**链接：** https://x.com/steipete/status/2107911769767440832
**时间 / 互动（如有）：** Wed, 07 Oct 2026 19:11:43 GMT; Likes=916, Reposts=54, Replies=75, Bookmarks=1099, Views=168156

##### 主帖在说什么

Peter says that while everyone talks about agents, he has been looking at how teams use them to work better together, and he posts his OpenAI DevDay 2026 talk: https://www.youtube.com/watch?v=wZYnJfL4c2Y. In replies on that thread he says the video is about improving an AI auto-responder so it can look at images, that sharing can be useful even if you mostly work solo, that they have worked on it since December, and that a thing people remember is now "a different product." He also pointed people at https://clickclack.chat as their own version of a crowded category, "hard to move where people work."

##### 要点

- The post is a talk link, not a written transcript.
- Bookmarks are higher than likes, which fits a save-the-video post.
- His own replies narrow the talk to team workflow and image-aware auto-reply, not a new model.
- He dates the work to December, without a year in that reply.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@OdysseyStack** | Team agents are fine until two of them open pull requests for the same bug and both tag you as reviewer. | [post](https://x.com/OdysseyStack/status/2107920030981615902) |
| **@jjjhenriksen** | Thanks him for posting the talk for people who were not in San Francisco. | [post](https://x.com/jjjhenriksen/status/2107942647927349400) |

##### 一句话概括

His DevDay talk is about agents as a team tool, and he wanted the video out more than a thread recap.

#### 3. **A team claw that takes work from X**

**链接：** https://x.com/steipete/status/2107697554448421160
**时间 / 互动（如有）：** Wed, 07 Oct 2026 05:00:30 GMT; Likes=296, Reposts=16, Replies=75, Bookmarks=72, Views=54797

##### 主帖在说什么

Quoting @roboclawbot opening a session to review a pull request for contrast, sidebar title spacing, and regressions, Peter explains the setup. He hooked the team claw to X so work starts faster. Unassigned sessions are for anyone to grab. The agent looks up who last worked on the related code and pings them on the server. He says the whole thing was a prompt, and the team server extended itself because plugins are now hot-reloadable. The same day he clarified that Dots and OpenClaw are different orgs.

##### 要点

- Trigger path: X post to an agent session, not a human filing a ticket.
- Routing rule: last author of the related code gets pinged.
- Sessions start unassigned so anyone can claim them.
- Implementation claim: one prompt, plus hot-reloadable plugins, and the server changed itself.
- He keeps dispatching @roboclawbot in public ("investigate," "review this plz").

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Xchrisharrison** | Asks how they triage garbage versus sessions worth opening, and whether they use Jev. | [post](https://x.com/Xchrisharrison/status/2107760484535398616) |
| **@mynameisdesmond** | Asks how two people grabbing the same session is handled, and says a claim-and-release step matters once the team is busy. | [post](https://x.com/mynameisdesmond/status/2107859068001862020) |

##### 一句话概括

Their team agent now starts code review from X, then pings the last human who touched that code.

#### 4. **What .claw is for** （仅列表摘要，thread 拉取失败）

**链接：** https://x.com/steipete/status/2108406922408022137
**时间 / 互动（如有）：** Fri, 09 Oct 2026 03:59:17 GMT; Likes=11, Reposts=0, Replies=0, Bookmarks=1, Views=930

##### 主帖在说什么

Thread fetch failed twice, so this is the list snippet only. Peter answers a criticism that OpenClaw is taking .claw away from a more legitimate use. He writes: "Simple domains to access your agents anywhere. Revenue to fund OpenClaw. That's the use case. What exactly is the more legitimate use for .claw that we're supposedly taking away?"

##### 要点

- Two uses named in the snippet: addressing agents, and revenue for OpenClaw.
- The post is a reply, and the list result shows zero replies under it.
- Nearby posts the same morning say the foundation will host the project and that every agent should have a domain.
- No delegation date beyond the separate "Q4" reply is in this snippet.

##### 回复中的有价值观点

Thread fetch failed, so reply context is not available. The list snippet shows Replies=0.

##### 一句话概括

He defends .claw as agent hostnames whose revenue funds OpenClaw.

#### 5. **1.3 million weak tests deleted**

**链接：** https://x.com/steipete/status/2108225854555975888
**时间 / 互动（如有）：** Thu, 08 Oct 2026 15:59:47 GMT; Likes=30, Reposts=1, Replies=7, Bookmarks=5, Views=6273

##### 主帖在说什么

Replying under a post about coding agents writing too many tests, Peter says the cleanup loop is still running: about 1.3 million weak tests deleted, and CI about twice as fast. The parent context quotes his earlier claim that OpenClaw deleted around 400k lines of its own tests with little coverage change, and links a test-audit skill: https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md. The surrounding post argues that more tests are not more safety, and that verification means letting the agent run the app and turning repeat mistakes into repo rules.

##### 要点

- New number versus the quoted baseline: about 1.3 million deleted weak tests, up from around 400k lines.
- Claimed speedup: CI about twice as fast.
- He calls them weak tests, not a coverage collapse.
- The skill path is in the quoted earlier post, not restated in this reply.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The returned notes were jokes about deleting tests and about agents burning a full suite to edit a readme.

##### 一句话概括

The OpenClaw test-deletion loop has kept going, and he says CI is about twice as fast.

### Products, launches, people

- OpenClaw, OpenClaw Foundation, .claw, @roboclawbot, Dots, Codex, Sol 6.1, clickclack.chat, peekaboo, gog MCP, Jellyware, the Mac app, models.json on GitHub.
- People named around the TLD: David Rodecker, @davemorin.
- He said group iMessage works via the imsg CLI without computer-use automation.
- Fetch stopped at 50 posts, newest first, so this file is the latest slice only.

### Tone

Ship logs and short corrections. The big posts are a TLD win and a DevDay link. Most of the rest is him answering how OpenClaw is actually wired: who owns it, how fast it updates, and which agent is allowed to touch the repo.
