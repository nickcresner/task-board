# HEARTBEAT.md - Proactive Checks

This file controls what I check during heartbeat polls.

## Check Schedule

**Email Checks:**
- 3x daily: 10:00, 14:00, 18:00 (UK time)
- Check for urgent/actionable emails
- Summarize if anything needs attention

**What to look for:**
- Starfish Properties maintenance issues
- The Maintenance Team emails (accounts@themaintenanceteam.co.uk)
- Urgent/priority flagged messages
- Invoices or payment requests
- Calendar invites requiring response

## Action Rules

**Alert immediately if:**
- Maintenance issues from Starfish/Arthur Online
- Emails from The Maintenance Team requiring action
- Payment due notifications
- Calendar events in next 2 hours
- Any email marked as "urgent" or "action required"

**Daily summary at:**
- 7:00am (morning briefing)
- 18:00 (end-of-day check)

## Skip checks when:
- Late night (23:00-08:00) unless urgent
- Weekend unless marked urgent
- Human is clearly in conversation

## TODO Integration

When checking emails, cross-reference with TODO.md:
- Any TODO items mentioned in emails?
- Payment reminders for TODO items?
- New tasks to add?

## Tracking

Check status tracked in: `memory/heartbeat-state.json`

Last email check: Check this file for timestamp
