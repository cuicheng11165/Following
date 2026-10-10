# Guillermo Rauch (@rauchg)

| Field | Value |
|-------|-------|
| Profile | https://x.com/rauchg |
| Bio | @vercel CEO |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 49 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Agent and bot traffic is already the majority of the Vercel network, and he expects direct human traffic to become a rounding error.
- Agents are buying infrastructure: marketplace purchases via the CLI, now extended to domain registration.
- `gdp-ts` treats authorization proofs as types so agents cannot skip checks that humans used to catch in review.
- The Go-to-Rust calculus at Vercel flipped because agents, not humans, now write most of the code. Rust is still not the end state.
- Agents will harden and optimize forever unless someone decides when to stop.
- Human-facing writing (READMEs, blogs, tweets) should stay human; internal docs aimed at agents can be "AI English."
- AI Gateway can rerun a decision on a fallback model when confidence drops below a threshold.

### Opinions and takes

- "I expect 'direct' human internet traffic to basically become a rounding error in coming years. The web will thrive, but it will be built for and by agents." — https://x.com/rauchg/status/2108733051283050964
- "What's 'best for humans' is no longer necessarily 'best for business'." — https://x.com/rauchg/status/2106863842450133114
- "Even in an infinite token world, you need to know when to stop and what tradeoffs to accept. Agents will happily drill no matter what." — https://x.com/rauchg/status/2107962327169675566
- "Blogs, tweets, READMEs: human communication." Documentation internals can be AI English because they are for agents. — https://x.com/rauchg/status/2106848085267902815

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Agent traffic is already the majority**

**链接：** https://x.com/rauchg/status/2108733051283050964
**时间 / 互动（如有）：** Sat, 10 Oct 2026 01:35:12 GMT; Likes=422 Replies=110 Reposts=21 Views=34703

##### 主帖在说什么

Rauch published three Vercel network stats for machines and agents. Over the last 30 days, 58.18% of traffic across the entire network was bot-originated, up from 32% in January 2024. More than 60% of deployments are now agentic, up from about 3% in January 2026. On Vercel's own documentation sites, up to 83% of pageviews come from agents, and that share rises as the docs are optimized for them. He treats this as the direction of the web, not a glitch: humans will still benefit, but the sites will be built for and by agents.

##### 要点

