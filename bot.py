
import discord
import re
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from yelp_api import *
import json
import requests
import disnake
from PIL import Image
import numpy as np
import urllib.request

REGEX = re.compile(r'"(.*?)"')

search_terms = ""         # string
location = "Orange, CA"                 # string
limit = 3                               # int (max 50)
radius = 10000                          # int (max 40000) in meters # string (best_match, rating, review_count, distance)
sort_by = "best_match" # string ("1" OR "1,2" OR "1,2,3" OR "1, 2, 3, 4")
price = "1, 2, 3, 4" # bool (True indicates only return open restaurants) (False returns all restaurants)
open_now = True
categories = "food"                     # string (filter by category)
latitude = 33.7879                      # float (latitude of location)
longitude = -117.8531                   # float (longitude of location)
attributes = "reservations"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def info(ctx):
    # ctx - context (information about how command was executed)
    await ctx.send("I am YelpBot")


@client.event
async def on_ready():
    print("YelpBot is now online.")


@client.event
async def on_message(message):
    # await message.add_reaction()
    # m_str = message.content()

    ### ask for user input (location) 
    if message.content.startswith("!location "):
        global location
        location = message.content[10:]
        await message.channel.send("Location set to: " + location)
        return
    # add emojis to message
    if message.author == client.user:
        i = message.content.count('\n')
        # await message.channel.send(i)
        if i < 1:
            return

        for i in range(message.content.count('\n') + 1):
            await message.add_reaction(chr(ord("\U0001F1E6") + i))
        return

# fetch reactions and find most voted
    if message.content.startswith("!done"):
        await message.delete()
        most_recent = None
        async for message in message.channel.history(limit=20):
            if message.author == client.user:
                if most_recent == None:
                    most_recent = message
                else:
                    if message.created_at > most_recent.created_at:
                        most_recent = message

        emoji_pattern = re.compile("["
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE)
        no_emoji = (emoji_pattern.sub(r'', most_recent.content))
        options = no_emoji.split('\n')
        # await message.channel.send("Most recent = " + most_recent.content)
        max = most_recent.reactions[0].count
        for i in range(len(most_recent.reactions) - 1):
            if most_recent.reactions[i].count < most_recent.reactions[i+1].count:
                max = most_recent.reactions[i+1].count

        winners = ""
        for i in range(len(most_recent.reactions)):
            if most_recent.reactions[i].count == max:
                await message.channel.send("Most voted for: " + most_recent.reactions[i].emoji)
                winners += options[i] + ", "
        winners = winners[:len(winners) - 2]
        search_terms = winners
        params = {'term': search_terms,
                  'location': location,
                  'limit': limit,
                  'price': price,
                  'categories': categories}
        response = search(params)
        parsed = json.loads(response.text)

        businesses = parsed["businesses"]


        for business in businesses:
            file = disnake.File("small_0.png", filename="image.png")
            print(business["rating"])
            embed=discord.Embed(title=business["name"], url=business["url"], description="Address: " + ", ".join(business["location"]["display_address"]) + "\n" + business["price"], color=0xdc143c)
            embed.set_image(url=business["image_url"])
            embed.set_footer(text=business["rating"], icon_url="https://logos-world.net/wp-content/uploads/2020/12/Yelp-Logo.png")
            embed.set_thumbnail(url="https://drjamestalkington.com/wp-content/uploads/2021/02/yelp-logo-png-round-8-copy.png")
            await message.channel.send(embed = embed)
        return

    if message.content.startswith('!eat'):

        # fields = re.findall(r'"(.*?)"', message)
        # await message.channel.send(fields[0], fields[1:] if len(fields) > 0 else [])
        await message.delete()
        args = message.content[5:].split(', ')
        # await message.channel.send(args)
        str = ''
        i = 0
        if len(args) <= 1:
            await message.channel.send("Enter more options to make a poll!")
            return
        for arg in args:
            str += chr(ord("\U0001F1E6") + i) + '  ' + arg + '\n'
            i += 1
        await message.channel.send(str)
        # for arg in args:
        # await message.add_reaction(chr(ord("\U0001F1E6") + 0))
        # n += 1
        # await str.add_reaction("\U0001F1E6")


@staticmethod
def get_emote(idx: int) -> str:
    """idx=0 -> A, idx=1 -> B, ... idx=25 -> Z"""
    if 0 <= idx < 26:
        return "\U0001F1E6"
        # return chr(ord("\U0001F1E6") + idx)
    return ""


# @client.event
# async def on_message_edit(before, after):
#     await before.channel.send(
#         f'{before.author} edit a message.\n'
#         f'Before: {before.content}\n'
#         f'After: {after.content}'
#     )

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)


pass
