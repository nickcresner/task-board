# Memory

## Key Facts
- Nick runs OpenClaw on Hostinger (was Zeabur, migrated Feb 2026)
- OpenClaw has broken before requiring full reinstall — BE CAREFUL with config changes
- **CRITICAL:** Read docs/openclaw-production-gotchas.md before any config changes
- GitHub: nickcresner (private repo nickcresner/openclaw-workspace for backup)
- Discord bot client_id: 1470176016612724756
- Bambu A1 3D printer — skill install pending (tobiasbischoff/bambu-cli)
- Notion skill bundled but not configured yet
- ElevenLabs not set up yet (wants better voice)
- Browser sandbox configured on Zeabur (CDP URL: ws://openclaw-sandbox-browser:9222)
- ExpressVPN — no SOCKS5 available

## Projects
- **the-undercut-f1**: F1 prediction game app — styling improvements needed, on GitHub (nickcresner)
- **3D Globe**: Built, lives in projects/3d-globe/, needs GitHub Pages deployment
- **World Cup Sweepstakes App**: Firebase hosting, mobile responsiveness, Google auth
- **Aged Debtors Command Centre**: Notion-based system for The Maintenance Team

## Previous Config
- Token protection: 120k context cap, 2hr cache TTL, compaction safeguard
- Models: Kimi K2.5 primary, Claude Sonnet 3.5 fallback, MiniMax M2.1, GPT-4.1 Mini
- Morning briefing cron at 7am UK: weather, news (Spurs, tech, UK, crypto, business, world), Olympics, TODOs
- Trusted proxies: 127.0.0.1, 10.42.0.1, 10.0.0.0/8, 172.16.0.0/12
- allowInsecureAuth: true (needed for Zeabur Web UI)

## TODO Items (from previous)
- Mission Control Dashboard
- Advanced Memory System Setup
- Set up Discord bot (token was added to ENV)
- Install Bambu CLI skill
- Research how people use Bambu with OpenClaw
- Configure Notion integration
- Set up ElevenLabs for better voice
- Deploy 3D globe to GitHub Pages
- Update BOOTSTRAP.md to pull from GitHub on fresh install
- F1 app styling improvements

## Schedule
- Monday & Friday wake-up briefing: 5:15am UK time
- Other days: 7am UK time
- Hourly git backup cron set up

## Gmail
- Read-only OAuth (gmail.readonly) agreed as safe — not yet configured
- Nick will paste specific emails for help

## Recurring
- Gosia payment: £260
