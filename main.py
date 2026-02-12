"""
UBB Discord Bot - Chatbot pentru comunitatea studentilor UBB
Ajuta cu calcule, informatii despre universitate si divertisment!
"""

import os
import discord
import datetime
import random
from discord.ext import commands
from dotenv import load_dotenv

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONFIGURARE SI INITIALIZARE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("Eroare: Nu am gasit token-ul! Ai creat fisierul .env?")
    print("Creeaza un fisier .env cu: DISCORD_TOKEN=your_token_here")
    exit()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# INCARCARE COGS (Module)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def load_cogs():
    """Incarca toti cogurile din folderul cogs/"""
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Cog incarcat: {filename[:-3]}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EVENIMENTE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.event
async def on_ready():
    """Se executa cand botul se conecteaza cu succes"""
    print(f'Botul {bot.user} este conectat!')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="studenti UBB")
    )

@bot.event
async def on_command_error(ctx, error):
    """Trateaza erori la comenzi"""
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Eroare - comanda nu exista",
            description=f"Nu am gasit comanda. Scrie !help pentru a vedea toate comenzile.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Argumente lipsa",
            description=f"Comanda este incompleta! Scrie !help {ctx.command.name} pentru detalii.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Eroare neasteptata",
            description="A aparut o eroare.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        print(f"Eroare: {error}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMENZI - INFORMATII SI AJUTOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='help')
async def help_command(ctx, command: str = None):
    """Afiseaza toate comenzile disponibile sau help pentru o anumita comanda"""
    
    commands_details = {
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
        "purge": {
            "descriere": "Sterge mesaje din canal (Admin only)",
            "utilizare": "!purge 10",
            "categorie": "Moderatie"
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
        },
        "adwarn": {
            "descriere": "Avertizeaza cu auto-ban dupa 3 warning-uri (Admin only)",
            "utilizare": "!adwarn @user [motiv]",
            "categorie": "Moderare Avansata (v2.0.0)"
        },
        "warnlist": {
            "descriere": "Vede avertisarile unui utilizator (Admin only)",
            "utilizare": "!warnlist @user",
            "categorie": "Moderare Avansata (v2.0.0)"
        }
    }
    
    if command is None:
        embed = discord.Embed(
            title="Comenzi Disponibile",
            description="Acestea sunt comenzile pe care le poti folosi cu acest bot.",
            color=discord.Color.blue()
        )
        
        commands_info = [
            ("Calcule si admitere", [
                "!medie note - Calculeaza media notelor (ex: !medie 10 9 8)",
                "!zile - Zile ramase pana la examenul de admitere",
                "!concurs - Zile ramase pana la concursul de admitere"
            ]),
            ("Informatii UBB", [
                "!ubb - Informatii despre Universitatea Babes-Bolyai",
                "!facultati - Facultati disponibile la UBB",
                "!contact - Date de contact ale universitatii"
            ]),
            ("Divertisment", [
                "!sfat - Un sfat pentru studiile tale",
                "!moneda - Arunca o moneda (cap/pajura)",
                "!roll - Arunca cu zarul (1-6)"
            ]),
            ("Stats si Achievements", [
                "!stats [@user] - Vede statisticile tale sau ale altcuiva",
                "!leaderboard - Top 10 utilizatori dupa XP",
                "!achievements [@user] - Vede achievements-urile"
            ]),
            ("Ranks & Progression", [
                "!rank [@user] - Vede rank-ul tau",
                "!rankinglist - Lista rank-urilor disponibile"
            ]),
            ("Economy", [
                "!balance - Vede balanta de monezi",
                "!transfer @user suma - Trimite bani",
                "!shop - Vede shop-ul",
                "!buy id - Cumpara item",
                "!inventory - Vede inventarul"
            ]),
            ("Mini-Jocuri", [
                "!blackjack pariu - Joaca Blackjack",
                "!slots pariu - Joaca Slots",
                "!hangman - Joaca Hangman",
                "!gamestats - Vede statistici jocuri"
            ]),
            ("Moderatie (Admin only)", [
                "!kick @user [motiv] - Elimina un utilizator",
                "!ban @user [motiv] - Baneaza un utilizator",
                "!unban user#1234 - Debaneaza un utilizator",
                "!warn @user [motiv] - Avertizeaza un utilizator",
                "!purge [numar] - Sterge mesaje (1-100)"
            ]),
            ("Notificari", [
                "!remind ore mesaj - Seteaza un reminder",
                "!reminders - Vede reamintirile tale",
                "!delreminder index - Sterge un reminder"
            ]),
            ("Configurare (Admin only)", [
                "!settings - Vede setarile serverului",
                "!setwelcome [mesaj] - Activeaza welcome message",
                "!setwelcomechannel #canal - Seteaza canalul welcome",
                "!setlogchannel #canal - Seteaza canalul de loguri",
                "!setautorole @role - Seteaza rolul automat"
            ]),
            ("Verificare", [
                "!verify - Verifica-te cu CAPTCHA",
                "!verificationstatus - Vede status verificare"
            ]),
            ("Admin", [
                "!logs [numar] - Vede logurile serverului",
                "!clearlog - Sterge logurile serverului"
            ])
        ]
        
        for category, cmds in commands_info:
            embed.add_field(name=category, value="\n".join(cmds), inline=False)
        
        embed.set_footer(text="Scrie !help <comanda> pentru mai detalii")
        await ctx.send(embed=embed)
    else:
        command = command.lower()
        if command in commands_details:
            info = commands_details[command]
            embed = discord.Embed(
                title=f"Help - {command.upper()}",
                color=discord.Color.green()
            )
            embed.add_field(name="Descriere", value=info["descriere"], inline=False)
            embed.add_field(name="Utilizare", value=f"`{info['utilizare']}`", inline=False)
            embed.add_field(name="Categorie", value=info["categorie"], inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Eroare",
                description=f"Comanda `{command}` nu exista! Scrie !help pentru lista completa.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

@bot.command(name='info')
async def info(ctx):
    """Informatii despre bot"""
    embed = discord.Embed(
        title="UBB Discord Bot",
        description="Un bot Discord creat pentru comunitatea studentilor Universitatii Babes-Bolyai",
        color=discord.Color.gold()
    )
    embed.add_field(name="Obiectiv", value="Ajuta studentii cu calcule, informatii si divertisment.", inline=False)
    embed.add_field(name="Versiune", value="1.3.0", inline=True)
    embed.add_field(name="Limbaj", value="Python + discord.py", inline=True)
    embed.add_field(name="Features", value="Stats, Ranks, Economy, Games, Verification", inline=False)
    embed.set_footer(text="Made for UBB students")
    await ctx.send(embed=embed)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMENZI - CALCULE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='medie')
