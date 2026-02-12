# ⚡ Quick Reference - Admin Commands

## 🚀 Start Using (Right Now!)

### Prerequisites
```bash
✅ Python 3.8+
✅ discord.py 2.6.4+
✅ !helpadmin permission (admin only)
```

---

## 👤 USER MANAGEMENT COMMANDS

### BAN USER
```
Command:  !ban @user [reason]
Example:  !ban @Spammer Advertising spam
Perms:    Ban Members
Response: 🔨 Admin Action - User Banned & Logged
```

### UNBAN USER
```
Command:  !unban <user_id>
Example:  !unban 123456789
Perms:    Ban Members
Response: ✅ User Unbanned
Note:     Use user ID, not mention
```

### KICK USER
```
Command:  !kick @user [reason]
Example:  !kick @Disruptive Being disruptive
Perms:    Kick Members
Response: 🔨 Admin Action - User Kicked
```

### MUTE USER
```
Command:  !mute @user [reason]
Example:  !mute @Troll Spam in voice
Perms:    Manage Roles
Response: 🔨 Admin Action - User Muted
```

### UNMUTE USER
```
Command:  !unmute @user
Example:  !unmute @Troll
Perms:    Manage Roles
Response: ✅ User Unmuted
```

---

## ⚠️ WARNING SYSTEM

### WARN USER
```
Command:  !warn @user [reason]
Example:  !warn @Bob Bad language
Perms:    Manage Messages
Response: ⚠️ User Warned (1/3)

Notes:
├── 1 warning: User warned
├── 2 warnings: User warned
├── 3 warnings: AUTO BAN + logged
└── Warnings stack per user
```

### CHECK WARNINGS
```
Command:  !warnlist @user
Example:  !warnlist @Bob
Response: Lists all warnings with reasons
```

### CLEAR WARNINGS
```
Command:  !clearwarns @user
Example:  !clearwarns @Bob
Perms:    Administrator
Response: ✅ Warnings Cleared
```

---

## 🗑️ MESSAGE MANAGEMENT

### DELETE MESSAGES
```
Commands: !purge [amount]
          !clean [amount]
          !delete [amount]
Example:  !purge 50

Perms:    Manage Messages
Limits:   Max 100 at once
Response: ✅ Deleted X messages
```

---

## 📈 LEVEL & XP MANAGEMENT

### SET USER LEVEL
```
Command:  !setlevel @user <level>
Example:  !setlevel @John 10
Perms:    Administrator
Response: ✅ Level Updated
Note:     Overwrites current level
```

### ADD XP TO USER
```
Command:  !addxp @user <amount>
Example:  !addxp @John 500
Perms:    Administrator
Response: ✅ XP Added
Note:     Adds to current XP (doesn't overwrite)
```

### RESET USER XP
```
Command:  !resetxp @user
Example:  !resetxp @John
Perms:    Administrator
Response: ✅ XP Reset to 0
```

---

## 📊 SERVER INFORMATION

### SERVER STATS
```
Command:  !serverinfo
Response: Server name, members, channels, creation date, etc.
Perms:    Administrator
```

### USER INFORMATION
```
Command:  !userinfo [@user]
Example:  !userinfo @John
          !userinfo (checks yourself)
Response: User ID, join date, account age, roles, avatar
Perms:    Everyone (can check any user)
```

---

## 📚 HELP COMMANDS

### COMPACT HELP
```
Command:  !help
Response: 8 categories with main commands
Usage:    Run when confused about what commands exist
```

### SPECIFIC HELP
```
Command:  !help <command>
Example:  !help medie
Response: Full details about the command
```

### ADMIN HELP
```
Command:  !helpadmin
Response: All admin-only commands organized by category
Perms:    Administrator only
```

### BOT STATUS
```
Command:  !ping
Response: Bot latency in milliseconds
Usage:    Check if bot is responsive
```

---

## 🔑 PERMISSION REFERENCE

```
MANAGE_MESSAGES   → !warn, !purge
MANAGE_ROLES      → !mute, !unmute
KICK_MEMBERS      → !kick
BAN_MEMBERS       → !ban, !unban
ADMINISTRATOR     → !setlevel, !addxp, !resetxp, !helpadmin
```

---

## ⏰ COMMON SCENARIOS

