# 💰 Money System - Complete Guide

Beautiful aesthetic money management commands for Discord UBB Bot.

---

## 🎯 Quick Start

### For Everyone
```
!balance [@user]    → See your or another user's balance
!transfer @user 50  → Send money to another user
!shop               → View available items to buy
!buy [item_id]      → Purchase an item  
!inventory [@user]  → View your items/balance
```

### For Admins ONLY
```
!addmoney @user 1000     → Give money to a user
!removemoney @user 500   → Take money from a user
```

---

## 📊 All Money Commands (Detailed)

### 💚 BALANCE
**See how much money you or someone else has**

```
Command:  !balance [@user]
Example:  !balance
          !balance @John
Perms:    Everyone
```

**Response Example:**
```
💰 Balanta lui John
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 5000 UBB Coins

[Timestamp]
```

---

### 📤 TRANSFER
**Send money to another player**

```
Command:  !transfer @user <amount>
Example:  !transfer @John 500
Perms:    Everyone
```

**Requirements:**
- Amount must be positive (> 0)
- Can't send to yourself
- Must have enough balance

**Response Example - Success:**
```
✅ Transfer Complet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai trimis 💰 500 catre @John

De la:          @You
Catre:          @John
Suma:           💰 500
Balanta noua:   💰 4500

[Timestamp]
```

**Response Example - Insufficient Funds:**
```
❌ Bani Insuficienti
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai doar 💰 300

[Timestamp]
```

---

### 🛍️ SHOP
**Browse and buy items with your coins**

```
Command:  !shop
Perms:    Everyone
```

**Response Shows:**
- Item name with emoji
- Price in coins
- Item ID (for buying)

**Example:**
```
🛍️ Shop UBB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cumpara iteme cu monezi tale!

✨ Premium Badge
Pret: 💰 500
ID: `1`

🎨 Nickname Color
Pret: 💰 300
ID: `2`

[More items...]

Balanta: 💰 5000 | Utilizeaza !buy [ID]

[Timestamp]
```

---

### 🛒 BUY
**Purchase an item from the shop**

```
Command:  !buy <item_id>
Example:  !buy 1
Perms:    Everyone
```

**Requirements:**
- Item must exist
- Must have enough coins

**Response Example - Success:**
```
✅ Cumparare Reusita
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai cumparatai ✨ Premium Badge

Item:           ✨ Premium Badge
Pret:           💰 500
Balanta Noua:   💰 4500

[User Thumbnail]

[Timestamp]
```

**Response Example - Not Enough Money:**
```
❌ Bani Insuficienti
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai nevoie de 💰 1000 dar ai doar 💰 300

[Timestamp]
```

---

### 🎒 INVENTORY
**See what items you or someone else owns**

```
Command:  !inventory [@user]
Example:  !inventory
          !inventory @John
Perms:    Everyone
```

**Response Example:**
```
🎒 Inventar - John
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Premium Badge
Cantitate: 2

🎨 Nickname Color
Cantitate: 1

💰 Balanta
💰 4500 UBB Coins

[User Thumbnail]

[Timestamp]
```

**Empty Inventory:**
```
🎒 Inventar - John
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inventarul este gol!

💰 Balanta
💰 2000 UBB Coins

[User Thumbnail]

[Timestamp]
```

---

## 🔨 ADMIN COMMANDS (Administrator Only)

### ➕ ADDMONEY (ADD COINS)
**Give coins to a user - Admin only**

```
Command:  !addmoney @user <amount>
Example:  !addmoney @John 1000
Perms:    Administrator
```

**Requirements:**
- Amount must be positive

**Response Example:**
```
🔨 Admin Action - Monezi Adaugate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai adaugat monezi lui @John

Utilizator:         @John
Suma Adaugata:      💰 1000
Balanta Anterioara: 💰 2000
Balanta Noua:       💰 3000

[User Thumbnail]

[Timestamp]
```

---

### ➖ REMOVEMONEY (DELETE COINS)
**Take coins from a user - Admin only**

```
Command:  !removemoney @user <amount>
Example:  !removemoney @John 500
Perms:    Administrator
```

**Requirements:**
- Amount must be positive
- User must have enough coins

**Response Example - Success:**
```
🔨 Admin Action - Monezi Sterse
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ai sters monezi de la @John

Utilizator:         @John
Suma Stearsa:       💰 500
Balanta Anterioara: 💰 2000
Balanta Noua:       💰 1500

[User Thumbnail]

[Timestamp]
```

