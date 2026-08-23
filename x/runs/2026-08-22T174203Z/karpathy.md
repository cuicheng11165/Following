# Andrej Karpathy (@karpathy)

| Field | Value |
|-------|-------|
| Profile | https://x.com/karpathy |
| Bio | deep learning |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 2 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Tearing down ML framework abstractions now that coding agents can write the math
- PyTorch as a “crappy IR” versus a tiny scalar Python spec that compiles
- Agent-era inversion: finite human attention no longer justifies heavy libraries

### Opinions and takes

- Autograd, `torch.nn`, and similar layers were built for a world of scarce intelligence and attention; agents can now do the drudgery and verification
- The logical endpoint is a microGPT-style spec (scalar Python with for-loops); everything else is compilation

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Tear down the abstractions — agents can write the backward pass**

**链接：** https://x.com/karpathy/status/2090478783895929036  
**时间 / 互动：** Thu 20 Aug · Likes 276 · Views ~35k

##### 主帖在说什么

Karpathy replies in Chris McCormick’s thread about writing a single compilable `forward_backward` function with no autograd and no `torch.nn` — just matrices, explicit gradient buffers, and stashed activations. Karpathy agrees it is increasingly appealing to tear those abstractions down now that agents can do the math, drudgery, and verification. The old stack, he says, was designed around finite human intelligence and attention.

##### 要点

- Agents can write and check backward math that humans used to hide behind autograd
- Framework abstractions were a response to scarce human attention, not a law of nature
- McCormick’s nanochat stash even skips storing 18GB post-ReLU activations by recomputing them

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@ChrisJMcCormick** | Wrote model code as one `forward_backward`: no autograd, no nn modules, `.gacc` gradient buffers, explicit activation stash (Claude wrote the backward math) | [post](https://x.com/ChrisJMcCormick/status/2089442519205765378) |
| **@Piyush_Goenka_** | Asks whether writing everything from scratch is much more resource-inefficient | [post](https://x.com/Piyush_Goenka_/status/2090486431248740444) |

##### 一句话概括

Coding agents make hand-written forward/backward cheaper than living inside PyTorch’s abstraction tax.

#### 2. **Your spec is microGPT; PyTorch is a crappy IR**

**链接：** https://x.com/karpathy/status/2090479399842054610  
**时间 / 互动：** Thu 20 Aug · Likes 186 · Views ~37k

##### 主帖在说什么

Follow-up in the same thread: if agents can compile from a tiny spec, the right source of truth is something like microGPT — scalar-valued Python with for-loops. Everything else is compilation. PyTorch, in that world, is “kind of a crappy IR.”

##### 要点

- Spec should be tiny, explicit, scalar Python
- Frameworks become intermediate representations, not the programming model
- Compilation, not library APIs, is the missing layer

##### 回复中的有价值观点

Thread replies mostly sat on the parent post; the high-signal continuation is Karpathy’s own follow-up rather than a large reply debate.

##### 一句话概括

The future training stack is a tiny Python spec plus a compiler — not a bigger nn.Module zoo.

### Products, launches, people

- Chris McCormick’s single-file `forward_backward` nanochat experiment
- References to modded-nanogpt PRs doing similar stash/recompute tricks

### Tone

Short, systems-minded, slightly gleeful about deleting abstractions. Two replies in one thread, not a product dump.
