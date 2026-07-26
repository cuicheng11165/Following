# Follow Builders — Blogs

> Source: `follow-builders` skill · `config/default-sources.json` · `blogs`  
> Total: **2** blogs  
> Fetch model: scrape via HTTP (central feed)

These are the official AI blogs tracked by the Follow Builders digest. The list is curated centrally and may update over time.

---

## Overview

| # | Name | Index URL | Article base URL | Type | Fetch method |
|---|------|-----------|------------------|------|--------------|
| 1 | Anthropic Engineering | https://www.anthropic.com/engineering | https://www.anthropic.com/engineering/ | scrape | http |
| 2 | Claude Blog | https://claude.com/blog | https://claude.com/blog/ | scrape | http |

---

## Detail entries

### 1. Anthropic Engineering

| Field | Value |
|-------|-------|
| **Name** | Anthropic Engineering |
| **Description** | Technical deep-dives from the Anthropic engineering team |
| **Index URL** | https://www.anthropic.com/engineering |
| **Article base URL** | https://www.anthropic.com/engineering/ |
| **Type** | `scrape` |
| **Fetch method** | `http` |
| **Organization** | Anthropic |
| **Content focus** | Engineering write-ups, system design, applied research |
| **Related X account** | Claude ([@claudeai](https://x.com/claudeai)) — also tracked as an X builder |
| **Source type** | Blog (`blogs`) |

### 2. Claude Blog

| Field | Value |
|-------|-------|
| **Name** | Claude Blog |
| **Description** | Product announcements and updates for Claude |
| **Index URL** | https://claude.com/blog |
| **Article base URL** | https://claude.com/blog/ |
| **Type** | `scrape` |
| **Fetch method** | `http` |
| **Organization** | Anthropic / Claude |
| **Content focus** | Product launches, feature updates, company news |
| **Related X account** | Claude ([@claudeai](https://x.com/claudeai)) — also tracked as an X builder |
| **Source type** | Blog (`blogs`) |

---

## Field reference

| Field in config | Description |
|-----------------|-------------|
| `name` | Display name used in digests |
| `type` | How the source is ingested (`scrape` = crawl index + articles) |
| `indexUrl` | Listing / index page used to discover new posts |
| `articleBaseUrl` | URL prefix for individual articles |
| `fetchMethod` | Transport used upstream (`http`) |

## Notes

- Full articles are scraped by the central feed and remixed into digests with original links preserved.
- Source list is managed centrally (see [follow-builders](https://github.com/zarazhangrui/follow-builders)).
- Related files: [builders.md](./builders.md) · [podcasts.md](./podcasts.md)
