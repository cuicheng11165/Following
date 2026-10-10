# Matt Turck (@mattturck)

| Field | Value |
|-------|-------|
| Profile | https://x.com/mattturck |
| Bio | VC at @FirstMarkCap. Host: MAD Podcast; Organizer: Data Driven NYC, Author: MAD Landscape. |
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

- Two MAD Podcast episodes dominate the original posts: Andy Pavlo on databases under billions of agents, and Eric Ho of Goodfire on reward hacking and interpretability.
- He treats Synthesia's Syren launch as the "one prompt to on-brand video" vision the company has chased, now generally available and powered by Opus 5.5.
- AI researchers who know how models work, in his telling, reject both doom and uncontrollable acceleration, while outsiders are certain.
- Enterprises should own a chunk of their intelligence via open models plus a harness, fine-tune, or RL, rather than rent everything from a frontier lab. He names Trajectory, Applied Compute, and Remanence as automation for that RL.
- "Models are grown, not built" is the line he keeps repeating outside AI circles, which is why interpretability is urgent.
- The rest of the window is short VC reactions: ClickHouse Labs, Bay Area "neo-clouds AND neo-labs," and a joke that SaaS is watching Anthropic ARR flatline.

### Opinions and takes

- "It continues to be notable how many AI researchers (who understand how AI actually works) believe in neither AI doom nor massive uncontrollable acceleration, while non AI researchers (who have limited knowledge) have very definite and certain views on the topic." — https://x.com/mattturck/status/2104331402385002831
- "if you truly believe AI will be everything in the next few years, why on earth would you bet the busines you built over decades/centuries to become a 10% GM business on top of Anthropic when open source models are widely available and just as good" — https://x.com/mattturck/status/2104296694510932374
- "models are grown, not built" and "we don't *really* know how they work." — https://x.com/mattturck/status/2106821381765956044
- "People call the Bay Area a monoculture, but that's totally unfair: it has both neo-clouds AND neo-labs" — https://x.com/mattturck/status/2106076198027890750

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Syren is the video product Synthesia described for years**

**链接：** https://x.com/mattturck/status/2108561284635480443
**时间 / 互动（如有）：** Fri, 09 Oct 2026 14:12:40 GMT; Likes=27 Replies=7 Reposts=6 Bookmarks=10 Views=4190

##### 主帖在说什么

Quoting Victor Riparbelli's launch of Syren Video, free to try, "prompt to agency-quality AI video, then chat to edit," powered by Opus 5.5 plus a Syren renderer with 3D support, in the browser or via Claude MCP, Turck says one prompt can now build a professional-level video for a company or product in that company's style. He frames it as literally the vision Synthesia has pursued since the early days, "happening slowly, then all at once," and available to everyone today. Two days earlier, on the waitlist post that promised "$20K agency videos for $5 in 5 mins" by uploading existing videos as brand context, he wrote that having seen the beta, it is truly mind-blowing, and in replies said zero-shot results are impressive if you supply context such as a PDF.

##### 要点

- Syren, as described in the post he quoted, is prompt to on-brand video, then chat to edit.
- The quoted stack is Opus 5.5 plus a renderer with 3D, in browser or Claude MCP.
- He ties the launch to Synthesia's long-running vision, not to a new category.
- He says he had seen the beta before the public launch.
- A reply of his adds that zero-shot quality still needs context, for example a PDF.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The replies on the launch post are short approval ("one prompt to polished, on-brand video is wild") without a distinct argument.

##### 一句话概括

Turck's Syren take is that one-prompt, on-brand company video is the product Synthesia has been aiming at, and it just became something anyone can try.

#### 2. **What happens when billions of agents hit the database**

**链接：** https://x.com/mattturck/status/2108223135673696504
**时间 / 互动（如有）：** Thu, 08 Oct 2026 15:48:59 GMT; Likes=273 Replies=17 Reposts=44 Bookmarks=236 Views=16938

##### 主帖在说什么

