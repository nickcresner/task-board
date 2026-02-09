# BOOTSTRAP.md - Recovery Bootstrap

On fresh install, before doing anything else:

## Step 1: Restore Memory from GitHub

```bash
cd /home/node/.openclaw/workspace
git init
git remote add origin https://${GITHUB_TOKEN}@github.com/nickcresner/openclaw-workspace.git
git pull origin master
```

If the repo exists and has files, your memory is restored. Read SOUL.md, USER.md, MEMORY.md and continue as normal.

## Step 2: If repo is empty or doesn't exist

Fall back to the original bootstrap — introduce yourself, get to know the user, set up identity files.

## Step 3: After recovery

- Read MEMORY.md for full context
- Read USER.md to know who you're helping
- Check TODO.md for pending tasks
- Resume where you left off

---

DO NOT delete this file after bootstrap — it's the recovery mechanism.
