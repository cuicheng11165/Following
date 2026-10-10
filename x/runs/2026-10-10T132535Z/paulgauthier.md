# Paul Gauthier (@paulgauthier)

| Field | Value |
|-------|-------|
| Profile | https://x.com/paulgauthier |
| Bio | Entrepreneur, investor, advisor |
| Source list | builders.md |
| Run ID | 2026-10-10T132535Z |
| Run dir | x/runs/2026-10-10T132535Z/ |

---

## Window: 2026-09-06 → 2026-10-10

- **Run ID:** 2026-10-10T132535Z
- **Fetched at:** 2026-10-10T13:25:35Z
- **Posts in window (fetched):** 7 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Most of the window is one experiment: a quantum-eraser test at UCSB that launched the photons carrying which-path information into space. Interference did not come back, which he says matches the partial trace.
- He estimates 73–82% of those launched photons propagate unmeasured indefinitely, and a follow-up says the model puts them 0.57 light-years out, crossing the Oort Cloud.
- He shipped a small Python DSL for optical-setup diagrams, meant to sit between a whiteboard sketch and a real table layout, and to be easy for an LLM to edit.
- In a reply about what AI cannot invent, he pointed at PyTheus rediscovering something other than entanglement swapping, which Mario Krenn said changed his view of what entanglement requires.

### Opinions and takes

- "Launching the photons did not restore interference." The null result is what quantum theory predicts "immediately, via the partial trace." The point of the experiment, he says, was to close a collapse-locality loophole, "not" to surprise anyone. https://x.com/paulgauthier/status/2105367773299798429
- "The thing is no one appears to have ever actually tested the unmeasured case under delayed-collapse interpretations. The carrier of the path marker was always rapidly measured." https://x.com/paulgauthier/status/2105427331104006326
- On PyTheus: Krenn said it "changed my perspective on what is necessary to create entanglement." Gauthier adds that this "is not the same as inventing teleportation, but it has a lot of conceptual novelty." https://x.com/paulgauthier/status/2097746979665395965

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **A Python DSL for optical setups**

**链接：** https://x.com/paulgauthier/status/2106149275881103548
**时间 / 互动（如有）：** Fri, 02 Oct 2026 22:28:12 GMT; Likes=9 Replies=2 Views=1573

##### 主帖在说什么

He made a small Python DSL for drawing optical-setup diagrams quickly. The intended gap is between a hand-drawn whiteboard sketch and an actual optical-table layout. Uses he names: sharing a setup with colleagues, and riffing with LLMs, because they can read and modify the code. A photo is attached; the tool did not describe it. He does not link a repo in the post text.

##### 要点

