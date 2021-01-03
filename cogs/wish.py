import discord
import json
import random
from discord.ext import commands

class Wish(commands.Cog):

    #Constructor
    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command()
    async def wish(self, ctx, numWishes = 1):
        bannerFiveStar = "Albedo"
        fiveStar = ["Keqing", "Qiqi", "Mona", "Diluc", "Jean"]
        bannerFourStar = ["Sucrose", "Bennett", "Fischl"]
        fourStarChar = ["Xinyan", "Diona", "Chongyun", "Noelle", "Ningguang",
                        "Xinqiu", "Beidou", "Xiangling", "Razor", "Barbara"]
        fourStarWep = ["Rust", "Sacrificial Bow", "The Stringless",
                       "Favonius Warbow", "Eye of Perception",
                       "Sacrificial Fragments", "The Widsith", "Favonius Codex",
                       "Favonius Lance", "Dragon's Bane", "Rainslasher",
                       "Sacrificial Greatsword", "The Bell",
                       "Favonius Greatsword", "Lion's Roar",
                       "Sacrificial Sword", "The Flute", "Favonius Sword"]
        threeStarWep = ["Slingshot", "Sharpshooter's Oath", "Raven Bow",
                        "Emerald Orb", "Thrilling Tales of Dragon Slayers",
                        "Magic Guide", "Black Tassel", "Debate club",
                        "Bloodtainted Greatsword", "Ferrous Shadow",
                        "Skyrider Sword", "Harbinger of Dawn", "Cool Steel"]

        with open(r"PATHTOPITYJSON",'r') as f:
            users = json.load(f)

        userID = str(ctx.author)

        if not userID in users:
            users[userID] = {}
            users[userID]['fourPity'] = 0
            users[userID]['fivePity'] = 0

        for i in range(0, numWishes):
            rng = random.randint(1, 1000)
            roll = ""
            if rng < 7:
                banner = random.randint(0, 1)
                if banner == 1:
                    roll = bannerFiveStar
                else:
                    roll = random.choice(fiveStar)
                users[userID]['fourPity'] = 0
                users[userID]['fivePity'] = 0
            elif rng < 58:
                if users[userID]['fivePity'] == 89:
                    banner = random.randint(0, 1)
                    if banner == 1:
                        roll = bannerFiveStar
                    else:
                        roll = random.choice(fiveStar)
                    users[userID]['fourPity'] = 0
                    users[userID]['fivePity'] = 0
                else:
                    banner = random.randint(0, 1)
                    if banner == 1:
                        roll = random.choice(bannerFourStar)
                    else:
                        charOrWep = random.randint(0, 1)
                        if charOrWep == 1:
                            roll = random.choice(fourStarChar)
                        else:
                            roll = random.choice(fourStarWep)
                    users[userID]['fourPity'] = 0
                    users[userID]['fivePity'] += 1
            else:
                if users[userID]['fivePity'] == 89:
                    banner = random.randint(0, 1)
                    if banner == 1:
                        roll = bannerFiveStar
                    else:
                        roll = random.choice(fiveStar)
                    users[userID]['fourPity'] = 0
                    users[userID]['fivePity'] = 0
                elif users[userID]['fourPity'] == 9:
                    banner = random.randint(0, 1)
                    if banner == 1:
                        roll = random.choice(bannerFourStar)
                        users[userID]['fourPity'] = 0
                        users[userID]['fivePity'] += 1
                    else:
                        charOrWep = random.randint(0, 1)
                        if charOrWep == 1:
                            roll = random.choice(fourStarChar)
                        else:
                            roll = random.choice(fourStarWep)
                        users[userID]['fourPity'] = 0
                        users[userID]['fivePity'] += 1
                else:
                    roll = random.choice(threeStarWep)
                    users[userID]['fourPity'] += 1
                    users[userID]['fivePity'] += 1
            await ctx.send(roll)

        with open(r"PATHTOPITYJSON",'w') as f:
            json.dump(users, f)

def setup(bot):
    bot.add_cog(Wish(bot))