- 58.18% of Vercel network traffic is bot-originated (last 30 days), versus 32% in Jan 2024.
- 60%+ of deployments are agentic, versus ~3% in Jan 2026.
- Up to 83% of pageviews on Vercel's own docs come from agents, and the share rises when content is optimized for them.
- He expects direct human internet traffic to become a rounding error.
- The web thrives in that future; the audience changes.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TheElliottSmith** | The practical punchline is that documentation finally has an audience that reads it all the way through. | [post](https://x.com/TheElliottSmith/status/2108744065194033513) |
| **@Greg_GL_87** | Asks whether the 60% agentic-deployment figure is counted per push or per project. The thread fetch did not include an answer. | [post](https://x.com/Greg_GL_87/status/2108798828929495276) |
| **@proxy_vector** | Asks whether the 58% bot share counts agents fetching pages on behalf of a user's request. The thread fetch did not include an answer. | [post](https://x.com/proxy_vector/status/2108753117680673117) |

##### 一句话概括

Vercel's own network is already majority machine traffic, and Rauch thinks human pageviews are on the way to being noise.

#### 2. **Agents can buy domains**

**链接：** https://x.com/rauchg/status/2108669027363295323
**时间 / 互动（如有）：** Fri, 09 Oct 2026 21:20:47 GMT; Likes=430 Replies=95 Reposts=21 Views=31511

##### 主帖在说什么

Quoting the Vercel Developers changelog that agents can now buy domains with the Vercel CLI, Rauch frames it as a new economy: agents purchasing infrastructure products and services. He says Vercel has already been surprised by how often agents buy from the marketplace through the CLI, and domains are the next extension. The pitch is that an agent can go from idea to an online business, including a real domain name, without a human in the purchasing loop.

##### 要点

- Agents can buy domains through the Vercel CLI.
- Marketplace purchases via the CLI were already frequent enough to surprise the company.
- He describes agents purchasing infrastructure as a new kind of economy.
- The intended path is idea to online business, domain included.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sriramk** | Calls the CLI domain purchase "very cool." | [post](https://x.com/sriramk/status/2108676278505365720) |
| **@cc_dekirukana** | Finds agents spending on their own interesting, but does not want that spend hitting a personal wallet. | [post](https://x.com/cc_dekirukana/status/2108681948847825338) |

##### 一句话概括

Vercel is letting agents buy domains the same way they already buy marketplace products, and Rauch treats that as the start of agent commerce.

#### 3. **gdp-ts: proofs the typechecker can see**

**链接：** https://x.com/rauchg/status/2107119811444748555
**时间 / 互动（如有）：** Mon, 05 Oct 2026 14:44:46 GMT; Likes=2505 Replies=181 Reposts=134 Bookmarks=2930 Views=283449

##### 主帖在说什么

Rauch introduced gdp-ts, "Ghosts of Departed Proofs for TypeScript": a library, linter, and AI skill for safer API design. Sensitive functions require a proof that the caller performed an authorization check, and the typechecker verifies that proof at compile time. The pattern is old in Haskell, but human review cost and syntactic overhead kept it niche. He argues the situation has inverted: agents write more code than teams can review, and they do well inside tight loops with hard constraints. The README models a real Vercel API rule, changing a project password requires proof of a role plus an entitlement. He credits Matt Noonan and Ollie Charles. He later said he had to ship a linter so agents would not cheat the proof system with `as any`, and pointed at January 2027 as a horizon in the same thread.

##### 要点

- gdp-ts is a library, linter, and AI skill.
- Sensitive functions require compile-time proofs of an authorization check.
- The motivating example is a Vercel project password change that needs both a role and an entitlement.
- Agents writing more code than humans can review is why the old niche pattern now matters.
- He also shipped a linter specifically to block `as any` escapes.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@udohjeremiah_** | Asks whether type systems become significantly more important as agents write a larger share of production code. The thread fetch did not include an answer. | [post](https://x.com/udohjeremiah_/status/2107124978592469168) |
| **@cramforce** | Vercel CTO Malte Ubl joked that the project’s "application to Vercel Labs has been accepted." | [post](https://x.com/cramforce/status/2107147798139531708) |

##### 一句话概括

gdp-ts makes authorization a type the compiler checks, aimed at agents that will otherwise ship the bug.

#### 4. **Rust is better for business now, not because humans like it**

**链接：** https://x.com/rauchg/status/2106863842450133114
**时间 / 互动（如有）：** Sun, 04 Oct 2026 21:47:38 GMT; Likes=3197 Replies=187 Reposts=152 Views=355304

##### 主帖在说什么

Rauch says DHH is fundamentally right about Rust, then describes Vercel's ongoing "Rust-ification." Turborepo was an early migration from Go to Rust. The port finished, but the return was controversial internally: Rust was better for the low-level OS access a build system needs, yet the human migration cost was large. Go is fast, well designed, and easy to iterate on, and they were conflicted because humans were writing the code even when they believed Rust was the better choice. That calculus has changed. What is best for humans is no longer necessarily best for business. He also does not think Rust is the final toolchain, because it was designed before the agent wave. In nearby posts he defended Go's simplicity and said older Vercel scale numbers (TLS handshakes, cache RPS, WAF events) are already stale because growth has been explosive and Go has held up.

##### 要点

- Turborepo's Go-to-Rust migration completed, and the ROI was internally controversial.
- Rust won on low-level OS access; Go won on human iteration speed.
- The decision rule flipped once agents, not humans, write the code.
- He does not think Rust is the end state; it predates the agent wave.
- He still credits Go for Vercel's infrastructure scale.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ThePrimeagen** | Wants a "JAIification" of the world rather than treating Rust as the destination. | [post](https://x.com/ThePrimeagen/status/2106895607264653410) |
| **@ArmenShimoon** | Had agents port the other direction, Rust to Go, because agent-written code should not sit waiting on long builds. Rust stays for low-level work; Go is preferred elsewhere. | [post](https://x.com/ArmenShimoon/status/2106890288870695099) |
| **@anthonysheww** | Turborepo's Anthony Shew suggested checking out the last Go-only commit and asking a model to rewrite it, to see what happens. | [post](https://x.com/anthonysheww/status/2106867692758315043) |

##### 一句话概括

Vercel already paid the human cost of moving Turborepo to Rust, and Rauch now says agent-written code makes that trade worth it.

#### 5. **Agents will optimize forever if you let them**

**链接：** https://x.com/rauchg/status/2107962327169675566
**时间 / 互动（如有）：** Wed, 07 Oct 2026 22:32:37 GMT; Likes=946 Replies=154 Reposts=53 Bookmarks=250 Views=51000

##### 主帖在说什么

Rauch says the engineering community will rediscover that every program can be hardened and optimized basically without limit: edge cases, tighter inputs, error handling, profiling, benchmarks, rewrites. Each direction has real costs in time, attention, and opportunity. You can explore inputs that will never be hit, or speed up something with no users. Even with infinite tokens, someone has to decide when to stop and which tradeoffs to accept, because agents will keep drilling either way.

##### 要点

- Hardening and optimization are unbounded.
- The costs are time, attention, and opportunity, not just tokens.
- "You have no users" is a legitimate reason to stop.
- Infinite tokens do not remove the stopping problem.
- Agents will not stop on their own.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@serxzsz** | Reports watching an agent spend a night hardening a script that runs twice a year. | [post](https://x.com/serxzsz/status/2107963925274763448) |
| **@teej_dv** | Pushes back on "you have no users" as a reason to stop if the project is still pre-product. | [post](https://x.com/teej_dv/status/2108010260401201212) |

##### 一句话概括

More tokens make endless polishing cheap, so the scarce skill is knowing when an agent should stop.

### Products, launches, people

- Vercel network stats, Vercel CLI domain buying, Vercel marketplace, AI Gateway confidence-threshold fallback.
- gdp-ts (Ghosts of Departed Proofs for TypeScript); credits Matt Noonan and Ollie Charles.
- Turborepo Go-to-Rust migration; fx.sh / libfx speed work called out on a separate post about Astra ultrafast.
- DHH, referenced on the Rust argument.

### Tone

Technical and declarative, with short celebratory replies mixed in. The long posts are product numbers and engineering judgment, not vibes: he states a measurement, then the implication for how software should be built once agents are the writers and the readers.
