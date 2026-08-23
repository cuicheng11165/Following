# Thibault Sottiaux (@thsottiaux)

| Field | Value |
|-------|-------|
| Profile | https://x.com/thsottiaux |
| Bio | Codex & ChatGPT @OpenAI |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 19 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Codex at 20M active users; banked usage reset as celebration
- Usage-limit panic: first blamed sub2api/fraud, then cache-hit regression
- GPT-5.6 Sol API price cut >20% for 3 months
- ChatGPT Sites as a “just prompt a music app” demo
- High-touch crisis comms (“never let a good crisis go to waste”)

### Opinions and takes

- Converting a ChatGPT/Codex subscription into API traffic (sub2api) is unsupported and gets fraud-flagged; Sign in With ChatGPT (official or OSS: Pi, OpenCode) is fine
- Cache hit rate is a first-class part of being “efficient” on usage limits
- Nice UX features that can be abused at scale will get revisited
- Crisis is also a chance to communicate more, not less

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **20M Codex users + a banked reset for everyone**

**链接：** https://x.com/thsottiaux/status/2090766694897619318  
**时间 / 互动：** Fri 21 Aug · Likes 19.6k · Views ~3.0M

##### 主帖在说什么

Tibo: Codex hit 20M active users this week. To celebrate, every Codex and ChatGPT Work user gets a **banked reset** they can spend later. On draining limits: they are not seeing anything abnormal, but there is an ongoing investigation. The prior post was a clarification of a *specific* pattern — sub2api / reselling subscription as API — not an accusation of all users. Official and OSS clients using Sign in With ChatGPT are fine.

##### 要点

- 20M Codex actives
- Banked reset (later confirmed landed by 8pm PST)
- Distinguishes fraud-shaped sub2api from normal clients
- Investigation still open on faster drain

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@macintogdev** | Accusing “us all of fraud is unconscionable” | [post](https://x.com/macintogdev/status/2090768090644549679) |
| **@TheFitFather_** | Theory: they turned off the 5h limit but accidentally applied weekly limits to the 5h window | [post](https://x.com/TheFitFather_/status/2090773334782886070) |

##### 一句话概括

Celebrate 20M with free tokens — while the community still thinks the limit math is broken.

#### 2. **Cache hit rate is why some usage is draining faster**

**链接：** https://x.com/thsottiaux/status/2091033630147854385  
**时间 / 互动：** Sat 22 Aug · Likes 8.7k · Views ~686k

##### 主帖在说什么

Update: for some users, cache hit rate this week is worse than the prior stable weeks. That can drain usage faster because hitting cache is a big part of being efficient. Investigating; update tomorrow. Follow-ups: “never let a good crisis go to waste”; “should be all propagated”; asking which model.

##### 要点

- New narrative vs yesterday’s “nothing abnormal”
- Cache as a hidden multiplier on subscription value
- Promises a next-day update

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@TheAhmadOsman** | Five banked resets is the least you could do | [post](https://x.com/TheAhmadOsman/status/2091035560219382034) |
| **@RealEverNever** | Not just this week; people report drain with *no* usage — stop the comfortable cache story | [post](https://x.com/RealEverNever/status/2091034153256915251) |
| **@ns123abc** | If cache is the issue, publish hit-rate numbers; the story changes every 24 hours | [post](https://x.com/ns123abc/status/2091076604675891513) |

##### 一句话概括

The second explanation (cache) did not close the trust gap; people want metrics, not narratives.

#### 3. **Prompted a music app on ChatGPT Sites to share an album**

**链接：** https://x.com/thsottiaux/status/2091014197144596734  
**时间 / 互动：** Sat 22 Aug · Likes 897 · Views ~163k

##### 主帖在说什么

@ajambrosino found Twitter music uploads too hard, so he prompted a whole music app hosted on ChatGPT Sites to share his album: `now-thats-what-i-call-slop.openai.chatgpt.site`. Plus/Work users can make and share their own sites from ChatGPT Work or desktop.

##### 要点

- ChatGPT Sites as a one-prompt hosting surface
- Demo is a joke-named album site, not a enterprise app
- Availability: Plus and above

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@thsottiaux** | Favorite track: Codex After Midnight | [post](https://x.com/thsottiaux/status/2091016731020169488) |
| **@kienbuilds** | Will listen while Luna swarm agents burn the banked reset | [post](https://x.com/kienbuilds/status/2091014787299787233) |

##### 一句话概括

The fun product this week is “prompt a website,” while the angry product is usage accounting.

### Products, launches, people

- Codex 20M actives + banked reset
- GPT-5.6 Sol API/credit price −20% for 3 months
- ChatGPT Sites
- Pi / OpenCode as supported Sign-in-with-ChatGPT clients
- Ishan shout-out

### Tone

On-call PM in a fire. Mix of celebration, damage control, French shrugs, and meme sites.
