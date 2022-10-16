import discord
import os
import random
import re
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    pass

# or:

@commands.command()
async def test(ctx):
    pass

bot.add_command(test)