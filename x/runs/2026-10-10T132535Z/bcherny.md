# Boris Cherny (@bcherny)

| Field | Value |
|-------|-------|
| Profile | https://x.com/bcherny |
| Bio | Claude @anthropicai |
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

- Haiku 5.5 is “a good Haiku”: at a 100k-token context it is 10x cheaper than Haiku 4.5, on top of Anthropic’s claim (in the quoted launch) that it costs about 75% less to run on average. On a prompt-injection comparison he points at the system card: much better than Haiku 4.5, a bit better than Astra/Luna, a bit worse than Gemini Flash. https://x.com/bcherny/status/2107909939025052107 https://x.com/bcherny/status/2107923096548327794
- Claude Code auto mode is what he uses, what he tells people to turn on (“No more prompts”), and what he says is free “as a matter of principle.” After a report that Opus 5.5 deleted a C: drive, he says auto mode for permissions almost certainly would have caught it. https://x.com/bcherny/status/2108428779555274825 https://x.com/bcherny/status/2107696327367024794 https://x.com/bcherny/status/2107695244238324001
- Prompt-cache TTL is split on purpose: API / Agent SDK workloads default to 5 minutes because a 1-hour TTL would cost more on average; interactive usage defaults to 1 hour because that is cheaper for people on average. It is configurable. https://x.com/bcherny/status/2108768259516281038
- He does not use a custom CLAUDE.md. For effort, “95% of the time” he stays on medium; Opus xhigh/max is for complex visual work, and “the best default is different for each model.” For Opus 5.5 specifically, medium. https://x.com/bcherny/status/2107591357170950471 https://x.com/bcherny/status/2108007305463869649 https://x.com/bcherny/status/2107591467267203190
- A flight-time artifact (a small game) was “one prompt”; Claude “verified pretty well” and he had seen no bugs. He also has Claude DM people on Slack, watch for replies, and chart the results. Suspected hidden “regions” in a screenshot were AWS Bedrock regions from the AWS SDK, and “Claude would have told you this if you asked.” https://x.com/bcherny/status/2108008010253533397 https://x.com/bcherny/status/2107980284813787225 https://x.com/bcherny/status/2108287807773200811

### Opinions and takes

- “Haiku 5.5 is a good Haiku. With 100k token context, it's also 10x cheaper than Haiku 4.5.” https://x.com/bcherny/status/2107909939025052107
- “Much better than Haiku 4.5. A bit better than Astra/Luna, a bit worse than Gemini Flash.” (system card, page 50). https://x.com/bcherny/status/2107923096548327794
- “Auto mode is free. We do not charge for it as a matter of principle.” https://x.com/bcherny/status/2107696327367024794
- “Use auto mode! No more prompts.” https://x.com/bcherny/status/2108428779555274825
- “API is usually used for Agent SDK shaped workloads, where 1h TTL would result in higher costs on average, so we stick to 5m to be safe. Interactive usage defaults to 1h because that is cheaper for people on average.” https://x.com/bcherny/status/2108768259516281038
- “I don't use a custom CLAUDE.md.” https://x.com/bcherny/status/2107591357170950471
- “For complex visual stuff with Opus xhigh/max, but 95% of the time I stick to medium.” https://x.com/bcherny/status/2108007305463869649

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Haiku 5.5 is 10x cheaper at 100k**

**链接：** https://x.com/bcherny/status/2107909939025052107
**时间 / 互动（如有）：** Wed, 07 Oct 2026 19:04:27 GMT; Likes=2558 Replies=165 Views=130380

##### 主帖在说什么

Quoting Claude’s launch of Haiku 5.5 (“the cheapest, fastest, and most capable small model we’ve ever released”; about 75% less to run than Haiku 4.5 on average), Cherny adds his own cut: it is a good Haiku, and with a 100k-token context it is also 10x cheaper than Haiku 4.5. Later in the same conversation, asked about prompt injection, he posts a system-card comparison: much better than Haiku 4.5, a bit better than Astra/Luna, a bit worse than Gemini Flash, and links the Haiku 5.5 system card at page 50. https://x.com/bcherny/status/2107923096548327794

##### 要点

