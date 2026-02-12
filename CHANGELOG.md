# Changelog

Toate schimbările notabile în acest proiect vor fi documentate în acest fișier.

## [1.3.0] - 2026-02-12 (RELEASED)

### Adaugat

**v1.3.0 - Ranks, Economy & Games System**

- Cog Ranks cu systema de progresie:
  - `!rank [@user]` - Vede rank-ul tau sau al altcuiva
  - `!rankinglist` - Lista tuturor rank-urilor disponibile
  - 8 rank-uri: Noob, Learner, Student, Scholar, Master, Legend, Mythical, Godlike
  - Progress bar visual pentru XP
  - Rank notifications cand se atinge nivel nou
  - Persistenta datelor in data/ranks.json

- Cog Economy cu moneda si shop:
  - `!balance [@user]` - Vede balanta de monezi
  - `!transfer @user suma` - Trimite bani
  - `!shop` - Vede shop-ul cu iteme
  - `!buy [ID]` - Cumpara item din shop
  - `!inventory [@user]` - Vede inventarul
  - Shop cu 5 iteme: Premium Badge, Nickname Color, Custom Prefix, Secret Role, Bot Response
  - Moneda de start: 100 UBB Coins
  - Persistenta in data/economy.json

- Cog Games cu mini-jocuri:
  - `!blackjack [pariu]` - Joc de Blackjack cu pariu
  - `!slots [pariu]` - Slot Machine cu jackpot
  - `!hangman` - Joc de Hangman - ghiceste cuvantul
  - `!gamestats [@user]` - Vede win rate la jocuri
  - Reward system: monezi castigate din jocuri
  - Tracking victorii si infrangeri
  - Persistenta in data/game_stats.json

- Cog Verification cu CAPTCHA:
  - `!verify` - Incepe procesul de verificare
  - `!verificationstatus [@user]` - Vede status verificare
  - CAPTCHA matematic pentru verificare
  - Auto-role assignment cand e verificat
  - Verified role management
  - Persistenta in data/verification.json

### Imbunatatit

- Help system cu 4 noi categorii: Ranks & Progression, Economy, Mini-Jocuri, Verificare
- Versiune bot actualizata la 1.3.0
- Requirements.txt cu Flask, yt-dlp, PyNaCl
- 4 coguri noi incarcate automat
- Comenzi info actualizate

## [1.2.0] - 2026-02-12

### Adaugat
- Cog Notifications cu systema de reminder-uri:
  - `!remind ore mesaj` - Seteaza un reminder dupa N ore
  - `!reminders` - Vede reminder-urile tale active
  - `!delreminder index` - Sterge un reminder
  - Task loop automat care verifica reminder-uri
  - Persistenta datelor in data/reminders.json
  
- Cog Logging cu inregistrare detaliata a actiunilor:
  - `!logs [numar]` - Vede logurile serverului
  - `!clearlog` - Sterge logurile serverului
  - Inregistrare mesaje sterse
  - Inregistrare mesaje editate
  - Inregistrare intrare/iesire membri
  - Inregistrare comenzi executate
  - Formatare timestamp la fiecare log
  
- Cog Settings cu configurari per-server:
  - `!settings` - Vede setarile curente ale serverului
  - `!setwelcome [mesaj]` - Activeaza/dezactiveaza welcome message
  - `!setwelcomechannel #canal` - Seteaza canalul pentru welcome
  - `!setlogchannel #canal` - Seteaza canalul pentru loguri
  - `!setautorole @role` - Seteaza rolul automat pentru membrii noi
  - Listener on_member_join pentru welcome si auto-role
  - Persistenta setarilor in data/server_settings.json

### Imbunatatit
- Help system cu noi categorii: Notificari, Configurare, Admin
- Versiune bot actualizata la 1.2.0
- README.md cu noile seznam de comenzi
- Documentatie mai completa pentru noile features

## [1.1.0] - 2026-02-12

### Adaugat
- Structura modulara cu Cogs pentru organizare
- Cog Moderation cu comenzi admin:
  - `!kick @user [motiv]` - Elimina utilizator
  - `!ban @user [motiv]` - Baneaza utilizator
  - `!unban user#1234` - Debaneaza utilizator
  - `!warn @user [motiv]` - Avertizeaza utilizator
  - `!purge [numar]` - Sterge mesaje (1-100)
- Cog Stats cu tracking utilizatori:
  - `!stats [@user]` - Vede statisticile tale
  - `!leaderboard` - Top 10 dupa XP
  - `!achievements [@user]` - Achievements
- Sistem de experience si niveluri
- Salvarea datelor in JSON
- Incarcare automata de cogs

### Imbunatatit
- Structura de cod mai modulara
- Help command actualizat cu toate categoriile noi
- Tracking automat de mesaje si comenzi
- Sistemul de stats cu persistenta datelor

### Sters
- Comanda `!salut` (simplificare)

## [1.0.0] - 2026-02-12

