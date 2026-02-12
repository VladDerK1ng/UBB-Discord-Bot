# 🎓 Best Practices - Ghid pentru Development

## 📋 Reguli de Bază

### 1. Organizare Cog-uri

**Bun:** Comenzi similare în același cog
```python
# cogs/moderation.py
class ModerationCog(commands.Cog):
    @commands.command(name='kick')
    async def kick(self, ctx, member: discord.Member):
        pass
    
    @commands.command(name='ban')
    async def ban(self, ctx, member: discord.Member):
        pass
```

**Rău:** Comenzi random în toate cog-urile
```python
# cogs/everything.py - EVITA!
@commands.command(name='kick')
@commands.command(name='medie')
@commands.command(name='balance')
```

---

### 2. Utilizare Config

**Bun:**
```python
from config import GRADE_MAXIMUM, UBB_INFO

async def medie(self, ctx, *note: int):
    if any(n > GRADE_MAXIMUM for n in note):
        await ctx.send("Nota prea mare!")
```

**Rău:**
```python
async def medie(self, ctx, *note: int):
    if any(n > 10 for n in note):  # Hardcoded!
        await ctx.send("Nota prea mare!")
```

---

### 3. Error Handling

**Bun:**
```python
from utils import create_error_embed

try:
    result = 10 / int(user_input)
except ValueError:
    embed = create_error_embed("Eroare", "Introdu un număr!")
    await ctx.send(embed=embed)
except ZeroDivisionError:
    embed = create_error_embed("Eroare", "Nu poți împărți la 0!")
    await ctx.send(embed=embed)
```

**Rău:**
```python
try:
    result = 10 / int(user_input)
except:  # Catch-all!
    await ctx.send("Eroare")
```

---

### 4. Validare Input

**Bun:**
```python
from utils import validate_grades

is_valid, error_msg = validate_grades(*note)
if not is_valid:
    embed = create_error_embed("Eroare", error_msg)
    return await ctx.send(embed=embed)
```

**Rău:**
```python
if not note:  # Validation inline
    return await ctx.send("Nicio nota!")
if any(n < 1 or n > 10 for n in note):
    return await ctx.send("Nota invalida!")
# ... more validations
```

---

### 5. Logging

**Bun:**
```python
import logging

logger = logging.getLogger(__name__)

async def some_command(self, ctx):
    logger.info(f"User {ctx.author} used command: {ctx.command.name}")
    try:
        # do something
    except Exception as e:
        logger.error(f"Error in some_command: {e}")
```

**Rău:**
```python
async def some_command(self, ctx):
    print(f"User used command")  # Use logging!
    # no error tracking
```

---

### 6. Docstring-uri

**Bun:**
```python
async def medie(self, ctx, *note: int):
    """Calculate the average of grades
    
    Example: !medie 10 9 8 7
    """
    pass
```

**Rău:**
```python
async def medie(self, ctx, *note: int):
    pass  # No documentation
```

---

### 7. Permissions & Checks

**Bun:**
```python
from discord.ext import commands

@commands.command(name='clean')
@commands.has_permissions(administrator=True)
async def clean(self, ctx):
    """Admins only"""
    pass
```

**Rău:**
```python
@commands.command(name='clean')
async def clean(self, ctx):
    if ctx.author.id != SERVER_OWNER_ID:  # Manual check
        return
    pass
```

---

## 🏗️ Structura Cogului

Fiecare cog trebuie să urmeze această structură:

```python
"""
Category Name Commands Cog
Descriere scurta a ce face cogul
"""

import discord
from discord.ext import commands
import logging

logger = logging.getLogger(__name__)

class CategoryCog(commands.Cog):
    """Docstring pentru cog"""
    
    def __init__(self, bot):
        self.bot = bot
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # COMMANDS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='command1')
    @commands.has_permissions(administrator=True)
    async def command1(self, ctx, arg1: str):
        """Descriere comanda"""
        try:
            # implementation
            pass
        except Exception as e:
            logger.error(f"Error in command1: {e}")
            await ctx.send("Eroare neasteptata!")
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # HELPER METHODS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    async def _helper_method(self):
        """Private helper method"""
        pass
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SETUP
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def setup(bot):
    """Load the CategoryCog into the bot"""
    await bot.add_cog(CategoryCog(bot))
    logger.info("CategoryCog loaded")
```

---

## 🎯 Naming Conventions

### Commands
```python
@commands.command(name='calculate_average')  # lowercase_with_underscores
async def calculate_average(self, ctx):
    pass
```

### Classes
```python
class ModerationCog(commands.Cog):  # PascalCase
    pass
```

### Methods & Functions
```python
async def _get_user_stats(self, user_id):  # lowercase_with_underscores
    # Private methods start with _
    pass

async def validate_input(self, data):  # lowercase_with_underscores
    # Public methods don't start with _
    pass
```

