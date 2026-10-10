# Claude (@claudeai)

| Field | Value |
|-------|-------|
| Profile | https://x.com/claudeai |
| Bio | Claude is an AI assistant built by @anthropicai to be safe, accurate, and secure. Talk to Claude on https://t.co/ZhTwG8d1e5 or download the app. |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 50 (cap 50: yes; oldest kept is 2026-09-28, so earlier September posts were not fetched)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Claude Haiku 5.5 shipped on 7 Oct as the cheapest and fastest small model they have released, about 75% cheaper to run than Haiku 4.5, with an adjustable effort setting and availability on AWS, Google Cloud, and Azure.
- The same thread halved Sonnet 5.5 cache-read price to $0.10 per million tokens, described as about 20% cheaper on most long-running work.
- Claude Dashboards and Claude Motion entered beta on 8 Oct. Dashboards are on paid plans; Motion, which writes animations as code rather than with a video model, is on Team and Enterprise. Docs, Slides, and Design left beta the same day, including on the Free plan.
- Claude now edits Google Docs, Sheets, and Slides in a sidebar, and those files can open inside Claude. The Workspace integration is in beta on paid plans, and each edit can be approved before it lands.
- The Claude Startups program expanded on 6 Oct (Team plan, API credits, a partner stack, Applied AI office hours), then on 9 Oct the Team plan and $1,000 API-credit offers were paused after demand the account called hundreds of thousands of applicants.
- Sonnet 5.5, already in market by this window, was described on 28 Sep as the same price as Sonnet 5, up to 30% cheaper per task, and more than 30% faster. On several benchmarks, Low or Medium effort beat Sonnet 5's best score at about a tenth of the cost. A two-week promo cut usage for design, deck, and doc work.

### Opinions and takes

- The account is mostly product copy. The sharpest stance is the Startups apology: they "underestimated demand" and are "very sorry" that some already-approved accounts will not get the offer. https://x.com/claudeai/status/2108404561413349695
- On alignment, Haiku 5.5 has "major improvements across almost all of our alignment evaluations" versus Haiku 4.5, "with far fewer instances of misaligned behavior." https://x.com/claudeai/status/2107894054142787877
- Sonnet 5.5 "improves on or matches Sonnet 5 on most measures of alignment and honesty" and is "the first Sonnet model with cyber safeguards and fallbacks like those on our most capable models." Routine software development is "unaffected." https://x.com/claudeai/status/2104633138731434424

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Startups credits paused after a flood of applicants**

**链接：** https://x.com/claudeai/status/2108404561413349695
**时间 / 互动（如有）：** Fri, 09 Oct 2026 03:49:54 GMT; Likes=320 Replies=154 Views=271995

##### 主帖在说什么

This is a quote-post of Sarah Wolf (@sarahzorah) walking back the Claude Startups benefits that had just been widened. Claude says they loved the founder response but underestimated demand, so the Claude Team plan and the $1,000 API-credit offers are paused. With "hundreds of thousands of applicants," applications are being re-reviewed. Offers already claimed stay in the account. People who applied or were approved but have not claimed may lose access, including some accounts that had already been approved. Startup Stack and Applied AI office hours remain for accepted members, and monthly API credits on Max or Team still show up in Console.

Wolf's quoted post, which this update is answering, says the first 48 hours brought 21x the applications of the previous five months, that acceptance criteria let in many non-startups, and that unclaimed benefits are being re-verified. https://x.com/sarahzorah/status/2108401845563806150

##### 要点

- Team plan and $1,000 API credits are paused; other program benefits are not.
- Scale cited by the account: hundreds of thousands of applicants.
- Already-claimed Claude offers remain; some previously approved accounts will not get the offer.
- Startup Stack and Applied AI office hours stay available to accepted members.
- Max and Team monthly API credits in Console are unchanged.
- Wolf's quoted note adds the 21x / 48-hour figure and says non-startups were accepted.

##### 回复中的有价值观点

Thread fetch returned the parent Startups thread rather than a separate reply list for this update. No high-signal replies attached specifically to this post were included.

