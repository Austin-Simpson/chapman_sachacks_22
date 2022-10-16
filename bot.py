import discord
import re
from discord.ext import commands

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
    if message.author == client.user:

        i = message.content.count('\n')
        
        # await message.channel.send(i)
        for i in range(message.content.count('\n') + 1):
            await message.add_reaction(chr(ord("\U0001F1E6") + i))
        
        return
    
    if message.content.startswith('!eat'):
        # fields = re.findall(r'"(.*?)"', message)
        # await message.channel.send(fields[0], fields[1:] if len(fields) > 0 else [])
        # await message.delete()
        args = message.content[5:].split(', ')
        # await message.channel.send(args)
        str = ""
        i = 0
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