**Response Example - Not Enough:**
```
❌ Bani Insuficienti
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@John are doar 💰 300

[Timestamp]
```

---

## 🎨 AESTHETIC FEATURES

### Emojis Used
- 💰 Money/balance
- 💚 Success operations
- ❌ Errors
- 🔨 Admin actions
- 🛍️ Shop
- 🎒 Inventory
- ✨ Items

### Colors
- 🟢 Green = Success
- 🔴 Red = Errors/Insufficient
- 🟣 Purple = Admin actions
- 🔵 Blue = Shop/Info

### Timestamps
Every response includes timestamp for audit trail

---

## 📈 Admin Features

### Money Management
- **Add coins** instantly to any user
- **Remove coins** for penalties
- **Audit trail** with timestamps
- **Detailed feedback** on what was done

### Use Cases
```
New member reward:     !addmoney @newbie 500
Penalty for rule break: !removemoney @rule_breaker 200
Event prize:           !addmoney @winner 2000
Economy reset:         !removemoney @user [all_amount]
```

---

## 💾 Data Persistence

✅ All money is saved to `data/economy.json`
✅ Data survives bot restarts
✅ Easy to backup (JSON format)
✅ Per-user tracking

---

## 🔍 TROUBLESHOOTING

### Issue: "Permission Denied" on addmoney
**Fix**: Make sure you have Administrator role in the server

### Issue: Transfer fails with "Insufficient Funds"
**Fix**: Check your balance first with `!balance`, then adjust amount

### Issue: Can't buy item from shop
**Fix**: 
- Check item ID is correct: `!shop`
- Check you have enough money: `!balance`
- Item might not exist

### Issue: Inventory shows "empty"
**Fix**: Buy an item from the shop first: `!buy 1`

---

## 📊 COMMAND USAGE STATS

```
Most Used:
1. !balance        - Check balance
2. !shop           - Browse items
3. !buy            - Purchase items
4. !inventory      - Check items
5. !transfer       - Send money

Admin Most Used:
1. !addmoney       - Rewards
2. !removemoney    - Penalties
```

---

## 🚀 QUICK SCENARIOS

### Scenario 1: New Player Setup
```
Step 1: Admin runs !addmoney @newplayer 1000
Result: Player has 1000 coins to start with
Step 2: Player runs !shop
Step 3: Player runs !buy 1 (buys item)
Step 4: Player runs !inventory (sees purchase)
```

### Scenario 2: Send Money to Friend
```
Step 1: Check balance: !balance
Step 2: !transfer @friend 500
Result: Friend receives 500 coins
Step 3: Verify: !balance (should be 500 less)
```

### Scenario 3: Rule Violation Penalty
```
Step 1: Admin runs !removemoney @rule_breaker 300
Result: User loses 300 coins as penalty
Step 2: Admin can verify: !balance @rule_breaker
```

### Scenario 4: Event Prize
```
Step 1: Event winners announced
Step 2: Admin runs !addmoney @winner1 2000
Step 3: Admin runs !addmoney @winner2 1500
Step 4: Winners can check balance: !balance
```

---

## 🎓 TIPS & TRICKS

✅ **DO:**
- Give starting money to new members
- Use money as rewards for activities
- Create fair economy with reasonable prices
- Give players choice via shop

❌ **DON'T:**
- Give too much money at once (inflation)
- Remove excessive money (harsh)
- Make items too expensive
- Forget to explain economy to new users

---

## 📞 QUICK REFERENCE

```
PUBLIC COMMANDS:
!balance              → Check balance
!transfer @user 100   → Send money
!shop                 → View items
!buy 1                → Purchase item
!inventory            → View items owned

ADMIN COMMANDS:
!addmoney @user 500   → Give coins
!removemoney @user 200 → Take coins
!helpadmin            → See all admin commands
```

---

## ✨ VISUAL PREVIEW

All messages now have:
- ✅ Beautiful emoji indicators
- ✅ Professional embed design
- ✅ Color-coded responses
- ✅ User avatars/thumbnails
- ✅ Timestamps on everything
- ✅ Clear field labels
- ✅ Currency symbol consistency

---

**The money system is now fully implemented with beautiful aesthetics!** 💰✨

Ready to use and deploy! Run `python main.py` and test with:
```
!balance
!shop
!helpadmin
/ping
```
