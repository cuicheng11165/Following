# Simon Willison (@simonw)

| Field | Value |
|-------|-------|
| Profile | https://x.com/simonw |
| Bio | Creator @datasetteproj, co-creator Django. PSF board. Hangs out with @natbat. He/Him. Mastodon: https://t.co/t0MrmnJW0K Bsky: https://t.co/OnWIyhX4CH |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 50 (cap 50: yes; oldest kept is 2026-10-03, so earlier posts in the window were not fetched)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- He built a blog feature entirely by voice with Codex Desktop while cooking, and wrote it up. He still will not let a model write for him; he uses it for proofreading and as a thesaurus.
- He is shopping for an open-weight mixture-of-experts coding model under 60GB of RAM that beats 12 tokens per second, and he currently likes Qwen3.5-35B-A3B.
- He highlighted a cluster of new agent sandboxes: Microsoft MxC (processcontainer / bubblewrap / seatbelt), Microsoft Quicksand (QEMU plus an Alpine container), and AWS Strands Box.
- He published notes arguing for default hard budget caps on "pretty much everything," and separate notes on Haiku 5.5 pricing, using the pelican-on-a-bicycle drawing test. He says Haiku 5.5 is far better at that test than Haiku 4.5, which cost 10x more.
- He rejected both moral status for LLMs and the "Super Intelligence" rename, tying the latter to a Justice Department headline that swapped "Artificial Intelligence" for "Super Intelligence" between plea and sentence.
- Side experiments in the same stretch: local Qwen 3.8 27B on long addition, Opus 5.5 writing game music, Mistral Large 4 on the pelican test, and an LLM plugin for an OpenAI "Jev-clone" decision model he says is based on GPT-6 Luna.

### Opinions and takes

- "This 'Super Intelligence' thing is just so, so, so stupid." He contrasts a 6 Oct DOJ headline, "Super Intelligence-Assisted Music Streaming Fraud," with the 19 Mar plea release that still said "Artificial Intelligence." "The name we've been using since 1956 works fine for me." https://x.com/simonw/status/2108346075874734127 https://x.com/simonw/status/2108346237619732553 https://x.com/simonw/status/2108346818086240373
- "I'm with the Rabbi. I do not want my LLMs to have moral status of any sort." Follow-up: if they are conscious, "that's slavery," so "we should aim to not have them be conscious," and "consciousness in software is a bug." He also wrote, "I don't think matrix arithmetic should ever be given the same moral status as life." https://x.com/simonw/status/2108314244014096439 https://x.com/simonw/status/2108318650050789823 https://x.com/simonw/status/2108330865575276869
- "I won't let AI write for me, but I do use it for proof-reading and as a thesaurus." https://x.com/simonw/status/2108557290412597610
- On whether coding agents make a community takeover of a large project realistic: a couple of years ago staffing cost would have made it "extremely unlikely," but he wonders if a small community could now "keep it moving." https://x.com/simonw/status/2108615902308769912
- On tests: "What do you call an integration test that doesn't use mocks?" He has been calling them "automated tests" and wishes the terminology "wasn't such a mess." https://x.com/simonw/status/2108325476934775164

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **A blog feature built by voice while cooking**

**链接：** https://x.com/simonw/status/2108547065634844839
**时间 / 互动（如有）：** Fri, 09 Oct 2026 13:16:10 GMT; Likes=349 Replies=181 Views=35988

##### 主帖在说什么

Willison says he built a new feature for his blog entirely by voice, using Codex Desktop, while he was cooking dinner. The post is a pointer to the write-up at https://simonwillison.net/2026/Oct/9/built-using-my-voice/. A follow-up in the thread is only "Example prompt:" plus a screenshot the tool did not transcribe, so the prompt text itself is not in the fetch.

##### 要点