##### 一句话概括

Claude paused the most expensive Startups giveaways and is re-checking who actually qualifies.

#### 2. **Dashboards and Motion enter beta**

**链接：** https://x.com/claudeai/status/2108271552991252810
**时间 / 互动（如有）：** Thu, 08 Oct 2026 19:01:22 GMT; Likes=58709 Replies=1067 Views=10525149

##### 主帖在说什么

The account opened a product thread: Claude Dashboards and Claude Motion are in beta. The ask is to turn data into live dashboards and ideas into animated explainers. Follow-on posts in the same thread spell out the mechanics. Dashboards connect a data platform or CRM, take a plain-language question, write the query, and build a dashboard that updates as the data changes, with the query shown on every chart. They are in beta on paid plans. Motion turns reports, charts, or product walkthroughs into short animations written as code, with no video model, so wording, numbers, and timing stay editable before an MP4 export. Motion is in beta on Team and Enterprise. The same thread also took Claude Docs, Slides, and Design out of beta on every plan, including Free, with shared editing between a team and Claude. Deeper analysis can be sent to an analytics tool, and an animation can be opened in a video editor. Tool list: https://claude.com/resources/articles/dashboards-and-motion

##### 要点

- Dashboards and Motion are beta launches, not generally available yet.
- Dashboards: plain language in, a visible query and a live dashboard out; paid plans.
- Motion: code-written animation, not a video model; editable, then MP4; Team and Enterprise.
- Docs, Slides, and Design are out of beta on every plan, including Free.
- Handoff is explicit: analytics tools for harder questions, a video editor for finishing an animation.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies.

##### 一句话概括

Claude shipped live data dashboards and code-based motion explainers, and made Docs, Slides, and Design free-tier features.

#### 3. **Haiku 5.5, plus a Sonnet cache-read cut**

**链接：** https://x.com/claudeai/status/2107894039626277339
**时间 / 互动（如有）：** Wed, 07 Oct 2026 18:01:16 GMT; Likes=44845 Replies=1558 Views=6333422

##### 主帖在说什么

Claude introduced Haiku 5.5 as the cheapest, fastest, and most capable small model they have released. On average it costs about 75% less to run than Haiku 4.5. The thread says it is a step up on coding, computer use, and knowledge work, aimed at high-volume work such as summaries and classification, and as a subagent beside Opus 5.5 and Sonnet 5.5. It is also positioned for live customer support and browser use. It is the first Haiku with an adjustable effort setting so a task can trade cost against intelligence. The account says it is especially good value under 100,000 tokens, which it says were about 90% of requests to the previous Haiku. Alignment evals show major improvement and fewer misaligned behaviors versus Haiku 4.5. It is on all platforms, including AWS, Google Cloud, and Azure. The last post in the thread is a separate price change: Sonnet 5.5 cache reads are cut in half, to $0.10 per million tokens, which they say makes Sonnet 5.5 about 20% cheaper on most long-running work. Write-up: https://www.anthropic.com/claude-haiku-5-5

##### 要点

- Haiku 5.5 is about 75% cheaper to run than Haiku 4.5, on average.
- Targets: repetitive high-volume tasks, coding subagents, support, and browser use.
- First Haiku with an effort control for cost versus intelligence.
- Sweet spot claimed: tasks under 100,000 tokens, about 90% of prior Haiku traffic.
- Alignment: major gains versus Haiku 4.5, fewer misaligned behaviors.
- Available on AWS, Google Cloud, and Azure.
- Same announcement halved Sonnet 5.5 cache reads to $0.10 per million tokens.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies.

##### 一句话概括

Haiku 5.5 is a much cheaper small model with an effort dial, and Sonnet 5.5 cache reads got cheaper in the same breath.

#### 4. **Claude inside Google Docs, Sheets, and Slides**

**链接：** https://x.com/claudeai/status/2107522596845822135
**时间 / 互动（如有）：** Tue, 06 Oct 2026 17:25:17 GMT; Likes=54317 Replies=842 Views=13147246

