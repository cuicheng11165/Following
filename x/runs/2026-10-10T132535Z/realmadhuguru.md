# Madhu Guru (@realmadhuguru)

| Field | Value |
|-------|-------|
| Profile | https://x.com/realmadhuguru |
| Bio | Sr Director, AI at Meta; Prev: Google - Led Gemini, Veo, Nano Banana. |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 23 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Startup surface area, in his telling, is the whole stack once the primary user is an agent: desktop and mobile OSes, cloud infra, identity and permissions, and interfaces for humans and agents together. Enterprise agent-readiness (APIs, connectors, MCPs) was the last few years; personal agents are now forcing the same rebuild on consumer products, with e-commerce as the early example. https://x.com/realmadhuguru/status/2108236391641706813
- Evals are the product spec, not a QA step after the agent exists. For complex apps, a jobs-to-be-done spec should become an environment plus verifiable evals so the team can hill-climb the harness and the model. Part 10 of his series says to score the trajectory, not only the final answer. https://x.com/realmadhuguru/status/2107292113214091355 https://x.com/realmadhuguru/status/2098064969464217720
- Paid AI adoption is a product problem. He cites a16z's "98% of US households aren't paying" chart and says even the paying 2% use the products shallowly, because the UI is an "airplane cockpit" of connectors, permissions, model pickers, and token meters. He expects that to look different within 12 months. https://x.com/realmadhuguru/status/2106450089938157720
- He disagrees with Ben Thompson that consumers do not want agents to do things for them. The relationship is task-dependent: browsing clothes can be entertainment; hiring a roofer is misery. Latent demand is for agents that remove friction on the miserable tasks. https://x.com/realmadhuguru/status/2102777931764498536
- Enterprise AI fails, he argues, when a central team uses an incremental-software playbook, under-invests in evals, and builds a platform from outside the workflow. The fix he names is leaders who have shipped AI products, evals as a first-class artifact, and builders embedded in finance, sales, and support. https://x.com/realmadhuguru/status/2098448235048378456

### Opinions and takes

- "Your evals are your product spec." https://x.com/realmadhuguru/status/2107292113214091355
- "Open-weight models did not start the drop in price per unit of intelligence. They are a tailwind on a trend that was already underway." Drivers he lists: distillation into smaller models, infra efficiency, and competition. Pattern he names: mid-size version x matches large version x-1, same intelligence for less money. https://x.com/realmadhuguru/status/2108618266776387886
- "AI adoption is largely a product problem today." https://x.com/realmadhuguru/status/2106450089938157720
- "Consumers don’t have one relationship with “doing things”." https://x.com/realmadhuguru/status/2102777931764498536
- "Before we solve AI alignment, we have a pretty serious human alignment problem." He calls Dario Amodei's pacing essay thoughtful, says he does not agree with every point, and says the bad-faith reaction is the prior problem. Questions he wants aligned: opportunity and risks, how to measure them, and how companies, governments, and countries coordinate. https://x.com/realmadhuguru/status/2098803717432860987
- "Safety and security are * features * of your AI product and model - not guardrails that need to be imposed on you from the outside." This is a quote-post of Mark Zuckerberg on Muse, alignment, and Meta delaying the launch for safety. https://x.com/realmadhuguru/status/2100312717739667963
- Prediction: over the next 12 months, more frontier-eval talent moves toward groups like METR, out of labs, data providers, and independent groups, pulled by funding, independence from lab equity, and existential-risk concern. https://x.com/realmadhuguru/status/2098859477219037691
- Agent-product marketing is missing the mark; travel booking became the canonical demo and does not communicate value to a non-technical consumer. https://x.com/realmadhuguru/status/2102807619903824352

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Rebuild every layer for agents**

**链接：** https://x.com/realmadhuguru/status/2108236391641706813
**时间 / 互动（如有）：** Thu, 08 Oct 2026 16:41:39 GMT; Likes=549 Replies=14 Views=36739

##### 主帖在说什么

Quote-posting a Satya Nadella article link, Madhu says massive startup opportunities are hiding in plain sight because every layer of the computing stack has to be rebuilt for agents. He splits the last few years (enterprise software made agent-ready via APIs, connectors, and MCPs) from the new pressure of personal agents on consumer products, with e-commerce as the early case. The rest of the stack he lists: desktop and mobile OSes where agents are first-class users; cloud infra agents operate directly; identity, permissions, and security for thousands of agents acting for a person; interfaces for agents, humans, or both. The prompt he gives founders is to walk each layer and ask what changes when the primary user is an agent.

##### 要点

