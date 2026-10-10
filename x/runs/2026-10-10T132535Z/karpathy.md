# Andrej Karpathy (@karpathy)

| Field | Value |
|-------|-------|
| Profile | https://x.com/karpathy |
| Bio | not fetched |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 14 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- The work around language models is shifting from generation to oversight: as models do more of the legwork, people should ask for discardable artifacts (diagrams, HTML, explainer videos) instead of walls of text. https://x.com/karpathy/status/2105819303471976479
- A text-only “Land or Water?” probe (16,200 lat/long queries, plotted as an image) shows models have compressed a map of the earth from internet text, with no images in the training signal beyond how text is arranged. https://x.com/karpathy/status/2105909609487872075
- Most people now paying attention to AI were onboarded in under a year, which he says confuses anyone who was in the field before 2026, and especially before 2012. https://x.com/karpathy/status/2106806571321966793
- He reads TypeSafe’s Jev as a neglected point on the LLM Pareto curve: no thinking, single token, low latency, “acceptable intelligence,” under-built because the field raced toward higher intelligence. https://x.com/karpathy/status/2102124533729955960
- Looking back at a 2015 RNN experiment that generated Linux source, he wishes he had trained on StackOverflow, which he thinks would have made promptable general Q&A obvious sooner. https://x.com/karpathy/status/2098828290152944093
- Shorter takes: dropping “Artificial” from AGI/ASI is just cleaner terminology he says the field has used for a decade; image-to-playable-world (“image → GTA”) ideas, including a 1906 San Francisco clip; large software projects as invisible “digital megastructures”; and a note that the only journalist he consistently replied to as a PhD student was someone who read the papers. https://x.com/karpathy/status/2103528977583546678 https://x.com/karpathy/status/2102484651072016848 https://x.com/karpathy/status/2098777547265950015 https://x.com/karpathy/status/2108727132918841657

### Opinions and takes

- “As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of our work will rise up the abstractions into oversight and understanding.” https://x.com/karpathy/status/2105819303471976479
- On the lat/long map: “The models know. From compressing the internet.” He later stressed there are “no images involved except the way you arrange the text responses in 2D.” https://x.com/karpathy/status/2105909609487872075 https://x.com/karpathy/status/2105912048668590090
- “99%+ of people who are now paying attention have been onboarded to anything related to AI in <1 year.” Pre-2026 people are “AI dinosaurs”; pre-2012 is the “gasp” case. https://x.com/karpathy/status/2106806571321966793
- Jev sits in “a regime that had a large revealed latent demand (no thinking, single token, low latency acceptable intelligence).” https://x.com/karpathy/status/2102124533729955960
- “If only I had thought to train it on StackOverflow instead I think it would have clicked for me that LLMs can be promptable, general purpose Q&A engines.” https://x.com/karpathy/status/2098828290152944093
- AGI leading to ASI is “~standard terminology”; drop “Artificial” because it is “redundant, cleaner.” https://x.com/karpathy/status/2103528977583546678

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Understanding model output: text, diagrams, HTML, video**

**链接：** https://x.com/karpathy/status/2105819303471976479
**时间 / 互动（如有）：** Fri, 02 Oct 2026 00:37:00 GMT; Likes=54941 Replies=1601 Views=7714333

##### 主帖在说什么

Karpathy argues that as language models take on more of the work, humans will spend more time trying to understand what they produced. He ranks output formats. Plain prose can be improved by asking for ASD-STE100, a controlled language spec from aerospace maintenance docs; he sometimes asks for “80% of the way to ASD-STE100” because the full spec is strict. He prefers diagrams over writing, then HTML pages (interactive, animated frontends), and is most bullish on fully custom explainer videos. A prompt he suggests is a “3b1b style” video that uses an ElevenLabs API key for narration, or a local free alternative. The close is that abundant intelligence and code make large, discardable artifacts (web apps, video explainers) rational to request.

##### 要点

