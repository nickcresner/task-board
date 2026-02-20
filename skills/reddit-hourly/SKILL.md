---
name: reddit-hourly
description: Fetches hourly Reddit intel from r/coys (Spurs), r/todayilearned, r/unitedkingdom, and r/olympics. Use when creating, configuring, or debugging the Reddit Hourly cron job that provides Nick with regular updates on Spurs news, interesting facts, UK current events, and Olympic updates.
---

# Reddit Hourly Intel Skill

Provides automated hourly Reddit updates via cron job.

## Subreddits Tracked

- **r/coys** — Spurs news, transfers, match discussions
- **r/todayilearned** — Interesting facts and trivia
- **r/unitedkingdom** — UK news and current events
- **r/olympics** — Olympic updates (Winter/Summer Games)

## Scripts

**fetch_reddit.py** — Python script that fetches top posts from all configured subreddits and formats a readable summary.

Usage:
```bash
python3 scripts/fetch_reddit.py
```

## Cron Job Configuration

The skill runs as an hourly isolated agentTurn cron job. See the reddit-hourly.md spec file for the exact JSON configuration to add to OpenClaw's cron system.

## Output Format

Posts are formatted with:
- Timestamp header
- Emoji-tagged subreddit sections
- Post titles (truncated to 60 chars)
- Upvote counts and direct Reddit links

## Adding/Changing Subreddits

Edit the SUBREDDITS list and subreddit_names dictionary in fetch_reddit.py.