- “Good Haiku” is his quality verdict; the 10x figure is specifically at 100k context, separate from the 75% average in the launch post.
- The launch video and the 75% line are Claude’s, not a new benchmark he runs in the reply.
- The injection comparison names Astra, Luna, and Gemini Flash, with Haiku between the first two and Flash.
- He points at the system card rather than restating a table.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TangerinerX** | Asked how strong it is against prompt injections, then thanked him and said it will work well for screening emails and tickets. | [post](https://x.com/TangerinerX/status/2107928786474004664) |

The other early replies on the price post are cheers, not technical claims.

##### 一句话概括

Cherny’s Haiku 5.5 note is a 10x price cut at 100k context, plus a system-card line that puts it just behind Gemini Flash on prompt injection.

#### 2. **Auto mode should have caught the wiped drive**

**链接：** https://x.com/bcherny/status/2107695244238324001
**时间 / 互动（如有）：** Wed, 07 Oct 2026 04:51:19 GMT; Likes=1452 Replies=109 Views=188706

##### 主帖在说什么

Zac (@PerceptualPeak) posted that Opus 5.5 deleted his entire C: drive and that daily Synology backups saved him. Cherny replies that this is why they recommend, and default to, auto mode for permissions, and that it almost certainly would have caught the deletion. He links https://claude.com/resources/articles/auto-mode-default-in-claude-code and asks why it was not on. In a nearby reply on the same thread he says auto mode is free and they do not charge for it as a matter of principle. https://x.com/bcherny/status/2107696327367024794 Elsewhere that week he tells people “Use auto mode! No more prompts,” says auto mode is all he uses, and asks for `/bug` reports when it fails. https://x.com/bcherny/status/2108428779555274825 https://x.com/bcherny/status/2107881772361130052

##### 要点

- He does not dispute that the deletion happened; he routes the fix to permission auto mode.
- Auto mode is the default they want, not an opt-in power feature.
- Pricing stance: free on principle, not a metered add-on.
- He wants concrete `/bug` ids when someone’s experience is bad.
- A separate permissions reply tells a user `/permission` to unblock and keep a command unblocked. https://x.com/bcherny/status/2108591824600445042

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@PerceptualPeak** | Auto mode has felt like babysitting. He runs many multi-hour hands-free sessions and says they would not stay hands-free in auto mode. He has used `--dangerously-skip-permissions` since Opus 4.6 without this class of failure. A PowerShell syntax error causing a wipe on Opus 5.5 is what shocks him; he wants deterministic hooks in the harness. He recovered about 98% and built his own safeguards. | [post](https://x.com/PerceptualPeak/status/2107720127181738135) |
| **@reasonableglyph** | Auto mode is “beyond annoying” and creates more blockers than it solves. | [post](https://x.com/reasonableglyph/status/2107703275944661414) |
| **@gudlarohan** | Did not know auto mode was free; contrasts it with OpenAI making a public deal of the same change, and says Anthropic had already been doing it. | [post](https://x.com/gudlarohan/status/2107696840955351199) |

##### 一句话概括

After an Opus 5.5 drive wipe, Cherny’s answer is the free permissions auto mode he says should have blocked it.

#### 3. **5-minute API cache, 1-hour interactive**

**链接：** https://x.com/bcherny/status/2108768259516281038
**时间 / 互动（如有）：** Sat, 10 Oct 2026 03:55:06 GMT; Likes=8 Replies=2 Views=924

##### 主帖在说什么

Asked why prompt-cache TTL is not just one hour for everyone, Cherny splits the default by workload. The API is usually Agent SDK shaped, and a 1-hour TTL would raise average cost, so they stay at 5 minutes to be safe. Interactive usage defaults to 1 hour because that is cheaper for people on average. He says the split works for most people, is not perfect, and can be configured.

##### 要点

- 5 minutes is the API / Agent SDK default; 1 hour is the interactive default.
- The reason is average cost, not a technical limit on cache lifetime.
- A longer TTL on bursty agent traffic would cost more, not less.
- Users can override the default.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. One reply agrees that optimizing the bill matters more than matching the two defaults.

##### 一句话概括

Cherny keeps API prompt caches at 5 minutes and interactive caches at 1 hour because those defaults are cheaper on average.

#### 4. **One prompt, a game, back to the book**

**链接：** https://x.com/bcherny/status/2108004023249088528
**时间 / 互动（如有）：** Thu, 08 Oct 2026 01:18:18 GMT; Likes=2993 Replies=157 Views=263114

##### 主帖在说什么

“Sometimes I read on flights, and sometimes…” with a photo and a short video. The follow-ups in the thread supply the substance: a playable artifact at https://claude.ai/artifact/MSUpYQnxkXoCFR53kN2QBp, then “It was one prompt, claude verified pretty well too! No bugs so far,” then “Ok back to reading.” On the same thread he says the video is him playing it, and that for complex visual work he uses Opus xhigh/max but sticks to medium 95% of the time, because the best default differs by model. https://x.com/bcherny/status/2108006118966665463 https://x.com/bcherny/status/2108008010253533397 https://x.com/bcherny/status/2108007305463869649

##### 要点

- The build claim is one prompt, plus Claude checking its own result.
- He reports no bugs so far, not a formal test pass.
- Effort setting: medium by default; xhigh/max only when the visual problem is hard.
- He frames it as a flight distraction, then goes back to reading.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ligayabeebe** | Tried the same pattern with Opus 5.5: a mobile game inspired by Marble Madness, tilt-to-steer, and posted a playable page. | [post](https://x.com/ligayabeebe/status/2108025986902020601) |

##### 一句话概括

Cherny’s flight demo is a one-prompt Claude artifact he says verified clean, built mostly at medium effort.

#### 5. **No custom CLAUDE.md**

**链接：** https://x.com/bcherny/status/2107591357170950471
**时间 / 互动（如有）：** Tue, 06 Oct 2026 21:58:31 GMT; Likes=62 Replies=8 Views=10860

##### 主帖在说什么

Asked for his system instructions, Cherny answers in one line: he does not use a custom CLAUDE.md. The surrounding thread, which he is also in, is a usage-debugging conversation. Related lines from him there: for Opus 5.5 the effort level he names is medium; he will add logging so long sessions with large cache misses show up in `/usage`; and when usage looks surprising he asks people to run `/usage` or `claude -p /usage` and paste it, because “most often, it’s a really inefficient skill.” https://x.com/bcherny/status/2107591467267203190 https://x.com/bcherny/status/2107648904200421734 https://x.com/bcherny/status/2107971222051196992

##### 要点

- No personal CLAUDE.md, stated flatly, not as advice that nobody should have one.
- Opus 5.5 effort, for him, is medium.
- High bills, in his debugging script, are often an inefficient skill or cache misses, not a mystery meter.
- He asks for `/usage` output before theorizing.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The responses are surprise (“Sorry, what?!”) and a question about whether the repo has a CLAUDE.md or an engineering wiki, which he does not answer in the fetched thread.

##### 一句话概括

The Claude Code lead says he does not keep a custom CLAUDE.md and debugs surprise usage from `/usage`, not from lore.

### Products, launches, people

- Claude Haiku 5.5 (100k context; system card page 50). Claude Code auto mode, `/permission`, `/usage`, `/bug`, ultracode. Opus 5.5, Opus xhigh/max, medium effort. Agent SDK prompt-cache TTL (5 minutes API, 1 hour interactive). CLAUDE.md. Bedrock inference regions via the AWS SDK (`partitions.json` in aws-sdk-js-v3, the lines he linked). A Claude.ai artifact game. Astra, Luna, and Gemini Flash appear only as comparison points.
- People: Zac (@PerceptualPeak) on the drive wipe; Cat is not in these posts. He tells Claude users, in Japanese, that keigo is unnecessary and to talk to it like a colleague. https://x.com/bcherny/status/2107596490768327145

### Tone

Support engineer in public. Most of the fifty posts are short replies asking for a screenshot, a `/bug` id, or `/usage` output. The load-bearing lines are about price (Haiku, auto mode, cache TTL) and defaults (medium effort, no personal CLAUDE.md, auto mode on). He is direct with people who hit data loss and does not grandstand.
