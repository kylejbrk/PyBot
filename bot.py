import discord, os, requests, re
from discord.ext import commands
from random import randint
from bs4 import BeautifulSoup
from imgurpython import ImgurClient 

token = os.environ.get('TOKEN')
servID = int(os.environ.get('SERVERID'))

description = '''Bot description here'''
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is live")

@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    '''
    Ping the bot 
    '''
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    '''
    Make the bot say something
    '''
    await ctx.send(content)

@bot.command()
async def coinflip(ctx):
    '''
    Flip a coin
    '''
    coin = randint(0, 1)
    if coin == 0:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')

@bot.command()
async def petittube(ctx):
    '''
    Get random Youtube video with 0 views
    '''
    petittube = requests.get('http://www.petittube.com/')
    soup = BeautifulSoup(petittube.content, 'html.parser')
    link = soup.find('iframe')['src']
    prefix = 'https://www.youtube.com/embed/'
    suffix = '?version=3&f=videos&app=youtube_gdata&autoplay=1'
    link = link[len(prefix)-1:-len(suffix)]

    await ctx.send('https://www.youtube.com/watch?v=' + link)

@bot.command()
async def roll(ctx, first:int):
    '''
    Roll a die of any side (i.e. !roll 6)
    '''
    await ctx.send(randint(1, first))

@bot.command()
async def xkcd(ctx):
    '''
    Get a random xkcd comic
    '''
    xkcd = requests.get('https://c.xkcd.com/random/comic/')
    soup = BeautifulSoup(xkcd.content, 'html.parser')
    link = soup.select('#comic img')
    await ctx.send('https:' + link[0].get('src'))

if __name__ == '__main__':
    bot.run(token)