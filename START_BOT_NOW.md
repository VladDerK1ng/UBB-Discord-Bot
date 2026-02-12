# ⚡ START BOT NOW - 2 Minute Setup

Quick steps to get your bot running **right now**.

---

## Step 1: Install Dependencies (30 seconds)

```bash
pip install -r requirements.txt
```

**What it does**: Installs discord.py and all required packages

---

## Step 2: Verify Bot Token (30 seconds)

Check if your bot token is set in `config.py`:

```python
# In config.py, find:
TOKEN = "your_bot_token_here"
```

**Don't have a token?**
1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Go to "Bot" tab
4. Click "Add Bot"
5. Click "Copy" under TOKEN
6. Paste into config.py

---

## Step 3: Run Bot (10 seconds)

```bash
python main.py
```

**You should see:**
```
2024-XX-XX 14:32:45 - Bot is running!
Features: Text commands (!) • Slash commands (/) • Ping prefix
Ready! Logged in as YourBotName#1234
```

**If error**: Check token is correct and bot has internet access

---

## Step 4: Test in Discord (30 seconds)

Go to your Discord server and type:

```
!help
```

**You should see**: 8 categories of commands with emojis

**Other quick tests**:
```
!ping                    → Shows bot latency
!info                    → Shows bot information
!helpadmin              → Admin commands (if you're admin)
@BotName help           → Also works! (ping prefix)
```

---

## ✅ If Everything Works

Congratulations! Your bot is running!

**Next steps:**
1. Read ADMIN_QUICK_REFERENCE.md for all commands
2. Run TESTING_CHECKLIST.md to verify all features
3. Start using admin commands like `!ban`, `!warn`, `!purge`

---

## ❌ If Something Doesn't Work

### Problem: "Bot not responding"
```
Check:
1. Is bot online in Discord? (see online status)
2. Is bot in your server? (check member list)
3. Is terminal showing "Ready! Logged in as..."?
4. Try: !help (not /help)
```

### Problem: "Permission Denied"
```
Check:
1. Are you an administrator in the server?
2. Is the bot's role above your role?
3. Does bot have required permissions?
Fix: Drag bot role higher in role list
```

### Problem: "Command Not Found"
```
Check:
1. Is command name correct? (typo?)
2. Try: !help to see all commands
3. Try: !helpadmin for admin commands
```

### Problem: Token Error
```
Check:
1. Is token in config.py correct?
2. Did you use correct quotes?
3. Is there extra spaces? (trim them)
Fix: Copy token again from Discord Developer Portal
```

---

## 🎯 Most Used Commands (Copy-Paste Ready)

### For Admins

```
!helpadmin                          → See all admin commands
!warn @user reason                  → Warn a user
!ban @user reason                   → Ban a user
!kick @user reason                  → Kick a user
!mute @user reason                  → Mute in voice
!unmute @user                       → Unmute user
!purge 50                          → Delete last 50 messages
!setlevel @user 10                 → Set user to level 10
!addxp @user 100                   → Give user 100 XP
!userinfo @user                    → See user details
```

### For Everyone

```
!help                               → See all commands
!ping                              → Check bot response time
!info                              → Bot information
```

---

## 📋 Command Syntax

### Required Arguments
```
!ban @user              ← @user is REQUIRED (blue in help)
```

### Optional Arguments
```
!ban @user [reason]     ← [reason] is OPTIONAL (in brackets)
```

### Copy These Examples

```bash
# Warn with reason
!warn @JohnDoe Spam in general

# Ban without reason
!ban @JohnDoe

# Purge messages
!purge 100

# Set level
!setlevel @JohnDoe 5

# Add XP
!addxp @JohnDoe 500
```

---

## 🔐 Permission Levels (Who Can Use What)

```
Everyone:           !help, !ping, !info
Administrators:     !ban, !kick, !helpadmin, !warn, !purge, !setlevel, !addxp
Manage Messages:    !warn, !purge
Ban Members:        !ban, !unban
Kick Members:       !kick
Manage Roles:       !mute, !unmute
```

---

## 💾 Where Data Is Saved

```
📁 data/
├── user_stats.json      ← User levels, XP
├── server_settings.json ← Server config
├── verification.json    ← Verification status
└── shop.json           ← Shop items
```

**Important**: Don't manually edit these files while bot is running!

---

## 🎨 All Features at a Glance

✅ Text commands (! prefix)
✅ Mention commands (@BoName)
✅ Slash commands (/) 
✅ Admin tools (ban, kick, mute, warn)
✅ Warning system (auto-ban at 3)
✅ Message cleanup (purge)
✅ Level management (XP/levels)
✅ User info (userinfo)
✅ Server info (serverinfo)
✅ Error handling (emoji responses)
✅ Data persistence (saved to JSON)
✅ Emoji aesthetics (❌ ✅ ⚠️ 🔨)
✅ Timestamps (on every message)

---

## 🚀 Advanced (Optional)

### Running in Background (Windows)

```bash
# Keep bot running after closing terminal:
python -m pip install pywin32
python main.py
# Then minimize, don't close
```

### Running on Linux/Mac

```bash
# Run in screen session
screen -S discord_bot
python main.py
# Press Ctrl+A then D to detach
# Type: screen -r discord_bot  # to reconnect
```

### Running with Auto-Restart

```bash
# Create a loop that restarts on crash
:loop
python main.py
goto loop
```

---

## 📞 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot offline | Restart: `python main.py` |
| Commands not working | Check token setup |
| Permission denied | Make sure you're admin |
| Slash commands missing | Restart Discord app |
| Data not saving | Check data/ folder exists |
| Bot slow | Restart bot, check internet |

---

## 📖 Need More Help?

- **Quick Reference**: ADMIN_QUICK_REFERENCE.md
- **Full Testing**: TESTING_CHECKLIST.md
- **Full Documentation**: README_COMPREHENSIVE.md
- **Technical Details**: UPDATE_COMPLETE.md
- **Development**: DEVELOPMENT.md

---

## 🎉 YOU'RE READY!

Your bot is now running with:
- 15+ admin commands
- Professional emoji design
- Multiple command prefixes
- Complete error handling
- Data persistence

**Run this now:**
```bash
python main.py
```

**Then type in Discord:**
```
!help
```

**Done!** Start using commands like:
- `!warn @user reason`
- `!ban @user reason`
- `!purge 50`

---

**Questions?** See the full documentation files above.

**Happy moderating!** 🤖✨
