# UBB Discord Bot

Un bot Discord complet, cu features avansate pentru comunitatea studentilor **Universitatii Babes-Bolyai (UBB)** din Cluj-Napoca. 

**Version:** 1.3.0 + 2.0.0 (Initial Implementation)

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
