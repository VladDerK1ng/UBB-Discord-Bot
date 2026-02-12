"""
Cog-ul Advanced Moderation cu Filter si Spam Detection
v2.0.0 Feature
"""

import discord
from discord.ext import commands
import json
import os
from datetime import datetime, timedelta

class AdvancedModeration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.moderation_file = "data/advanced_moderation.json"
        self.load_moderation()
        
        # Cuvinte interzise
        self.forbidden_words = ["offensive", "badword", "spam"]
        
        # Spam tracking
        self.message_count = {}
    
    def load_moderation(self):
        """Incarca configurarile de moderare"""
        if not os.path.exists(self.moderation_file):
            self.moderation_config = {}
            self.forbidden_words = []
        else:
            try:
                with open(self.moderation_file, 'r') as f:
                    data = json.load(f)
                    # Handle both old format (direct config) and new format
                    if isinstance(data, dict) and "config" in data:
                        self.moderation_config = data.get("config", {})
                        self.forbidden_words = data.get("forbidden_words", [])
                    else:
                        # Old format - convert
                        self.moderation_config = data
                        self.forbidden_words = []
            except:
                self.moderation_config = {}
                self.forbidden_words = []
    
    def save_moderation(self):
        """Salveaza configurarile"""
        os.makedirs(os.path.dirname(self.moderation_file), exist_ok=True)
        data = {
            "config": self.moderation_config,
            "forbidden_words": self.forbidden_words
        }
        with open(self.moderation_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    @commands.command(name='setwordfilter')
    @commands.has_permissions(administrator=True)
    async def set_word_filter(self, ctx, *, words: str = None):
        """Seteaza cuvinte interzise"""
        if words is None:
            embed = discord.Embed(
                title="Cuvinte Interzise Curente",
                description=", ".join(self.forbidden_words) if self.forbidden_words else "Nu sunt cuvinte interzise",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
            return
        
        self.forbidden_words = [w.lower().strip() for w in words.split(",")]
        self.save_moderation()  # SAVE TO FILE!
        
        embed = discord.Embed(
            title="Cuvinte Interzise Actualizate",
            description=", ".join(self.forbidden_words),
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='setspamprotect')
    @commands.has_permissions(administrator=True)
    async def set_spam_protect(self, ctx, messages: int = 5, minutes: int = 1):
        """Seteaza protectia anti-spam"""
        guild_id = str(ctx.guild.id)
        
        if guild_id not in self.moderation_config:
            self.moderation_config[guild_id] = {}
        
        self.moderation_config[guild_id]["spam_limit"] = messages
        self.moderation_config[guild_id]["spam_window"] = minutes * 60
        self.save_moderation()
        
        embed = discord.Embed(
            title="Spam Protection Setata",
            description=f"{messages} mesaje in {minutes} minut(e)",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Verifica mesajele pentru filtru de cuvinte si spam"""
        if message.author.bot or not message.guild:
            return
        
        # Verifica cuvinte interzise
        message_content = message.content.lower()
        for forbidden in self.forbidden_words:
            if forbidden in message_content:
                try:
                    await message.delete()
                    embed = discord.Embed(
                        title="Mesaj sters",
                        description=f"Mesajul tau continea un cuvant interzis.",
                        color=discord.Color.red()
                    )
                    await message.author.send(embed=embed)
                except:
                    pass
                return
        
        # Verifica spam
        guild_config = self.moderation_config.get(str(message.guild.id), {})
        if "spam_limit" in guild_config:
            user_id = str(message.author.id)
            current_time = datetime.now()
            
            if user_id not in self.message_count:
                self.message_count[user_id] = []
            
            # Pastreaza doar mesajele din ultimi N secunde
            spam_window = guild_config.get("spam_window", 60)
            self.message_count[user_id] = [
                t for t in self.message_count[user_id]
                if (current_time - t).total_seconds() < spam_window
            ]
            
            spam_limit = guild_config.get("spam_limit", 5)
            self.message_count[user_id].append(current_time)
            
            if len(self.message_count[user_id]) > spam_limit:
                try:
                    await message.author.timeout(timedelta(minutes=5), reason="Spam")
                    
                    embed = discord.Embed(
                        title="Timeout pentru Spam",
                        description="Ai fost pus in timeout pentru 5 minute pentru spam.",
                        color=discord.Color.red()
                    )
                    await message.author.send(embed=embed)
                except:
                    pass
    
    @commands.command(name='adwarn')
    @commands.has_permissions(kick_members=True)
    async def warn_user(self, ctx, user: discord.Member, *, reason: str = None):
        """Avertizeaza un utilizator cu auto-ban dupa 3 warning-uri"""
        guild_id = str(ctx.guild.id)
        user_id = str(user.id)
        
        if guild_id not in self.moderation_config:
            self.moderation_config[guild_id] = {}
        
        if "warnings" not in self.moderation_config[guild_id]:
            self.moderation_config[guild_id]["warnings"] = {}
        
        if user_id not in self.moderation_config[guild_id]["warnings"]:
            self.moderation_config[guild_id]["warnings"][user_id] = []
        
        warning = {
            "reason": reason or "No reason provided",
            "timestamp": datetime.now().isoformat(),
            "moderator": str(ctx.author.id)
        }
        
        self.moderation_config[guild_id]["warnings"][user_id].append(warning)
        self.save_moderation()
        
        warnings_count = len(self.moderation_config[guild_id]["warnings"][user_id])
        
        embed = discord.Embed(
            title="Avertizare Adaugata",
            description=f"{user.mention} a fost avertizat",
            color=discord.Color.orange()
        )
        embed.add_field(name="Motiv", value=reason or "No reason", inline=False)
        embed.add_field(name="Avertizari", value=f"{warnings_count}/3", inline=False)
        
        await ctx.send(embed=embed)
        
        # Auto-ban dupa 3 avertisari
        if warnings_count >= 3:
            try:
                await user.ban(reason="Auto-ban dupa 3 avertisari")
                embed = discord.Embed(
                    title="Auto-Ban Aplicat",
                    description=f"{user.name} a fost banat automatic dupa 3 avertisari",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
            except:
                pass
    
    @commands.command(name='warnlist')
    @commands.has_permissions(kick_members=True)
    async def check_warnings(self, ctx, user: discord.Member):
        """Verifica avertisarile unui utilizator"""
        guild_id = str(ctx.guild.id)
        user_id = str(user.id)
        
        warnings = self.moderation_config.get(guild_id, {}).get("warnings", {}).get(user_id, [])
        
        embed = discord.Embed(
            title=f"Avertisari - {user.name}",
            color=discord.Color.orange()
        )
        
        if not warnings:
            embed.description = "Nu are avertisari"
        else:
            for idx, warning in enumerate(warnings, 1):
                embed.add_field(
                    name=f"Avertizare #{idx}",
                    value=f"**Motiv:** {warning['reason']}\n**Data:** {warning['timestamp'][:10]}",
                    inline=False
                )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AdvancedModeration(bot))
