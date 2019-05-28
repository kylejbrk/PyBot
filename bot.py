import discord
import os
from random import randint
from bs4 import BeautifulSoup as bs4
from markdown import markdown
from imgurpython import ImgurClient

token = os.environ.get('TOKEN')
servID = int(os.environ.get('SERVERID'))

client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(servID)

    if message.content == '!hello':
        await message.channel.send("Hi")
    elif message.content == '!help':
        await message.channel.send(getCommands())
    elif message.content == '!users':
        await message.channel.send(f"""Number of Members: {id.member_count}""")
    elif message.content[:2] == '!d' and message.content[2:].isdigit():
        diceSide = int(message.content[2:])
        await message.channel.send(randint(1, diceSide))
    elif message.content == '!coinflip':
        coin = randint(0, 1)
        if coin == 0:
            await message.channel.send('Heads')
        else:
            await message.channel.send('Tails')

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == 'general':
            await message.channel.send(f'''Welcome to the server {member.mention}''')

def getCommands():
    file = open('README.md', 'r')
    data = file.read().splitlines()
    file.close()

    bCmd = False
    commands = ['**Commands**']
    for line in data:
        if line == '# Commands':
            bCmd = True
            continue
        elif bCmd:
            commands.append(line)
            if line == '```' and len(commands) > 2:
                break
    commands.append('**Author:**')
    commands.append('https://github.com/kylejbrk/Rabbot')
    return('\n'.join(commands))

client.run(token)