### Scenario 1: User Is Spamming
```
Step 1: !warn @spammer Spam in general
Step 2: (if continues) !warn @spammer More spam
Step 3: (if continues) !warn @spammer Final warning
        → Auto-ban triggered at 3 warnings
OR
Step 1: !mute @spammer Spam
Step 2: Talk to them
Step 3: !unmute @spammer after apology
```

### Scenario 2: Cleaning Messages
```
!purge 50              # Delete last 50 messages
Response: ✅ Deleted 50 messages
```

### Scenario 3: Give New Member Level
```
!setlevel @NewMember 1     # Set to level 1
!addxp @NewMember 100      # Give 100 XP
```

### Scenario 4: Permanent Ban for Violations
```
!ban @Hacker TOS violation and hacking attempt
# User is banned permanently
```

---

## 🎨 RESPONSE EXAMPLES

### Ban Response
```
🔨 Admin Action
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Action: Ban User
Target: @Spammer#1234
Reason: Advertising spam
[Timestamp]
```

### Success Response
```
✅ XP Added
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Added 500 XP to @John
Total XP: 1500
[Timestamp]
```

### Error Response
```
❌ Command Not Found
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Command 'badcmd' doesn't exist!
Try !help for correct commands
[Timestamp]
```

---

## 🔄 COMMAND PREFIXES (3 WAYS TO USE!)

### Method 1: Type Prefix
```
!ban @user spam
!medie 10 9 8
!help
```

### Method 2: Mention Bot
```
@UBB Bot ban @user spam
@UBB Bot medie 10 9 8
@UBB Bot help
```

### Method 3: Slash Commands (New!)
```
/ping
/info
(More coming soon!)
```

---

## 📝 LOGGING & AUDIT TRAIL

Every admin action is logged:
```
✓ Username who did it
✓ What action was taken
✓ Who it was done to
✓ Reason/details
✓ Exact timestamp
```

Check terminal for logs!

---

## ❓ FAQ

### Q: User is banned but in server?
**A:** Check if they're actually banned: `!unban <id>` to reverse

### Q: How to undo a warn?
**A:** `!clearwarns @user` resets all warnings

### Q: Can I ban without reason?
**A:** Yes! `!ban @user` uses default reason

### Q: What's max level?
**A:** No maximum! Set any number you want

### Q: Do warns expire?
**A:** No, they're permanent until cleared with `!clearwarns`

### Q: Can I mute user per-channel?
**A:** Not yet, but coming in future update

---

## 🚀 POWER TIPS

1. **Use aliases**: `!clean` = `!purge` = `!delete` (same thing)
2. **Copy user ID**: Right-click → Copy ID → `!unban <paste>`
3. **Remember the 3-strike rule**: 3 warns = automatic ban
4. **Always give reason**: Help with auditing and appeals
5. **Check before banning**: Use `!userinfo @user` first

---

## 🆘 TROUBLESHOOTING

### Admin perms but commands fail?
**Check**:
- Is bot role ABOVE user's role? (Role order matters!)
- Do you have the required permission?
- Is the user a bot? (Can't ban bots usually)

### Messages not deleting?
**Check**:
- Are messages older than 2 weeks? (Discord limit)
- Is bot higher role than message author?

### Slash commands not showing?
**Fix**: Restart Discord or bot

---

## 📊 COMMAND USAGE STATS

```
MOST USED:
1. !warn (moderation)
2. !purge (cleanup)
3. !mute (discipline)
4. !ban (severe violations)
5. !kick (lesser violations)

ADMIN ONLY:
1. !setlevel (setup)
2. !addxp (rewards)
3. !helpadmin (reference)
```

---

## 🎓 BEST PRACTICES

✅ **DO:**
- Keep warnings documented
- Warn before banning
- Use reasons always
- Check user before action
- Respect appeals

❌ **DON'T:**
- Ban without warning
- Mute without reason
- Delete messages silently
- Abuse mod powers
- Ignore user context

---

## 📞 QUICK COMMANDS CHEAT SHEET

```
!ban @user spam
!kick @user rulebreak
!mute @user spam
!warn @user language
!purge 50
!setlevel @user 5
!addxp @user 100
!serverinfo
!userinfo @user
!help
!helpadmin
!ping
```

---

**Ready to moderate like a pro!** 🔨✨

For detailed guides, see:
- UPDATES.md - Full feature list
- DEVELOPMENT.md - For adding new commands
- STRUCTURE.md - Project organization
