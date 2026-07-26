# Follow Builders — Podcasts

> Source: `follow-builders` skill · `config/default-sources.json` · `podcasts`  
> Total: **6** podcasts  
> Content: YouTube / podcast episodes (transcripts via central feed)

These are the AI podcasts tracked by the Follow Builders digest. The list is curated centrally and may update over time.

---

## Overview

| # | Name | Public URL | RSS / Feed |
|---|------|------------|------------|
| 1 | Latent Space | https://www.youtube.com/@LatentSpacePod | [RSS](https://pod2txt.vercel.app/api/feed?url=https://api.substack.com/feed/podcast/1084089.rss) |
| 2 | Training Data | https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8 | [RSS](https://feeds.megaphone.fm/trainingdata) |
| 3 | No Priors | https://www.youtube.com/@NoPriorsPodcast | [RSS](https://feeds.megaphone.fm/nopriors) |
| 4 | Unsupervised Learning | https://www.youtube.com/@RedpointAI | [RSS](https://feeds.simplecast.com/dOSE_bdP) |
| 5 | The MAD Podcast with Matt Turck | https://www.youtube.com/@DataDrivenNYC/videos | [RSS](https://anchor.fm/s/f2ee4948/podcast/rss) |
| 6 | AI & I by Every | https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL | [RSS](https://anchor.fm/s/ed1f5584/podcast/rss) |

---

## Detail entries

### 1. Latent Space

| Field | Value |
|-------|-------|
| **Name** | Latent Space |
| **Public URL** | https://www.youtube.com/@LatentSpacePod |
| **YouTube / channel** | `@LatentSpacePod` |
| **RSS URL** | https://pod2txt.vercel.app/api/feed?url=https://api.substack.com/feed/podcast/1084089.rss |
| **Underlying Substack feed** | https://api.substack.com/feed/podcast/1084089.rss |
| **Source type** | Podcast (`podcasts`) |
| **Notes** | RSS is proxied via `pod2txt.vercel.app` for transcript-friendly feed access |

### 2. Training Data

| Field | Value |
|-------|-------|
| **Name** | Training Data |
| **Public URL** | https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8 |
| **YouTube playlist ID** | `PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8` |
| **RSS URL** | https://feeds.megaphone.fm/trainingdata |
| **RSS host** | Megaphone |
| **Source type** | Podcast (`podcasts`) |

### 3. No Priors

| Field | Value |
|-------|-------|
| **Name** | No Priors |
| **Public URL** | https://www.youtube.com/@NoPriorsPodcast |
| **YouTube / channel** | `@NoPriorsPodcast` |
| **RSS URL** | https://feeds.megaphone.fm/nopriors |
| **RSS host** | Megaphone |
| **Source type** | Podcast (`podcasts`) |

### 4. Unsupervised Learning

| Field | Value |
|-------|-------|
| **Name** | Unsupervised Learning |
| **Public URL** | https://www.youtube.com/@RedpointAI |
| **YouTube / channel** | `@RedpointAI` (Redpoint) |
| **RSS URL** | https://feeds.simplecast.com/dOSE_bdP |
| **RSS host** | Simplecast |
| **Source type** | Podcast (`podcasts`) |

### 5. The MAD Podcast with Matt Turck

| Field | Value |
|-------|-------|
| **Name** | The MAD Podcast with Matt Turck |
| **Public URL** | https://www.youtube.com/@DataDrivenNYC/videos |
| **YouTube / channel** | `@DataDrivenNYC` |
| **Host (related builder)** | Matt Turck ([@mattturck](https://x.com/mattturck)) — also tracked as an X builder |
| **RSS URL** | https://anchor.fm/s/f2ee4948/podcast/rss |
| **RSS host** | Anchor / Spotify for Podcasters |
| **Source type** | Podcast (`podcasts`) |

### 6. AI & I by Every

| Field | Value |
|-------|-------|
| **Name** | AI & I by Every |
| **Public URL** | https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL |
| **YouTube playlist ID** | `PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL` |
| **Publisher** | Every |
| **Related builder** | Dan Shipper ([@danshipper](https://x.com/danshipper)) — also tracked as an X builder |
| **RSS URL** | https://anchor.fm/s/ed1f5584/podcast/rss |
| **RSS host** | Anchor / Spotify for Podcasters |
| **Source type** | Podcast (`podcasts`) |

---

## Field reference

| Field in config | Description |
|-----------------|-------------|
| `name` | Display name used in digests |
| `url` | Public / YouTube page for the show |
| `rssUrl` | Podcast RSS feed used for episode discovery (and transcript pipeline upstream) |

## Notes

- Episode transcripts and metadata are fetched by the central feed; the agent does not scrape YouTube or call third-party APIs itself.
- Source list is managed centrally (see [follow-builders](https://github.com/zarazhangrui/follow-builders)).
- Related files: [builders.md](./builders.md) · [blogs.md](./blogs.md)
