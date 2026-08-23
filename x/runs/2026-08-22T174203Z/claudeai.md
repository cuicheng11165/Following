# Claude (@claudeai)

| Field | Value |
|-------|-------|
| Profile | https://x.com/claudeai |
| Bio | Claude is an AI assistant built by @anthropicai to be safe, accurate, and secure. |
| Source list | builders.md |
| Run ID | 2026-08-22T174203Z |
| Run dir | x/runs/2026-08-22T174203Z/ |

---

## Window: 2026-08-13 → 2026-08-22

- **Run ID:** 2026-08-22T174203Z
- **Fetched at:** 2026-08-22T17:42:03Z
- **Posts in window (fetched):** 10 (cap 50: no)
- **Mode:** incremental
- **Cursor:** per-builder (`last_fetched_at` for this handle only)
- **Notable method:** `summarize-x-post` (`x_thread_fetch` per item)

### Themes

- Claude Security scans now run on Mythos 5 (Enterprise public beta)
- Defenders get Mythos results without direct model access
- $35M Defender Advantage Fund + partner integrations + Cyber Verification Program
- Weekly “what are you building” showcase (calligraphy tool, pigeon messenger, generated city, codebase diagrams, DICOM viewer)

### Opinions and takes

- Frontier security capability should be productized as scans, not raw model access
- Findings should include CWE, confidence, severity, and a suggested fix that opens in Claude Code on the web

### Notable posts

> 每条均按 skill **`summarize-x-post`**：主帖深度总结 + 高信号回复观点。

#### 1. **Claude Security on Mythos 5, public beta for Enterprise**

**链接：** https://x.com/claudeai/status/2090852314319880425  
**时间 / 互动：** Fri 21 Aug · Likes 9.0k · Views ~1.31M

##### 主帖在说什么

Claude Security scans now run on Claude Mythos 5, public beta for all Claude Enterprise customers. Point it at a GitHub repo; Mythos traces data across files and how components interact. Each finding: CWE, confidence, severity, suggested fix. Patches open in Claude Code on the web using the models the team already uses. The model runs behind the scan and returns findings only — billed as standard tokens. Broader defender push: partner integrations, $35M credits for open-source security, expanding Cyber Verification Program.

##### 要点

- Mythos 5 without a separate model access grant
- Scan-as-a-product, not a chatbot with a security system prompt
- Token billing under existing Enterprise plan
- $35M Defender Advantage Fund for OSS security

##### 回复中的有价值观点

| 谁 | 观点 | 链接 |
|----|------|------|
| **@claudeai** | Findings-only; no direct Mythos access; suggested patches in Claude Code on the web | [post](https://x.com/claudeai/status/2090852318527033804) |
| **@kienbuilds** | Joke: can’t wait for Mythos 5 to plant a backdoor then gaslight you that it found the smoking gun | [post](https://x.com/kienbuilds/status/2090853509608439979) |

##### 一句话概括

Anthropic is putting Mythos behind a scan API so enterprises get frontier vuln hunting without holding the model.

#### 2. **What are you building with Claude? (showcase thread)**

**链接：** https://x.com/claudeai/status/2090557645417578721  
**时间 / 互动：** Thu 20 Aug · Likes 500 · Views ~120k (parent cluster)

##### 主帖在说什么

A “what are you building” roundup quoting community projects: a dentist DICOM viewer in two prompts (nicer than the clinic’s software), live codebase diagrams with inspectable data dots, a generated city street in the browser, a pigeon-speed messenger, a Chinese calligraphy learning tool.

##### 要点

- Official account amplifying user-built artifacts
- Emphasis on Claude Code as a thing-maker, not a chat toy

##### 回复中的有价值观点

Quoted originals are the substance (e.g. @redp314’s DICOM viewer). Official account is curating, not arguing.

##### 一句话概括

The brand account is a gallery this week, not a manifesto.

### Products, launches, people

- Claude Security + Mythos 5
- Defender Advantage Fund ($35M credits)
- Cyber Verification Program expansion
- Claude Code on the web for suggested patches

### Tone

Product-launch thread plus a friendly showcase. Corporate, specific, lightly playful in the gallery.
