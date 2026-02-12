"""
Cog-ul Economy System cu Moneda Virtuala
v1.3.0 Feature
"""

import discord
from discord.ext import commands
import json
import os
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balance_file = "data/economy.json"
        self.shop_file = "data/shop.json"
        self.load_economy()
        self.load_shop()
        
        # Moneda nume
        self.currency = "UBB Coins"
        self.currency_emoji = "💰"
    
    def load_economy(self):
        """Incarca datele economice"""
        if not os.path.exists(self.balance_file):
            self.balances = {}
        else:
            try:
                with open(self.balance_file, 'r') as f:
                    self.balances = json.load(f)
            except:
                self.balances = {}
    
    def load_shop(self):
        """Incarca shop-ul"""
        if not os.path.exists(self.shop_file):
            self.shop = {
                "1": {"name": "Premium Badge", "price": 500, "emoji": "✨", "type": "badge"},
                "2": {"name": "Nickname Color", "price": 300, "emoji": "🎨", "type": "color"},
                "3": {"name": "Custom Prefix", "price": 1000, "emoji": "📝", "type": "prefix"},
                "4": {"name": "Secret Role", "price": 2000, "emoji": "🔐", "type": "role"},
                "5": {"name": "Bot Response", "price": 750, "emoji": "🤖", "type": "feature"},
            }
            self.save_shop()
        else:
            try:
                with open(self.shop_file, 'r') as f:
                    self.shop = json.load(f)
            except:
                self.shop = {}
    
    def save_economy(self):
        """Salveaza datele economice"""
        os.makedirs(os.path.dirname(self.balance_file), exist_ok=True)
        with open(self.balance_file, 'w') as f:
            json.dump(self.balances, f, indent=4)
    
    def save_shop(self):
        """Salveaza shop-ul"""
        os.makedirs(os.path.dirname(self.shop_file), exist_ok=True)
        with open(self.shop_file, 'w') as f:
            json.dump(self.shop, f, indent=4)
    
    def get_balance(self, user_id):
        """Obtine balanta unui utilizator"""
        user_id = str(user_id)
        if user_id not in self.balances:
            self.balances[user_id] = {"balance": 100, "items": {}}
            self.save_economy()
        return self.balances[user_id]["balance"]
    
    def add_coins(self, user_id, amount):
        """Adauga monezi"""
        user_id = str(user_id)
        if user_id not in self.balances:
            self.balances[user_id] = {"balance": 0, "items": {}}
        self.balances[user_id]["balance"] += amount
        self.save_economy()
    
    def remove_coins(self, user_id, amount):
        """Scade monezi"""
        user_id = str(user_id)
        if user_id not in self.balances:
            self.balances[user_id] = {"balance": 0, "items": {}}
        if self.balances[user_id]["balance"] >= amount:
            self.balances[user_id]["balance"] -= amount
            self.save_economy()
            return True
        return False
    
    @commands.command(name='balance')
    async def balance(self, ctx, user: discord.Member = None):
        """Vede balanta ta sau a altcuiva"""
        if user is None:
            user = ctx.author
        
        balance = self.get_balance(user.id)
        
        embed = discord.Embed(
            title=f"Balanta lui {user.name}",
            description=f"{self.currency_emoji} {balance} {self.currency}",
            color=discord.Color.gold()
        )
        embed.set_thumbnail(url=user.avatar.url)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='transfer')
    async def transfer(self, ctx, user: discord.Member, amount: int):
        """Trimite monezi unei persoane"""
        if amount <= 0:
            embed = discord.Embed(
                title="Eroare",
                description="Trebuie sa transferi o suma pozitiva!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        if user == ctx.author:
            embed = discord.Embed(
                title="Eroare",
                description="Nu poti trimite bani tie insuti!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        if self.remove_coins(ctx.author.id, amount):
            self.add_coins(user.id, amount)
            
            embed = discord.Embed(
                title="Transfer Complet",
                description=f"Ai trimis {self.currency_emoji} {amount} catre {user.name}",
                color=discord.Color.green()
            )
            embed.add_field(name="Balanta noua", value=f"{self.currency_emoji} {self.get_balance(ctx.author.id)}", inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Bani Insuficienti",
                description=f"Ai doar {self.currency_emoji} {self.get_balance(ctx.author.id)}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
    
    @commands.command(name='shop')
    async def shop(self, ctx):
        """Vede shop-ul disponibil"""
        embed = discord.Embed(
            title="Shop UBB",
            description="Cumpara iteme cu monezi tale!",
            color=discord.Color.blue()
        )
        
        for item_id, item in self.shop.items():
            embed.add_field(
                name=f"{item['emoji']} {item['name']}",
                value=f"Pret: {self.currency_emoji} {item['price']}\nID: `{item_id}`",
                inline=False
            )
        
        embed.set_footer(text="Utilizeaza !buy [ID] pentru a cumpara")
        await ctx.send(embed=embed)
    
    @commands.command(name='buy')
    async def buy(self, ctx, item_id: str):
        """Cumpar un item din shop"""
        if item_id not in self.shop:
            embed = discord.Embed(
                title="Eroare",
                description="Item-ul nu exista in shop!",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        item = self.shop[item_id]
        balance = self.get_balance(ctx.author.id)
        
        if balance < item["price"]:
            embed = discord.Embed(
                title="Bani Insuficienti",
                description=f"Ai nevoie de {self.currency_emoji} {item['price']} dar ai doar {self.currency_emoji} {balance}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        if self.remove_coins(ctx.author.id, item["price"]):
            user_id = str(ctx.author.id)
            if user_id not in self.balances:
                self.balances[user_id] = {"balance": self.get_balance(user_id), "items": {}}
            
            if item_id not in self.balances[user_id]["items"]:
                self.balances[user_id]["items"][item_id] = 0
            
            self.balances[user_id]["items"][item_id] += 1
            self.save_economy()
            
            embed = discord.Embed(
                title="Cumparare Reusita",
                description=f"Ai cumparatai {item['emoji']} {item['name']}",
                color=discord.Color.green()
            )
            embed.add_field(
                name="Pret",
                value=f"{self.currency_emoji} {item['price']}",
                inline=True
            )
            embed.add_field(
                name="Balanta Noua",
                value=f"{self.currency_emoji} {self.get_balance(ctx.author.id)}",
                inline=True
            )
            await ctx.send(embed=embed)
    
    @commands.command(name='inventory')
    async def inventory(self, ctx, user: discord.Member = None):
        """Vede inventarul tau sau al altcuiva"""
        if user is None:
            user = ctx.author
        
        user_id = str(user.id)
        items = self.balances.get(user_id, {}).get("items", {})
        
        embed = discord.Embed(
            title=f"Inventar - {user.name}",
            color=discord.Color.purple()
        )
        
        if not items or all(v == 0 for v in items.values()):
            embed.description = "Inventarul este gol!"
        else:
            for item_id, count in items.items():
                if count > 0 and item_id in self.shop:
                    item = self.shop[item_id]
                    embed.add_field(
                        name=f"{item['emoji']} {item['name']}",
                        value=f"Cantitate: {count}",
                        inline=False
                    )
        
        embed.add_field(
            name="Balanta",
            value=f"{self.currency_emoji} {self.get_balance(user.id)}",
            inline=False
        )
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Economy(bot))
