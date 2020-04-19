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
        await ctx.send('Sending a GET request to local server.')
        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:5000/') as r:
                if r.status == 200:
                    # js = await 
                    await ctx.send('Successfully received main menu response from server.')
                    print(js)
                elif r.status == 404:
                    await ctx.send('Successfully received 404 response.')
                else:
                    await ctx.send('Did not receive a 200 response from server.')

def setup(discord):
    discord.add_cog(Online(discord))