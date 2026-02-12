"""
Information and Help Commands Cog
"""

import discord
from discord import app_commands
from discord.ext import commands
from config import (
    BOT_NAME, BOT_VERSION, BOT_DESCRIPTION,
    COMMANDS_BY_CATEGORY, COMMANDS_DETAILS
)


class InfoCog(commands.Cog):
    """Commands for getting information about the bot and help"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='help')
    async def help_command(self, ctx, command: str = None):
        """Display all available commands or help for a specific command"""
        
        if command is None:
            # Compact help menu
            embed = discord.Embed(
                title=f"📚 {BOT_NAME} - Help Menu",
                description="Use `!help <command>` for detailed info or `!helpadmin` for admin commands",
                color=discord.Color.blue()
            )
            
            embed.add_field(
                name="🧮 Calculations",
                value="`!medie` `!zile` `!concurs`",
                inline=False
            )
            embed.add_field(
                name="ℹ️ Information",
                value="`!ubb` `!facultati` `!contact`",
                inline=False
            )
            embed.add_field(
                name="🎉 Fun",
                value="`!sfat` `!moneda` `!roll`",
                inline=False
            )
            embed.add_field(
                name="📊 Stats",
                value="`!stats` `!leaderboard` `!achievements`",
                inline=False
            )
            embed.add_field(
                name="💰 Economy",
                value="`!balance` `!transfer` `!addmoney` `!removemoney` `!shop` `!buy` `!inventory` `!use` `!gift`",
                inline=False
            )
            embed.add_field(
                name="🎮 Games",
                value="`!blackjack` `!slots` `!hangman` `!trivia`",
                inline=False
            )
            embed.add_field(
                name="🎵 Music",
                value="`!play` `!skip` `!pause` `!stop`",
                inline=False
            )
            embed.add_field(
                name="🔔 Notifications",
                value="`!remind` `!reminders` `!delreminder`",
                inline=False
            )
            
            embed.set_footer(text=f"v{BOT_VERSION} | Type !helpadmin for admin commands")
            embed.timestamp = discord.utils.utcnow()
            await ctx.send(embed=embed)
        
        else:
            # Detailed help for specific command
            command = command.lower()
            if command in COMMANDS_DETAILS:
                info = COMMANDS_DETAILS[command]
                embed = discord.Embed(
                    title=f"❓ Help - {command.upper()}",
                    color=discord.Color.green()
                )
                embed.add_field(name="📝 Description", value=info["descriere"], inline=False)
                embed.add_field(name="💬 Usage", value=f"`{info['utilizare']}`", inline=False)
                embed.add_field(name="🏷️ Category", value=info["categorie"], inline=False)
                embed.timestamp = discord.utils.utcnow()
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="❌ Command Not Found",
                    description=f"Command `{command}` doesn't exist! Try `!help`",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
    
    @commands.command(name='helpadmin')
    @commands.has_permissions(administrator=True)
    async def help_admin(self, ctx):
        """Display admin-only commands"""
        embed = discord.Embed(
            title="🔨 Admin Commands",
            description="Advanced administrative commands for server management",
            color=discord.Color.red()
        )
        
        embed.add_field(
            name="👤 User Management",
            value="`!kick @user [reason]` - Kick user\n"
                  "`!ban @user [reason]` - Ban user\n"
                  "`!unban <user_id>` - Unban user\n"
                  "`!mute @user [reason]` - Mute user\n"
                  "`!unmute @user` - Unmute user",
            inline=False
        )
        
        embed.add_field(
            name="⚠️ Warnings",
            value="`!warn @user [reason]` - Warn user (3 = auto ban)\n"
                  "`!warnlist @user` - Check warnings\n"
                  "`!clearwarns @user` - Clear all warnings",
            inline=False
        )
        
        embed.add_field(
            name="🗑️ Message Management",
            value="`!purge [amount]` - Delete messages (max 100)\n"
                  "`!clean [amount]` - Alias for purge",
            inline=False
        )
        
        embed.add_field(
            name="📈 Level & XP",
            value="`!setlevel @user <level>` - Set user level\n"
                  "`!addxp @user <amount>` - Add XP\n"
                  "`!resetxp @user` - Reset XP/level to 0",
            inline=False
        )
        
        embed.add_field(
            name="📊 Server & User Info",
            value="`!serverinfo` - Server statistics\n"
                  "`!userinfo [@user]` - User details",
            inline=False
        )
        
        embed.add_field(
            name="💰 Economy Management",
            value="`!addmoney @user <amount>` - Add coins to user\n"
                  "`!removemoney @user <amount>` - Remove coins from user",
            inline=False
        )
        
        embed.set_footer(text=f"Use !help <command> for detailed info | v{BOT_VERSION}")
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name='info')
    async def info(self, ctx):
        """Display information about the bot"""
        embed = discord.Embed(
            title=f"🤖 {BOT_NAME}",
            description=BOT_DESCRIPTION,
            color=discord.Color.gold()
        )
        embed.add_field(name="🎯 Purpose", value="Help students with calculations, info & entertainment", inline=False)
        embed.add_field(name="📌 Version", value=BOT_VERSION, inline=True)
        embed.add_field(name="🐍 Language", value="Python + discord.py", inline=True)
        embed.add_field(
            name="✨ Features",
            value="Stats • Ranks • Economy • Games • Music • Verification • Admin Tools",
            inline=False
        )
        
        embed.set_footer(text="Made for UBB students | Type !help for commands")
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot ping and response time"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"**⏱️ Latency:** `{latency}ms`",
            color=discord.Color.blue()
        )
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SLASH COMMANDS (/)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @app_commands.command(name='ping', description="Check bot latency")
    async def ping_slash(self, interaction: discord.Interaction):
        """Slash command version of ping"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"**⏱️ Latency:** `{latency}ms`",
            color=discord.Color.blue()
        )
        embed.timestamp = discord.utils.utcnow()
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name='info', description="Show bot information")
    async def info_slash(self, interaction: discord.Interaction):
        """Slash command version of info"""
        embed = discord.Embed(
            title=f"🤖 {BOT_NAME}",
            description=BOT_DESCRIPTION,
            color=discord.Color.gold()
        )
        embed.add_field(name="🎯 Purpose", value="Help students with calculations, info & entertainment", inline=False)
        embed.add_field(name="📌 Version", value=BOT_VERSION, inline=True)
        embed.add_field(name="🐍 Language", value="Python + discord.py", inline=True)
        embed.add_field(
            name="✨ Features",
            value="Stats • Ranks • Economy • Games • Music • Verification • Admin Tools",
            inline=False
        )
        embed.set_footer(text="Made for UBB students")
        embed.timestamp = discord.utils.utcnow()
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    """Load the InfoCog into the bot"""
    await bot.add_cog(InfoCog(bot))
