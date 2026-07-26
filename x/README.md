# X Builders 摘要索引

| 字段 | 值 |
|------|-----|
| **窗口** | 2026-06-26 → 2026-07-26 |
| **模式** | 重写：Notable posts 使用 **`summarize-x-post`**（`x_thread_fetch` 主帖 + 高信号回复） |
| **Skill** | `summarize-x-builders` → 每条 Notable 调用 `summarize-x-post` 工作流 |
| **来源** | `builders.md` |

**Notable 标准：** 每条含「主帖在说什么 / 要点 / 回复中的有价值观点 / 一句话概括」，禁止列表摘要一句话带过。

每人列表抓取上限 **50** 条；深度总结 **3–5** 条高信号帖。

---

## 总览

| Handle | 姓名 | 列表帖 | Deep notables | 一句话 | 文件 |
|--------|------|--------|---------------|--------|------|
| `karpathy` | Andrej Karpathy | 9 | 5 | 语音 ramble mind meld、/compact、Fable three.js | [karpathy.md](./karpathy.md) |
| `swyx` | Swyx | 50 | 5 | SmolForge、Poolside eval、控制/数据面 | [swyx.md](./swyx.md) |
| `joshwoodward` | Josh Woodward | 40 | 5 | Spark、3.6 Flash、Gemini Notebook | [joshwoodward.md](./joshwoodward.md) |
| `bcherny` | Boris Cherny | 50 | 5 | AI 采用四阶段、领域知识进 CLAUDE.md | [bcherny.md](./bcherny.md) |
| `thsottiaux` | Thibault Sottiaux | 50 | 5 | ChatGPT Work 超 Codex、登录云浏览器 | [thsottiaux.md](./thsottiaux.md) |
| `petergyang` | Peter Yang | 40 | 5 | Codex 工作系统、Voice、indie 变现 | [petergyang.md](./petergyang.md) |
| `thenanyu` | Nan Yu | 40 | 5 | Systems thinking、agent review memory | [thenanyu.md](./thenanyu.md) |
| `realmadhuguru` | Madhu Guru | 47 | 5 | 开放权重企业栈；加入 Meta | [realmadhuguru.md](./realmadhuguru.md) |
| `AmandaAskell` | Amanda Askell | 8 | 4 | 概率沟通、基率错觉与命名品味 | [AmandaAskell.md](./AmandaAskell.md) |
| `_catwu` | Cat Wu | 44 | 5 | Cowork / Tag 非工程落地 | [_catwu.md](./_catwu.md) |
| `trq212` | Thariq | 50 | 5 | 砍掉 80% system prompt | [trq212.md](./trq212.md) |
| `GoogleLabs` | Google Labs | 3 | 3 | NotebookLM→Gemini Notebook；MusicFX | [GoogleLabs.md](./GoogleLabs.md) |
| `amasad` | Amjad Masad | 50 | 5 | Self-driving company；agent 安全 | [amasad.md](./amasad.md) |
| `rauchg` | Guillermo Rauch | 50 | 5 | 软件工厂 eve.dev；Next evals | [rauchg.md](./rauchg.md) |
| `alexalbert__` | Alex Albert | 5 | 5 | Opus 5 表格/deck；Fable 限流 | [alexalbert__.md](./alexalbert__.md) |
| `levie` | Aaron Levie | 50 | 5 | 开放权重 + Box 评测 + 企业 agent | [levie.md](./levie.md) |
| `ryolu_` | Ryo Lu | 33 | 5 | 梦想源头长文；Cursor 设计；反 slop | [ryolu_.md](./ryolu_.md) |
| `garrytan` | Garry Tan | 50 | 5 | Startup School；SF 建房/CEQA | [garrytan.md](./garrytan.md) |
| `mattturck` | Matt Turck | 50 | 5 | Cerebras 长谈 + model routing | [mattturck.md](./mattturck.md) |
| `zarazhangrui` | Zara Zhang | 48 | 5 | AI-native 组织；自费工具与招聘 | [zarazhangrui.md](./zarazhangrui.md) |
| `nikunj` | Nikunj Kothari | 50 | 5 | Proof-of-prompt；职衔失信号 | [nikunj.md](./nikunj.md) |
| `steipete` | Peter Steinberger | 50 | 5 | Autoreview 多轮；graph engineer | [steipete.md](./steipete.md) |
| `danshipper` | Dan Shipper | 50 | 5 | Opus 5 vibe；Codex 史；All Access | [danshipper.md](./danshipper.md) |
| `adityaag` | Aditya Agarwal | 41 | 5 | 文化吃掉战略；memory 原语 | [adityaag.md](./adityaag.md) |
| `sama` | Sam Altman | 50 | 5 | ChatGPT Work；开源双轨；Sol | [sama.md](./sama.md) |
| `claudeai` | Claude | 50 | 5 | Opus 5、Cowork skill、Fable 配额 | [claudeai.md](./claudeai.md) |

---

## 统计

| 指标 | 值 |
|------|-----|
| 重写成功 | 26 / 26 |
| Deep notables（约） | ~125 条，均 `x_thread_fetch` |
| `x-summary-state.json` | **未改动**（同窗口重写） |

下次 `/summarize-x-builders` 将按人增量抓取，且 Notable 继续走 `summarize-x-post`。
