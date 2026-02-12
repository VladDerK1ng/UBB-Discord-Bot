"""
UBB Discord Bot - Main Entry Point
Chatbot pentru comunitatea studentilor UBB
Ajuta cu calcule, informatii despre universitate si divertisment!

This is the main module that initializes and runs the Discord bot.
All specific command logic is organized in separate cogs for better maintainability.

Features:
- Text commands with prefix: !command
- Slash commands: /command
- Ping-based prefix detection
- Comprehensive error handling
- Professional logging
"""

import os
import logging
import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN, COMMAND_PREFIX, INTENTS, BOT_NAME, BOT_STATUS

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LOGGING CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VALIDATION AND INITIALIZATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if not TOKEN:
    logger.error("DISCORD_TOKEN not found in environment!")
    logger.info("Please create a .env file with: DISCORD_TOKEN=your_token_here")
    exit(1)

# Initialize the bot with command prefix and intents
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=INTENTS, help_command=None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COG LOADING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def load_cogs():
    """Load all cogs from the cogs directory"""
    cogs_dir = './cogs'
    loaded_count = 0
    failed_count = 0
    
    # Cogs to skip due to conflicts
    skip_cogs = {'moderation', 'advanced_moderation', 'info'}
    
    for filename in os.listdir(cogs_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            cog_name = filename[:-3]
            
            # Skip conflicting cogs
            if cog_name in skip_cogs:
                logger.info(f"⊘ Skipped cog: {cog_name} (conflicts with admin_extended)")
                continue
            
            try:
                await bot.load_extension(f'cogs.{cog_name}')
                logger.info(f"✓ Loaded cog: {cog_name}")
                loaded_count += 1
            except Exception as e:
                logger.error(f"✗ Failed to load cog {cog_name}: {str(e)}")
                failed_count += 1
    
    logger.info(f"Cog Loading Summary: {loaded_count} loaded, {failed_count} failed")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SLASH COMMANDS (Direct registration in main.py)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.tree.command(name="ping", description="Check bot latency")
async def slash_ping(interaction: discord.Interaction):
    """Slash command: Check bot ping"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"**⏱️ Latency:** `{latency}ms`",
        color=discord.Color.blue()
    )
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="balance", description="Check your balance")
async def slash_balance(interaction: discord.Interaction, user: discord.User = None):
    """Slash command: Check balance"""
    target_user = user if user else interaction.user
    embed = discord.Embed(
        title=f"💰 Balance - {target_user.name}",
        description="Use `!balance @user` for more details",
        color=discord.Color.gold()
    )
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="help", description="Show all available commands")
async def slash_help(interaction: discord.Interaction):
    """Slash command: Help menu"""
    embed = discord.Embed(
        title="📚 Bot Help",
        description="Use `!help` for full command list",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Quick Commands",
        value="`!help` - All commands\n`!balance` - Your balance\n`!shop` - View shop\n`!buy [id]` - Purchase item",
        inline=False
    )
    embed.add_field(
        name="Economy Commands",
        value="`!inventory` - Your items\n`!use [id]` - Use item\n`!gift @user [id]` - Gift item",
        inline=False
    )
    embed.add_field(
        name="Admin Commands",
        value="`!helpadmin` - Admin commands (admin only)",
        inline=False
    )
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed, ephemeral=False)


@bot.tree.command(name="shop", description="View available items")
async def slash_shop(interaction: discord.Interaction):
    """Slash command: View shop"""
    embed = discord.Embed(
        title="🛍️ Shop",
        description="Use `!shop` to see all items and buy with `!buy [id]`",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Items Available",
        value="Use `!shop` command for full details",
        inline=False
    )
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TEXT COMMANDS (Direct registration in main.py)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.command(name='help')
async def help_command(ctx, command: str = None):
    """Display all available commands or help for a specific command"""
    from config import BOT_VERSION, COMMANDS_DETAILS
    
    if command is None:
        # Compact help menu
        embed = discord.Embed(
            title="📚 UBB Discord Bot - Help Menu",
            description="Use `!help <command>` for details or `!helpadmin` for admin commands",
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


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EVENT HANDLERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@bot.event
async def on_ready():
    """Triggered when the bot successfully connects to Discord"""
    logger.info(f"✓ Bot connected as {bot.user}")
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        logger.info(f"✓ Synced {len(synced)} app commands")
    except Exception as e:
        logger.error(f"✗ Failed to sync commands: {e}")
    
    # List loaded cogs
    logger.info(f"✓ Loaded {len(bot.cogs)} cogs: {', '.join(bot.cogs.keys())}")
    
    # List loaded commands
    all_commands = [cmd.name for cmd in bot.commands]
    logger.info(f"✓ Loaded {len(all_commands)} text commands")
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=BOT_STATUS
        )
    )


@bot.event
async def on_message(message):
    """Handle messages and enable ping-based prefix"""
    if message.author == bot.user:
        return
    
    # Allow ping as prefix
    if message.content.startswith(bot.user.mention):
        # Replace ping with command prefix
        message.content = message.content.replace(bot.user.mention, "!", 1).strip()
    
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    logger.error(f"Command error in {ctx.command}: {error}")
    
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❌ Command Not Found",
            description="Nu am gasit comanda. Scrie !help pentru a vedea toate comenzile.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="⚠️ Missing Arguments",
            description=f"Comanda este incompleta! Scrie !help {ctx.command.name} pentru detalii.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)
    
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="🔒 Permission Denied",
            description="Nu ai permisiunile necesare pentru a executa aceasta comanda.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    
    elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
            title="🔒 Bot Permission Denied",
            description="Botul nu are permisiunile necesare pentru a executa aceasta actiune.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    
    else:
        embed = discord.Embed(
            title="❌ Unexpected Error",
            description="A aparut o eroare neasteptata. Incearca mai tarziu.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        logger.error(f"Unexpected error: {error}", exc_info=True)


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Handle slash command errors"""
    logger.error(f"App command error: {error}")
    
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(
            "🔒 Nu ai permisiunile necesare pentru aceasta comanda.",
            ephemeral=True
        )
    elif isinstance(error, app_commands.BotMissingPermissions):
        await interaction.response.send_message(
            "🔒 Botul nu are permisiunile necesare.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "❌ A aparut o eroare neasteptata.",
            ephemeral=True
        )
        logger.error(f"App command error details: {error}", exc_info=True)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BOT STARTUP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def main():
    """Main bot startup function"""
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info(f"Starting {BOT_NAME}...")
    logger.info(f"Features: Text commands (!) • Slash commands (/) • Ping prefix")
    logger.info("=" * 60)
    
    import asyncio
    asyncio.run(main())