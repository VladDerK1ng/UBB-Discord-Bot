"""
Cog-ul de Notificari Programate - Remindere si programari
"""

import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import json
import os

class Notifications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders_file = "data/reminders.json"
        self.load_reminders()
        self.check_reminders.start()
    
    def load_reminders(self):
        """Incarca reamintirile din fisier"""
        if not os.path.exists(self.reminders_file):
            self.reminders = {}
        else:
            with open(self.reminders_file, 'r') as f:
                self.reminders = json.load(f)
    
    def save_reminders(self):
        """Salveaza reamintirile in fisier"""
        os.makedirs(os.path.dirname(self.reminders_file), exist_ok=True)
        with open(self.reminders_file, 'w') as f:
            json.dump(self.reminders, f, indent=4)
    
    @commands.command(name='remind')
    async def remind(self, ctx, hours: int, *, message: str):
        """Seteaza un reminder dupa N ore
        
        Utilizare: !remind 24 Studia pentru examen!
        """
        if hours < 1 or hours > 720:
            embed = discord.Embed(
                title="Eroare",
                description="Reminder-ul trebuie sa fie intre 1 si 720 ore (30 zile)!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        reminder_id = str(ctx.author.id)
        reminder_time = (datetime.now() + timedelta(hours=hours)).isoformat()
        
        if reminder_id not in self.reminders:
            self.reminders[reminder_id] = []
        
        self.reminders[reminder_id].append({
            "time": reminder_time,
            "message": message,
            "channel_id": ctx.channel.id,
            "user_id": ctx.author.id
        })
        
        self.save_reminders()
        
        embed = discord.Embed(
            title="Reminder setat",
            description=f"Vei primi reminder-ul in {hours} ore!",
            color=discord.Color.green()
        )
        embed.add_field(name="Mesaj", value=message, inline=False)
        embed.set_footer(text=f"Setat la {datetime.now().strftime('%H:%M:%S')}")
        await ctx.send(embed=embed)
    
    @commands.command(name='reminders')
    async def list_reminders(self, ctx):
        """Vede reamintirile tale active"""
        reminder_id = str(ctx.author.id)
        
        if reminder_id not in self.reminders or not self.reminders[reminder_id]:
            embed = discord.Embed(
                title="Nu ai reminder-uri active",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            return
        
        embed = discord.Embed(
            title="Reminderurile tale",
            color=discord.Color.blue()
        )
        
        for i, reminder in enumerate(self.reminders[reminder_id], 1):
            reminder_datetime = datetime.fromisoformat(reminder["time"])
            time_left = reminder_datetime - datetime.now()
            
            hours = int(time_left.total_seconds() // 3600)
            minutes = int((time_left.total_seconds() % 3600) // 60)
            
            embed.add_field(
                name=f"#{i}",
                value=f"**{reminder['message']}**\nRamas: {hours}h {minutes}m",
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='delreminder')
    async def delete_reminder(self, ctx, index: int):
        """Sterge un reminder dupa index
        
        Utilizare: !delreminder 1
        """
        reminder_id = str(ctx.author.id)
        
        if reminder_id not in self.reminders or index < 1 or index > len(self.reminders[reminder_id]):
            embed = discord.Embed(
                title="Eroare",
                description="Reminder-ul nu exista!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        deleted = self.reminders[reminder_id].pop(index - 1)
        self.save_reminders()
        
        embed = discord.Embed(
            title="Reminder sters",
            description=f"Reminder-ul a fost sters cu succes!",
            color=discord.Color.green()
        )
        embed.add_field(name="Era", value=deleted["message"], inline=False)
        await ctx.send(embed=embed)
    
    @tasks.loop(minutes=1)
    async def check_reminders(self):
        """Verifica reamintirile si le trimite daca e cazul"""
        now = datetime.now()
        reminders_to_delete = []
        
        for user_id, reminders in self.reminders.items():
            for i, reminder in enumerate(reminders):
                reminder_time = datetime.fromisoformat(reminder["time"])
                
                if now >= reminder_time:
                    try:
                        channel = self.bot.get_channel(reminder["channel_id"])
                        if channel:
                            embed = discord.Embed(
                                title="Reminder!",
                                description=f"<@{reminder['user_id']}>,\n\n{reminder['message']}",
                                color=discord.Color.blue()
                            )
                            embed.set_footer(text="Reminder trimis")
                            await channel.send(embed=embed)
                        
                        reminders_to_delete.append((user_id, i))
                    except:
                        pass
        
        for user_id, index in reversed(reminders_to_delete):
            self.reminders[user_id].pop(index)
        
        if reminders_to_delete:
            self.save_reminders()
    
    @check_reminders.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Notifications(bot))