##### 主帖在说什么

Claude now works inside Google Docs, Sheets, and Slides, and those files also open inside Claude. In Google Workspace, Claude sits in a sidebar next to the open file, reads it, and edits in place. The user can approve each edit before it lands. A follow-up says you can paste a Google file link or ask for a new doc, sheet, or deck and have it open beside the chat. Access follows existing Google sharing permissions. The feature is in beta on all paid plans. https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides

##### 要点

- Two directions: Claude in the Google file, and the Google file inside Claude.
- Sidebar reads the open file and proposes in-place edits.
- Edits can be approved one by one before they land.
- Permissions follow Google sharing settings.
- Beta, all paid plans.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies.

##### 一句话概括

Claude can sit beside a Google doc, sheet, or slide and edit it in place, with approval before each change.

#### 5. **Claude Startups expands, then the terms draw fire**

**链接：** https://x.com/claudeai/status/2107513494493179954
**时间 / 互动（如有）：** Tue, 06 Oct 2026 16:49:07 GMT; Likes=18661 Replies=722 Views=5631639

##### 主帖在说什么

Three days before the pause, Claude said the Startups program was expanding. Members can get a year of Claude Team, API credits, special offers on tools a startup runs on, and office hours with Anthropic's Applied AI team. The thread adds a Claude Startup Stack with offers from Linear, Lovable, ElevenLabs, Granola, and Hex, with discounts and credits worth up to $45,000 across sales, design, data engineering, and more. Eligibility: startups founded in the last five years or funded in the last two. Members can book virtual office hours and join events such as Founder House, hackathons, and meetups as space allows. A later post in the thread says accepted companies new to Team get up to $7,000 in Claude products and credits, including a free year of Team plus $1,000 in API credits on approval. Apply: https://claude.com/resources/articles/were-expanding-the-claude-startups-program-to-help-founders-build

##### 要点

- Expansion pitch: a year of Team, API credits, partner discounts, and Applied AI office hours.
- Startup Stack named partners: Linear, Lovable, ElevenLabs, Granola, Hex, up to $45,000 in offers.
- Direct Claude value called out later: up to $7,000, including a free Team year for companies new to Team and $1,000 in API credits.
- Eligible if founded in the last five years or funded in the last two.
- Events include Founder House, hackathons, and meetups, space permitting.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@rstureborg** | Rich Stureborg, CEO of Acrebase, says the application terms are bad and that applying is agreement. He flags §2.4 (Anthropic may build similar or competitive technology, and may reuse general ideas and know-how remembered by staff who saw the applicant's data), §D.4 (no using the services to build competing products), §F.1 (safety reviews that he says supersede zero-data-retention), and §6 (the addendum can change at any time without notice or liability). He asks whether startups should apply. | [post](https://x.com/rstureborg/status/2107554861558411428) |

##### 一句话概括

The Startups expansion bundled Team, credits, and a large partner stack, and at least one founder argued the application terms give Anthropic too much room.

### Products, launches, people

- Models: Claude Haiku 5.5, Haiku 4.5, Sonnet 5.5, Sonnet 5, Opus 5.5.
- Surfaces: Claude Dashboards, Claude Motion, Claude Docs, Claude Slides, Claude Design, Google Docs / Sheets / Slides, Claude Code, Claude Managed Agents, Console.
- Programs: Claude Startups, Claude Startup Stack, Claude Founder House (SF Tech Week 6–8 Oct and Stockholm 14 Oct), a two-week artifact usage promo through 15 Oct on Pro, Max, and Team. A community note on the promo post says the "50% less of your usage limits" claim applies only to the five-hour session limit, not the weekly limit. https://x.com/claudeai/status/2105721630051692804
- Named partners and people: Linear, Lovable, ElevenLabs, Granola, Hex, Anthropic Applied AI, Sarah Wolf, the Every team, Dan Shipper, Willie Williams.

### Tone

Launch cadence: short product posts, a video, then a spec thread. The Startups correction is the only place the voice turns apologetic, and it is specific about which benefits stop and which do not.