- Oversight and understanding rise as models do more of the legwork themselves.
- ASD-STE100 is a practical writing constraint he has had success with; soften to ~80% when the spec is too stringent.
- Diagrams are easier to parse than prose; HTML is better still because models are “really good at frontend.”
- Custom explainer video is the format he is “most bullish on,” and he says it is “actually starting to work.”
- Ask for artifacts that would never have been worth building when code was scarce.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@bondsnbourbon** | Followed the suggestion and generated a 3b1b-style explainer on stochastic calculus, and said it recalled a first encounter with the topic in professional education. | [post](https://x.com/bondsnbourbon/status/2105892170263650792) |
| **@Grady_Booch** | Quotes the diagrams line and points at UML as the existing practice for making structure easier to parse than prose. | [post](https://x.com/Grady_Booch/status/2105864893887082857) |

##### 一句话概括

Karpathy wants people to stop reading raw model text and instead demand diagrams, web pages, and bespoke explainer videos.

#### 2. **“Land or Water?” shows models know the map**

**链接：** https://x.com/karpathy/status/2105909609487872075
**时间 / 互动（如有）：** Fri, 02 Oct 2026 06:35:51 GMT; Likes=18677 Replies=646 Views=1320501

##### 主帖在说什么

Quoting Celeste’s “results for all claudes” plot, Karpathy calls the eval cool: ask an LLM “Land or Water?” plus a latitude and longitude, as text, 16,200 times, and plot the answers as an image. The models know the geography. He attributes that to compressing the internet. In a follow-up on the same thread he stresses the result comes only from reading and predicting text; no images are involved except arranging the text answers in 2D. https://x.com/karpathy/status/2105912048668590090

##### 要点

- The probe is text in, binary land/water out, rasterized into a map.
- 16,200 coordinate queries are enough to see coastlines.
- His explanation is compression of internet text, not a vision model.
- He separately underlines that the 2D picture is just how you lay out text responses.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@Acezhang01** | Always answering “water” scores about 70% because most of the planet is ocean, so Sonnet 4.5 at 60% is worse than never guessing land; 90%+ is where the map is actually known. | [post](https://x.com/Acezhang01/status/2105916183744790760) |
| **@paul_cal** | Points at an earlier Jev run of a related globe/continent probe and says Jev’s grasp looks on par with some of the best models a year ago; “I love this eval.” | [post](https://x.com/paul_cal/status/2105916964228993315) |

##### 一句话概括

A dumb lat/long quiz, plotted, is Karpathy’s evidence that text-only training already stored a world map.

#### 3. **Newcomers vs “AI dinosaurs”**

**链接：** https://x.com/karpathy/status/2106806571321966793
**时间 / 互动（如有）：** Sun, 04 Oct 2026 18:00:03 GMT; Likes=2798 Replies=126 Views=197267

##### 主帖在说什么

This is a reply to Elvis (@omarsar0), who had said the output-format tips in Karpathy’s big post were things practitioners had been doing for over a year, then argued for a universal human–agent interface built from Notion-like pages, artifacts, and on-the-fly UI. Karpathy’s mental model for the pile-on is cohort, not novelty: 99%+ of people now paying attention were onboarded to AI in less than a year. That is confusing to “AI dinosaurs,” meaning anyone in AI before 2026, or “gasp,” before 2012.

##### 要点

- He frames the reaction to familiar advice as a new-audience effect, not a claim that the tips are new to researchers.
- “Paying attention” is the group he is talking about, not the set of people who already build with models.
- Pre-2026 is already “dinosaur”; pre-2012 is the sharper cut.
- He does not dispute Elvis’s interface experiments; he explains why the post traveled.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sagivo** | The newcomers are not the confused ones; the dinosaurs are, because they remember when none of this worked. | [post](https://x.com/sagivo/status/2106808497488756794) |
| **@omarsar0** | Agrees, thanks him for sharing experiments anyway, and says useful discussion gets lost under “hateful replies” and cheap jabs. | [post](https://x.com/omarsar0/status/2106811289796239384) |

##### 一句话概括

Karpathy thinks the audience explosion, not the ideas, is what makes old AI advice feel new.

#### 4. **Jev on the low-latency Pareto curve**

**链接：** https://x.com/karpathy/status/2102124533729955960
**时间 / 互动（如有）：** Mon, 21 Sep 2026 19:55:19 GMT; Likes=3288 Replies=139 Views=259999

##### 主帖在说什么

Replying to Will Depue, who called Jev a zero-shot classifier with “frontier-ish intelligence” and wondered why nobody had built it sooner, Karpathy places Jev on the LLM Pareto frontier in a regime with revealed demand: no thinking, single token, low latency, acceptable intelligence. He says that regime was under-invested because the industry was racing toward higher intelligence.

##### 要点

- Jev is not “just a small model” in his framing; it is a point the capability race skipped.
- The demanded properties are explicit: no chain-of-thought, one token, low latency.
- “Acceptable intelligence” is enough when latency and cost dominate.
- Latent demand showed up once someone shipped that point.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@CompleteSkeptic** | Calls the take pretraining-centric. The real question is how you trade intelligence for a use case, including the conflict between RLHF and RLVR “even in string land.” He is CEO of TypeSafe, the lab behind Jev. | [post](https://x.com/CompleteSkeptic/status/2102132467146829922) |
| **@paraschopra** | Startups are about choosing tradeoffs; a field blasting toward full automation and high intelligence leaves openings. | [post](https://x.com/paraschopra/status/2102276500431188025) |

##### 一句话概括

Karpathy treats Jev as proof that the fast, shallow, single-token corner of the LLM curve was under-built.

#### 5. **StackOverflow, not Linux source, would have clicked**

**链接：** https://x.com/karpathy/status/2098828290152944093
**时间 / 互动（如有）：** Sat, 12 Sep 2026 17:37:13 GMT; Likes=3379 Replies=90 Views=129088

##### 主帖在说什么

Someone posted that they were reading Karpathy’s 2015 blog on RNNs and an experiment generating Linux source code. Karpathy replies that if he had trained that model on StackOverflow instead, it would have clicked for him that the same systems could be promptable, general-purpose Q&A engines. The closer is “Ah well.”

##### 要点

- The 2015 setup he is reacting to was code generation (Linux source), not question answering.
- He treats StackOverflow-style text as the dataset that would have made “promptable Q&A” obvious.
- He is describing a missed conceptual step, not announcing a new training run.
- The tone is retrospective, not a claim about today’s models.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies. The visible replies are jokes about a missed career and “Open Andrej” subscriptions, not technical disagreement.

##### 一句话概括

Karpathy thinks a 2015 StackOverflow run, not Linux source, would have shown him that LLMs are general Q&A engines.

### Products, launches, people

- ASD-STE100, ElevenLabs, 3Blue1Brown-style (“3b1b”) explainers.
- Jev / TypeSafe (Will Depue’s thread; Diogo Almeida / @CompleteSkeptic replies). Celeste’s Claude land/water chart. Sonnet 4.5 is named only in a reply, as a baseline.
- People: Jack (unnamed further; the journalist who read papers), Grady Booch, Elvis (@omarsar0).
- No product launch of his own in this window. “So ready to do my part in pacing the frontier” is a one-line reply without a named project. https://x.com/karpathy/status/2102063518979969034

### Tone

Reflective and teacherly. The highest-reach post is a practical stack of output formats, not a model release. He is comfortable being the “dinosaur” who explains why a new audience is surprised, and he credits compression and neglected Pareto points rather than new architectures.
