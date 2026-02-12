"""
Cog-ul de Rank-uri Personalizate cu Progresie Vizuala
v1.3.0 Feature
"""

import discord
from discord.ext import commands
import json
import os

class Ranks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ranks_file = "data/ranks.json"
        self.load_ranks()
        
        # Definire rank-uri cu emoticoane si XP necesare
        self.rank_tiers = [
            {"level": 1, "name": "Noob", "emoji": "🥚", "xp_required": 0},
            {"level": 2, "name": "Learner", "emoji": "🐣", "xp_required": 100},
            {"level": 3, "name": "Student", "emoji": "📚", "xp_required": 300},
            {"level": 4, "name": "Scholar", "emoji": "🎓", "xp_required": 600},
            {"level": 5, "name": "Master", "emoji": "⚡", "xp_required": 1000},
            {"level": 6, "name": "Legend", "emoji": "👑", "xp_required": 1500},
            {"level": 7, "name": "Mythical", "emoji": "🌟", "xp_required": 2500},
            {"level": 8, "name": "Godlike", "emoji": "🔱", "xp_required": 5000},
        ]
    
    def load_ranks(self):
        """Incarca datele de rank-uri"""
        if not os.path.exists(self.ranks_file):
            self.ranks = {}
        else:
            try:
                with open(self.ranks_file, 'r') as f:
                    self.ranks = json.load(f)
            except:
                self.ranks = {}
    
    def save_ranks(self):
        """Salveaza datele de rank-uri"""
        os.makedirs(os.path.dirname(self.ranks_file), exist_ok=True)
        with open(self.ranks_file, 'w') as f:
            json.dump(self.ranks, f, indent=4)
    
    def get_rank(self, xp):
        """Determina rank-ul pe baza XP"""
        for rank in reversed(self.rank_tiers):
            if xp >= rank["xp_required"]:
                return rank
        return self.rank_tiers[0]
    
    def get_progress_bar(self, current_xp, next_tier_xp):
        """Creeaza o progress bar vizuala"""
        if current_xp >= next_tier_xp:
            progress = 10
        else:
            progress = int((current_xp / next_tier_xp) * 10)
        
        filled = "█" * progress
        empty = "░" * (10 - progress)
        return f"{filled}{empty} {current_xp}/{next_tier_xp}"
    
    @commands.command(name='rank')
    async def view_rank(self, ctx, user: discord.Member = None):
        """Vede rank-ul tau sau al altcuiva"""
        if user is None:
            user = ctx.author
        
        user_id = str(user.id)
        
        # Obtine XP din stats
        try:
            with open("data/user_stats.json", 'r') as f:
                stats = json.load(f)
                user_xp = stats.get(user_id, {}).get("experience", 0)
        except:
            user_xp = 0
        
        current_rank = self.get_rank(user_xp)
        
        # Gaseste next rank
        next_rank = None
        for rank in self.rank_tiers:
            if rank["xp_required"] > user_xp:
                next_rank = rank
                break
        
        if next_rank is None:
            next_rank = self.rank_tiers[-1]
        
        progress = self.get_progress_bar(user_xp, next_rank["xp_required"])
        
        embed = discord.Embed(
            title=f"Rank-ul lui {user.name}",
            color=discord.Color.gold()
        )
        embed.add_field(
            name=f"{current_rank['emoji']} {current_rank['name']}",
            value=f"Level {current_rank['level']}",
            inline=False
        )
        embed.add_field(
            name="Experienta",
            value=f"```{progress}```",
            inline=False
        )
        embed.add_field(
            name="XP Total",
            value=f"{user_xp} XP",
            inline=True
        )
        embed.add_field(
            name="Pana la urmatorul Rank",
            value=f"{next_rank['xp_required'] - user_xp} XP",
            inline=True
        )
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text=f"Rank global: {current_rank['level']}/8")
        
        await ctx.send(embed=embed)
    
    @commands.command(name='rankinglist')
    async def ranking_list(self, ctx):
        """Vede lista tuturor rank-urilor disponibile"""
        embed = discord.Embed(
            title="Rank-uri Disponibile",
            description="Progresie de la Noob pana la Godlike",
            color=discord.Color.purple()
        )
        
        for rank in self.rank_tiers:
            embed.add_field(
                name=f"{rank['emoji']} {rank['name']} (Level {rank['level']})",
                value=f"Necesita {rank['xp_required']} XP",
                inline=False
            )
        
        embed.set_footer(text="Acumuleaza XP prin mesaje si comenzi!")
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Notifica cand utilizatorul atinge un nou rank"""
        # Acest listener va fi apelat din stats cog la gainarea XP
        pass

async def setup(bot):
    await bot.add_cog(Ranks(bot))