- The claim is the method: voice in, Codex Desktop, a shipped blog feature, done while cooking.
- He does not describe the feature in the post text; the detail lives on the linked page, which was not opened for this digest.
- The thread's next post is an example prompt image, not additional prose.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bhaveyx** | Bhavesh Chaudhari asked whether Willison is using AI to help write the site content. The thread fetch did not include Willison's answer. A later post of his, in the same conversation, says he will not let AI write for him and uses it for proofreading and as a thesaurus. | [post](https://x.com/bhaveyx/status/2108548747793924136) |

##### 一句话概括

He treated voice plus Codex Desktop as enough to ship a real blog feature without sitting down to type.

#### 2. **Open-weight MoE for coding under 60GB**

**链接：** https://x.com/simonw/status/2108608482442449261
**时间 / 互动（如有）：** Fri, 09 Oct 2026 17:20:12 GMT; Likes=278 Replies=121 Views=47723

##### 主帖在说什么

He asked for the best open-weight mixture-of-experts LLM for coding that fits in less than 60GB of RAM. He thinks MoE is probably required for interactive speed on the hardware he has, and he wants faster than 12 tokens per second. A minute later he named his current pick: Qwen3.5-35B-A3B, and asked what is newer and a bit stronger.

##### 要点

- Constraint: open weights, coding, under 60GB RAM.
- Speed bar: faster than 12 tokens per second.
- He thinks a dense model will not be interactive enough on his machines, so MoE is the bet.
- Current favorite he is willing to name: Qwen3.5-35B-A3B, with an explicit ask for something more recent.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@leolaporte** | Leo Laporte says he runs Qwen 3.8 Flash Next with Strata on a 24GB RTX 1090 plus 128GB of system RAM, an old gaming rig, and gets "decent smarts" at over 100 tokens per second on prose. Prefill is fast, so time to first token feels like a cloud model. The downside he names is one lane at a time. | [post](https://x.com/leolaporte/status/2108614329545453613) |

##### 一句话概括

He wants a local coding MoE that is actually interactive under 60GB, and Qwen3.5-35B-A3B is the baseline he is comparing against.

#### 3. **Microsoft MxC and the sandbox pile-up**

**链接：** https://x.com/simonw/status/2108216753604248000
**时间 / 互动（如有）：** Thu, 08 Oct 2026 15:23:37 GMT; Likes=1117 Replies=139 Views=67758

##### 主帖在说什么

Quoting GitHub's Kyle Daigle on MxC, Willison says Microsoft's new open-source sandbox library looks promising and works across Windows, macOS, and Linux, using processcontainer, bubblewrap, and seatbelt. Repo: https://github.com/microsoft/mxc. He then pointed at Quicksand, a Microsoft Python library that bundles QEMU and can run an Alpine Linux container; he says he has tried it on macOS, Windows, and Linux. https://github.com/microsoft/quicksand. He also quote-posted AWS's Marc Brooker on Strands Box and wrote, "must be something in the air."

##### 要点

- MxC is the post: cross-platform, open source, three different OS sandbox primitives underneath.
- Quicksand is the related Microsoft project he has personally run on all three desktop OSes.
- He groups AWS Strands Box with them as the same week's pattern, not as a review of Strands itself.
- He does not claim to have audited MxC; "looks very promising" is the strength of the claim.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@olshansky** | Daniel Olshansky, who says he is an FDE at OpenAI, calls Windows sandboxing one of the hardest challenges in that work so far. He says the Codex team is already on it and links `openai/codex` `codex-rs/mxc-sandbox`. | [post](https://x.com/olshansky/status/2108241268094763356) |

##### 一句话概括

He flagged MxC as the practical cross-platform agent sandbox, and noted Microsoft and AWS shipping sandboxes in the same week.

#### 4. **Haiku 5.5 pelicans and the 10x price drop**

**链接：** https://x.com/simonw/status/2107938675405586713
**时间 / 互动（如有）：** Wed, 07 Oct 2026 20:58:38 GMT; Likes=245 Replies=92 Views=35119

##### 主帖在说什么

He pointed at a blog post of pelican drawings plus pricing notes on Claude Haiku 5.5: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/. The follow-up is the comparison he wants remembered: Haiku 5.5 is "SO MUCH better" at drawing pelicans riding bicycles than Claude Haiku 4.5, which he says was released almost a year ago and cost 10x more. The Haiku 4.5 attempt is an image the tool did not describe.

##### 要点

- The post is a pricing-and-quality note, not a launch of his own.
- Quality proxy: the pelican-on-a-bicycle SVG test.
- Price claim in the tweet: Haiku 4.5 cost 10x what Haiku 5.5 costs, and the new small model draws that scene much better.
- The blog URL is where the pricing notes live; this digest does not add numbers that were not in the posts.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@funcOfJoe** | Joe Duffy, founder of Pulumi, wonders whether pelicans on bicycles are now too in-distribution to be a useful test, and suggests switching to walruses playing bagpipes. | [post](https://x.com/funcOfJoe/status/2108275071538418152) |

##### 一句话概括

His Haiku 5.5 take is that the cheap small model finally clears a silly drawing test the previous Haiku missed, at a tenth of the price.

#### 5. **Default hard budget caps**

**链接：** https://x.com/simonw/status/2106528704902164855
**时间 / 互动（如有）：** Sat, 03 Oct 2026 23:35:55 GMT; Likes=919 Replies=256 Views=122060

##### 主帖在说什么

He published an argument that default hard budget caps are going to be needed on pretty much everything: https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/. The post itself does not restate the essay. The claim in the tweet is the prescription: hard caps should be the default, not an advanced setting.

##### 要点

- The recommendation is universal defaults, not a single vendor feature.
- "Hard" is doing the work: a cap that actually stops spend, not a warning.
- He sends readers to the essay rather than arguing the mechanism in the post.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@biilmann** | Matt Biilmann, CEO of Netlify, says a hard cap was one reason Netlify switched to credit-based pricing a year ago. | [post](https://x.com/biilmann/status/2106550759458533513) |
| **@full_kelly_** | A practical stand-in: virtual cards with no credit line and a usage limit around $1. | [post](https://x.com/full_kelly_/status/2106605112571695442) |
| **@ExiledonMoon** | Restates the piece as an allowance: "We taught the computer to think. Now we have to give it an allowance." | [post](https://x.com/ExiledonMoon/status/2106544659128594488) |

##### 一句话概括

He wants spend limits to be the default on agent and API products, and readers answered with credits and prepaid cards.

### Products, launches, people

- His own: the voice-built blog feature, the Haiku 5.5 pelican/pricing note, the hard-budget-caps essay, an LLM plugin for what he calls OpenAI's Jev-clone decision model based on GPT-6 Luna (https://simonwillison.net/2026/Oct/6/llm-openai-decisions/), a local Qwen 3.8 27B addition experiment, and a scrimshaw jukebox page for Opus 5.5 music.
- Models and tools he names: Codex Desktop, Qwen3.5-35B-A3B, Qwen 3.8 Flash Next, Strata, Qwen 3.8 27B, Claude Haiku 5.5, Claude Haiku 4.5, Opus 5.5, Opus 4.5, Mistral Large 4 ("Le Chonk"), GPT-6 Luna, Dot, ChatGPT, Microsoft MxC, Microsoft Quicksand, AWS Strands Box.
- People in the threads: Kyle Daigle, Marc Brooker, Leo Laporte, Joe Duffy, Matt Biilmann, Daniel Olshansky, Miguel de Icaza.

### Tone

Practical and slightly exasperated. He ships small write-ups, names the tool and the number, and uses jokes (pelicans, "Super Intelligence") to mark where a vendor claim has gotten sloppy. He is explicit that models are instruments, not authors and not moral patients.
