from yelp import *
import discord
import re
from discord.ext import commands
from discord.utils import get

REGEX = re.compile(r'"(.*?)"')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix = '!', intents = intents)

        
@bot.command()
async def info(ctx):
    #ctx - context (information about how command was executed)
    await ctx.send("I am YelpBot")



@client.event
async def on_ready():
    print("YelpBot is now online.")


@client.event
async def on_message(message):
    # await message.add_reaction()
    # m_str = message.content()

#### add emojis to message
    if message.author == client.user:
        i = message.content.count('\n')
        # await message.channel.send(i)
        if i < 1:
            return

        for i in range(message.content.count('\n') + 1):
            await message.add_reaction(chr(ord("\U0001F1E6") + i))
        return 
    
#### fetch reactions and find most voted
    if message.content.startswith("!done"):
        
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
                winners += options[i]

        await message.channel.send(most_recent.reactions[0].count)
        await message.channel.send(winners)
        # await message.channel.send(reactions)
        return

                

    if message.content.startswith('!eat'):
        
        # fields = re.findall(r'"(.*?)"', message)
        # await message.channel.send(fields[0], fields[1:] if len(fields) > 0 else [])
        # await message.delete()
        args = message.content[5:].split(', ')
        # await message.channel.send(args)
        str = ''
        i = 0
        if len(args) <= 1:
            await message.channel.send("Enter more options to make a poll, dirtbag!")    
            return
        for arg in args:
            str += chr(ord("\U0001F1E6") + i) + '  ' + arg + '\n'
            i += 1
        await message.channel.send(str)
        # for arg in args:
        # await message.add_reaction(chr(ord("\U0001F1E6") + 0))
            # n += 1
        # await str.add_reaction("\U0001F1E6") 




    if message.content == 'hello':
        await message.channel.send('Welcome to YelpBot dirtbag')

@staticmethod
def get_emote(idx: int) -> str:
    """idx=0 -> A, idx=1 -> B, ... idx=25 -> Z"""
    if 0 <= idx < 26:
        return "\U0001F1E6"
        # return chr(ord("\U0001F1E6") + idx)
    return ""


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )
    

client.run('MTAzMDk0MDUyMjc5OTQzNTc5Nw.G3Ryq8.P_AONddzU9s3NIEg4_ZAdfZXOIXrSQPLpZ4Q9w')



pass