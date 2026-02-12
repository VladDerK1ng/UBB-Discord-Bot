"""
Cog-ul Mini-jocuri Integrate cu Reward System
v1.3.0 Feature
"""

import discord
from discord.ext import commands
import random
import json
import os

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games_file = "data/game_stats.json"
        self.load_game_stats()
    
    def load_game_stats(self):
        """Incarca statistici jocuri"""
        if not os.path.exists(self.games_file):
            self.game_stats = {}
        else:
            try:
                with open(self.games_file, 'r') as f:
                    self.game_stats = json.load(f)
            except:
                self.game_stats = {}
    
    def save_game_stats(self):
        """Salveaza statistici jocuri"""
        os.makedirs(os.path.dirname(self.games_file), exist_ok=True)
        with open(self.games_file, 'w') as f:
            json.dump(self.game_stats, f, indent=4)
    
    def add_game_stat(self, user_id, game, result):
        """Adauga o statistica de joc"""
        user_id = str(user_id)
        if user_id not in self.game_stats:
            self.game_stats[user_id] = {"blackjack": {"wins": 0, "losses": 0, "total": 0}, 
                                       "slots": {"wins": 0, "losses": 0, "total": 0},
                                       "hangman": {"wins": 0, "losses": 0, "total": 0}}
        
        if game in self.game_stats[user_id]:
            self.game_stats[user_id][game]["total"] += 1
            if result == "win":
                self.game_stats[user_id][game]["wins"] += 1
            else:
                self.game_stats[user_id][game]["losses"] += 1
        
        self.save_game_stats()
    
    @commands.command(name='blackjack')
    async def blackjack(self, ctx, bet: int = None):
        """
        Joc de Blackjack cu monezi
        Utilizare: !blackjack 100
        """
        if bet is None:
            embed = discord.Embed(
                title="Blackjack - Cum se Joaca",
                description="Trebuie sa ajungi la 21 fara sa depasesti!",
                color=discord.Color.red()
            )
            embed.add_field(name="Comenzi", value="!hit - Iau o carte\n!stand - Stau", inline=False)
            embed.add_field(name="Utilizare", value="!blackjack [pariu]", inline=False)
            await ctx.send(embed=embed)
            return
        
        if bet <= 0:
            await ctx.send("Parirul trebuie sa fie pozitiv!")
            return
        
        # Verifica bani si deducte bet
        try:
            with open("data/economy.json", 'r') as f:
                economy = json.load(f)
            
            user_id = str(ctx.author.id)
            balance = economy.get(user_id, {}).get("balance", 0)
            
            if balance < bet:
                embed = discord.Embed(
                    title="Bani Insuficienti",
                    description=f"Ai nevoie de 💰 {bet} dar ai doar 💰 {balance}",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
                return
            
            # Deducte bet-ul din balanta
            if user_id not in economy:
                economy[user_id] = {"balance": 0, "items": {}}
            economy[user_id]["balance"] -= bet
        except Exception as e:
            embed = discord.Embed(
                title="Eroare",
                description="Nu am gasit datele economice.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        # Joc
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10, J, Q, K sunt 10, A este 11
        
        player_hand = [random.choice(cards), random.choice(cards)]
        dealer_hand = [random.choice(cards), random.choice(cards)]
        
        player_total = sum(player_hand)
        dealer_total = sum(dealer_hand)
        
        embed = discord.Embed(
            title="Blackjack",
            color=discord.Color.red()
        )
        embed.add_field(name="Cartile Tale", value=f"{player_hand} = {player_total}", inline=False)
        embed.add_field(name="Carta Dilerului", value=f"[{dealer_hand[0]}, ?]", inline=False)
        embed.add_field(name="Pariu", value=f"💰 {bet}", inline=False)
        embed.set_footer(text="Alege: !hit sau !stand")
        
        msg = await ctx.send(embed=embed)
        
        # Logica Blackjack
        result = "loss"
        winnings = 0
        final_msg = ""
        
        if player_total == 21 and len(player_hand) == 2:
            result = "win"
            winnings = int(bet * 2.5)
            final_msg = f"🎉 BLACKJACK! Ai castigat 💰 {winnings}"
        elif player_total > 21:
            result = "loss"
            final_msg = f"💥 BUST! Ai pierdut 💰 {bet}"
        elif player_total > dealer_total:
            result = "win"
            winnings = bet * 2
            final_msg = f"✅ Ai castigat! Dilerrul are {dealer_total}. Castig: 💰 {winnings}"
        elif player_total < dealer_total and dealer_total <= 21:
            result = "loss"
            final_msg = f"❌ Ai pierdut! Dilerrul are {dealer_total}. Pierdere: 💰 {bet}"
        else:
            result = "loss"
            final_msg = f"Tie! Totul este egal. Pariu returnat: 💰 {bet}"
            winnings = bet
        
        # Actualizeaza balanta
        try:
            economy[user_id]["balance"] += winnings
            with open("data/economy.json", 'w') as f:
                json.dump(economy, f, indent=4)
        except:
            pass
        
        self.add_game_stat(ctx.author.id, "blackjack", result)
        
        embed = discord.Embed(
            title="Rezultat Blackjack",
            description=final_msg,
            color=discord.Color.green() if result == "win" else discord.Color.red()
        )
        embed.add_field(name="Balanta Noua", value=f"💰 {economy[user_id]['balance']}", inline=False)
        await msg.edit(embed=embed)
    
    @commands.command(name='slots')
    async def slots(self, ctx, bet: int = None):
        """
        Joc de Slot Machine
        Utilizare: !slots 50
        """
        if bet is None or bet <= 0:
            embed = discord.Embed(
                title="Slots Machine",
                description="Joc de noroc cu pariu",
                color=discord.Color.gold()
            )
            embed.add_field(name="Utilizare", value="!slots [pariu]", inline=False)
            embed.add_field(name="Payout", value="🎰 Match 3 = 5x pariul", inline=False)
            await ctx.send(embed=embed)
            return
        
        symbols = ["🍎", "🍊", "🍋", "🍌", "🍇", "🎰"]
        
        reels = [random.choice(symbols) for _ in range(3)]
        
        embed = discord.Embed(
            title="Slot Machine",
            description=f"{reels[0]} | {reels[1]} | {reels[2]}",
            color=discord.Color.gold()
        )
        embed.add_field(name="Pariu", value=f"💰 {bet}", inline=False)
        
        if reels[0] == reels[1] == reels[2]:
            result = "win"
            winnings = bet * 5
            embed.add_field(name="Rezultat", value=f"🎉 JACKPOT! Ai castigat 💰 {winnings}", inline=False)
            embed.color = discord.Color.green()
        elif reels[0] == reels[1] or reels[1] == reels[2]:
            result = "win"
            winnings = bet * 2
            embed.add_field(name="Rezultat", value=f"Ai castigat 💰 {winnings}", inline=False)
            embed.color = discord.Color.green()
        else:
            result = "loss"
            embed.add_field(name="Rezultat", value=f"Ai pierdut 💰 {bet}", inline=False)
            embed.color = discord.Color.red()
        
        self.add_game_stat(ctx.author.id, "slots", result)
        await ctx.send(embed=embed)
    
    @commands.command(name='hangman')
    async def hangman(self, ctx):
        """
        Joc de Hangman
        Ghiceste cuvantul!
        """
        words = ["discord", "python", "programming", "university", "computer", "developer", "algorithm", "gaming", "database", "network"]
        word = random.choice(words).lower()
        
        guessed = set()
        wrong = set()
        max_wrong = 6
        
        embed = discord.Embed(
            title="Hangman - Ghiceste Cuvantul",
            color=discord.Color.blue()
        )
        display = " ".join([letter if letter in guessed else "_" for letter in word])
        embed.add_field(name="Cuvantul", value=f"`{display}`", inline=False)
        embed.add_field(name="Gresite", value=f"{', '.join(wrong) if wrong else 'None'}", inline=False)
        embed.add_field(name="Incercari Ramase", value=f"{max_wrong - len(wrong)}/{max_wrong}", inline=False)
        embed.set_footer(text="Scrie o litera: !guess a")
        
        msg = await ctx.send(embed=embed)
        
        result = "loss"
        # Asteapta raspunsuri pentru 60 de secunde
        attempts = 0
        while attempts < max_wrong and len(guessed) < len(set(word)):
            try:
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel and len(m.content) == 1 and m.content.isalpha()
                
                response = await self.bot.wait_for("message", check=check, timeout=10)
                letter = response.content.lower()
                
                if letter in guessed or letter in wrong:
                    continue
                
                if letter in word:
                    guessed.add(letter)
                else:
                    wrong.add(letter)
                    attempts += 1
                
                display = " ".join([letter if letter in guessed else "_" for letter in word])
                embed = discord.Embed(
                    title="Hangman",
                    color=discord.Color.blue()
                )
                embed.add_field(name="Cuvantul", value=f"`{display}`", inline=False)
                embed.add_field(name="Gresite", value=f"{', '.join(wrong) if wrong else 'None'}", inline=False)
                embed.add_field(name="Incercari Ramase", value=f"{max_wrong - attempts}/{max_wrong}", inline=False)
                await msg.edit(embed=embed)
                
                if len(guessed) >= len(set(word)):
                    result = "win"
                    break
                    
            except:
                break
        
        self.add_game_stat(ctx.author.id, "hangman", result)
        
        result_embed = discord.Embed(
            title="Hangman Terminat",
            description=f"Cuvantul era: `{word}`",
            color=discord.Color.green() if result == "win" else discord.Color.red()
        )
        result_embed.add_field(name="Rezultat", value="✅ AI CASTIGAT!" if result == "win" else "❌ AI PIERDUT!", inline=False)
        await msg.edit(embed=result_embed)
    
    @commands.command(name='gamestats')
    async def game_stats(self, ctx, user: discord.Member = None):
        """Vede statistici jocuri"""
        if user is None:
            user = ctx.author
        
        user_id = str(user.id)
        stats = self.game_stats.get(user_id, {})
        
        embed = discord.Embed(
            title=f"Statistici Jocuri - {user.name}",
            color=discord.Color.gold()
        )
        
        for game, data in stats.items():
            total = data.get("total", 0)
            if total > 0:
                win_rate = (data.get("wins", 0) / total * 100)
                embed.add_field(
                    name=game.upper(),
                    value=f"Victorii: {data.get('wins', 0)}\nInfrangeri: {data.get('losses', 0)}\nWin Rate: {win_rate:.1f}%",
                    inline=True
                )
        
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Games(bot))