- It is a diagram DSL, not a ray-trace or a lab-control system.
- The design goal is speed: sketch-level, not a finished table drawing.
- He calls out LLM editability as a reason to use code instead of a drawing.
- No package name or repository URL is in the post.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ethereaglehq** | Agrees the whiteboard-to-table gap is the real one, and asks whether an LLM writes valid DSL on the first try or whether he parses it and bounces errors back before anyone looks at the layout. The thread fetch did not include an answer. | [post](https://x.com/ethereaglehq/status/2106151454776189020) |

##### 一句话概括

He wrote a tiny Python dialect so an optical sketch can be shared, and rewritten by a model, without pretending to be a full table layout.

#### 2. **Which-path photons launched from the UCSB roof**

**链接：** https://x.com/paulgauthier/status/2105367773299798429
**时间 / 互动（如有）：** Wed, 30 Sep 2026 18:42:47 GMT; Likes=12 Replies=3 Views=1701

##### 主帖在说什么

He asks what a quantum eraser does if the which-path information is never measured. From the lab roof at UCSB they launched the photons that carried that information into space, and a flat ΛCDM transmission model estimates 73–82% will propagate unmeasured forever. Launching had no effect on interference, which he says is consistent with quantum theory. He argues the unmeasured case had not been tested: earlier experiments always recorded the which-path marker with a detector, an absorber, or the environment. In this setup the marker photons went by fiber to the roof and out through a window, through the atmosphere, the Milky Way, and into the intergalactic medium. Their entangled twins stayed in the lab interferometer. They alternated launching and measuring. Across 6.6 hours and 100 million photon detections there was no statistically significant difference in the twins' unconditioned interference. Theory predicts that null via the partial trace. He says earlier work may have left a collapse-locality loophole, in which the which-path measurement could still causally influence the interference record. For photons that stay unmeasured, that influence is not available. He compares the aim to loophole-closing Bell tests: the result is not surprising; the goal was to drop a physical assumption from a test of the partial trace. Joint work with Sahil Patel, Sean Doan, and Galan Moody in the Quantum Photonics Lab at UCSB, supported by the NSF Quantum Foundry and the UCSB NRT program. Preprint and data links in the post are https://t.co/dR3pn3hrUK and https://t.co/NTlehRPPtQ.

The thread's own figures add the timing. Pair creation encodes path information at 0 ns. The idler is launched on an outgoing null trajectory at about 300 ns and leaves the past light cone of the signal-detection event at about 425 ns. The signal is detected at about 600 ns. A later post says the model puts most of those photons still propagating, now 0.57 light-years away and crossing the Oort Cloud: https://x.com/paulgauthier/status/2105367780975423664 and https://paulg.info/complementarity-photons/. In a reply he adds that, to his knowledge, the unmeasured case under delayed-collapse interpretations was never actually run, because the path marker was always measured quickly. https://x.com/paulgauthier/status/2105427331104006326

##### 要点

- Experiment: launch the which-path idler photons into space instead of detecting them.
- Transmission estimate: 73–82% never measured (also written T_∞ ≈ 73–82%).
- Outcome: no statistically significant change in the twins' unconditioned interference versus measuring the idlers.
- Data scale: 6.6 hours, 100 million detections.
- Causal claim: the idler exits the signal's past light cone before the signal is detected (~425 ns versus ~600 ns).
- Interpretation he wants: the partial trace, with the collapse-locality loophole closed for the surviving photons. Not a surprise result.
- Follow-up distance: 0.57 light-years, in the Oort Cloud, on the model's account.

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@M_Decoherence** | The unmeasured marker still matters because path information can remain in the joint state even if nobody reads it. Whether interference is recoverable is decided by the coincidence data. | [post](https://x.com/M_Decoherence/status/2105422847137214940) |

##### 一句话概括

They threw the which-path photons off the roof toward space, and the lab interference stayed gone, which is what the partial trace already said.

#### 3. **PyTheus and what entanglement requires**

**链接：** https://x.com/paulgauthier/status/2097746979665395965
**时间 / 互动（如有）：** Wed, 09 Sep 2026 18:00:28 GMT; Likes=4 Replies=0 Views=466

##### 主帖在说什么

This is a reply to Paul Raymond-Robichaud, who posted a quantum-teleportation circuit and said the math is trivial but the idea was revolutionary, and that it is the kind of conceptual jump AI is nowhere close to inventing. Gauthier asks whether he knows the PyTheus result on rediscovering entanglement swapping. He quotes Mario Krenn: it "changed my perspective on what is necessary to create entanglement." Gauthier grants it is not the same as inventing teleportation, but says it has a lot of conceptual novelty. The quoted Krenn post, from 2024, describes an AI-found protocol that entangles two distant particles without starting from entanglement, without Bell-state projections, and without measuring every ancilla, by using a superposition of the origins of photon multiplets. Krenn says they first thought the simpler answer was wrong. The implementation he credits is Xiaosong Ma's group at Nanjing University.

##### 要点

- He is answering a "AI cannot invent teleportation" claim, not announcing his own result.
- The counterexample he offers is PyTheus, and specifically that it did not hand back textbook entanglement swapping.
- He keeps the bar: conceptual novelty is not the same achievement as inventing teleportation.
- The Krenn line he wants in the conversation is about what is not necessary for entanglement.

##### 回复中的有价值观点

Thread fetch returned no high-signal replies.

##### 一句话概括

He treats PyTheus's simpler entanglement protocol as evidence that a model can surface a real conceptual shortcut, short of inventing teleportation.

### Products, launches, people

- The optical-setup Python DSL (no public name or repo in the post).
- The UCSB roof launch experiment, with Sahil Patel, Sean Doan, and Galan Moody; Quantum Photonics Lab; NSF Quantum Foundry; UCSB NRT. Write-up he linked: https://paulg.info/complementarity-photons/
- PyTheus and Mario Krenn's entanglement-swapping result, as a citation, not his release. Xiaosong Ma's group at Nanjing University is in the quoted paper note.

### Tone

Lab notebook, not product marketing. The posts are long, numbered, and careful about what was not surprising. The DSL note is the only software aside, and it is aimed at colleagues and at models that can edit the diagram code.