async def medie(ctx, *note: int):
    """Calculeaza media notelor
    
    Utilizare: !medie 10 9 8 7
    """
    if not note:
        embed = discord.Embed(
            title="Nicio nota introdusa",
            description="Scrie notele dupa comanda, ex: !medie 10 9 8",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return
    
    if any(n < 1 or n > 10 for n in note):
        embed = discord.Embed(
            title="Nota invalida",
            description="Notele trebuie sa fie intre 1 si 10!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return
    
    media = sum(note) / len(note)
    color = discord.Color.green() if media >= 4.5 else discord.Color.red()
    
    embed = discord.Embed(
        title="Calculul Mediei",
        description=f"Note: {', '.join(map(str, note))}",
        color=color
    )
    embed.add_field(name="Media", value=f"**{media:.2f}**", inline=True)
    embed.add_field(name="Total note", value=f"**{len(note)}**", inline=True)
    embed.add_field(name="Promovat?", value="DA" if media >= 4.5 else "NU", inline=True)
    
    await ctx.send(embed=embed)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMENZI - CALENDARE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='zile')
async def zile(ctx):
    """Zile ramase pana la examen"""
    an_actual = datetime.datetime.now().year
    admitere = datetime.datetime(an_actual, 7, 15)
    azi = datetime.datetime.now()
    diferenta = admitere - azi
    
    embed = discord.Embed(
        title="Examen de Admitere",
        color=discord.Color.blue()
    )
    embed.add_field(name="Data", value="15 Iulie", inline=True)
    embed.add_field(name="Zile ramase", value=f"**{diferenta.days}**", inline=True)
    embed.add_field(name="Ore ramase", value=f"**{diferenta.days * 24 + diferenta.seconds // 3600}**", inline=True)
    
    if diferenta.days < 0:
        embed.set_footer(text="Examenul a trecut!")
    else:
        embed.set_footer(text="Mult succes la pregatire!")
    
    await ctx.send(embed=embed)

@bot.command(name='concurs')
async def concurs(ctx):
    """Zile ramase pana la concurs"""
    an_actual = datetime.datetime.now().year
    data_concurs = datetime.datetime(an_actual, 3, 21)
    azi = datetime.datetime.now()
    diferenta = data_concurs - azi
    
    embed = discord.Embed(
        title="Concurs de Admitere",
        color=discord.Color.purple()
    )
    embed.add_field(name="Data", value="21 Martie", inline=True)
    embed.add_field(name="Zile ramase", value=f"**{diferenta.days}**", inline=True)
    embed.add_field(name="Ore ramase", value=f"**{diferenta.days * 24 + diferenta.seconds // 3600}**", inline=True)
    
    if diferenta.days < 0:
        embed.set_footer(text="Concursul a trecut!")
    else:
        embed.set_footer(text="Pregatire intensa!")
    
    await ctx.send(embed=embed)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMENZI - INFORMATII UBB
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='ubb')
async def ubb(ctx):
    """Informatii despre UBB"""
    embed = discord.Embed(
        title="Universitatea Babes-Bolyai",
        description="Una dintre cele mai prestigioase universitati din Romania",
        color=discord.Color.gold()
    )
    embed.add_field(name="Locatie", value="Cluj-Napoca, Romania", inline=False)
    embed.add_field(name="Infiintata", value="1959", inline=True)
    embed.add_field(name="Studenti", value="~35,000", inline=True)
    embed.add_field(name="Domenii", value="Inginerie, Biologie, Matematica, Fizica, Informatica si multe altele", inline=False)
    embed.set_footer(text="Scrie !facultati pentru a vedea facultatile disponibile")
    
    await ctx.send(embed=embed)

