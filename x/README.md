# X Builders 运行目录

每次 `/summarize-x-builders` 写入独立文件夹 `x/runs/<运行时间UTC>/`，避免单文件无限追加。

仅有新帖的 builder 会生成 `<handle>.md`；无更新的人只推进 `x-summary-state.json` 游标。

| 最新 | [./latest](./latest) → `runs/2026-08-13T041940Z/` |
|------|----------------------------------------|

## 历史运行（新 → 旧）

| Run ID | 路径 | 说明 |
|--------|------|------|
| 2026-08-13T041940Z | [runs/2026-08-13T041940Z/](./runs/2026-08-13T041940Z/) | Incremental since 2026-08-05; Gemini 1B, Codex 15M/Linux, Claude watermark, Grok 4.6 |
| 2026-08-05T040829Z | [runs/2026-08-05T040829Z/](./runs/2026-08-05T040829Z/) | Incremental + 8 new-handle backfills; Tibo Codex/Luna, sama optimist, RoboTTT, MoK, Grok 4.5 |
| 2026-08-03T024802Z | [runs/2026-08-03T024802Z/](./runs/2026-08-03T024802Z/) | Incremental since 2026-08-01; Karpathy LoTR/Opus5, Vercel @v, YC QM, Tibo Google LMChat |
| 2026-08-01T131655Z | [runs/2026-08-01T131655Z/](./runs/2026-08-01T131655Z/) | Prior full incremental run |
| 2026-07-29T033235Z | [runs/2026-07-29T033235Z/](./runs/2026-07-29T033235Z/) | Prior run |
| 2026-07-26T201500Z | [runs/2026-07-26T201500Z/](./runs/2026-07-26T201500Z/) | Prior run |

Default retention: keep last **10** run folders; older runs may be deleted after a successful job.
