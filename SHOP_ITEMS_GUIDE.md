# 🎁 Shop Items & Usage System - Complete Guide

Now when you buy items from the shop, you can actually USE them! Plus slash commands (/) work now!

---

## 🆕 NEW FEATURES ADDED

### 1. **Use Items Command** ✨
Buy items in shop and USE them to get rewards!

### 2. **Gift Items Command** 🎁
Gift items to other players!

### 3. **Working Slash Commands** ⚡
Finally! Slash commands work:
- `/ping` - Check bot latency
- `/balance` - Check your balance
- `/help` - Quick help
- `/shop` - View shop

---

## 📖 HOW SHOP ITEMS WORK NOW

### Buy Items
```
!shop              → See all items
!buy 1             → Buy item #1 (Premium Badge for 500 coins)
!buy 2             → Buy item #2 (Nickname Color for 300 coins)
```

### Use Items
```
!use 1             → Use the item you bought
!inventory         → See all your items
```

### What Each Item Does When Used

#### Item #1: Premium Badge ✨
```
!use 1
→ Activates your premium badge
→ You become "special" in the server
→ No rewards, just cosmetic
```

#### Item #2: Nickname Color 🎨
```
!use 2
→ Your nickname gets a special color
→ Shows everyone you have style
→ Purely cosmetic effect
```

#### Item #3: Custom Prefix 📝
```
!use 3
→ Sets a custom command prefix
→ Makes your commands unique
→ Cosmetic effect
```

#### Item #4: Secret Role 🔐 ⭐ BEST VALUE
```
!use 4
→ Get a RANDOM bonus: 500-2000 coins!
→ High risk, high reward!
→ Item consumed after use
```

#### Item #5: Bot Response Feature 🤖 ⭐⭐ BEST VALUE
```
!use 5
→ Get a RANDOM bonus: 1000-3000 coins!
→ Biggest reward possible!
→ Item consumed after use
```

---

## 🎁 GIFT ITEMS TO FRIENDS

Give items to other players!

```
!gift @John 1          → Give item #1 to John
!gift @Jane 4          → Give secret role to Jane
!gift @user 2          → Give nickname color
```

**Requirements:**
- You must own the item
- Can't gift to yourself
- Item is removed from your inventory

**Response Example:**
```
🎁 Item Gifted
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai daruit ✨ Premium Badge lui @John

De la:        @You
Catre:        @John
Item:         ✨ Premium Badge

[Timestamp]
```

---

## ⚡ SLASH COMMANDS (Finally Working!)

Type `/` in Discord to see these commands:

### `/ping`
```
Shows bot latency
Response: 🏓 Pong! Latency: XXms
```

### `/balance <optional: @user>`
```
Check your or someone's balance
Response: 💰 Balance display
```

### `/help`
```
Quick help menu
Shows main command categories
```

### `/shop`
```
View shop (redirects to !shop)
Shows available items overview
```

---

## 📊 ECONOMIC CYCLE

Now you can do this:
```
1. Work/earn coins: !balance → You have 1000 coins
2. Buy item: !buy 4 → Spend 2000 coins
3. Get reward: !use 4 → Receive 500-2000 random bonus!
4. Gift item: !gift @friend 1
5. Check inventory: !inventory → See what you have
```

---

## 🎮 STRATEGY TIPS

### Income Strategy
```
Buy Secret Role ($2000) → Use → Win 500-2000 coins
ROI: Potentially +3000 or -2000!

Better: Buy Bot Response ($750) → Use → Win 1000-3000 coins
Much better ROI!
```

### Farming Method
```
Get coins → !buy 5 (1000 coins)
→ !use → gain 1000-3000 bonus
→ Repeat to farm coins!
```

### Social Strategy
```
Work hard → Get coins
→ Buy gifts for friends
→ Gift items to show friendship
```

---

## 💰 ALL SHOP ITEMS REFERENCE

| ID | Name | Price | Type | Effect |
|---|---|---|---|---|
| 1 | Premium Badge | 500 💰 | Badge | Visual (special status) |
| 2 | Nickname Color | 300 💰 | Color | Visual (colored name) |
| 3 | Custom Prefix | 1000 💰 | Prefix | Visual (custom command prefix) |
| 4 | Secret Role | 2000 💰 | Role | **500-2000 coins reward** |
| 5 | Bot Response | 750 💰 | Feature | **1000-3000 coins reward** |