- The opportunity is infrastructure and interface, not another agent app on today's stack.
- Enterprise agent-readiness work (APIs, connectors, MCPs) is necessary and, in his view, already the recent focus.
- Personal agents extend the same problem to consumer products.
- Concrete layers: OS, cloud, identity/permissions/security, shared human-agent UI.
- He does not name a company he is starting; this is a map, posted from a Meta AI role.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@AGTPinsights** | Ties the "rebuild every layer" claim to home robotics at 1X: unlike roads, every home is different, so generalization and the infra around it are still open. | [post](https://x.com/AGTPinsights/status/2108252199222648855) |

##### 一句话概括

If the primary user is an agent, the startup map is the whole stack, not another connector.

#### 2. **Evals are the product spec**

**链接：** https://x.com/realmadhuguru/status/2107292113214091355
**时间 / 互动（如有）：** Tue, 06 Oct 2026 02:09:26 GMT; Likes=170 Replies=43 Views=7866

##### 主帖在说什么

The most common mistake, he says, is treating evals as an extra QA step once the agent is built. AI products are different: the evals are the product spec. The same day he adds a condition for complex applications: the jobs-to-be-done spec should quickly become an environment plus evals, ideally verifiable. That translation is hard for complex pre-existing systems, but it is what lets a team hill-climb the harness and the model; otherwise iteration on the agent is limited. Simpler applications worry him less. https://x.com/realmadhuguru/status/2107486363864199595

He had already published part 10 of the series on Sep 10: measure steps, not only the result. Two trajectories can both answer "42"; one makes four clean tool calls, the other makes 17, repeats searches, and recovers from errors. His checklist is to define the workflow, the task in each step, whether each step is its own eval or a slice of a larger one, and which tasks are median versus hard, then read steps before the final score. https://x.com/realmadhuguru/status/2098064969464217720

##### 要点

- Evals are not a late QA gate.
- For complex products, the spec has to become an environment and verifiable evals.
- That setup is how you hill-climb harness and model together.
- Part 10: identical answers can hide a bad trajectory.
- He points readers at the rest of the series from the enterprise-failure post.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ItsGoharr** | Evals are the product; the model is a dependency. | [post](https://x.com/ItsGoharr/status/2107347628707164219) |
| **@ivan_makarov** | Evals are the verification loop and are derivative of the spec; the spec is the input, the eval is the error signal. | [post](https://x.com/ivan_makarov/status/2107301317467336839) |
| **@iLegend_AI** | An eval is the spec only if it is versioned with the prompt; otherwise the eval drifts. Pin an eval hash per prompt version and diff failures, not scores. | [post](https://x.com/iLegend_AI/status/2107569753028219302) |

##### 一句话概括

If the eval is an afterthought, you do not have a spec, and you cannot hill-climb the agent.

#### 3. **Adoption is a cockpit problem**

**链接：** https://x.com/realmadhuguru/status/2106450089938157720
**时间 / 互动（如有）：** Sat, 03 Oct 2026 18:23:32 GMT; Likes=220 Replies=47 Views=21249

##### 主帖在说什么

Quote-posting a16z's chart that 98% of US households are not paying for AI, he says adoption is largely a product problem. Even among the 2% who pay, usage is shallow. The reason he gives is the interface: most AI products look like airplane cockpits with a hundred levers (connectors, permissions, model selection, token usage). He says this has started to change, and that the next 12 months will look materially different as product teams make AI easier to use.

##### 要点

- He accepts the 98% / 2% split from a16z as the setup, then argues depth, not just conversion, is the problem.
- The blamed surface is control density: connectors, permissions, model choice, tokens.
- The forecast is 12 months, attributed to product teams rather than a model breakthrough.
- He does not name a shipping Meta product as the fix in this post.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@RyanWink15** | A second cause: people do not know which tasks match the capability, and "PhD level" does not resonate because most people do not need that. | [post](https://x.com/RyanWink15/status/2106479188811423788) |
| **@CrabDude** | Separates AI from applied AI. Says roughly 1% of users know how to prompt because it is an untrained muscle, while applied AI will sit inside ordinary software and users may not notice. | [post](https://x.com/CrabDude/status/2106482417934696509) |
| **@rohanv_rm_** | Points at Muse and Instinct as products where people describe an outcome instead of picking a model or managing connectors. | [post](https://x.com/rohanv_rm_/status/2106534846151696798) |

##### 一句话概括

Households are not paying, and the payers are not going deep, because the product still looks like a cockpit.

#### 4. **Disagreeing with Ben Thompson on consumer agents**

**链接：** https://x.com/realmadhuguru/status/2102777931764498536
**时间 / 互动（如有）：** Wed, 23 Sep 2026 15:11:41 GMT; Likes=166 Replies=49 Views=113130

##### 主帖在说什么

TBPN clipped Ben Thompson arguing that consumer AI has a marketing problem because average consumers do not want to be more productive: flight-booking demos are absurd, shopping is entertainment, and people enjoy the friction. Madhu says he respectfully disagrees. Consumers do not have one relationship with "doing things." From Google and now Meta consumer and SMB products, he says browsing clothes can be entertainment for some people, while hiring a roofer is miserable for most. Even shopping splits: sometimes you want an hour of browsing, sometimes you want the right thing delivered. He compares Thompson's argument to early-2000s objections to buying clothes or a television online. For some tasks, better means almost zero effort; for others, more options and an informed decision. He calls latent demand for agents that remove the miserable friction immense. In a later reply to Ben he agrees the travel-booking demo has become canonical and does not communicate value to a non-technical consumer. https://x.com/realmadhuguru/status/2102807619903824352

##### 要点

- The disagreement is about task type, not about whether flight-booking demos are bad marketing.
- Examples: clothes browsing versus hiring a roofer; browse-for-an-hour versus deliver-asap.
- The roofer path he lists: search, reviews, phone tag, insurance, inspection, quotes, hidden costs, past work, hire, schedule.
- Historical analogy: "I need to try clothes on" and "I will look at the TV at Circuit City."
- He later concedes the marketing critique of the travel demo specifically.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@sudhichada** | Thompson is right that flight-booking is the wrong lead; the pitch should be "hire a roofer" and other tasks people hate. | [post](https://x.com/sudhichada/status/2102779800817639548) |
| **@chriscocuzzo** | Does not think the roofing example actually disagrees with Thompson, and questions whether hiring a roofer is the perfect agent use case. | [post](https://x.com/chriscocuzzo/status/2102799778841272372) |
| **@luigifulinello** | Existing assistant use for research, scheduling, and buying home services already shows people want to get things done, not only be entertained. | [post](https://x.com/luigifulinello/status/2102790649548279813) |

##### 一句话概括

Consumers do not want every task automated, but the miserable ones are a real agent market.

#### 5. **Why enterprise AI efforts fail**

**链接：** https://x.com/realmadhuguru/status/2098448235048378456
**时间 / 互动（如有）：** Fri, 11 Sep 2026 16:27:01 GMT; Likes=112 Replies=15 Views=13077

##### 主帖在说什么

Quote-posting Aaron Levie's notes from meetings with technology leaders in banking, media, information services, insurance, and consulting, Madhu lists three failure modes. First, old playbooks: a CEO picks a lieutenant, that person builds a central AI team from trusted people, and the skill gap shows up because the last 15 years of product work were incremental while AI needs experimentation. Second, under-investment in evals; he points at his series. Third, building for the company from the outside: the central team declares itself a platform, ships tools disconnected from the workflow, and gets begrudging adoption without productivity gains. His remedies: hire leaders who have shipped AI products and can earn trust with the people whose jobs are changing; make evals first-class; embed the best builders inside finance, sales, and support and build with those teams.

##### 要点

- Failure mode 1 is org design and a skill gap, not model choice.
- Failure mode 2 is evals, cross-referencing his own series (part 10 is linked from the thread).
- Failure mode 3 is a platform team sitting outside the work.
- Remedies match the failures one for one: experienced AI leaders, evals, embedded builders.
- He is responding to Levie's field notes (cyber, multi-model spend, agent identity, process change, evals, legacy systems), not replacing them.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@gkhalin** | Also monitor adoption. Announce a feature, see who has not adopted it, and talk to them; hundreds of people cannot track every new approach themselves. | [post](https://x.com/gkhalin/status/2098453466662199591) |

##### 一句话概括

Central AI teams using an incremental playbook, weak evals, and an outside-in platform will not move the work.

### Products, launches, people

- Meta (his role), and prior Google work on Gemini, Veo, and Nano Banana, stated in the bio rather than as a new launch.
- Muse, mentioned by him and by Zuckerberg; a reply also names Instinct next to Muse.
- Satya Nadella (article link), Ben Thompson via TBPN, Aaron Levie, Dario Amodei, Mark Zuckerberg, Gavin Baker, Sriram Krishnan, METR.
- No new Madhu-shipped product name in this window. The posts are arguments and a continuing evals series.

### Tone

Numbered, managerial, and specific. He writes in checklists and contrasts (entertainment versus misery, owner-built platform versus embedded builders, open-weight as tailwind rather than cause). Disagreement is explicit and polite. The lighter posts ("human-written smell," "Stud traders like Kaushik love Muse") sit next to the essays without changing the register.
