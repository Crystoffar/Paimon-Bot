import discord
from discord.ext import commands

class Wish(commands.Cog):

    #Constructor
    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command()
    async def wish(self, ctx, numWishes = 1):
        for i in range(0, numWishes):
            await ctx.send("wash!")

def setup(bot):
    bot.add_cog(Wish(bot))
