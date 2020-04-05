import discord
import os
import token
from discord.ext import commands
from token import *

discord = commands.Bot(command_prefix = '.')

@discord.event
async def on_ready():
    print('Alexa has loaded into the server.')

@discord.command()
async def load(ctx, extension):
    discord.load_extension(f'cogs.{extension}')

@discord.command()
async def unload(ctx, extension):
    discord.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        discord.load_extension(f'cogs.{filename[:-3]}')

discord.run(token)