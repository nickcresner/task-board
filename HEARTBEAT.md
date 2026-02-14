# HEARTBEAT.md - Quick Checks Only

## Every 30 Minutes
- [ ] Check active tasks stale? (>2h no update)
- [ ] Archive bloated sessions (>2MB)
- [ ] Self-review every ~4 hours

## Email Checks (10am, 2pm, 6pm)
- Starfish/The Maintenance Team urgent issues
- Payment requests
- Calendar events <2h

## Skip When
- 23:00-08:00 unless urgent
- Weekend unless urgent
- User is in conversation

## Heavy Work → Cron Jobs
- Content research: 6am cron
- News summary: 8am cron
- Daily recap: 6pm cron
- Credit check: hourly cron
- Memory cleanup: hourly cron

Last check: see memory/heartbeat-state.json
