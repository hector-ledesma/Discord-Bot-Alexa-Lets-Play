import discord
import aiohttp
import asyncio
from discord.ext import commands

class Online(commands.Cog):

    def __init__(self, discord):
        self.discord = discord

    @commands.Cog.listener()
    async def on_ready(self):
        print('Online commands are ready to be tested.')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('Hello!')
        print('hello to you too!')

    @commands.command()
    async def test(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:5000/') as r:
                if r.status == 200:
                    js = await r.json()

def setup(discord):
    discord.add_cog(Online(discord))