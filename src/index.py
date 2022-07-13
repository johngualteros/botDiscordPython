import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot=commands.Bot(command_prefix='>',description='This is a helper Bot')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx,number1:int,number2:int):
    await ctx.send(number1+number2)

@bot.command()
async def stats(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}",description="Lorem ipsum blah",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="Server Created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region",value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID",value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://i.morioh.com/210715/ff989a40.webp")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v='+search_results[0])

#Event

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='ExamplePython',url='http://www.twitch.tv/helbergalarga7'))
    print('The bot is ready')

@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

bot.run(token)