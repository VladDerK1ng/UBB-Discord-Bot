# 🤖 UBB Discord Bot

Un bot Discord complet și profesional pentru comunitatea studenților **Universității Babeș-Bolyai (UBB)** din Cluj-Napoca, cu sistem de economie, jocuri, moderație și comenzi utile.

**Versiune:** 1.3.0 ✅ | **Status:** Production Ready 🟢

---

## 📋 Cuprins

- [Features](#-features)
- [Comenzi Disponibile](#-comenzi-disponibile)
- [Instalare](#-instalare)
- [Utilizare](#-utilizare)
- [Configurare](#-configurare)
- [Structura](#structura-proiectului)

---

## ✨ Features

### Sistem de Comenzi
- ✅ **Text Commands**: `!command` (prefix standard)
- ✅ **Slash Commands**: `/command` (Discord moderne)
- ✅ **Mention Prefix**: `@BotName command`
- ✅ **Help System**: `!help` și `!help <command>`

### Economie & Shop
- ✅ **Sistem de Monedă**: UBB Coins (💰)
- ✅ **Transfer de Bani**: `!transfer @user suma`
- ✅ **Shop cu Iteme**: 5 tipuri de iteme (badge, color, prefix, role, feature)
- ✅ **Inventory System**: Cumpără și ține iteme
- ✅ **Item Usage**: `!use [id]` pentru a folosi iteme și obține recompense
- ✅ **Item Gifting**: `!gift @user [id]` pentru a oferi iteme altui jucător
- ✅ **Admin Controls**: Adaugă/elimină bani utilizatorilor

### Jocuri & Entertainment
- ✅ **Jocuri de Noroc**: Blackjack, Slots (cu pariu)
- ✅ **Jocuri de Cuvinte**: Hangman, Trivia, Wordle
- ✅ **Leaderboards**: Top 10 la jocuri
- ✅ **Stats Tracking**: Urmărește progresul tău

### Sistem de Rank-uri
- ✅ **8 Niveluri de Rank**: De la Noob la Godlike
- ✅ **XP System**: Câștigă XP și avansează
- ✅ **Achievements**: Unlock-uri speciale

### Moderație & Admin
- ✅ **Kick/Ban**: Elimină/Banează utilizatori
- ✅ **Warning System**: Avertizări cu auto-ban la 3 avertisări
- ✅ **Purge Messages**: Șterge mesaje în bulk
- ✅ **Server Logging**: Log automat al acțiunilor
- ✅ **User Info**: Vezi detalii despre utilizatori

### Alte Features
- ✅ **Verificare CAPTCHA**: Sistem anti-bot
- ✅ **Reminderi**: `!remind` pentru reamintiri
- ✅ **Notificări**: Sistem de notificări personalizate
- ✅ **Music Bot**: Redare muzică din YouTube
- ✅ **Configurare Per-Server**: Setări personalizate

---

## 📖 Comenzi Disponibile

### 💰 Comenzi de Economie

```
!balance [@user]           Vede balanta de monezi
!transfer @user <suma>    Trimite bani altui utilizator
!addmoney @user <suma>    Admin: Adaugă bani
!removemoney @user <suma> Admin: Elimină bani
!shop                     Afișează toate itemele disponibile
!buy <id>                 Cumpără un item din shop
!inventory [@user]        Vede itemele pe care le deții
!use <id>                 Folosește un item și obține recompensă
!gift @user <id>          Daruiește un item altui jucător
```

### 🎮 Comenzi de Jocuri

```
!blackjack [pariu]        Joaca Blackjack cu pariu
!slots [pariu]            Joaca Slot Machine
!hangman                  Ghicește cuvântul (Hangman)
!trivia                   Quiz cu 5 întrebări
!wordle                   Ghicește cuvântul în 6 tentative
!gamestats                Vezi statistici la jocuri
```

### 📊 Comenzi de Stats & Ranks

```
!stats [@user]            Vezi statistici personale
!leaderboard              Top 10 jucători după XP
!achievements [@user]     Vezi achievements unlock-ate
!rank [@user]             Vezi rank-ul tău actual
!rankinglist              Vezi lista completă de rank-uri
!levels                   Info despre sistem de niveluri
```

### 🔔 Reminderi & Notificări

```
!remind <ore> <mesaj>     Setează un reminder
!reminders                Vezi reamintirile tale
!delreminder <index>      Șterge un reminder
```

### 🎵 Comenzi de Muzică

```
/play [query]             Redă melodie din YouTube
!queue                    Afișează coada de melodii
/skip                     Trece la următoarea melodie
!pause                    Pauza melodia
!resume                   Continuă melodia
/stop                     Oprește playback
```

### ⚙️ Comenzi Admin

```
!kick @user [motiv]       Elimină utilizator din server
!ban @user [motiv]        Banează utilizator
!unban <username#1234>    Debanează utilizator
!warn @user [motiv]       Avertizează utilizator
!warnlist @user           Vezi avertisarile unui utilizator
!clearwarns @user         Șterge avertisarile
!purge [numar]            Șterge ultimele N mesaje
!userinfo @user           Info detaliate despre utilizator
!serverinfo               Info despre server
!setlogchannel #canal     Seteaza canalul de loguri
!setautorole @role        Seteaza rolul automat
```

### ℹ️ Comenzi Generale

```
!help                     Afișează toate comenzile
!help <comanda>           Help detaliat pentru o comandă
/ping                     Latența botului
/balance [@user]          Balanța (slash command)
/help                     Help rapid (slash command)
/shop                     Shop (slash command)
```

### 🧮 Informatii UBB

```
!ubb                      Info despre Universitatea Babeș-Bolyai
!facultati                Lista facultăților
!contact                  Date de contact universitate
!medie <note>             Calculează media notelor
!zile                     Zile rămase până la examen
```

---

## 🚀 Instalare

### Cerințe Sistem
- **Python**: 3.8+
- **discord.py**: 2.3.0+
- **Internet**: Pentru conectare Discord

### Pași de Instalare

#### 1. Clone Repository
```bash
git clone https://github.com/USERNAME/discord-ubb-bot.git
cd discord-ubb-bot
```

#### 2. Instalează Dependențe
```bash
pip install -r requirements.txt
```

#### 3. Configurează Token
Creează fișierul `.env` în rădăcina proiectului:
```
DISCORD_TOKEN=your_bot_token_here
```

#### 4. Pornește Botul
```bash
python main.py
```

**Output așteptat:**
```
============================================================
Starting UBB Discord Bot...
Features: Text commands (!) • Slash commands (/) • Ping prefix
============================================================
✓ Bot connected as BotName#0000
✓ Synced 5 app commands
✓ Loaded 12 cogs: AdminCommandsCog, Economy, Games, ...
✓ Loaded 60+ text commands
```

---

## 📱 Cum să Creezi Bot-ul pe Discord

### 1. Discord Developer Portal

1. Accesează [Discord Developer Portal](https://discord.com/developers/applications)
2. Click pe "New Application"
3. Dă-i un nume botului și acceptă termenii
4. Mergi la secțiunea "Bot" din stânga

### 2. Configurare Bot

1. Click pe "Add Bot"
2. Sub token, click "Copy" pentru a copia token-ul secret
3. Adaugă token-ul în fișierul `.env`

### 3. Permisiuni

1. Mergi la "OAuth2" → "URL Generator"
2. Selectează scopuri: `bot`
3. Selectează permisiuni necesare:
   - Manage Roles
   - Manage Channels
   - Send Messages
   - Embed Links
   - Attach Files
   - Use Slash Commands
   - Manage Messages (pentru purge)

### 4. Adaugă la Server

1. Copiază URL-ul generat din "URL Generator"
2. Deschide URL-ul în browser
3. Selectează serverul unde vrei să adaugi botul
4. Confirmă permisiunile

---

## ⚙️ Configurare

### Setări Global (config.py)

```python
# Bot settings
BOT_NAME = "UBB Discord Bot"
BOT_VERSION = "1.3.0"
COMMAND_PREFIX = "!"

# Features
ENABLE_MUSIC = True
ENABLE_GAMES = True
ENABLE_ECONOMY = True
```

### Setări Per-Server

Admini pot configura cu comenzile:
```
!setwelcome [mesaj]       - Welcome message
!setautorole @role        - Rol automat pentru noi membri
!setlogchannel #canal     - Canalul de loguri
```

---

## 💻 Utilizare

### Exemplu: Sistem de Economie

```
1. !balance
   → Ai 1000 UBB Coins

2. !shop
   → Afișează 5 iteme disponibile (300-2000 coins fiecare)

3. !buy 5
   → Cumperi item "Bot Response Feature" pentru 750 coins
   → Acum ai 250 coins și 1x Bot Response în inventory

4. !use 5
   → Folosești itemul și câștigi 1000-3000 coins random!
   → Item-ul este consumat din inventory

5. !inventory
   → Vezi ce iteme mai ai

6. !gift @John 1
   → Dai itemul "Premium Badge" lui John
```

### Exemplu: Joc Blackjack

```
!blackjack 500
→ Pariezi 500 coins pe o rundă de Blackjack
→ Dacă câștigi: +1000 coins
→ Dacă pierzi: -500 coins
→ Putem vedea detalii cu !gamestats
```

### Exemplu: Help

```
!help
→ Afișează toate comenzile în categorii

!help balance
→ Help detaliat: "Check balance - !balance [@user]"

/help
→ Slash command version a help-ului
```

---

## 📁 Structura Proiectului

```
discord-ubb-bot/
├── main.py                      # Bot principal + runtime
├── config.py                    # Configurare globală
├── requirements.txt             # Dependențe Python
├── .env                         # Token-uri (GIT-IGNORED)
├── .gitignore                   # Fișiere ignorate
├── LICENSE                      # MIT License
├── CHANGELOG.md                 # Istoricul versiunilor
├── README.md                    # Documentație (acest fișier)
│
├── cogs/                        # Module (Extensii Bot)
│   ├── __init__.py
│   ├── admin_extended.py       # 15+ comenzi admin
│   ├── economy.py              # Shop, iteme, inventory
│   ├── games.py                # Jocuri de noroc
│   ├── logging.py              # Sistem de logging
│   ├── music.py                # Redare muzică YouTube
│   ├── notifications.py        # Sistem notificări
│   ├── ranks.py                # Sistem rank-uri + XP
│   ├── settings.py             # Setări per-server
│   ├── stats.py                # Stats & leaderboards
│   ├── verification.py         # CAPTCHA & verificare
│   └── fun.py                  # Comenzi divertisment
│
├── data/                        # Stocare persistentă
│   ├── user_stats.json         # Stats utilizatori
│   ├── server_settings.json    # Setări per-server
│   ├── economy.json            # Balanțe & inventory
│   ├── shop.json               # Definiții iteme
│   └── verification.json       # Status verificare
│
└── api/                         # REST API (v2.0.0)
    └── bot_api.py              # API endpoints
```

---

## 🔧 Troubleshooting

### Bot nu se conectează
- Verifica dacă token-ul din `.env` este corect
- Verifica conexiunea la internet
- Asigură-te că bot-ul are permisiunile necesare

### Comenzi slash nu apar
- Discord are cache - restart-ează aplicația
- Așteptă 1-5 minute pentru sincronizare
- Type `/` pentru a forța refresh-ul listei

### Help command nu funcționează
- Asigură-te că `!help` este în comenzi (ar trebui să fie)
- Folosește `help` în loc de `help command` pentru detalii

### Jocurile nu functionează
- Verifica dacă sunt încărcate cog-urile de jocuri
- Asigură-te că ai permisiunile de send messages

---

## 📊 Stack Tehnologic

| Component | Versiune | Purpose |
|-----------|----------|---------|
| **Python** | 3.11 | Limbaj de programare |
| **discord.py** | 2.3.0+ | Framework Discord |
| **Python-dotenv** | 1.0.0 | Variabile de mediu |
| **Storage** | JSON | Persistență date |
| **Hosting** | Local/Cloud | Unde rulează botul |

---

## 🎯 Roadmap

### ✅ v1.3.0 (Current)
- [x] Sistem de economie complet
- [x] Shop cu iteme usable
- [x] Jocuri (Blackjack, Slots, Hangman, Trivia)
- [x] Sistem rank-uri și XP
- [x] Admin commands (kick, ban, warn, purge)
- [x] Slash commands funcționale
- [x] Help command
- [x] Moderație și logging

### 🔄 v2.0.0 (Planned)
- [ ] REST API pentru bot
- [ ] Web Dashboard pentru stats
- [ ] Caching system pentru performance
- [ ] Custom commands per-server
- [ ] Automated reports & analytics
- [ ] Voice chat support (PyNaCl)

---

## 🤝 Contributii

Dacă ai idei pentru features noi, bug reports, sau improvement-uri:

1. **Fork** repository-ul
2. **Creează** o branch nouă: `git checkout -b feature/amazing-feature`
3. **Commit** schimbările: `git commit -m 'Add amazing feature'`
4. **Push** la branch: `git push origin feature/amazing-feature`
5. **Deschide** un Pull Request

Orice ajutor este binevenit! 💪

---

## 📝 Licență

Acest proiect este sub [MIT License](LICENSE) - poți folosi liber cu atribuire.

---

## 👥 Contact & Support

| Canal | Link |
|-------|------|
| **Discord Server** | În curs de adăugare |
| **Issues & Bugs** | GitHub Issues |
| **Sugestii** | GitHub Discussions |
| **Email** | contact@example.com |

---

## 🔗 Linkuri Importante

- 🎓 [Universitatea Babeș-Bolyai](https://www.ubb.ro)
- 📚 [discord.py Documentation](https://discordpy.readthedocs.io/)
- 🛠️ [Discord Developer Portal](https://discord.com/developers)
- 💻 [GitHub Repository](#)

---

## 🌟 Stats

- **60+** Comenzi text
- **5+** Slash commands
- **12** Cogs (module)
- **8** Nivele de rank
- **5** Tipuri de iteme
- **4+** Jocuri
- **3** Tipuri de comenzi (text, slash, mention)

---

## ⭐ Dacă îți place botul, dă-i un STAR! ⭐

```
     _    _   __        ___    _____
    | |  | | / /       / _ \  / ____|
    | |  | |/ /  ____| | | || |
    | |  |   <  |_____| | | || |
    | |__| |\ \       | |_| || |____
     \____/|_| \_\      \___/ \_____|

Mulțumim că folosești UBB Discord Bot! 🚀
```

---

**Versiune:** 1.3.0 ✅  
**Ultima actualizare:** 13 februarie 2026  
**Status:** Production Ready 🟢  
**Cogs Încărcate:** 12/15  
**Comenzi Disponibile:** 65+

## Versiuni si Features

### v1.0.0 - Core Commands
Calcule, informatii UBB, divertisment, stats si moderatie de baza

### v1.1.0 - Modular Architecture  
Cogs system, stats tracking cu XP, achievements

### v1.2.0 - Notifications & Logging
Reminder system, server logging, configurare per-server

### v1.3.0 - Ranks, Economy & Games (CURRENT)
Systema de rank-uri, economy cu moneda si shop, mini-jocuri, verificare cu CAPTCHA

### v2.0.0 - Enterprise Features (INITIAL IMPLEMENTATION)
REST API, Music Bot, Advanced Games (Trivia/Wordle), Advanced Moderation

## Comenzi Disponibile

### Calcule Academice (v1.0.0)
- `!medie` - Calculeaza media notelor
- `!zile` - Zile ramase pana la examenul de admitere
- `!concurs` - Zile ramase pana la concursul de admitere

### Informatii UBB (v1.0.0)
- `!ubb` - Informatii despre Universitatea Babes-Bolyai
- `!facultati` - Lista facultatilor disponibile
- `!contact` - Date de contact

### Divertisment & Jocuri (v1.0.0)
- `!sfat` - Sfaturi motivatoare
- `!moneda` - Arunca o moneda
- `!roll` - Arunca un zar

### Stats & Achievements (v1.1.0)
- `!stats [@user]` - Vede statisticile tale
- `!leaderboard` - Top 10 utilizatori dupa XP
- `!achievements [@user]` - Vede achievements-urile

### Notificari si Reminderi (v1.2.0)
- `!remind ore mesaj` - Seteaza un reminder
- `!reminders` - Vede reamintirile tale
- `!delreminder index` - Sterge un reminder

### Ranks & Progression (v1.3.0)
- `!rank [@user]` - Vede rank-ul tau
- `!rankinglist` - Lista rank-urilor disponibile (Noob - Godlike)

### Economy System (v1.3.0)
- `!balance` - Vede balanta de monezi (UBB Coins)
- `!transfer @user suma` - Trimite bani
- `!shop` - Vede shop-ul cu iteme
- `!buy [ID]` - Cumpara item din shop
- `!inventory` - Vede inventarul tau

### Mini-Jocuri (v1.3.0)
- `!blackjack [pariu]` - Joaca Blackjack cu pariu
- `!slots [pariu]` - Joaca Slot Machine
- `!hangman` - Joaca Hangman - ghiceste cuvantul
- `!gamestats` - Vede statistici la jocuri

### Advanced Games (v2.0.0)
- `!trivia` - Trivia cu 5 intrebari din cultura generala
- `!wordle` - Wordle - ghiceste cuvantul in 6 incercari
- `!highscores` - Top 10 la Trivia

### Music Bot (v2.0.0)
- `!play [query]` - Reda melodii din YouTube
- `!queue` - Afiseaza lista de asteptare
- `!skip` - Trece la urmatoarea melodie
- `!pause` - Pauza melodia
- `!resume` - Continua melodia
- `!volume [0-100]` - Setare volum
- `!stop` - Oprit playback si curata queue

### Verificare (v1.3.0)
- `!verify` - Verifica-te cu CAPTCHA
- `!verificationstatus` - Vede status verificare

### Moderatie & Admin (v1.0.0+)
- `!kick @user [motiv]` - Elimina utilizator (admin)
- `!ban @user [motiv]` - Baneaza utilizator (admin)
- `!unban user#1234` - Debaneaza utilizator (admin)
- `!warn @user [motiv]` - Avertizeaza utilizator (admin)
- `!purge [numar]` - Sterge mesaje (admin)
- `!setwordfilter [cuvinte]` - Seteaza cuvinte interzise (v2.0.0, admin)
- `!setspamprotect [msgs] [min]` - Anti-spam rules (v2.0.0, admin)
- `!warnings @user` - Vede avertisarile (v2.0.0, admin)

### Configurare Server (v1.2.0+, Doar admini)
- `!settings` - Vede setarile serverului
- `!setwelcome [mesaj]` - Activeaza welcome message
- `!setwelcomechannel #canal` - Seteaza canalul welcome
- `!setlogchannel #canal` - Seteaza canalul de loguri
- `!setautorole @role` - Seteaza rolul automat

### Logging & Audit (v1.2.0+, Doar admini)
- `!logs [numar]` - Vede logurile serverului
- `!clearlog` - Sterge logurile

### General

- `!help` - Afiseaza toate comenzile disponibile
- `!help [comanda]` - Ajutor pentru o anumita comanda
- `!info` - Informatii despre bot

## 🚀 Instalare

### Cerințe
- Python 3.8+
- discord.py 2.0+
- python-dotenv

### Pași

1. **Clone repository-ul:**
```bash
git clone https://github.com/USERNAME/discord-ubb-bot.git
cd discord-ubb-bot
```

2. **Instalează dependențele:**
```bash
pip install -r requirements.txt
```

3. **Creează un fișier `.env`:**
```
DISCORD_TOKEN=your_discord_bot_token_here
```

4. **Pornește botul:**
```bash
python main.py
```

## Crearea Bot-ului pe Discord

1. Du-te la [Discord Developer Portal](https://discord.com/developers/applications)
2. Click pe "New Application" și dă-i un nume
3. Mergi la "Bot" și click "Add Bot"
4. Sub token, click "Copy" pentru a copia token-ul
5. Adaugă token-ul în fișierul `.env`
6. Mergi la "OAuth2" > "URL Generator"
7. Selectează `bot` la scopes
8. Selectează permisiunile necesare (Send Messages, Embed Links, etc.)
9. Copiază URL-ul generat și accesează-l pentru a adăuga botul la server

## Dependente

```
discord.py==2.3.0
python-dotenv==1.0.0
```

## Exemple de Utilizare

### Calculeaza media
```
!medie 9 8 10 7
```
Output: Media: 8.50

### Zile ramase
```
!zile
```
Output: Zile ramase pana la examen: 145

### Vede statisticile
```
!stats
!leaderboard
```

## Stack Tehnologic

- Limbaj: Python 3.11
- Framework: discord.py 2.3.0
- Stocare: JSON files
- Gazduit: Local / Cloud (Heroku, Replit, etc.)

## Structura Proiectului

```
discord-ubb-bot/
├── main.py              # Fisierul principal cu comenzile generale
├── cogs/                # Moduri (extensii ale bot-ului)
│   ├── moderation.py   # Comenzi de moderatie (kick, ban, warn, purge)
│   └── stats.py        # Sistemul de stats si achievements
├── data/                # Dosarul pentru stocarea datelor
│   └── user_stats.json # Datele utilizatorilor (persistenta)
├── requirements.txt    # Dependentele Python
├── .env.example        # Template pentru variabilele de mediu
├── .gitignore          # Fisiere ignorate de Git
├── LICENSE             # MIT License
├── CHANGELOG.md        # Istoricul versiunilor
└── README.md           # Acest fisier
```

## Contributii

Contributiile sunt binevenite! Daca ai idei pentru mai multe caracteristici:

1. Fork-ul repository-ului
2. Creeaza o branch noua (`git checkout -b feature/amazing-feature`)
3. Commit-ul tau (`git commit -m 'Add some amazing feature'`)
4. Push la branch (`git push origin feature/amazing-feature`)
5. Deschide un Pull Request

## Licenta

Acest proiect este sub [MIT License](LICENSE)

## Autor

Creat cu dragoste pentru comunitatea UBB

## Link-uri Importante

- [Universitatea Babeș-Bolyai](https://www.ubb.ro)
- [Discord.py Documentație](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers)

## ⭐ Dacă îți place botul, dă-i un star! ⭐

---

**Versiune:** 1.0.0  
**Ultim update:** Februarie 2026
