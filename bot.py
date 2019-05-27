import discord
import os
from random import randint

token = os.environ.get('TOKEN')
# servID = int(os.environ.get('SERVERID'))

client = discord.Client()

@client.event
async def on_message(message):
    # id = client.get_guild(servID)

    if message.content == '!hello':
        await message.channel.send("Hi")
    # elif message.content == '!users':
    #     await message.channel.send(f"""# of Members: {id.member_count}""") 
    elif message.content[:2] == '!d' and message.content[2:].isdigit():
        diceSide = int(message.content[2:])
        await message.channel.send(randint(1,diceSide))
    elif message.content == '!coinflip':
        coin = randint(0,1)
        if coin == 0:
            await message.channel.send('Heads')
        else:
            await message.channel.send('Tails')

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == 'general':
            await message.channel.send(f'''Welcome to the server {member.mention}''')

client.run(token)