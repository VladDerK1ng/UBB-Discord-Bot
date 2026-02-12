"""
Utility functions for working with Discord embeds with aesthetic design
"""

import discord
from datetime import datetime


def create_error_embed(title: str, description: str, color=discord.Color.red()):
    """Create a standardized error embed"""
    embed = discord.Embed(
        title=f"❌ {title}",
        description=description,
        color=color
    )
    embed.timestamp = datetime.now()
    return embed


def create_info_embed(title: str, description: str = "", color=discord.Color.blue()):
    """Create a standardized info embed"""
    embed = discord.Embed(
        title=f"ℹ️ {title}",
        description=description,
        color=color
    )
    embed.timestamp = datetime.now()
    return embed


def create_success_embed(title: str, description: str = "", color=discord.Color.green()):
    """Create a standardized success embed"""
    embed = discord.Embed(
        title=f"✅ {title}",
        description=description,
        color=color
    )
    embed.timestamp = datetime.now()
    return embed


def create_warning_embed(title: str, description: str = ""):
    """Create a standardized warning embed"""
    embed = discord.Embed(
        title=f"⚠️ {title}",
        description=description,
        color=discord.Color.orange()
    )
    embed.timestamp = datetime.now()
    return embed


def create_admin_action_embed(action: str, target: str, reason: str = "", color=discord.Color.red()):
    """Create an embed for admin actions"""
    embed = discord.Embed(
        title=f"🔨 Admin Action",
        color=color
    )
    embed.add_field(name="Action", value=action, inline=False)
    embed.add_field(name="Target", value=target, inline=True)
    if reason:
        embed.add_field(name="Reason", value=reason, inline=False)
    embed.timestamp = datetime.now()
    return embed


def create_help_compact(title: str, commands_list: list, color=discord.Color.blue()):
    """Create a compact help embed"""
    embed = discord.Embed(
        title=f"📚 {title}",
        color=color
    )
    for cmd in commands_list:
        embed.add_field(name=cmd['name'], value=cmd['desc'], inline=False)
    embed.set_footer(text="Use !help <command> for more details | Type !helpadmin for admin commands")
    embed.timestamp = datetime.now()
    return embed


def create_stat_embed(title: str, stats: dict, color=discord.Color.blurple()):
    """Create an embed for displaying statistics"""
    embed = discord.Embed(
        title=f"📊 {title}",
        color=color
    )
    for key, value in stats.items():
        embed.add_field(name=key, value=value, inline=True)
    embed.timestamp = datetime.now()
    return embed
