# OpenClaw Production Gotchas

**Source:** https://kaxo.io/insights/openclaw-production-gotchas/  
**Saved:** 2026-02-12

## Critical Pitfalls to Remember

### 1. The Four Model Stores
- Main config file
- Session state files (cron sessions bake model at creation)
- Cron job payloads
- Model allowlist

**Fix:** Change ALL four or crons will use stale models. Test with a cron, not interactive session.

### 2. Silent Heartbeat Failures
- Missing `models.json` in agent dir = heartbeat never fires
- No error, no log
- Check: SOUL.md, models.json, auth-profiles.json must exist

### 3. Gateway Race Condition
- **NEVER edit config while gateway is running**
- Gateway writes in-memory state to disk on shutdown
- **Correct order:** Stop gateway → Edit files → Start gateway

### 4. Invalid Config Keys Prevent Hot Reload
- `openclaw doctor --fix` finds stale/invalid keys
- Invalid keys silently block hot reload
- After any upgrade, run doctor immediately

### 5. Agents Writing Their Own Config
- Agents can hallucinate and write bad configs
- **Defense:** `chmod 444` on workspace files (NOT gateway-managed files)
- Gateway needs write: models.json, auth-profiles.json, auth.json

### 6. Upgrade Drift
- Every update is a potential migration
- Snapshot ~/.openclaw/ before upgrading
- Run `openclaw doctor --fix` after
- Regenerate gateway token after major version jumps

### 7. Heartbeat Model Choice
- Don't route heartbeats to local models (unreliable)
- Use cheapest API model for heartbeats
- Right-size context windows to actual platform limits

## Key Commands
```bash
# Validate config
openclaw doctor

# Fix invalid keys
openclaw doctor --fix

# Check model allowlist
openclaw models list --allowed

# Test cron with specific model
openclaw cron run <jobId> --model openrouter/moonshotai/kimi-k2.5
```

## Pre-Restart Checklist
- [ ] Stop gateway (don't use restart)
- [ ] Edit config files
- [ ] Run `openclaw doctor` to validate
- [ ] Start gateway
- [ ] Verify heartbeat fires correctly