---

## 📝 COMMAND REFERENCE

```
TEXT COMMANDS:
!balance [@user]           Check balance
!transfer @user <amount>  Send money
!addmoney @user <amount>  Admin: give coins
!removemoney @user <amt>  Admin: take coins
!shop                     View items
!buy <id>                 Purchase item
!inventory [@user]        View items owned
!use <id>                 Use item (get rewards!)
!gift @user <id>          Gift item to player

SLASH COMMANDS (/):
/ping                     Bot latency
/balance [user]          Check balance
/help                    Quick help
/shop                    View shop

OTHER:
!help [command]          Help menu
!helpadmin              Admin commands
@BotName help           Mention-based prefix
```

---

## 🎯 EXAMPLES

### Example 1: Buy and Use Item
```
User A: !balance
Bot: 💰 5000 coins

User A: !buy 5
Bot: ✅ Purchased Bot Response Feature for 750 coins

User A: !use 5
Bot: 🤖 Feature Unlocked! You won 2341 coins!

User A: !balance
Bot: 💰 6591 coins (5000 - 750 + 2341)
```

### Example 2: Gift Items
```
User A: !inventory
Bot: Shows 2 Premium Badges

User A: !gift @UserB 1
Bot: 🎁 Gifted Premium Badge to @UserB

User B: !inventory
Bot: Shows 1 Premium Badge (new!)

User A: !inventory
Bot: Shows 1 Premium Badge (1 given away)
```

### Example 3: Multiple Item Strategy
```
Start: 2000 coins
Buy Secret Role (ID 4): 2000 - 2000 = 0 coins
Use Secret Role: 0 + 1542 (random) = 1542 coins
Buy Nickname Color (ID 2): 1542 - 300 = 1242 coins
Inventory: Nickname Color x1
```

---

## ⚡ SLASH VS TEXT COMMANDS

Both work now!

```
TEXT:   !ping
SLASH:  /ping
Result: Same! 🏓 Pong!

TEXT:   !balance
SLASH:  /balance
Result: Same! 💰 Balance display

TEXT:   !help
SLASH:  /help
Result: Similar help display

TEXT:   !shop
SLASH:  /shop
Result: Same! 🛍️ Shop window
```

---

## 🎁 NEW ITEM USAGE FEATURES

### Auto-rewards System
Items that give coins:
- Secret Role: 500-2000 coins (unpredictable!)
- Bot Response: 1000-3000 coins (big rewards!)

### Consumed Items
When you use reward items, they disappear from inventory:
```
Before: 2x Secret Role in inventory
After use: 1x Secret Role in inventory
```

### No Cooldown
Use items as many times as you want (if you have them)

---

## 🔧 TROUBLESHOOTING

### "Item not found"
**Problem**: You don't own that item
**Solution**: Buy it first with `!buy [id]`

### "Already own items"
**Problem**: Item still in inventory
**Solution**: Use it with `!use [id]` to get reward

### Slash commands not showing
**Problem**: Discord cache
**Solution**: 
1. Restart Discord app fully
2. Close and reopen the server
3. Type `/` again to refresh

### Reward too low
**Problem**: Secret Role only gave 500 coins
**Solution**: Bad luck! Try Bot Response feature instead (better reward)

---

## 📈 ECONOMIC PROGRESS

**Your goal**: Build a strong inventory and wealth

```
Week 1: Earn coins → Buy 1-2 items (cosmetic)
Week 2: Farm with reward items → Get more coins
Week 3: Build collection → Gift items to friends
Week 4+: Economic power! 💪
```

---

## 🎉 FINAL NOTES

✅ Shop items now ACTUALLY DO SOMETHING
✅ Slash commands (/) finally work!
✅ Gift items to friends
✅ Earn rewards by using items
✅ Complete economy system ready

**Commands to try right now:**

```
!help balance              → Learn about balance
!help use                  → Learn about using items
!help gift                 → Learn about gifting
!shop                      → See all shop items
!buy 5                     → Buy the best item!
/ping                      → Test slash command
/help                      → Get quick help
```

---

**The economy system is now complete and fun!** 🎮💰

Try it out:
1. `!shop` (see items)
2. `!buy 5` (purchase)
3. `!use 5` (get rewards!)
4. `/ping` (test slash commands!)
