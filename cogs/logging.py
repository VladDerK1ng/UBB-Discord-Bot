"""
Cog-ul de Logging Detaliat - Inregistrare actiuni bot pe server
"""

import discord
from discord.ext import commands
from datetime import datetime
import json
import os

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logs_file = "data/server_logs.json"
        self.load_logs()
    
    def load_logs(self):
        """Incarca logurile din fisier"""
        if not os.path.exists(self.logs_file):
            self.logs = {}
        else:
            try:
                with open(self.logs_file, 'r') as f:
                    self.logs = json.load(f)
            except:
                self.logs = {}
    
    def save_logs(self):
        """Salveaza logurile in fisier"""
        os.makedirs(os.path.dirname(self.logs_file), exist_ok=True)
        with open(self.logs_file, 'w') as f:
            json.dump(self.logs, f, indent=4)
    
    def add_log(self, guild_id, action_type, author, target, description):
        """Adauga un log la inregistrare"""
        guild_id = str(guild_id)
        
        if guild_id not in self.logs:
            self.logs[guild_id] = []
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "author": author,
            "author_id": author.id if hasattr(author, 'id') else author,
            "target": target,
            "target_id": target.id if hasattr(target, 'id') else target,
            "description": description
        }
        
        self.logs[guild_id].append(log_entry)
        self.save_logs()
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """Log-uieste mesajele sterse"""
        if message.author.bot:
            return
        
        if message.guild:
            self.add_log(
                message.guild.id,
                "MESSAGE_DELETE",
                message.author,
                message.channel,
                f"Mesaj sters: {message.content[:100]}"
            )
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """Log-uieste mesajele editate"""
        if before.author.bot or before.content == after.content:
            return
        
        if before.guild:
            self.add_log(
                before.guild.id,
                "MESSAGE_EDIT",
                before.author,
                before.channel,
                f"Inainte: {before.content[:50]} | Dupa: {after.content[:50]}"
            )
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Log-uieste intrarea unui membru"""
        if member.guild:
            self.add_log(
                member.guild.id,
                "MEMBER_JOIN",
                member,
                member.guild,
                f"{member} a intrat in server"
            )
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Log-uieste plecarea unui membru"""
        if member.guild:
            self.add_log(
                member.guild.id,
                "MEMBER_LEAVE",
                member,
                member.guild,
                f"{member} a parasit serverul"
            )
    
    @commands.Cog.listener()
    async def on_command(self, ctx):
        """Log-uieste comenzile executate"""
        if ctx.guild:
            self.add_log(
                ctx.guild.id,
                "COMMAND_EXECUTED",
                ctx.author,
                ctx.channel,
                f"Comanda: {ctx.command.name} - {ctx.message.content[1:50]}"
            )
    
    @commands.command(name='logs')
    @commands.has_permissions(administrator=True)
    async def view_logs(self, ctx, limit: int = 10):
        """Vede logurile serverului (doar admin)
        
        Utilizare: !logs 20
        """
        guild_id = str(ctx.guild.id)
        
        if guild_id not in self.logs or not self.logs[guild_id]:
            embed = discord.Embed(
                title="Nu sunt loguri inregistrate",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            return
        
        logs = self.logs[guild_id][-limit:]
        
        embed = discord.Embed(
            title=f"Loguri serverului ({len(logs)} din {len(self.logs[guild_id])})",
            color=discord.Color.blue()
        )
        
        for log in reversed(logs):
            timestamp = datetime.fromisoformat(log["timestamp"]).strftime("%d.%m %H:%M")
            author = log["author"]
            action = log["action"].replace("_", " ")
            
            embed.add_field(
                name=f"[{timestamp}] {action}",
                value=f"**De la:** {author}\n**Descriere:** {log['description']}",
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='clearlog')
    @commands.has_permissions(administrator=True)
    async def clear_logs(self, ctx):
        """Sterge logurile serverului (doar admin)"""
        guild_id = str(ctx.guild.id)
        
        if guild_id in self.logs:
            removed_count = len(self.logs[guild_id])
            del self.logs[guild_id]
            self.save_logs()
            
            embed = discord.Embed(
                title="Loguri sterse",
                description=f"{removed_count} inregistrari au fost sterse",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Nu sunt loguri",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Logging(bot))
