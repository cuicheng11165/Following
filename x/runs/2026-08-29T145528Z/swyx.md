# Swyx (@swyx)

| Field | Value |
|-------|-------|
| Profile | https://x.com/swyx |
| Bio | achieve ambition with intentionality, intensity, integrity & insanity. Affiliations include smol.ai, DX tips, Cognition, AI Engineer, Latent Space. |
| Source list | builders.md |
| Run ID | 2026-08-29T145528Z |
| Run dir | x/runs/2026-08-29T145528Z/ |

---

## Window: 2026-08-22 → 2026-08-29

- **Run ID:** 2026-08-29T145528Z
- **Fetched at:** 2026-08-29T14:55:28Z
- **Posts in window (fetched):** 12 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Codex local “locked use” is unsafe on macOS right now; cloud still isn’t a full substitute
- Open models as the starting point for sovereign AI
- Agents as operators of ancient software (QuickBooks, California DMV)

### Opinions and takes

- Do not use Codex “locked use” while it depends on unstable Mac features
- Cloud would be nicer for everything, but it isn’t there yet
- Sovereign AI starts with open models (citing last month’s AI summit)

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **PSA: skip Codex “locked use” — it locked his Keychain twice**

**链接：** https://x.com/swyx/status/2092492963435946494  
**时间 / 互动：** Wed 26 Aug · Likes 36 · Replies 63 · Views ~11k

##### 主帖在说什么

Swyx warns not to use Codex “locked use” capabilities: they rely on unstable macOS features and have locked him out of his Keychain twice in one week. Cheng Lou pointed to Apple developer forums calling it a known bug. He’d prefer to do everything in the cloud, but says the cloud isn’t ready.

##### 要点

- Codex locked-use currently depends on unstable Mac APIs
- Twice this week: full macOS Keychain lockout
- Temporary workaround exists; cloud is not yet a replacement

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@_chenglou** | Temporary fix: `security unlock-keychain ~/Library/Keychains/login.keychain-db` | [post](https://x.com/_chenglou/status/2092493254281552019) |
| **@firtoz** | Asks what’s still missing from cloud; is exploring custom VM sandboxes | [post](https://x.com/firtoz/status/2092499250844217457) |

##### 一句话概括

Local agent “lock the machine” features are shipping ahead of OS stability; keep the keys in your own hands until cloud catch-up.

#### 2. **What’s missing from cloud? You — and janky OpenClaw via Codex**

**链接：** https://x.com/swyx/status/2092794604403986800  
**时间 / 互动：** Thu 27 Aug · Likes 1 · Replies 4 · Views ~433

##### 主帖在说什么

Reply in the same Keychain thread: “What’s missing from cloud? you.” Not a glib answer — he uses Codex as a janky OpenClaw a lot for operating ancient software like QuickBooks and dealing with the California DMV.

##### 要点

- Cloud agents still lack *you* (local identity, local software, local government sites)
- Codex is being used as a stand-in personal agent for legacy ops

##### 回复中的有价值观点

Thread fetch on the parent PSA already captured the cloud-gap replies; this follow-up is Swyx’s own answer to that gap.

##### 一句话概括

The remaining cloud gap is local-you: identity, ancient apps, and government websites.

#### 3. **Sovereign AI starts with open models**

**链接：** https://x.com/swyx/status/2093093810121404585  
**时间 / 互动：** Thu 27 Aug · Likes 5 · Views ~3.6k

##### 主帖在说什么

Agrees that last month’s AI summit (Grady and Sonya) was extremely on point with a sovereign-AI focus, “and it all starts with open models.”

##### 要点

- Sovereign AI is a live practitioner theme, not just policy talk
- Open models are the prerequisite layer

##### 回复中的有价值观点

Short agreement post; no high-signal independent replies in the list fetch.

##### 一句话概括

If you want sovereign AI, start by running open models.

### Products, launches, people

- Codex locked-use / macOS Keychain bug (via @_chenglou, Apple forums)
- OpenClaw used as a comparison for “janky” local agent ops
- Eugene Wei’s *Status as a Service* (annual tribute)

### Tone

Practical, slightly exasperated operator: one hard PSA, then short replies. Less conference-platform this window, more “I just locked myself out of my Mac.”
