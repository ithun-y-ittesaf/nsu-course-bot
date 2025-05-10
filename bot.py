import discord
from discord.ext import commands
from utils.scheduler import start_scheduler

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load commands
from commands.add_course import add_course
from commands.remove_course import remove_course
from commands.helpme import helpme
from commands.check import check

bot.add_command(add_course)
bot.add_command(remove_course)
bot.add_command(helpme)
bot.add_command(check)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    start_scheduler(bot)

import os
bot.run(os.getenv("DISCORD_TOKEN"))