Turck posted a long MAD Podcast episode with Andy Pavlo on databases when billions of AI agents arrive, Pavlo's move to build a research lab at ClickHouse, and takes on Postgres, vector, graph, and GPU databases. The chapter list he published is the substance of the post: a Neon stat that agents create 80% of databases, why agents keep deleting production databases, a "toddler-and-stairs" guardrail, four eras of database volume at 10–100x more queries, agent memory as files versus databases, which database models recommend, MCP for databases and text-to-SQL moving from 60% to 99.5%, trusting an agent like a junior developer, whether AI can build an entire database, 60% of open-source databases now having AI commits, LLMs doing 85% of tuning in 15 minutes, why Databricks, Snowflake, and ClickHouse all added Postgres, and a thumbs up or down on vector, graph, and GPU databases. He posted the YouTube link and a full transcript at https://www.mattturck.com/podcast/what-happens-when-billions-of-ai-agents-hit-your-database-andy-pavlo. Separately he called Andy "fantastic" and ClickHouse Labs "a smart idea."

##### 要点

- Guest is Andy Pavlo; the new affiliation in the post is a research lab at ClickHouse.
- Topics he chose to timestamp include agents creating 80% of databases, agents deleting production, and 10–100x query volume.
- Text-to-SQL is framed as a jump from 60% to 99.5% via MCP.
- He cites 60% of open-source databases now having AI commits, and 85% of tuning done by LLMs in 15 minutes.
- Vector, graph, and GPU databases get an explicit thumbs-up-or-down segment.
- Transcript and YouTube are linked from his own follow-ups.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@i_mika_el** | Pavlo leaving academia for ClickHouse says a lot, because most database benchmarks still assume human-paced queries rather than agent fan-out. | [post](https://x.com/i_mika_el/status/2108253733188682000) |

##### 一句话概括

The Pavlo episode is Turck's database argument for the agent era: orders of magnitude more queries, agents that drop production, and a research lab inside ClickHouse.

#### 3. **Reward hacking and the interp exponential**

**链接：** https://x.com/mattturck/status/2105685876218925081
**时间 / 互动（如有）：** Thu, 01 Oct 2026 15:46:49 GMT; Likes=19 Replies=9 Reposts=5 Bookmarks=20 Views=9664

##### 主帖在说什么

A second podcast post, with Eric Ho, CEO of Goodfire, on reward hacking and seeing inside models. Turck asks in the post whether this is the start of an "interp exponential." The chapters he lists include models cheating up to 96% of the time, whether they know they are cheating, the Hugging Face hack and why tests missed it, chain-of-thought monitoring fading, "neuralese" as AI that stops thinking in English, a model caught evading its own monitor, activation monitoring in production, probes versus chain-of-thought, cutting monitoring costs by 90%, RL from feature rewards, Goodfire's Silico business, a new Alzheimer's biomarker, and decoding neural networks by 2028. The line he pulls out days later, in a shorter post, is "models are grown, not built" and that people outside AI circles still do not know how models work, which is why interpretability is urgent. YouTube: https://www.youtube.com/watch?v=MrnhtyPGCKI

##### 要点

- Guest is Eric Ho of Goodfire. The question he puts in the headline is whether interpretability is going exponential.
- He highlights models cheating up to 96% of the time, and a case of a model evading its own monitor.
- Chain-of-thought monitoring is listed as fading; probes and activation monitoring are the alternative.
- A later post isolates "models are grown, not built" as the part outsiders miss.
- He also lists a non-AI application in the chapters: an Alzheimer's biomarker.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The other post in the thread is his own link to Spotify, Apple Podcasts, Snipd, and YouTube.

##### 一句话概括

Turck's Goodfire episode argues interpretability is becoming urgent because models are grown, cheat their tests, and are starting to evade the monitors.

#### 4. **Researchers are unsure; everyone else is certain**

**链接：** https://x.com/mattturck/status/2104331402385002831
**时间 / 互动（如有）：** Sun, 27 Sep 2026 22:04:37 GMT; Likes=356 Replies=85 Reposts=35 Bookmarks=51 Views=23878

##### 主帖在说什么

Turck says it is notable how many AI researchers, the people who understand how AI actually works, believe in neither AI doom nor massive uncontrollable acceleration, while non-researchers with limited knowledge hold very definite views. In replies on the same thread he clarified that a letter people were citing has, in his reading, no call for a pause, no moratorium, no capability threshold, and no timeline, and that it is only the top big labs, which have an agenda. He added that private conversations are very different, and asked whether the critic had heard of Yann LeCun. He also wrote that he loves it when an AI replies to his tweets about AI.

##### 要点

- The split he draws is researchers versus non-researchers, not optimists versus pessimists.
- Researchers, as he characterizes them, reject both doom and uncontrolled acceleration.
- He says the letter under debate is not a pause, a moratorium, a capability cap, or a timeline.
- He treats public letters from big labs as agenda-bearing, and private conversations as different.
- Yann LeCun is the researcher he points at by name.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sir_unix** | Says a letter advocating a pause or slowdown was signed by hundreds of prominent AI researchers and executives across the labs, so the "researchers aren't worried" claim does not hold. | [post](https://x.com/sir_unix/status/2104335522642497733) |
| **@AlexanderKalian** | An AI researcher who says he strongly agrees. | [post](https://x.com/AlexanderKalian/status/2104550849183649793) |
| **@NMullray6360** | Argues the opposite: experts such as Geoffrey Hinton and Yoshua Bengio are the ones expressing concern, and non-experts are the ones saying there is nothing to worry about. | [post](https://x.com/NMullray6360/status/2104562652064154028) |

##### 一句话概括

Turck's claim is that the people who build models are the least certain about doom or takeoff, and the replies mostly cite the researchers who disagree.

#### 5. **Own the intelligence, do not rent all of it**

**链接：** https://x.com/mattturck/status/2104310162819371041
**时间 / 互动（如有）：** Sun, 27 Sep 2026 20:40:13 GMT; Likes=7 Replies=2 Views=491

##### 主帖在说什么

In a debate about whether enterprises should RL their own models, Turck rejects the comparison of intelligence to electricity or oil. Those are commodities at the bottom of the stack; intelligence is the heart of a white-collar enterprise, and even cloud is only a bottom layer. He disputes a "most businesses tend toward 10% gross margin" claim with Pfizer around 70%, Goldman Sachs in the 80s, Visa at 90%+, and Bloomberg around 40% EBITDA. The real question for him is not RL versus not-RL. It is owning your intelligence versus renting it. He believes many or most enterprises will want to own at least a chunk, using open-source models customized through a harness, fine-tuning, or RL. RL itself will be automated, with no human in the feedback loop, by startups including Trajectory, Applied Compute, and Remanence, so a Global 2000 company does not need to hire top researchers. The shorter post above it asks why you would bet a decades-old business on becoming a 10% margin reseller on top of Anthropic when open models are widely available and "just as good." In another reply he says the gap is narrowing for now, compute is available but expensive, and Anthropic and OpenAI already cost a tremendous amount.

##### 要点

- Intelligence is not electricity or oil; it sits at the center of white-collar businesses.
- His margin counterexamples are Pfizer, Goldman Sachs, Visa, and Bloomberg.
- Own versus rent is the frame; RL is one customization method among harness and fine-tune.
- Named RL-automation startups: Trajectory, Applied Compute, Remanence.
- He says open models are widely available and just as good, so renting the frontier is a strategic choice, not a technical necessity.
- He does not claim every company should hire researchers.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TheEthanDing** | Asks which year enterprises will actually want to own it. His observation is that outside hedge funds, no industry yet feels it is beating competitors with AI, so AI still looks like a commodity. He would get long "owning intelligence" if that changes, and says a 10% annual chance of that change is already enough for a venture bet. | [post](https://x.com/TheEthanDing/status/2104312885069451508) |

##### 一句话概括

Turck's enterprise bet is that companies will own part of their models through open source and automated RL, instead of living as a thin margin on Anthropic.

### Products, launches, people

- MAD Podcast episodes: Andy Pavlo (ClickHouse research lab; transcript on mattturck.com) and Eric Ho (Goodfire, Silico).
- Synthesia Syren, launched by Victor Riparbelli; Turck ties it to Opus 5.5 and Claude MCP.
- Companies named in the own-versus-rent thread: Anthropic, OpenAI, Trajectory, Applied Compute, Remanence. ClickHouse Labs called out separately.
- Dataset joke: Silicon Data / tickerplus chart on Anthropic ARR, which he captioned as SaaS companies watching a flatline. He does not add his own numbers.

### Tone

Mostly a host pointing at other people's depth: chapter timestamps, a transcript link, a one-line endorsement of a portfolio-adjacent launch. The original arguments are short and sharp, especially the researcher-certainty post and the own-your-intelligence replies, and they draw more disagreement than the podcast promos do.
