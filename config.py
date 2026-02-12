"""
Configuration and Constants for UBB Discord Bot
"""

import os
from dotenv import load_dotenv
import discord

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENVIRONMENT AND TOKEN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'
INTENTS = discord.Intents.default()
INTENTS.message_content = True

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BOT INFORMATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BOT_NAME = "UBB Discord Bot"
BOT_VERSION = "1.3.0"
BOT_DESCRIPTION = "Un bot Discord creat pentru comunitatea studentilor Universitatii Babes-Bolyai"
BOT_STATUS = "studenti UBB"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# UNIVERSITY INFORMATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UBB_INFO = {
    "name": "Universitatea Babes-Bolyai",
    "location": "Cluj-Napoca, Romania",
    "founded": "1959",
    "students": "~35,000",
    "website": "https://www.ubb.ro",
    "email": "contact@ubb.ro",
    "phone": "+40 264 405 300",
    "address": "Str. Kogalniceanu, nr. 1, Cluj-Napoca, 400084",
    "domains": "Inginerie, Biologie, Matematica, Fizica, Informatica si multe altele"
}

FACULTIES = [
    "Facultatea de Matematica si Informatica",
    "Facultatea de Fizica",
    "Facultatea de Biologie si Geologie",
    "Facultatea de Inginerie",
    "Facultatea de Filologie",
    "Facultatea de Istorie si Filosofie",
    "Facultatea de Drept",
    "Facultatea de Litere",
    "Facultatea de Economie si Gestionare de Afaceri",
    "Facultatea de Geografie"
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IMPORTANT DATES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMPORTANT_DATES = {
    "admission_exam": {
        "name": "Examen de Admitere",
        "month": 7,
        "day": 15
    },
    "competition": {
        "name": "Concurs de Admitere",
        "month": 3,
        "day": 21
    }
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MOTIVATION TIPS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MOTIVATION_TIPS = [
    "Succesul nu vine cu o noapte! Studiaza consistent!",
    "Seteaza-ti obiective clare si atinge-le pas cu pas!",
    "Cititul este cheia - fa note in timp ce studiezi!",
    "Odihna-te suficient! Creierul tau merita asta!",
    "Nu te compara cu ceilalti - compara-te cu persoana din ieri!",
    "O problema grea? Ia pauze regulate si revino cu o minte prospata!",
    "Greselile sunt lectii - nu renunta daca cazi!",
    "Doresti succes? Munca grea + dedicatie = Rezultate!"
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# GRADES SETTINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GRADE_MINIMUM = 1
GRADE_MAXIMUM = 10
PASSING_GRADE = 4.5

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMMANDS INFORMATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMMANDS_BY_CATEGORY = {
    "Calcule si admitere": [
        "!medie note - Calculeaza media notelor (ex: !medie 10 9 8)",
        "!zile - Zile ramase pana la examenul de admitere",
        "!concurs - Zile ramase pana la concursul de admitere"
    ],
    "Informatii UBB": [
        "!ubb - Informatii despre Universitatea Babes-Bolyai",
        "!facultati - Facultati disponibile la UBB",
        "!contact - Date de contact ale universitatii"
    ],
    "Divertisment": [
        "!sfat - Un sfat pentru studiile tale",
        "!moneda - Arunca o moneda (cap/pajura)",
        "!roll - Arunca cu zarul (1-6)"
    ],
    "Stats si Achievements": [
        "!stats [@user] - Vede statisticile tale sau ale altcuiva",
        "!leaderboard - Top 10 utilizatori dupa XP",
        "!achievements [@user] - Vede achievements-urile"
    ],
    "Ranks & Progression": [
        "!rank [@user] - Vede rank-ul tau",
        "!rankinglist - Lista rank-urilor disponibile"
    ],
    "Economy": [
        "!balance - Vede balanta de monezi",
        "!transfer @user suma - Trimite bani",
        "!shop - Vede shop-ul",
        "!buy id - Cumpara item",
        "!inventory - Vede inventarul"
    ],
    "Mini-Jocuri": [
        "!blackjack pariu - Joaca Blackjack",
        "!slots pariu - Joaca Slots",
        "!hangman - Joaca Hangman",
        "!gamestats - Vede statistici jocuri"
    ],
    "Moderatie (Admin only)": [
        "!kick @user [motiv] - Elimina un utilizator",
        "!ban @user [motiv] - Baneaza un utilizator",
        "!unban user#1234 - Debaneaza un utilizator",
        "!warn @user [motiv] - Avertizeaza un utilizator",
        "!purge [numar] - Sterge mesaje (1-100)"
    ],
    "Notificari": [
        "!remind ore mesaj - Seteaza un reminder",
        "!reminders - Vede reamintirile tale",
        "!delreminder index - Sterge un reminder"
    ],
    "Configurare (Admin only)": [
        "!settings - Vede setarile serverului",
        "!setwelcome [mesaj] - Activeaza welcome message",
        "!setwelcomechannel #canal - Seteaza canalul welcome",
        "!setlogchannel #canal - Seteaza canalul de loguri",
        "!setautorole @role - Seteaza rolul automat"
    ],
    "Verificare": [
        "!verify - Verifica-te cu CAPTCHA",
        "!verificationstatus - Vede status verificare"
    ],
    "Admin": [
        "!logs [numar] - Vede logurile serverului",
        "!clearlog - Sterge logurile serverului"
    ]
}

COMMANDS_DETAILS = {
    "help": {
        "descriere": "Afiseaza toate comenzile disponibile",
        "utilizare": "!help sau !help <comanda>",
        "categorie": "Informatii"
    },
    "helpadmin": {
        "descriere": "Afiseaza comenzile admin (Admin only)",
        "utilizare": "!helpadmin",
        "categorie": "Admin"
    },
    "medie": {
        "descriere": "Calculeaza media notelor",
        "utilizare": "!medie 10 9 8 7",
        "categorie": "Calcule si admitere"
    },
    "zile": {
        "descriere": "Arata zilele ramase pana la examenul de admitere",
        "utilizare": "!zile",
        "categorie": "Calcule si admitere"
    },
    "concurs": {
        "descriere": "Arata zilele ramase pana la concursul de admitere",
        "utilizare": "!concurs",
        "categorie": "Calcule si admitere"
    },
    "ubb": {
        "descriere": "Informatii generale despre Universitatea Babes-Bolyai",
        "utilizare": "!ubb",
        "categorie": "Informatii UBB"
    },
    "facultati": {
        "descriere": "Lista facultatilor disponibile la UBB",
        "utilizare": "!facultati",
        "categorie": "Informatii UBB"
    },
    "contact": {
        "descriere": "Date de contact ale universitatii",
        "utilizare": "!contact",
        "categorie": "Informatii UBB"
    },
    "sfat": {
        "descriere": "Un sfat motivator pentru studiu",
        "utilizare": "!sfat",
        "categorie": "Divertisment"
    },
    "moneda": {
        "descriere": "Arunca o moneda virtuala (cap/pajura)",
        "utilizare": "!moneda",
        "categorie": "Divertisment"
    },
    "roll": {
        "descriere": "Arunca un zar (implicit 1-6)",
        "utilizare": "!roll sau !roll 20",
        "categorie": "Divertisment"
    },
    "stats": {
        "descriere": "Vede statisticile tale sau ale altcuiva",
        "utilizare": "!stats sau !stats @user",
        "categorie": "Stats si Achievements"
    },
    "leaderboard": {
        "descriere": "Top 10 utilizatori dupa XP",
        "utilizare": "!leaderboard",
        "categorie": "Stats si Achievements"
    },
    "achievements": {
        "descriere": "Vede achievements-urile tale sau ale altcuiva",
        "utilizare": "!achievements sau !achievements @user",
        "categorie": "Stats si Achievements"
    },
    "kick": {
        "descriere": "Elimina un utilizator din server (Admin only)",
        "utilizare": "!kick @user [motiv]",
        "categorie": "Moderatie"
    },
    "ban": {
        "descriere": "Baneaza un utilizator (Admin only)",
        "utilizare": "!ban @user [motiv]",
        "categorie": "Moderatie"
    },
    "unban": {
        "descriere": "Debaneaza un utilizator (Admin only)",
        "utilizare": "!unban user#1234",
        "categorie": "Moderatie"
    },
    "warn": {
        "descriere": "Avertizeaza un utilizator (Admin only)",
        "utilizare": "!warn @user [motiv]",
        "categorie": "Moderatie"
    },
    "purge": {
        "descriere": "Sterge mesaje din canal (Admin only)",
        "utilizare": "!purge 10",
        "categorie": "Moderatie"
    },
    "adwarn": {
        "descriere": "Avertizeaza cu auto-ban dupa 3 warning-uri (Admin only)",
        "utilizare": "!adwarn @user [motiv]",
        "categorie": "Advanced Moderation"
    },
    "warnlist": {
        "descriere": "Vede avertisarile unui utilizator (Admin only)",
        "utilizare": "!warnlist @user",
        "categorie": "Advanced Moderation"
    },
    "remind": {
        "descriere": "Seteaza un reminder dupa N ore",
        "utilizare": "!remind 24 Studia pentru examen!",
        "categorie": "Notificari"
    },
    "reminders": {
        "descriere": "Vede reamintirile tale active",
        "utilizare": "!reminders",
        "categorie": "Notificari"
    },
    "delreminder": {
        "descriere": "Sterge un reminder dupa index",
        "utilizare": "!delreminder 1",
        "categorie": "Notificari"
    },
    "logs": {
        "descriere": "Vede logurile serverului (Admin only)",
        "utilizare": "!logs 20",
        "categorie": "Admin"
    },
    "clearlog": {
        "descriere": "Sterge logurile serverului (Admin only)",
        "utilizare": "!clearlog",
        "categorie": "Admin"
    },
    "settings": {
        "descriere": "Vede setarile curente ale serverului",
        "utilizare": "!settings",
        "categorie": "Configurare"
    },
    "setwelcome": {
        "descriere": "Seteaza mesajul de welcome",
        "utilizare": "!setwelcome Bine ai venit!",
        "categorie": "Configurare"
    },
    "setwelcomechannel": {
        "descriere": "Seteaza canalul pentru welcome",
        "utilizare": "!setwelcomechannel #channel",
        "categorie": "Configurare"
    },
    "setlogchannel": {
        "descriere": "Seteaza canalul pentru loguri",
        "utilizare": "!setlogchannel #logs",
        "categorie": "Configurare"
    },
    "setautorole": {
        "descriere": "Seteaza rol automat pentru membrii noi",
        "utilizare": "!setautorole @role",
        "categorie": "Configurare"
    },
    "rank": {
        "descriere": "Vede rank-ul tau sau al altcuiva",
        "utilizare": "!rank sau !rank @user",
        "categorie": "Ranks & Progression"
    },
    "rankinglist": {
        "descriere": "Lista tuturor rank-urilor disponibile",
        "utilizare": "!rankinglist",
        "categorie": "Ranks & Progression"
    },
    "balance": {
        "descriere": "Vede balanta ta de monezi",
        "utilizare": "!balance",
        "categorie": "Economy"
    },
    "transfer": {
        "descriere": "Trimite monezi unei persoane",
        "utilizare": "!transfer @user 100",
        "categorie": "Economy"
    },
    "addmoney": {
        "descriere": "[ADMIN] Adauga monezi unui utilizator",
        "utilizare": "!addmoney @user 1000",
        "categorie": "Economy - Admin"
    },
    "removemoney": {
        "descriere": "[ADMIN] Sterge monezi unui utilizator",
        "utilizare": "!removemoney @user 500",
        "categorie": "Economy - Admin"
    },
    "shop": {
        "descriere": "Vede shop-ul disponibil",
        "utilizare": "!shop",
        "categorie": "Economy"
    },
    "buy": {
        "descriere": "Cumpara un item din shop",
        "utilizare": "!buy 1",
        "categorie": "Economy"
    },
    "inventory": {
        "descriere": "Vede inventarul tau",
        "utilizare": "!inventory",
        "categorie": "Economy"
    },
    "use": {
        "descriere": "Foloseste un item din inventar",
        "utilizare": "!use 1",
        "categorie": "Economy"
    },
    "gift": {
        "descriere": "Daruieste un item altui utilizator",
        "utilizare": "!gift @user 1",
        "categorie": "Economy"
    },
    "blackjack": {
        "descriere": "Joaca Blackjack cu pariu",
        "utilizare": "!blackjack 100",
        "categorie": "Mini-Jocuri"
    },
    "slots": {
        "descriere": "Joaca Slot Machine",
        "utilizare": "!slots 50",
        "categorie": "Mini-Jocuri"
    },
    "hangman": {
        "descriere": "Joaca Hangman - Ghiceste cuvantul",
        "utilizare": "!hangman",
        "categorie": "Mini-Jocuri"
    },
    "gamestats": {
        "descriere": "Vede statistici jocuri",
        "utilizare": "!gamestats",
        "categorie": "Mini-Jocuri"
    },
    "verify": {
        "descriere": "Verifica-te cu CAPTCHA pentru a accesa full server",
        "utilizare": "!verify",
        "categorie": "Verificare"
    },
    "verificationstatus": {
        "descriere": "Vede status de verificare",
        "utilizare": "!verificationstatus",
        "categorie": "Verificare"
    },
    "play": {
        "descriere": "Reda o melodie sau URL YouTube",
        "utilizare": "!play Imagine Dragons - Believer",
        "categorie": "Muzica (v2.0.0)"
    },
    "queue": {
        "descriere": "Vede lista de melodii in coada",
        "utilizare": "!queue",
        "categorie": "Muzica (v2.0.0)"
    },
    "skip": {
        "descriere": "Sare la urmatoarea melodie",
        "utilizare": "!skip",
        "categorie": "Muzica (v2.0.0)"
    },
    "pause": {
        "descriere": "Pauzeza melodia curenta",
        "utilizare": "!pause",
        "categorie": "Muzica (v2.0.0)"
    },
    "resume": {
        "descriere": "Reia melodia oprita",
        "utilizare": "!resume",
        "categorie": "Muzica (v2.0.0)"
    },
    "volume": {
        "descriere": "Seteaza volumul (0-100)",
        "utilizare": "!volume 50",
        "categorie": "Muzica (v2.0.0)"
    },
    "stop": {
        "descriere": "Opreste muzica si goleaza coada",
        "utilizare": "!stop",
        "categorie": "Muzica (v2.0.0)"
    },
    "trivia": {
        "descriere": "Joaca Trivia - 5 intrebari cu +100 XP pentru raspunsuri corecte",
        "utilizare": "!trivia",
        "categorie": "Jocuri Avansate (v2.0.0)"
    },
    "wordle": {
        "descriere": "Joaca Wordle - Ghiceste cuvantul in 10 incercari",
        "utilizare": "!wordle",
        "categorie": "Jocuri Avansate (v2.0.0)"
    },
    "highscores": {
        "descriere": "Vede top 10 jucatori la jocuri avansate",
        "utilizare": "!highscores",
        "categorie": "Jocuri Avansate (v2.0.0)"
    },
    "setwordfilter": {
        "descriere": "Seteaza cuvinte interzise auto-sterse (Admin only)",
        "utilizare": "!setwordfilter cuvant1 cuvant2",
        "categorie": "Moderare Avansata (v2.0.0)"
    },
    "setspamprotect": {
        "descriere": "Seteaza protectie anti-spam cu timeout (Admin only)",
        "utilizare": "!setspamprotect 5 10",
        "categorie": "Moderare Avansata (v2.0.0)"
    }
}
