# Following

一个面向 AI 从业者的个人信息追踪与知识归档项目。

项目关注真正参与产品、研究和工程实践的 AI builders，而不是单纯转述热点的内容账号。目前仓库整理了 **26 个 X（Twitter）账号、6 档播客和 2 个官方博客**，并将每位 builder 的近期动态分别总结为可检索、可版本管理的 Markdown 文档。

> 本项目主要参考了 [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) 的理念与信息源设计：**Follow builders, not influencers**。感谢原项目作者提供的思路和公开实现。

## 项目功能

### 1. 维护 AI builders 信息源

[`builders.md`](./builders.md) 收录当前关注的 26 个 AI builder 账号，包括：

- AI 实验室与研究：Andrej Karpathy、Sam Altman、Amanda Askell 等
- AI 编程与 Agent：Boris Cherny、Cat Wu、Thariq、Peter Steinberger 等
- AI 产品与创业：Amjad Masad、Guillermo Rauch、Aaron Levie、Garry Tan 等
- 产品、投资与行业观察：Nan Yu、Matt Turck、Zara Zhang、Dan Shipper 等

文件不仅提供账号链接，也包含人物简介、关注方向和按主题整理的推荐索引，方便继续增删和维护自己的关注列表。

### 2. 按人生成 X 动态摘要

[`x/`](./x/) 为每位 builder 保存一份独立的动态摘要，例如 [`x/karpathy.md`](./x/karpathy.md)。每份摘要包含：

- 指定时间窗口内的主要话题
- 值得关注的观点和判断
- 代表性帖子及原文链接
- 涉及的产品、发布和人物
- 发言风格与整体倾向

[`x/README.md`](./x/README.md) 提供本次抓取的汇总索引，可快速查看所有人的更新数量和一句话摘要。

### 3. 支持按账号增量更新

项目通过 [`x-summary-state.json`](./x-summary-state.json) 为每个账号分别保存抓取游标：

- 已成功处理的账号从自己的 `last_fetched_at` 继续更新
- 新加入的账号默认回填最近 30 天
- 某个账号抓取失败时不会推进其游标，也不会影响其他账号
- 每个账号成功后即可独立保存状态，降低批量任务中断造成的数据丢失

这比使用一个全局更新时间更适合会持续增删账号的个人关注列表。

### 4. 整理播客与博客目录

- [`podcasts.md`](./podcasts.md)：6 档 AI 播客及其公开页面、RSS 信息
- [`blogs.md`](./blogs.md)：Anthropic Engineering 和 Claude Blog 等官方博客源

当前仓库主要将它们作为结构化信息源目录；现有自动摘要流程重点处理 X 动态。

### 5. 提供可复用的 Grok Skill

仓库内置 [`.grok/skills/summarize-x-builders/`](./.grok/skills/summarize-x-builders/)：

- 从 `builders.md` 自动解析账号
- 按账号计算独立抓取窗口
- 分页获取近期公开帖子
- 将中文摘要写入 `x/<handle>.md`
- 更新汇总索引和增量状态

在支持项目级 Skill 的 Grok 环境中，可运行：

```text
/summarize-x-builders
```

也可以使用 `/x-builders`，或直接用自然语言要求更新 builders 的 X 动态。

## 目录结构

```text
.
├── README.md
├── builders.md
├── podcasts.md
├── blogs.md
├── x-summary-state.json
├── x/
│   ├── README.md
│   └── <handle>.md
└── .grok/
    └── skills/
        └── summarize-x-builders/
            ├── SKILL.md
            ├── references/
            │   └── output-template.md
            └── scripts/
                └── parse_builders.py
```

## 与 `follow-builders` 的关系和区别

本项目沿用了上游项目“关注真正做事的人，并用 AI 降低信息消费成本”的核心思路，也参考了其默认 builder、播客和博客列表。但两者的目标和使用方式有所不同：

| 对比项 | `zarazhangrui/follow-builders` | 当前项目 |
|--------|-------------------------------|----------|
| 核心形态 | 可安装的 AI digest skill | 可直接浏览和版本管理的个人知识仓库 |
| 数据获取 | 从每日更新的中央 feed 获取 X、播客和博客内容 | 由本地 Grok Skill 根据 `builders.md` 逐个查询 X |
| 主要输出 | 将多种来源重组为一份每日或每周简报 | 为每位 builder 长期维护独立的 Markdown 摘要 |
| 更新状态 | 面向一次 digest 的阅读历史和偏好 | 为每个账号维护独立的增量抓取游标 |
| 信息源管理 | 默认来源由上游中央维护并自动更新 | 来源文件保存在仓库内，可按个人需求直接修改 |
| 交付方式 | 支持聊天内、Telegram、Email 等方式定时推送 | 以 Git 仓库内的 Markdown 文件和索引为主 |
| 个性化方式 | 配置语言、频率、投递方式和摘要 prompt | 直接编辑名单、Skill、模板及已有摘要 |
| 当前覆盖 | X、播客、官方博客均进入 digest 流程 | X 已实现摘要与增量更新；播客、博客目前以目录整理为主 |

简单来说：

- 如果你需要一份自动送达的综合 AI 日报或周报，上游 `follow-builders` 更接近开箱即用的订阅工具。
- 如果你希望自己维护关注对象，并将不同 builder 的长期观点沉淀为可搜索、可比较、可通过 Git 追踪的笔记，当前项目更适合作为个人知识库。

当前项目不是 `follow-builders` 的完整移植，也不依赖其中央 feed；它是在相同理念下，针对“按人追踪、增量更新、本地归档”场景做的一次独立实践。

## 使用方式

### 浏览已有内容

1. 从 [`x/README.md`](./x/README.md) 查看最近一次更新总览。
2. 打开对应的 `x/<handle>.md` 阅读某位 builder 的详细摘要。
3. 通过原文链接回到 X 核对上下文。

### 修改关注列表

在 [`builders.md`](./builders.md) 的 Overview 表格中添加或移除账号。Skill 会从表格解析名称、handle 和 X 主页地址，并按 handle 去重。

新账号没有历史游标时，首次运行会自动回填最近 30 天；已有账号则从各自上次成功时间继续抓取。

### 更新摘要

在 Grok 中运行 `/summarize-x-builders`。完成后重点检查：

- `x/README.md`：本轮整体结果
- `x/<handle>.md`：每人的新增摘要窗口
- `x-summary-state.json`：每个账号的成功状态与下一次抓取起点

## 注意事项

- 项目仅整理公开信息，摘要不代表原作者的完整观点。
- AI 摘要可能遗漏语境或细节，重要信息请以每条内容附带的原文链接为准。
- 单个账号一次最多抓取 50 条帖子；达到上限时，时间窗口内可能仍有未覆盖内容。
- 人物职位和信息源会随时间变化，仓库中的介绍应定期核对。

## 致谢

感谢 [Zara Zhang](https://github.com/zarazhangrui) 和 [follow-builders](https://github.com/zarazhangrui/follow-builders) 提供的项目理念、信息源设计和实践参考。
