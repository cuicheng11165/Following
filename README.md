**English** | [中文](./README.zh-CN.md)

# Following

A personal information-tracking and knowledge-archiving project for AI practitioners.

The project follows AI builders who actively work on products, research, and engineering rather than accounts that simply repeat trending news. It currently organizes **26 X (Twitter) accounts, 6 podcasts, and 2 official blogs**, with each builder's recent activity summarized in searchable, version-controlled Markdown files.

> This project is primarily inspired by the philosophy and source design of [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders): **Follow builders, not influencers**. Many thanks to the original author for sharing the idea and implementation.

## Features

### 1. Maintain a curated list of AI builders

[`builders.md`](./builders.md) contains 26 AI builder accounts, including:

- AI labs and research: Andrej Karpathy, Sam Altman, Amanda Askell, and others
- AI coding and agents: Boris Cherny, Cat Wu, Thariq, Peter Steinberger, and others
- AI products and startups: Amjad Masad, Guillermo Rauch, Aaron Levie, Garry Tan, and others
- Product, investing, and industry analysis: Nan Yu, Matt Turck, Zara Zhang, Dan Shipper, and others

In addition to profile links, the file includes short biographies, areas of interest, and topic-based recommendations. The list can be edited directly to match your own interests.

### 2. Generate per-builder X summaries

[`x/`](./x/) stores a separate activity summary for each builder, such as [`x/karpathy.md`](./x/karpathy.md). Each summary includes:

- Major themes within the selected time window
- Notable opinions and observations
- Representative posts with links to the originals
- Products, launches, and people mentioned
- A short description of the builder's overall tone

[`x/README.md`](./x/README.md) provides an index of the latest run, including post counts and a one-line summary for every builder.

### 3. Update each account incrementally

[`x-summary-state.json`](./x-summary-state.json) maintains a separate cursor for every account:

- Previously processed accounts resume from their own `last_fetched_at`
- Newly added accounts backfill the previous 30 days by default
- A failed account does not advance its cursor or prevent other accounts from completing
- State can be saved after each successful account, reducing data loss if a batch run is interrupted

Per-account cursors are more reliable than a single global timestamp when accounts are frequently added to or removed from a personal watchlist.

### 4. Organize podcast and blog sources

- [`podcasts.md`](./podcasts.md): 6 AI podcasts with public pages and RSS information
- [`blogs.md`](./blogs.md): official sources including Anthropic Engineering and the Claude Blog

At present, these files serve primarily as structured source directories. The automated summarization workflow currently focuses on X activity.

### 5. Provide a reusable Grok Skill

The repository includes [`.grok/skills/summarize-x-builders/`](./.grok/skills/summarize-x-builders/), which:

- Parses accounts from `builders.md`
- Calculates an independent fetch window for each account
- Retrieves recent public posts with pagination
- Writes summaries to `x/<handle>.md`
- Updates the index and incremental state

In a Grok environment that supports project-level Skills, run:

```text
/summarize-x-builders
```

You can also use `/x-builders` or ask in natural language to update the builders' X activity.

## Project structure

```text
.
├── README.md
├── README.zh-CN.md
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

## Relationship to and differences from `follow-builders`

This project adopts the upstream project's core idea—follow people who build and use AI to reduce the cost of consuming information—and references its default builder, podcast, and blog lists. The two projects differ in their goals and usage:

| Area | `zarazhangrui/follow-builders` | This project |
|------|-------------------------------|--------------|
| Core format | An installable AI digest skill | A browsable, version-controlled personal knowledge repository |
| Data source | A centrally maintained feed containing X, podcast, and blog content | A local Grok Skill that queries X account by account from `builders.md` |
| Main output | A combined daily or weekly digest | A long-lived Markdown summary for each builder |
| Update state | Reading history and preferences for digest runs | An independent incremental fetch cursor for each account |
| Source management | Default sources are centrally managed and updated | Source files live in the repository and can be edited directly |
| Delivery | Supports in-chat, Telegram, email, and other scheduled delivery methods | Primarily Markdown files and indexes stored in Git |
| Customization | Configure language, frequency, delivery, and summary prompts | Edit the watchlist, Skill, templates, and archived summaries directly |
| Current coverage | X, podcasts, and official blogs are included in the digest pipeline | X supports summaries and incremental updates; podcasts and blogs are currently organized as directories |

In short:

- If you want a combined AI daily or weekly digest delivered automatically, the upstream `follow-builders` project is closer to a ready-to-use subscription tool.
- If you want to maintain your own watchlist and build a searchable, comparable, Git-tracked archive of each builder's ideas over time, this project is designed as a personal knowledge base.

This project is not a complete port of `follow-builders` and does not depend on its central feed. It is an independent implementation of the same philosophy, optimized for per-person tracking, incremental updates, and local archival.

## Usage

### Browse existing summaries

1. Open [`x/README.md`](./x/README.md) to see the latest update overview.
2. Open the corresponding `x/<handle>.md` file for a detailed summary of a builder.
3. Follow the original post links to verify context and details.

### Edit the watchlist

Add or remove accounts in the Overview table in [`builders.md`](./builders.md). The Skill parses the name, handle, and X profile URL from the table and deduplicates entries by handle.

New accounts receive a 30-day backfill on their first run. Existing accounts resume from their own last successful timestamps.

### Update summaries

Run `/summarize-x-builders` in Grok. After it completes, review:

- `x/README.md`: overall results for the latest run
- `x/<handle>.md`: the new summary window for each builder
- `x-summary-state.json`: account status and the starting point for the next fetch

## Notes

- The project organizes public information only. Summaries do not represent the full views of the original authors.
- AI-generated summaries may omit context or details. Verify important information using the original links included with each item.
- A maximum of 50 posts is fetched per account in one run. A capped window may contain additional posts that were not included.
- Roles and sources change over time, so profile descriptions should be reviewed periodically.

## Acknowledgements

Thanks to [Zara Zhang](https://github.com/zarazhangrui) and [follow-builders](https://github.com/zarazhangrui/follow-builders) for the project philosophy, source design, and implementation reference.
