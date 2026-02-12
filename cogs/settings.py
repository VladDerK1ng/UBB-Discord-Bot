"""
Cog-ul de Configurari per-Server - Settings si preferinte
"""

import discord
from discord.ext import commands
import json
import os

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = "data/server_settings.json"
        self.load_settings()
        self.default_settings = {
            "prefix": "!",
            "welcome_enabled": False,
            "welcome_message": "Bine ai venit pe server!",
            "welcome_channel": None,
            "log_channel": None,
            "auto_role": None,
            "moderation_enabled": True,
            "language": "ro"
        }
    
    def load_settings(self):
        """Incarca setarile din fisier"""
        if not os.path.exists(self.settings_file):
            self.settings = {}
        else:
            try:
                with open(self.settings_file, 'r') as f:
                    self.settings = json.load(f)
            except:
                self.settings = {}
    
    def save_settings(self):
        """Salveaza setarile in fisier"""
        os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)
    
    def get_guild_settings(self, guild_id):
        """Obtine setarile unui server"""
        guild_id = str(guild_id)
        if guild_id not in self.settings:
            self.settings[guild_id] = self.default_settings.copy()
            self.save_settings()
        return self.settings[guild_id]
    
    @commands.command(name='settings')
    @commands.has_permissions(administrator=True)
    async def view_settings(self, ctx):
        """Vede setarile curente ale serverului"""
        settings = self.get_guild_settings(ctx.guild.id)
        
        embed = discord.Embed(
            title=f"Setarile pentru {ctx.guild.name}",
            color=discord.Color.blue()
        )
        
        welcome_status = "Activat" if settings["welcome_enabled"] else "Dezactivat"
        mod_status = "Activat" if settings["moderation_enabled"] else "Dezactivat"
        
        embed.add_field(name="Prefix", value=settings["prefix"], inline=False)
        embed.add_field(name="Limbaj", value=settings["language"], inline=False)
        embed.add_field(name="Welcome", value=welcome_status, inline=False)
        embed.add_field(name="Moderare", value=mod_status, inline=False)
        
        if settings["welcome_channel"]:
            embed.add_field(
                name="Canal Welcome",
                value=f"<#{settings['welcome_channel']}>",
                inline=False
            )
        
        if settings["log_channel"]:
            embed.add_field(
                name="Canal Loguri",
                value=f"<#{settings['log_channel']}>",
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='setwelcome')
    @commands.has_permissions(administrator=True)
    async def set_welcome(self, ctx, *, message: str = None):
        """Seteaza mesajul de welcome
        
        Utilizare: !setwelcome Bine ai venit pe {user}!
        {user} - username-ul membrului nou
        """
        settings = self.get_guild_settings(ctx.guild.id)
        
        if message:
            settings["welcome_message"] = message
            settings["welcome_enabled"] = True
            self.settings[str(ctx.guild.id)] = settings
            self.save_settings()
            
            embed = discord.Embed(
                title="Welcome setat",
                description=message.replace("{user}", ctx.author.name),
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            settings["welcome_enabled"] = not settings["welcome_enabled"]
            self.settings[str(ctx.guild.id)] = settings
            self.save_settings()
            
            status = "Activat" if settings["welcome_enabled"] else "Dezactivat"
            embed = discord.Embed(
                title=f"Welcome {status}",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
    
    @commands.command(name='setwelcomechannel')
    @commands.has_permissions(administrator=True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        """Seteaza canalul pentru mesajul welcome"""
        settings = self.get_guild_settings(ctx.guild.id)
        settings["welcome_channel"] = channel.id
        self.settings[str(ctx.guild.id)] = settings
        self.save_settings()
        
        embed = discord.Embed(
            title="Canal welcome setat",
            description=f"Welcome mesajele vor fi trimise in {channel.mention}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='setlogchannel')
    @commands.has_permissions(administrator=True)
    async def set_log_channel(self, ctx, channel: discord.TextChannel):
        """Seteaza canalul pentru loguri"""
        settings = self.get_guild_settings(ctx.guild.id)
        settings["log_channel"] = channel.id
        self.settings[str(ctx.guild.id)] = settings
        self.save_settings()
        
        embed = discord.Embed(
            title="Canal loguri setat",
            description=f"Logurile vor fi inregistrate in {channel.mention}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='setautorole')
    @commands.has_permissions(administrator=True)
    async def set_auto_role(self, ctx, role: discord.Role):
        """Seteaza rol automat pentru membrii noi"""
        settings = self.get_guild_settings(ctx.guild.id)
        settings["auto_role"] = role.id
        self.settings[str(ctx.guild.id)] = settings
        self.save_settings()
        
        embed = discord.Embed(
            title="Auto-role setat",
            description=f"Membrii noi vor primi automat rolul {role.mention}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Trimite mesajul welcome si adauga auto-role"""
        settings = self.get_guild_settings(member.guild.id)
        
        if settings["auto_role"]:
            try:
                role = member.guild.get_role(settings["auto_role"])
                if role:
                    await member.add_roles(role)
            except:
                pass
        
        if settings["welcome_enabled"] and settings["welcome_channel"]:
            try:
                channel = self.bot.get_channel(settings["welcome_channel"])
                if channel:
                    welcome_msg = settings["welcome_message"].replace("{user}", member.name)
                    embed = discord.Embed(
                        title="Bun venit!",
                        description=welcome_msg,
                        color=discord.Color.green()
                    )
                    embed.set_thumbnail(url=member.avatar.url)
                    await channel.send(embed=embed)
            except:
                pass

async def setup(bot):
    await bot.add_cog(Settings(bot))
