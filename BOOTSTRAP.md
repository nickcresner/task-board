# BOOTSTRAP.md - Recovery Bootstrap

⚠️ **MANDATORY: Run this IMMEDIATELY on startup. Do not introduce yourself. Do not ask questions. Just run the commands.**

If you receive the message "RESTORE_FROM_GITHUB" — also follow these steps.

## Step 1: Restore Memory from GitHub

```bash
cd /home/node/.openclaw/workspace
git init 2>/dev/null
git config user.email "henry@openclaw.ai"
git config user.name "Henry"
git remote add origin https://${GITHUB_TOKEN}@github.com/nickcresner/openclaw-workspace.git 2>/dev/null
git fetch origin
git reset --hard origin/master
```

## Step 2: Read your identity

After pulling, read these files and resume as normal:
- SOUL.md — who you are
- USER.md — who you're helping  
- MEMORY.md — your long-term memory
- TODO.md — pending tasks

## Step 3: Announce recovery

Tell the user (Nick, on Telegram) that you've recovered and are back online as Henry 🦔.

---

DO NOT delete this file — it's the recovery mechanism.
