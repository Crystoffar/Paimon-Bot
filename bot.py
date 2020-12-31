import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = '!:')

#Events
@bot.event
async def on_ready():
    print('Paimon is ready!')

#Commands
@bot.command()
async def ehe(ctx):
    await ctx.send('"Ehe" te nandayo?!')

#Loading Cogs
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

#Obtaining Token
tokenFile = open("token.txt", "r")
tokenStr = tokenFile.read()
tokenFile.close()

bot.run(tokenStr)
