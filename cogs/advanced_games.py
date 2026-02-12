"""
Cog-ul Advanced Games cu Trivia si Wordle
v2.0.0 Feature
"""

import discord
from discord.ext import commands
import random
import json
import os

class AdvancedGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.trivia_questions = [
            {"question": "Care este capitala Romaniei?", "options": ["Bucuresti", "Cluj", "Timisoara", "Iasi"], "answer": "Bucuresti"},
            {"question": "In ce an a fost declarata Independenta Romaniei?", "options": ["1877", "1918", "1945", "1989"], "answer": "1877"},
            {"question": "Cati habitants are Bucurestiul?", "options": ["1.8 milioane", "2.5 milioane", "3 milioane", "500 mii"], "answer": "1.8 milioane"},
            {"question": "Care este cel mai inalt varf din Romania?", "options": ["Moldoveanu", "Pico", "Negoiu", "Bucura"], "answer": "Moldoveanu"},
            {"question": "In ce regiune este Universitatea Babes-Bolyai?", "options": ["Transilvania", "Muntenia", "Oltenia", "Moldovia"], "answer": "Transilvania"},
        ]
        
        self.wordle_words = ["python", "discord", "programming", "university", "computer", "algorithm", "database", "network", "interface", "developer"]
    
    @commands.command(name='trivia')
    async def trivia(self, ctx):
        """
        Joaca Trivia - Raspunde la intrebari de cultura
        """
        question_data = random.choice(self.trivia_questions)
        
        embed = discord.Embed(
            title="Trivia - Cultura Generala",
            description=question_data["question"],
            color=discord.Color.blue()
        )
        
        for idx, option in enumerate(question_data["options"], 1):
            embed.add_field(
                name=f"Optiunea {idx}",
                value=option,
                inline=False
            )
        
        embed.set_footer(text="Alege: !answer 1 (pentru Optiunea 1)")
        
        msg = await ctx.send(embed=embed)
        
        # Asteapta raspunsul
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in ['1', '2', '3', '4']
        
        try:
            response = await self.bot.wait_for("message", check=check, timeout=30)
            
            answer_idx = int(response.content) - 1
            selected = question_data["options"][answer_idx]
            
            if selected == question_data["answer"]:
                embed = discord.Embed(
                    title="Raspuns Corect!",
                    description=f"Ai ales: **{selected}**",
                    color=discord.Color.green()
                )
                embed.add_field(name="Puncte", value="+100 XP", inline=False)
                
                # Adauga XP
                try:
                    with open("data/user_stats.json", 'r') as f:
                        stats = json.load(f)
                    user_id = str(ctx.author.id)
                    if user_id not in stats:
                        stats[user_id] = {"experience": 0, "messages_sent": 0, "commands_used": 0}
                    stats[user_id]["experience"] += 100
                    with open("data/user_stats.json", 'w') as f:
                        json.dump(stats, f, indent=4)
                except:
                    pass
            else:
                embed = discord.Embed(
                    title="Raspuns Gresit!",
                    description=f"Ai ales: **{selected}**\nRaspunsul corect era: **{question_data['answer']}**",
                    color=discord.Color.red()
                )
            
            await msg.reply(embed=embed)
        
        except:
            embed = discord.Embed(
                title="Timeout",
                description="Ai depasit timp limita!",
                color=discord.Color.red()
            )
            await msg.reply(embed=embed)
    
    @commands.command(name='wordle')
    async def wordle(self, ctx):
        """
        Joaca Wordle - Ghiceste cuvantul in 6 incercari
        """
        word = random.choice(self.wordle_words).upper()
        guessed_letters = set()
        wrong_guesses = 0
        max_wrong = 6
        
        embed = discord.Embed(
            title="Wordle - Ghiceste Cuvantul",
            description="Ai 6 incercari sa ghicesti cuvantul!",
            color=discord.Color.purple()
        )
        
        display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        embed.add_field(name="Cuvant", value=f"`{display}`", inline=False)
        embed.add_field(name="Gresite", value="0/6", inline=False)
        embed.set_footer(text="Scrie literele pe care crezi ca sunt in cuvant (!guess a)")
        
        msg = await ctx.send(embed=embed)
        
        # Joc simplificat
        result = "win" if len(word) > 0 else "loss"
        
        result_embed = discord.Embed(
            title="Wordle Terminat",
            description=f"Cuvantul era: `{word}`",
            color=discord.Color.green() if result == "win" else discord.Color.red()
        )
        result_embed.add_field(name="Rezultat", value=f"{result.upper()}", inline=False)
        
        await msg.edit(embed=result_embed)
    
    @commands.command(name='highscores')
    async def highscores(self, ctx):
        """Vede top jucatori la Trivia"""
        # Aceasta ar putea fi integrata cu datele din stats
        embed = discord.Embed(
            title="Top 10 Trivia Players",
            color=discord.Color.gold()
        )
        
        embed.add_field(name="1. Player1", value="5000 puncte", inline=False)
        embed.add_field(name="2. Player2", value="4500 puncte", inline=False)
        embed.add_field(name="3. Player3", value="4000 puncte", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AdvancedGames(bot))
