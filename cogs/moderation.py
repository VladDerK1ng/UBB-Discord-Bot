"""
Cog-ul de moderatie - comenzi pentru administrare
"""

import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Fara motiv"):
        """Elimina un utilizator din server"""
        if member.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner:
            embed = discord.Embed(
                title="Eroare",
                description="Nu poti elimina pe cineva cu un rol mai mare sau egal cu al tau!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="Utilizator eliminat",
            description=f"**{member}** a fost eliminat din server.",
            color=discord.Color.orange()
        )
        embed.add_field(name="Motiv", value=reason, inline=False)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Fara motiv"):
        """Baneaza un utilizator din server"""
        if member.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner:
            embed = discord.Embed(
                title="Eroare",
                description="Nu poti bana pe cineva cu un rol mai mare sau egal cu al tau!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="Utilizator banat",
            description=f"**{member}** a fost banat din server.",
            color=discord.Color.red()
        )
        embed.add_field(name="Motiv", value=reason, inline=False)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name: str):
        """Debaneaza un utilizator"""
        try:
            banned_users = await ctx.guild.bans()
            
            # Incearca sa gaseste utilizatorul dupa:
            # 1. Username (format nou)
            # 2. Username#Discriminator (format vechi)
            # 3. User ID
            target_user = None
            
            for ban_entry in banned_users:
                user = ban_entry.user
                # Verifica format nou (doar username)
                if str(user.name).lower() == member_name.lower():
                    target_user = user
                    break
                # Verifica format vechi (username#discriminator)
                if '#' in member_name:
                    name_parts = member_name.split('#')
                    if (user.name.lower(), user.discriminator) == (name_parts[0].lower(), name_parts[1]):
                        target_user = user
                        break
                # Verifica dupa ID
                try:
                    if user.id == int(member_name):
                        target_user = user
                        break
                except ValueError:
                    pass
            
            if target_user:
                await ctx.guild.unban(target_user)
                embed = discord.Embed(
                    title="✅ Utilizator Debanat",
                    description=f"**{target_user}** a fost debanat.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="❌ Eroare",
                    description="Utilizatorul nu a fost gasit in lista de banati! Incearca: @username, username#1234, sau ID",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="❌ Eroare",
                description=f"Eroare la debano: {str(e)}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
    
    @commands.command(name='warn')
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="Fara motiv"):
        """Avertizeaza un utilizator"""
        embed = discord.Embed(
            title="Avertisment",
            description=f"**{member}** a fost avertizat.",
            color=discord.Color.gold()
        )
        embed.add_field(name="Motiv", value=reason, inline=False)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
        await ctx.send(embed=embed)
        
        try:
            await member.send(f"Ai primit un avertisment in {ctx.guild.name}: {reason}")
        except:
            pass
    
    @commands.command(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = 10):
        """Sterge un numar de mesaje
        
        Utilizare: !purge 5 (sterge ultimele 5 mesaje)
        """
        if amount < 1 or amount > 100:
            embed = discord.Embed(
                title="Eroare",
                description="Trebuie sa stergi intre 1 si 100 de mesaje!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        deleted = await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            title="Mesaje sterse",
            description=f"Am sters **{len(deleted) - 1}** mesaje.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed, delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
