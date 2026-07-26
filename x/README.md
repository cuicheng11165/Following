# X Builders 摘要索引

| 字段 | 值 |
|------|-----|
| **窗口** | 2026-06-26 → 2026-07-26 |
| **模式** | 30-day backfill + **Notable posts 新标准重写** |
| **重写时刻** | 2026-07-26T19:28:25Z |
| **来源** | `builders.md` |
| **Skill** | `summarize-x-builders` |

**Notable posts 标准：** 每条为 2–5 句观点/内容总结 + `链接：`，禁止「一句话标签 + URL」。

每人最多抓取 **50** 条帖子；标记 cap 的人窗口内实际发帖可能更多。

---

## 总览

| Handle | 姓名 | 帖子数 | Notable | 一句话 | 文件 |
|--------|------|--------|---------|--------|------|
| `karpathy` | Andrej Karpathy | 9 | 7 | LLM 碎碎念工作流、Fable 可玩世界与语言 cringe 化观察 | [karpathy.md](./karpathy.md) |
| `swyx` | Swyx | 50 | 8 | SmolForge dogfood、Poolside 开放 eval 与 control/data plane | [swyx.md](./swyx.md) |
| `joshwoodward` | Josh Woodward | 50 | 8 | Gemini Spark/3.6 Flash、Notebook 更名与用户反馈 Top10 | [joshwoodward.md](./joshwoodward.md) |
| `bcherny` | Boris Cherny | 50 | 8 | AI 采用四步、领域知识基础设施化与 Opus 5 抗注入 | [bcherny.md](./bcherny.md) |
| `thsottiaux` | Thibault Sottiaux | 50 | 8 | ChatGPT Work 用户超 Codex、Voice/登录态 agent | [thsottiaux.md](./thsottiaux.md) |
| `petergyang` | Peter Yang | 50 | 8 | Codex 实战访谈、Voice 多线程与 indie 变现难 | [petergyang.md](./petergyang.md) |
| `thenanyu` | Nan Yu | 50 | 7 | Systems thinking、agent code review memory | [thenanyu.md](./thenanyu.md) |
| `realmadhuguru` | Madhu Guru | 47 | 8 | 开放权重重塑企业栈；加入 Meta | [realmadhuguru.md](./realmadhuguru.md) |
| `AmandaAskell` | Amanda Askell | 8 | 7 | 概率沟通、基率错觉与命名品味 | [AmandaAskell.md](./AmandaAskell.md) |
| `_catwu` | Cat Wu | 44 | 8 | Opus 5 / Tag / Cowork 非工程落地 | [_catwu.md](./_catwu.md) |
| `trq212` | Thariq | 50 | 8 | 砍掉 80% system prompt：thin prompts + thick context | [trq212.md](./trq212.md) |
| `GoogleLabs` | Google Labs | 3 | 3 | NotebookLM→Gemini Notebook；MusicFX 下线 | [GoogleLabs.md](./GoogleLabs.md) |
| `amasad` | Amjad Masad | 50 | 8 | Replit 降价与移动端；agent 安全事件 | [amasad.md](./amasad.md) |
| `rauchg` | Guillermo Rauch | 50 | 8 | 软件工厂 eve.dev；AI Gateway/v0/CDN | [rauchg.md](./rauchg.md) |
| `alexalbert__` | Alex Albert | 5 | 5 | Opus 5 / Fable：表格与 deck 近顾问级 | [alexalbert__.md](./alexalbert__.md) |
| `levie` | Aaron Levie | 50 | 8 | 开放权重+企业 agent；Box 评测与护城河 | [levie.md](./levie.md) |
| `ryolu_` | Ryo Lu | 33 | 8 | Cursor 设计团队扩张；守住梦想源头、反 slop | [ryolu_.md](./ryolu_.md) |
| `garrytan` | Garry Tan | 50 | 8 | Startup School 2026 + SF 建房/CEQA | [garrytan.md](./garrytan.md) |
| `mattturck` | Matt Turck | 50 | 8 | Cerebras 推理芯片长访谈 + model routing | [mattturck.md](./mattturck.md) |
| `zarazhangrui` | Zara Zhang | 48 | 8 | AI-native 组织与 human-human-agent 协作 | [zarazhangrui.md](./zarazhangrui.md) |
| `nikunj` | Nikunj Kothari | 50 | 8 | Proof-of-prompt、职衔失信号与湾区育儿 | [nikunj.md](./nikunj.md) |
| `steipete` | Peter Steinberger | 50 | 8 | OpenClaw 并行 QA + Codex/Sol harness | [steipete.md](./steipete.md) |
| `danshipper` | Dan Shipper | 50 | 8 | Opus 5 vibe check；Every All Access | [danshipper.md](./danshipper.md) |
| `adityaag` | Aditya Agarwal | 41 | 8 | 文化吃掉战略；SPC fellowship | [adityaag.md](./adityaag.md) |
| `sama` | Sam Altman | 50 | 8 | 5.6 Sol/ChatGPT Work；开源+闭源双赢 | [sama.md](./sama.md) |
| `claudeai` | Claude | 50 | 8 | Opus 5、Fable 配额；Voice/Cowork/Teachers | [claudeai.md](./claudeai.md) |

---

## 统计

| 指标 | 值 |
|------|-----|
| 重写成功 | 26 / 26 |
| 失败 | 0 |
| `x-summary-state.json` | **未改动**（重写同一窗口，游标仍为上次成功时间） |

下次 `/summarize-x-builders` 将按每人 `last_fetched_at` **增量**抓取，并继续使用新版 Notable posts 标准。