### Variables
```python
MAX_ATTEMPTS = 3  # CONSTANT_LIKE
user_list = []    # lowercase_with_underscores
userId = None     # AVOID camelCase
```

---

## 🔄 Reusing Code

### Embed Creation
```python
from utils import create_error_embed, create_success_embed

# Instead of creating embed every time:
embed = create_error_embed("Error", "Something went wrong")
await ctx.send(embed=embed)
```

### Date Utilities
```python
from utils import days_until, hours_until

days_left = days_until(7, 15)  # 15 Iulie
hours_left = hours_until(7, 15)
```

### Validators
```python
from utils import validate_grades

is_valid, error_msg = validate_grades(*note)
if not is_valid:
    return await ctx.send(error_msg)
```

---

## 📦 Adăugare Funcție Nouă în Utils

### 1. Identifica categoria (embed_utils, date_utils, etc.)
### 2. Adauga funcția

**File: utils/converters.py**
```python
"""
Converter utilities for Discord types
"""

async def convert_member(guild, identifier: str):
    """Convert string to discord.Member"""
    member = guild.get_member_named(identifier)
    if not member:
        raise ValueError(f"Member not found: {identifier}")
    return member
```

### 3. Adauga în `utils/__init__.py`
```python
from .converters import convert_member

__all__ = [
    # ... existing
    'convert_member'
]
```

### 4. Foloseste în cog
```python
from utils import convert_member

@commands.command(name='info')
async def info(self, ctx, member_name: str):
    member = await convert_member(ctx.guild, member_name)
```

---

## ⚠️ Common Mistakes

### ❌ Mistake 1: Hardcoded Values
```python
# BAD
if grade > 10:
    return

# GOOD
from config import GRADE_MAXIMUM
if grade > GRADE_MAXIMUM:
    return
```

### ❌ Mistake 2: Duplicate Code
```python
# BAD - In multiple cogs
embed = discord.Embed(title="Error", color=discord.Color.red())
await ctx.send(embed=embed)

# GOOD - Use utils
from utils import create_error_embed
embed = create_error_embed("Error", description)
await ctx.send(embed=embed)
```

### ❌ Mistake 3: Missing Error Handling
```python
# BAD
async def get_user_balance(self, user_id: int):
    balance = self.data[user_id]['balance']  # KeyError if missing!
    return balance

# GOOD
async def get_user_balance(self, user_id: int):
    try:
        return self.data[user_id]['balance']
    except KeyError:
        logger.error(f"User {user_id} not found")
        return 0
```

### ❌ Mistake 4: Tight Coupling
```python
# BAD - Dependent on specific file
with open('hardcoded/path/data.json') as f:
    data = json.load(f)

# GOOD - Use constants
from config import DATA_PATH
with open(DATA_PATH / 'data.json') as f:
    data = json.load(f)
```

### ❌ Mistake 5: No Validation
```python
# BAD
@commands.command()
async def give_points(self, ctx, user: str, points: str):
    user_obj = ctx.guild.get_member(user)  # user might be invalid
    amount = int(points)  # ValueError if not int
    # proceed...

# GOOD
@commands.command()
async def give_points(self, ctx, user: discord.Member, points: int):
    # Discord converts automatically, validates for us
    # proceed with confident types
```

---

## 📊 Performance Tips

### 1. Cache Frequently Used Data
```python
# BAD - Every command call
async def get_config(self):
    with open('config.json') as f:
        return json.load(f)

# GOOD - Cache it
def __init__(self, bot):
    self.bot = bot
    self._config_cache = None

async def get_config(self):
    if self._config_cache is None:
        with open('config.json') as f:
            self._config_cache = json.load(f)
    return self._config_cache
```

### 2. Use Async Properly
```python
# BAD - Blocking I/O
import requests
response = requests.get('http://api.example.com')

# GOOD - Non-blocking
import aiohttp
async with aiohttp.ClientSession() as session:
    async with session.get('http://api.example.com') as resp:
        data = await resp.json()
```

### 3. Batch Database Operations
```python
# BAD
for user in users:
    await database.update_user(user)  # N queries

# GOOD
await database.bulk_update_users(users)  # 1 query
```

---

## ✅ Checklist pentru Commit

- [ ] Cod testat
- [ ] Docstring-uri adăugate
- [ ] Fără hardcoded values
- [ ] Logging configurat
- [ ] Error handling implementat
- [ ] Niciun `print()` (folosește logging)
- [ ] Niciun `except: pass`
- [ ] Imports organizate
- [ ] Fără commented-out code
- [ ] Type hints complete

---

## 🚀 Quote-uri motivationale pentru devs

> "A messy codebase leads to a messy life." - Your future self  
> "Write code for humans first, computers second." - Unknown  
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." - Martin Fowler  

Keep coding! 🎉
