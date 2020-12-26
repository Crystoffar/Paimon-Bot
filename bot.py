import discord
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

#Obtaining Token
tokenFile = open("token.txt", "r")
tokenStr = tokenFile.read()
tokenFile.close()

bot.run(tokenStr)
