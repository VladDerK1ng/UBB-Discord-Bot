"""
Advanced Admin Commands Cog
Comenzi administrative avansate pentru managementul serverului
"""

import discord
from discord.ext import commands
import json
import os
from utils import create_admin_action_embed, create_error_embed, create_success_embed
import logging

logger = logging.getLogger(__name__)

DATA_FILE = 'data/user_stats.json'


class AdminCommandsCog(commands.Cog):
    """Advanced administrative commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # UTILITY METHODS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def _load_user_data(self):
        """Load user data from JSON"""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_user_data(self, data):
        """Save user data to JSON"""
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # BAN/UNBAN COMMANDS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Ban a user from the server
        
        Usage: !ban @user [reason]
        """
        try:
            await member.ban(reason=reason)
            embed = create_admin_action_embed(
                "Ban User",
                f"{member.mention} ({member.name}#{member.discriminator})",
                reason,
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            logger.info(f"{ctx.author} banned {member} - Reason: {reason}")
        except discord.Forbidden:
            embed = create_error_embed("Permission Denied", "I don't have permission to ban this user")
            await ctx.send(embed=embed)
    
    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban_user(self, ctx, user_id: int):
        """Unban a user from the server
        
        Usage: !unban <user_id>
        """
        try:
            user = await self.bot.fetch_user(user_id)
            await ctx.guild.unban(user)
            embed = create_success_embed(
                "User Unbanned",
                f"Unbanned {user.mention}"
            )
            await ctx.send(embed=embed)
            logger.info(f"{ctx.author} unbanned {user}")
        except discord.NotFound:
            embed = create_error_embed("User Not Found", "Could not find user with that ID")
            await ctx.send(embed=embed)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # MUTE/UNMUTE COMMANDS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='mute')
    @commands.has_permissions(manage_roles=True)
    async def mute_user(self, ctx, member: discord.Member, *, reason: str = "No reason"):
        """Mute a user (remove speak permissions)
        
        Usage: !mute @user [reason]
        """
        try:
            await member.edit(mute=True, reason=reason)
            embed = create_admin_action_embed(
                "User Muted",
                member.mention,
                reason,
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            logger.info(f"{ctx.author} muted {member}")
        except discord.Forbidden:
            embed = create_error_embed("Permission Denied", "Cannot mute this user")
            await ctx.send(embed=embed)
    
    @commands.command(name='unmute')
    @commands.has_permissions(manage_roles=True)
    async def unmute_user(self, ctx, member: discord.Member):
        """Unmute a user
        
        Usage: !unmute @user
        """
        try:
            await member.edit(mute=False)
            embed = create_success_embed(
                "User Unmuted",
                f"{member.mention} can now speak!"
            )
            await ctx.send(embed=embed)
            logger.info(f"{ctx.author} unmuted {member}")
        except discord.Forbidden:
            embed = create_error_embed("Permission Denied", "Cannot unmute this user")
            await ctx.send(embed=embed)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # KICK COMMAND
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, member: discord.Member, *, reason: str = "No reason"):
        """Kick a user from the server
        
        Usage: !kick @user [reason]
        """
        try:
            await member.kick(reason=reason)
            embed = create_admin_action_embed(
                "User Kicked",
                f"{member.mention}",
                reason,
                color=discord.Color.dark_orange()
            )
            await ctx.send(embed=embed)
            logger.info(f"{ctx.author} kicked {member}")
        except discord.Forbidden:
            embed = create_error_embed("Permission Denied", "Cannot kick this user")
            await ctx.send(embed=embed)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PURGE/CLEAN MESSAGES
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='purge', aliases=['clean', 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def purge_messages(self, ctx, amount: int = 10):
        """Delete messages from current channel
        
        Usage: !purge [amount] (max 100)
        """
        if amount > 100:
            amount = 100
        if amount < 1:
            embed = create_error_embed("Invalid Amount", "Amount must be between 1 and 100")
            await ctx.send(embed=embed)
            return
        
        try:
            deleted = await ctx.channel.purge(limit=amount)
            embed = create_success_embed(
                "Messages Deleted",
                f"Deleted **{len(deleted)}** messages from {ctx.channel.mention}"
            )
            await ctx.send(embed=embed, delete_after=5)
            logger.info(f"{ctx.author} purged {len(deleted)} messages")
        except discord.Forbidden:
            embed = create_error_embed("Permission Denied", "Cannot delete messages in this channel")
            await ctx.send(embed=embed)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # LEVEL/XP MANAGEMENT
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='setlevel')
    @commands.has_permissions(administrator=True)
    async def set_level(self, ctx, member: discord.Member, level: int):
        """Set user level/XP
        
        Usage: !setlevel @user <level>
        """
        if level < 0:
            embed = create_error_embed("Invalid Level", "Level cannot be negative")
            await ctx.send(embed=embed)
            return
        
        data = self._load_user_data()
        user_id = str(member.id)
        
        if user_id not in data:
            data[user_id] = {"xp": 0, "level": 0}
        
        data[user_id]["level"] = level
        self._save_user_data(data)
        
        embed = create_success_embed(
            "Level Updated",
            f"{member.mention}'s level set to **{level}**"
        )
        await ctx.send(embed=embed)
        logger.info(f"{ctx.author} set {member} level to {level}")
    
    @commands.command(name='addxp')
    @commands.has_permissions(administrator=True)
    async def add_xp(self, ctx, member: discord.Member, xp: int):
        """Add XP to a user
        
        Usage: !addxp @user <amount>
        """
        if xp < 0:
            embed = create_error_embed("Invalid Amount", "XP cannot be negative")
            await ctx.send(embed=embed)
            return
        
        data = self._load_user_data()
        user_id = str(member.id)
        
        if user_id not in data:
            data[user_id] = {"xp": 0, "level": 0}
        
        data[user_id]["xp"] = data[user_id].get("xp", 0) + xp
        self._save_user_data(data)
        
        embed = create_success_embed(
            "XP Added",
            f"Added **{xp}** XP to {member.mention}\nTotal XP: **{data[user_id]['xp']}**"
        )
        await ctx.send(embed=embed)
        logger.info(f"{ctx.author} added {xp} XP to {member}")
    
    @commands.command(name='resetxp')
    @commands.has_permissions(administrator=True)
    async def reset_xp(self, ctx, member: discord.Member):
        """Reset a user's XP and level
        
        Usage: !resetxp @user
        """
        data = self._load_user_data()
        user_id = str(member.id)
        
        if user_id in data:
            data[user_id] = {"xp": 0, "level": 0}
            self._save_user_data(data)
        
        embed = create_success_embed(
            "XP Reset",
            f"Reset {member.mention}'s XP and level to 0"
        )
        await ctx.send(embed=embed)
        logger.info(f"{ctx.author} reset {member} XP")
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # WARNING SYSTEM
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='warn')
    @commands.has_permissions(manage_messages=True)
    async def warn_user(self, ctx, member: discord.Member, *, reason: str = "No reason"):
        """Warn a user
        
        Usage: !warn @user [reason]
        """
        user_id = str(member.id)
        
        if user_id not in self.warnings:
            self.warnings[user_id] = []
        
        self.warnings[user_id].append(reason)
        warn_count = len(self.warnings[user_id])
        
        embed = create_admin_action_embed(
            "User Warned",
            member.mention,
            f"{reason}\n**Warning {warn_count}/3**",
            color=discord.Color.yellow()
        )
        await ctx.send(embed=embed)
        
        if warn_count >= 3:
            try:
                await member.ban(reason="Automatic ban: 3 warnings")
                embed = create_admin_action_embed(
                    "Auto Ban",
                    member.mention,
                    "Reached 3 warnings"
                )
                await ctx.send(embed=embed)
                del self.warnings[user_id]
            except discord.Forbidden:
                pass
        
        logger.info(f"{ctx.author} warned {member} ({warn_count}/3)")
    
    @commands.command(name='warnlist')
    @commands.has_permissions(manage_messages=True)
    async def warn_list(self, ctx, member: discord.Member):
        """Check warnings for a user
        
        Usage: !warnlist @user
        """
        user_id = str(member.id)
        
        if user_id not in self.warnings or not self.warnings[user_id]:
            embed = create_success_embed(
                "No Warnings",
                f"{member.mention} has no warnings"
            )
            await ctx.send(embed=embed)
            return
        
        warns = self.warnings[user_id]
        warn_text = "\n".join([f"**{i+1}.** {w}" for i, w in enumerate(warns)])
        
        embed = discord.Embed(
            title=f"⚠️ Warnings for {member.name}",
            description=warn_text,
            color=discord.Color.yellow()
        )
        embed.add_field(name="Total Warnings", value=f"{len(warns)}/3", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name='clearwarns')
    @commands.has_permissions(administrator=True)
    async def clear_warns(self, ctx, member: discord.Member):
        """Clear all warnings for a user
        
        Usage: !clearwarns @user
        """
        user_id = str(member.id)
        
        if user_id in self.warnings:
            del self.warnings[user_id]
        
        embed = create_success_embed(
            "Warnings Cleared",
            f"Cleared all warnings for {member.mention}"
        )
        await ctx.send(embed=embed)
        logger.info(f"{ctx.author} cleared warns for {member}")
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # SERVER INFO & STATS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    @commands.command(name='serverinfo')
    @commands.has_permissions(administrator=True)
    async def server_info(self, ctx):
        """Get server information
        
        Usage: !serverinfo
        """
        guild = ctx.guild
        embed = discord.Embed(
            title=f"📊 {guild.name}",
            color=discord.Color.blurple()
        )
        embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
        embed.add_field(name="📝 Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="👑 Owner", value=guild.owner.mention, inline=True)
        embed.add_field(name="📅 Created", value=guild.created_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="🔒 Verification Level", value=str(guild.verification_level), inline=True)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else "")
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)
    
    @commands.command(name='userinfo')
    async def user_info(self, ctx, member: discord.Member = None):
        """Get user information
        
        Usage: !userinfo [@user]
        """
        member = member or ctx.author
        embed = discord.Embed(
            title=f"👤 {member.name}",
            color=member.color
        )
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
        embed.add_field(name="Roles", value=" ".join([r.mention for r in member.roles[1:]]) or "None", inline=False)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)


async def setup(bot):
    """Load the AdminCommandsCog into the bot"""
    await bot.add_cog(AdminCommandsCog(bot))
