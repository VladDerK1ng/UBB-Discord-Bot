"""
Fun and Entertainment Commands Cog
"""

import random
import discord
from discord.ext import commands
from config import MOTIVATION_TIPS
from utils import create_info_embed, validate_dice_value


class FunCog(commands.Cog):
    """Commands for fun and entertainment"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='sfat')
    async def sfat(self, ctx):
        """Get a motivational tip"""
        embed = discord.Embed(
            title="💪 Sfat pentru Tine",
            description=random.choice(MOTIVATION_TIPS),
            color=discord.Color.gold()
        )
        embed.set_footer(text="🚀 Tu poti!")
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(name='moneda')
    async def moneda(self, ctx):
        """Flip a virtual coin"""
        rezultat = random.choice(['🪙 CAP', '🪙 PAJURA'])
        color = discord.Color.gold() if 'CAP' in rezultat else discord.Color.greyple()
        
        embed = discord.Embed(
            title="Arunca Moneda",
            description=f"**{rezultat}**",
            color=color
        )
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(name='roll', aliases=['zaruri', 'dice'])
    async def roll(self, ctx, max_val: int = 6):
        """Roll a dice (default 1-6)"""
        is_valid, error_msg = validate_dice_value(max_val)
        
        if not is_valid:
            embed = discord.Embed(
                title="❌ Valoare invalida",
                description=error_msg,
                color=discord.Color.red()
            )
            embed.timestamp = discord.utils.utcnow()
            await ctx.send(embed=embed)
            return
        
        rezultat = random.randint(1, max_val)
        emoji = "🎲"
        
        embed = discord.Embed(
            title="Arunca Zarul",
            description=f"{emoji} **{rezultat}** / {max_val}",
            color=discord.Color.red() if rezultat == max_val else discord.Color.blue()
        )
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)


async def setup(bot):
    """Load the FunCog into the bot"""
    await bot.add_cog(FunCog(bot))