### Adaugat
- Comanda `!help` - Afiseaza toate comenzile disponibile
- Comanda `!medie` - Calculeaza media notelor (cu validare)
- Comanda `!zile` - Zile ramase pana la examenul de admitere (cu an dinamic)
- Comanda `!concurs` - Zile ramase pana la concursul de admitere
- Comanda `!ubb` - Informatii generale despre UBB
- Comanda `!facultati` - Lista facultatilor UBB
- Comanda `!contact` - Date de contact ale universitatii
- Comanda `!sfat` - Sfaturi motivatoare aleatoare
- Comanda `!salut` - Salutari prietenoase aleatoare
- Comanda `!moneda` - Arunca o moneda virtuala
- Comanda `!roll` - Arunca un zar (1-6)
- Comanda `!info` - Informatii despre bot
- Discord Embeds - Mesaje frumoase si colorate
- Error Handling - Tratare profesionala a erorilor
- Documentatie completa in README.md
- Variabile de mediu cu .env.example

### Imbunatatit
- Structura de cod mai organizata si comentata
- Status de bot dinamic (watching "studenti UBB")
- Validare robusta pentru comenzi (ex: note 1-10)
- Output formatat elegant cu embeds

### Securitate
- Token-ul stocat in .env (nu in cod!)
- .gitignore pentru a proteja fisierele sensibile
- Verificare de token la startup

## [2.0.0] - 2026-02-12 (RELEASED - Initial Implementation)

### Adaugat

**v2.0.0 - Enterprise Features & Advanced Systems**

- **REST API Complete** - `api/bot_api.py`:
  - `/api/v1/health` - Health check endpoint
  - `/api/v1/stats/user/<user_id>` - User statistics
  - `/api/v1/stats/leaderboard` - Global leaderboard (top 10)
  - `/api/v1/economy/balance/<user_id>` - Economy details
  - `/api/v1/economy/shop` - Shop items listing
  - `/api/v1/logs/server/<server_id>` - Server audit logs (cu limit param)
  - `/api/v1/ranks/user/<user_id>` - User rank si progression
  - `/api/v1/games/stats/<user_id>` - Game statistics
  - `/api/v1/analytics/summary` - Bot analytics summary
  - API Key authentication cu decorator
  - CORS support pentru cross-origin requests
  - Flask framework cu jsonify responses
  - Completare cu timestamp la fiecare request
  - Error handlers pentru 404 si 500

- **Music Bot Cog** - `cogs/music.py`:
  - `!play [query]` - Reda melodii din YouTube
  - `!queue` - Afiseaza lista de asteptare
  - `!skip` - Trece la urmatoarea melodie
  - `!pause` - Pauza melodia
  - `!resume` - Continua melodia
  - `!volume [0-100]` - Setare volum
  - `!stop` - Oprit si curata queue
  - Queue system cu unlimited songs
  - Per-guild queue management
  - Volume control (0-100%)
  - Loop si shuffle flags (prepared)

- **Advanced Games Cog** - `cogs/advanced_games.py`:
  - `!trivia` - Trivia cu 5 intrebari din cultura generala
  - `!wordle` - Wordle game - ghiceste cuvantul
  - `!highscores` - Top 10 Trivia players
  - 5 Trivia questions cu 4 options fiecare
  - 10 Wordle cuvinte disponibile
  - +100 XP reward per trivia corect
  - Auto-integration cu stats system
  - Timeout 30 secunde per intrebare
  - Feedback embed cu raspuns corect/gresit

- **Advanced Moderation Cog** - `cogs/advanced_moderation.py`:
  - `!setwordfilter [cuvinte]` - Seteaza cuvinte interzise (admin)
  - `!setspamprotect [msgs] [minutes]` - Anti-spam rules (admin)
  - `!warn @user [motiv]` - Avertizeaza utilizator (admin)
  - `!warnings @user` - Vede avertisarile (admin)
  - Word filter cu auto-delete mesaje
  - Spam detection si tracking
  - Timeout automat dupa spam detect
  - Auto-ban dupa 3 avertisari
  - Warning system cu motiv si timestamp
  - Per-server configurare (spam_limit, spam_window)

### Technical Details

- **API Endpoints**: 9 active endpoints completi
- **Coguri Adaugate**: 4 (Music, AdvancedGames, AdvancedModeration, + 4 din v1.3.0)
- **Total Coguri Active**: 11 unique cogs
- **Data Files**: user_stats.json, economy.json, ranks.json, game_stats.json, server_logs.json, server_settings.json, verification.json, advanced_moderation.json, reminders.json
- **Database Integration**: JSON-based persistence (ready for SQL migration)
- **Authentication**: API Key based cu header X-API-Key

### Imbunatatit

- API ready pentru production
- Music queue management optimizat
- Advanced games cu XP rewards
- Anti-spam si word filter cu escalation
- Requirements.txt cu Flask, yt-dlp, PyNaCl
- Total 15+ coguri incarcate automat

## Viitor (Planificat)

### v2.1.0 - Web Dashboard
- Flask web interface cu template Jinja2
- Discord OAuth2 authentication
- User profile view si stats
- Server management panel
- Real-time updates cu WebSocket

### v2.2.0 - Database Migration
- PostgreSQL migration
- Redis caching layer
- Celery task queue
- Advanced analytics engine

### v3.0.0 - Platform Expansion
- Multi-platform support
- Telegram bot wrapper
- Slack integration
- Custom API clients

---

**Pentru mai multe detalii, consulta [README.md](README.md)**