@bot.command(name='facultati')
async def facultati(ctx):
    """Lista facultatilor UBB"""
    embed = discord.Embed(
        title="Facultati UBB",
        description="Facultatile disponibile la Universitatea Babes-Bolyai",
        color=discord.Color.blue()
    )
    
    facultati_list = [
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
    
    embed.add_field(name="Facultati disponibile:", value="\n".join(facultati_list), inline=False)
    embed.set_footer(text="Viziteaza ubb.ro pentru mai multe informatii")
    
    await ctx.send(embed=embed)

@bot.command(name='contact')
async def contact(ctx):
    """Date de contact UBB"""
    embed = discord.Embed(
        title="Contact UBB",
        color=discord.Color.green()
    )
    embed.add_field(name="Website", value="https://www.ubb.ro", inline=False)
    embed.add_field(name="Email", value="contact@ubb.ro", inline=False)
    embed.add_field(name="Telefon", value="+40 264 405 300", inline=False)
    embed.add_field(name="Adresa", value="Str. Kogalniceanu, nr. 1, Cluj-Napoca, 400084", inline=False)
    embed.set_footer(text="Pentru mai multe informatii, viziteaza site-ul oficial")
    
    await ctx.send(embed=embed)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COMENZI - DIVERTISMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='sfat')
async def sfat(ctx):
    """Un sfat motivator"""
    sfaturi = [
        "Succesul nu vine cu o noapte! Studiaza consistent!",
        "Seteaza-ti obiective clare si atinge-le pas cu pas!",
        "Cititul este cheia - fa note in timp ce studiezi!",
        "Odihna-te suficient! Creierul tau merita asta!",
        "Nu te compara cu ceilalti - compara-te cu persoana din ieri!",
        "O problema grea? Ia pauze regulate si revino cu o minte prospata!",
        "Greselile sunt lectii - nu renunta daca cazi!",
        "Doresti succes? Munca grea + dedicatie = Rezultate!"
    ]
    
    embed = discord.Embed(
        title="Sfat pentru Tine",
        description=random.choice(sfaturi),
        color=discord.Color.gold()
    )
    embed.set_footer(text="Tu poti!")
    
    await ctx.send(embed=embed)

@bot.command(name='moneda')
async def moneda(ctx):
    """Arunca o moneda virtuala"""
    rezultat = random.choice(['CAP', 'PAJURA'])
    
    embed = discord.Embed(
        title="Arunca Moneda",
        description=f"Rezultat: **{rezultat}**",
        color=random.choice([discord.Color.gold(), discord.Color.greyple()])
    )
    
    await ctx.send(embed=embed)

@bot.command(name='roll')
async def roll(ctx, max_val: int = 6):
    """Arunca un zar (implicit 1-6)"""
    if max_val < 1:
        embed = discord.Embed(
            title="Valoare invalida",
            description="Zarul trebuie sa aiba minim 1 si maxim!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return
    
    rezultat = random.randint(1, max_val)
    
    embed = discord.Embed(
        title="Rezultatul Zarului",
        description=f"Zarul se rostogoleste...\n\n**{rezultat}** / {max_val}",
        color=discord.Color.red()
    )
    
    await ctx.send(embed=embed)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PORNIRE BOT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == "__main__":
    print("Se porneste UBB Discord Bot...")
    import asyncio
    asyncio.run(main())