"""
Cog-ul de Stats si Achievements - tracking utilizatorilor
"""

import discord
from discord.ext import commands
import json
import os
from datetime import datetime

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stats_file = "data/user_stats.json"
        self.load_stats()
    
    def load_stats(self):
        """Incarca datele de stats din fisier"""
        if not os.path.exists(self.stats_file):
            self.stats = {}
        else:
            with open(self.stats_file, 'r') as f:
                self.stats = json.load(f)
    
    def save_stats(self):
        """Salveaza datele de stats in fisier"""
        os.makedirs(os.path.dirname(self.stats_file), exist_ok=True)
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=4)
    
    def get_user_stats(self, user_id):
        """Obtine statisticile unui utilizator"""
        user_id = str(user_id)
        if user_id not in self.stats:
            self.stats[user_id] = {
                "commands_used": 0,
                "messages_sent": 0,
                "last_message": None,
                "achievements": [],
                "level": 1,
                "experience": 0
            }
            self.save_stats()
        return self.stats[user_id]
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Tracker pentru mesaje"""
        if message.author == self.bot.user:
            return
        
        user_stats = self.get_user_stats(message.author.id)
        user_stats["messages_sent"] += 1
        user_stats["experience"] += 5
        user_stats["last_message"] = datetime.now().isoformat()
        
        if user_stats["experience"] >= user_stats["level"] * 100:
            user_stats["level"] += 1
            user_stats["achievements"].append(f"Level {user_stats['level']}")
        
        self.save_stats()
    
    @commands.Cog.listener()
    async def on_command(self, ctx):
        """Tracker pentru comenzi"""
        user_stats = self.get_user_stats(ctx.author.id)
        user_stats["commands_used"] += 1
        user_stats["experience"] += 10
        self.save_stats()
    
    @commands.command(name='stats')
    async def stats(self, ctx, member: discord.Member = None):
        """Afiseaza statisticile unui utilizator"""
        if member is None:
            member = ctx.author
        
        user_stats = self.get_user_stats(member.id)
        
        embed = discord.Embed(
            title=f"Statistici - {member.name}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Level", value=f"**{user_stats['level']}**", inline=True)
        embed.add_field(name="Experience", value=f"**{user_stats['experience']} XP**", inline=True)
        embed.add_field(name="Comenzi Folosite", value=f"**{user_stats['commands_used']}**", inline=True)
        embed.add_field(name="Mesaje Trimise", value=f"**{user_stats['messages_sent']}**", inline=True)
        
        if user_stats["achievements"]:
            embed.add_field(
                name="Achievements",
                value=", ".join(user_stats["achievements"]),
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='leaderboard')
    async def leaderboard(self, ctx):
        """Afiseaza top 10 utilizatori dupa XP"""
        sorted_users = sorted(
            self.stats.items(),
            key=lambda x: x[1].get("experience", 0),
            reverse=True
        )[:10]
        
        embed = discord.Embed(
            title="Leaderboard XP",
            description="Top 10 utilizatori",
            color=discord.Color.gold()
        )
        
        for i, (user_id, stats) in enumerate(sorted_users, 1):
            try:
                user = await self.bot.fetch_user(int(user_id))
                embed.add_field(
                    name=f"#{i} - {user.name}",
                    value=f"**{stats.get('experience', 0)} XP** | Level {stats.get('level', 1)}",
                    inline=False
                )
            except:
                pass
        
        await ctx.send(embed=embed)
    
    @commands.command(name='achievements')
    async def achievements(self, ctx, member: discord.Member = None):
        """Afiseaza achievements-urile unui utilizator"""
        if member is None:
            member = ctx.author
        
        user_stats = self.get_user_stats(member.id)
        
        embed = discord.Embed(
            title=f"Achievements - {member.name}",
            color=discord.Color.purple()
        )
        
        if user_stats["achievements"]:
            achievements_list = "\n".join([f"  {ach}" for ach in user_stats["achievements"]])
            embed.description = achievements_list
        else:
            embed.description = "Nu ai inca niciun achievement!"
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Stats(bot))
