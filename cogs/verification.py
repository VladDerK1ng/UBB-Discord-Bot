"""
Cog-ul Verification System cu Auto-Role
v1.3.0 Feature
"""

import discord
from discord.ext import commands
import json
import os
import random
import string

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.verification_file = "data/verification.json"
        self.load_verification()
    
    def load_verification(self):
        """Incarca datele de verificare"""
        if not os.path.exists(self.verification_file):
            self.verified = {}
        else:
            try:
                with open(self.verification_file, 'r') as f:
                    self.verified = json.load(f)
            except:
                self.verified = {}
    
    def save_verification(self):
        """Salveaza datele de verificare"""
        os.makedirs(os.path.dirname(self.verification_file), exist_ok=True)
        with open(self.verification_file, 'w') as f:
            json.dump(self.verified, f, indent=4)
    
    def generate_captcha(self):
        """Genereaza un CAPTCHA simplu"""
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        
        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2
        
        question = f"{num1} {operator} {num2} = ?"
        return question, answer
    
    def generate_code(self):
        """Genereaza un cod de verificare"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    @commands.command(name='verify')
    async def verify(self, ctx):
        """Incepe procesul de verificare"""
        user_id = str(ctx.author.id)
        
        # Reincarca datele din fisier pentru a verifica status actual
        self.load_verification()
        
        if user_id in self.verified:
            # Check daca utilizatorul are deja rolul
            verified_role = None
            for role in ctx.guild.roles:
                if role.name.lower() == "verified":
                    verified_role = role
                    break
            
            if verified_role and verified_role in ctx.author.roles:
                embed = discord.Embed(
                    title="✅ Deja Verificat",
                    description=f"Esti deja verificat cu rolul Verified, {ctx.author.name}!",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
                return
            elif verified_role:
                # Utilizatorul e verificat dar nu are rol - adauga-l acum
                try:
                    await ctx.author.add_roles(verified_role)
                    embed = discord.Embed(
                        title="✅ Rol Adaugat",
                        description=f"Iti adaugam rolul Verified, {ctx.author.name}!",
                        color=discord.Color.green()
                    )
                    await ctx.send(embed=embed)
                    return
                except Exception as e:
                    pass  # Continua cu procesul normal
            # Daca nu exista rol, continua cu verificare
        
        # Trimite DM cu verificare
        embed = discord.Embed(
            title="Verificare Discord Bot UBB",
            description="Raspunde la intrebarea pentru a verifica contul.",
            color=discord.Color.blue()
        )
        
        question, answer = self.generate_captcha()
        embed.add_field(name="Intrebare", value=f"```{question}```", inline=False)
        embed.set_footer(text="Raspunde cu numarul din intrebarea de mai sus. Ai 60 de secunde.")
        
        try:
            dm = await ctx.author.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(
                title="Eroare",
                description="Nu pot trimite DM. Te rog deschide DM-urile din setarile serverului si incearca din nou.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        # Asteapta raspunsul
        def check(m):
            return m.author == ctx.author and m.channel == dm.channel
        
        try:
            response = await self.bot.wait_for("message", check=check, timeout=60)
        except:
            await dm.edit(content="Verificare expirata. Incearca din nou cu !verify")
            return
        
        try:
            user_answer = int(response.content)
            if user_answer == answer:
                self.verified[user_id] = {"verified": True, "date": str(__import__('datetime').datetime.now())}
                self.save_verification()
                
                # Cauta sau creeaza rolul de verified
                verified_role = None
                for role in ctx.guild.roles:
                    if role.name.lower() == "verified":
                        verified_role = role
                        break
                
                # Daca rolul nu exista, incearca sa il creezi
                if verified_role is None:
                    try:
                        verified_role = await ctx.guild.create_role(
                            name="Verified",
                            color=discord.Color.green(),
                            reason="Rol pentru utilizatori verificati"
                        )
                    except Exception as e:
                        await dm.edit(content=f"Eroare creando rol: {str(e)}")
                        return
                
                # Adauga rolul utilizatorului
                if verified_role:
                    try:
                        # Verifica daca bot are permisiunea de a adauga rol
                        if ctx.guild.me.top_role.position > verified_role.position:
                            await ctx.author.add_roles(verified_role)
                            status_msg = "✅ Verified Role Adaugat"
                        else:
                            status_msg = "⚠️ Rol Verified creat dar nu pot adaugat (perm)"
                    except Exception as e:
                        status_msg = f"⚠️ Eroare adaugando rol: {str(e)}"
                else:
                    status_msg = "⚠️ Nu pot crea rol Verified"
                
                embed = discord.Embed(
                    title="✅ Verificare Reusita!",
                    description="Esti acum verificat in serverul UBB!",
                    color=discord.Color.green()
                )
                embed.add_field(name="Status Rol", value=status_msg, inline=False)
                await response.reply(embed=embed)
            else:
                embed = discord.Embed(
                    title="❌ Raspuns Incorect",
                    description=f"Raspunsul corect era **{answer}**. Incearca din nou cu !verify",
                    color=discord.Color.red()
                )
                await response.reply(embed=embed)
        except ValueError:
            await response.reply("❌ Te rog introduce un numar valid! Ex: 5 sau -3")
    
    @commands.command(name='verificationstatus')
    async def verification_status(self, ctx, user: discord.Member = None):
        """Vede status de verificare"""
        if user is None:
            user = ctx.author
        
        user_id = str(user.id)
        is_verified = user_id in self.verified
        
        embed = discord.Embed(
            title=f"Status Verificare - {user.name}",
            color=discord.Color.green() if is_verified else discord.Color.orange()
        )
        
        if is_verified:
            embed.add_field(
                name="Status",
                value="✅ Verificat",
                inline=False
            )
        else:
            embed.add_field(
                name="Status",
                value="❌ Neverificat",
                inline=False
            )
            embed.add_field(
                name="Cum se Verifica",
                value="Utilizeaza comanda `!verify` pentru a incepe",
                inline=False
            )
        
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Trimite mesaj de bun venit cu info verificare"""
        if member.guild.id:  # Doar pentru servere
            embed = discord.Embed(
                title="Bun venit pe ServerUBB!",
                description=f"Salut {member.mention}! Te rugam sa te verifici pentru a accesa serverul complet.",
                color=discord.Color.blue()
            )
            embed.add_field(
                name="Cum se Verifica",
                value="Utilizeaza comanda `!verify` in orice canal",
                inline=False
            )
            embed.add_field(
                name="Beneficii",
                value="Acces la jocuri, economy, ranks si mai mult!",
                inline=False
            )
            
            try:
                await member.send(embed=embed)
            except:
                pass

async def setup(bot):
    await bot.add_cog(Verification(bot))
