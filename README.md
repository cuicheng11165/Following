# Following

跟踪 AI builders 的信息源与 X 动态摘要。

## 内容

| 路径 | 说明 |
|------|------|
| [`builders.md`](./builders.md) | X 上关注的 26 位 AI builders 及简介 |
| [`podcasts.md`](./podcasts.md) | 关注的播客源 |
| [`blogs.md`](./blogs.md) | 关注的博客源 |
| [`x/`](./x/) | 每人最近 X 帖子摘要（按 handle 分文件） |
| [`x-summary-state.json`](./x-summary-state.json) | 每人增量抓取游标（v2） |
| [`.grok/skills/summarize-x-builders/`](./.grok/skills/summarize-x-builders/) | 抓取并总结 X 动态的 Grok skill |

信息源列表对齐 [follow-builders](https://github.com/zarazhangrui/follow-builders) 的默认配置，本地可自行维护。

## Skill：`summarize-x-builders`

在 Grok 中运行 `/summarize-x-builders`：

1. 从 `builders.md` 解析 handle  
2. 按 **每人** 的 `last_fetched_at` 增量抓取（新人无记录则回填 30 天）  
3. 写入 `X/<handle>.md`  
4. 更新 `x-summary-state.json`

## 许可

个人笔记 / 公开分享用途。X 帖子摘要为二次整理，请以原文链接为准。
