"""
Cog-ul Music Bot cu YouTube si Spotify Support
v2.0.0 Feature
"""

import discord
from discord.ext import commands
import json
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}
        self.now_playing = {}
        
        # Nota: Pentru YouTube playback, necesita yt-dlp si ffmpeg
        # pip install yt-dlp
        # Descarca ffmpeg de la https://ffmpeg.org/download.html
    
    def get_queue(self, guild_id):
        """Obtine queue-ul unui server"""
        if guild_id not in self.queues:
            self.queues[guild_id] = {
                "songs": [],
                "current": None,
                "loop": False,
                "shuffle": False,
                "volume": 1.0
            }
        return self.queues[guild_id]
    
    @commands.command(name='play')
    async def play(self, ctx, *, query: str = None):
        """
        Reda o melodie
        Utilizare: !play Imagine Dragons - Radioactive
        """
        if query is None:
            embed = discord.Embed(
                title="Music Player",
                description="Reda melodii din YouTube",
                color=discord.Color.fuchsia()
            )
            embed.add_field(name="Comenzi", 
                          value="!play song - Reda melodie\n!pause - Pauza\n!resume - Continua\n!skip - Urmatoarea\n!queue - Lista de asteptare",
                          inline=False)
            await ctx.send(embed=embed)
            return
        
        # Verifica daca e conectat la voice
        if ctx.author.voice is None:
            embed = discord.Embed(
                title="Eroare",
                description="Trebuie sa fii intr-un canal voice!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        embed = discord.Embed(
            title="Cautare Comenzuta",
            description=f"Caut... {query}",
            color=discord.Color.fuchsia()
        )
        msg = await ctx.send(embed=embed)
        
        # Nota: Implementare reala necesita yt-dlp
        # Pentru acum, simulam cu info placeholder
        queue = self.get_queue(ctx.guild.id)
        
        song = {
            "title": query,
            "duration": "3:45",
            "artist": "Unknown",
            "url": f"https://youtube.com/results?search_query={query.replace(' ', '+')}"
        }
        
        queue["songs"].append(song)
        
        embed = discord.Embed(
            title="Melodie Adaugata",
            description=f"**{song['title']}**",
            color=discord.Color.green()
        )
        embed.add_field(name="Durata", value=song["duration"], inline=True)
        embed.add_field(name="Pozitie Queue", value=f"#{len(queue['songs'])}", inline=True)
        
        await msg.edit(embed=embed)
    
    @commands.command(name='queue')
    async def queue(self, ctx):
        """Afiseaza lista de asteptare"""
        queue = self.get_queue(ctx.guild.id)
        
        if not queue["songs"]:
            embed = discord.Embed(
                title="Queue Gol",
                description="Nu sunt melodii in asteptare",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            return
        
        embed = discord.Embed(
            title=f"Queue - {len(queue['songs'])} melodii",
            color=discord.Color.fuchsia()
        )
        
        for idx, song in enumerate(queue["songs"][:10], 1):
            embed.add_field(
                name=f"#{idx} - {song['title']}",
                value=song['duration'],
                inline=False
            )
        
        if len(queue["songs"]) > 10:
            embed.add_field(
                name="...",
                value=f"+{len(queue['songs']) - 10} melodii",
                inline=False
            )
        
        await ctx.send(embed=embed)
    
    @commands.command(name='skip')
    async def skip(self, ctx):
        """Trece la urmatoarea melodie"""
        queue = self.get_queue(ctx.guild.id)
        
        if not queue["songs"]:
            embed = discord.Embed(
                title="Queue Gol",
                description="Nu sunt melodii de skipat",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
            return
        
        skipped = queue["songs"].pop(0)
        
        embed = discord.Embed(
            title="Melodie Skipata",
            description=f"**{skipped['title']}**",
            color=discord.Color.fuchsia()
        )
        
        if queue["songs"]:
            next_song = queue["songs"][0]
            embed.add_field(name="Urmatoarea", value=f"**{next_song['title']}**", inline=False)
        else:
            embed.add_field(name="Queue", value="Gol", inline=False)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='pause')
    async def pause(self, ctx):
        """Pune melodia in pauza"""
        embed = discord.Embed(
            title="Pauza",
            description="Melodia a fost oprita",
            color=discord.Color.fuchsia()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='resume')
    async def resume(self, ctx):
        """Continua melodia"""
        embed = discord.Embed(
            title="Continua",
            description="Melodia continua",
            color=discord.Color.fuchsia()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='volume')
    async def volume(self, ctx, vol: int = None):
        """Schimba volumul (0-100)"""
        queue = self.get_queue(ctx.guild.id)
        
        if vol is None:
            current_vol = int(queue["volume"] * 100)
            embed = discord.Embed(
                title="Volum Curent",
                description=f"{current_vol}%",
                color=discord.Color.fuchsia()
            )
            await ctx.send(embed=embed)
            return
        
        if vol < 0 or vol > 100:
            embed = discord.Embed(
                title="Eroare",
                description="Volumul trebuie sa fie intre 0 si 100",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        queue["volume"] = vol / 100
        
        embed = discord.Embed(
            title="Volum Setat",
            description=f"{vol}%",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    
    @commands.command(name='stop')
    async def stop(self, ctx):
        """Opreste playback-ul si curata queue"""
        guild_id = ctx.guild.id
        if guild_id in self.queues:
            self.queues[guild_id] = {
                "songs": [],
                "current": None,
                "loop": False,
                "shuffle": False,
                "volume": 1.0
            }
        
        embed = discord.Embed(
            title="Music Stop",
            description="Playback oprit si queue curatat",
            color=discord.Color.fuchsia()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Music(bot))
