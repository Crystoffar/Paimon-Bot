import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!:')

@client.event
async def on_ready():
    print('Paimon is ready!')

tokenFile = open("token.txt", "r")
tokenStr = tokenFile.read()
tokenFile.close()

client.run(tokenStr)
