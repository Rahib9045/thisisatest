import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up bot with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    """Responds with a friendly hello message"""
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command(name='ping')
async def ping(ctx):
    """Check the bot's latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 