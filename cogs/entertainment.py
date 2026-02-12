"""
Utilities and Calculation Commands Cog
"""

import discord
from discord.ext import commands
from config import UBB_INFO, FACULTIES, IMPORTANT_DATES
from utils import (
    create_error_embed,
    create_info_embed,
    validate_grades,
    days_until,
    hours_until,
    get_date_status
)


class UtilitiesCog(commands.Cog):
    """Commands for calculations and UBB information"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='medie')
    async def medie(self, ctx, *note: int):
        """Calculate the average of grades
        
        Usage: !medie 10 9 8 7
        """
        is_valid, error_msg = validate_grades(*note)
        
        if not is_valid:
            embed = create_error_embed("Eroare", error_msg)
            await ctx.send(embed=embed)
            return
        
        media = sum(note) / len(note)
        color = discord.Color.green() if media >= 4.5 else discord.Color.red()
        status = "✅ PROMOVAT" if media >= 4.5 else "❌ RESPINS"
        
        embed = discord.Embed(
            title="📊 Calculul Mediei",
            description=f"Note: {', '.join(map(str, note))}",
            color=color
        )
        embed.add_field(name="📈 Media", value=f"**{media:.2f}**", inline=True)
        embed.add_field(name="📝 Total Note", value=f"**{len(note)}**", inline=True)
        embed.add_field(name="📌 Status", value=status, inline=True)
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(name='zile')
    async def zile(self, ctx):
        """Days remaining until the admission exam"""
        date_info = IMPORTANT_DATES["admission_exam"]
        days = days_until(date_info["month"], date_info["day"])
        hours = hours_until(date_info["month"], date_info["day"])
        has_passed = get_date_status(date_info["month"], date_info["day"])
        
        embed = discord.Embed(
            title="📅 Examen de Admitere",
            color=discord.Color.blue()
        )
        embed.add_field(name="📍 Data", value="15 Iulie", inline=True)
        embed.add_field(name="⏰ Zile Ramase", value=f"**{days}**", inline=True)
        embed.add_field(name="⌚ Ore Ramase", value=f"**{hours}**", inline=True)
        
        if has_passed:
            embed.set_footer(text="⏳ Examenul a trecut!")
        else:
            embed.set_footer(text="💪 Mult succes la pregatire!")
        
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name='concurs')
    async def concurs(self, ctx):
        """Days remaining until the competition"""
        date_info = IMPORTANT_DATES["competition"]
        days = days_until(date_info["month"], date_info["day"])
        hours = hours_until(date_info["month"], date_info["day"])
        has_passed = get_date_status(date_info["month"], date_info["day"])
        
        embed = discord.Embed(
            title="🏆 Concurs de Admitere",
            color=discord.Color.purple()
        )
        embed.add_field(name="📍 Data", value="21 Martie", inline=True)
        embed.add_field(name="⏰ Zile Ramase", value=f"**{days}**", inline=True)
        embed.add_field(name="⌚ Ore Ramase", value=f"**{hours}**", inline=True)
        
        if has_passed:
            embed.set_footer(text="⏳ Concursul a trecut!")
        else:
            embed.set_footer(text="🔥 Pregatire intensa!")
        
        embed.timestamp = discord.utils.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name='ubb')
    async def ubb(self, ctx):
        """Information about UBB"""
        embed = discord.Embed(
            title=f"🎓 {UBB_INFO['name']}",
            description="Una dintre cele mai prestigioase universitati din Romania",
            color=discord.Color.gold()
        )
        embed.add_field(name="📍 Locatie", value=UBB_INFO["location"], inline=False)
        embed.add_field(name="📅 Infiintata", value=UBB_INFO["founded"], inline=True)
        embed.add_field(name="👥 Studenti", value=UBB_INFO["students"], inline=True)
        embed.add_field(name="🎯 Domenii", value=UBB_INFO["domains"], inline=False)
        embed.set_footer(text="Scrie !facultati pentru a vedea facultatile disponibile")
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(name='facultati')
    async def facultati(self, ctx):
        """List of UBB faculties"""
        embed = discord.Embed(
            title="🏛️ Facultati UBB",
            description="Facultatile disponibile la Universitatea Babes-Bolyai",
            color=discord.Color.blue()
        )
        
        facultati_text = "\n".join([f"• {f}" for f in FACULTIES])
        embed.add_field(name="Disponibile:", value=facultati_text, inline=False)
        embed.set_footer(text="Viziteaza ubb.ro pentru mai multe informatii")
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)

    @commands.command(name='contact')
    async def contact(self, ctx):
        """UBB contact information"""
        embed = discord.Embed(
            title="📞 Contact UBB",
            color=discord.Color.green()
        )
        embed.add_field(name="🌐 Website", value=UBB_INFO["website"], inline=False)
        embed.add_field(name="📧 Email", value=UBB_INFO["email"], inline=False)
        embed.add_field(name="☎️ Telefon", value=UBB_INFO["phone"], inline=False)
        embed.add_field(name="📍 Adresa", value=UBB_INFO["address"], inline=False)
        embed.set_footer(text="Pentru mai multe informatii, viziteaza site-ul oficial")
        embed.timestamp = discord.utils.utcnow()
        
        await ctx.send(embed=embed)


async def setup(bot):
    """Load the UtilitiesCog into the bot"""
    await bot.add_cog(UtilitiesCog(bot))
