import os
import discord
from discord.ext import commands

token = os.getenv('Token')

client = commands.Bot(command_prefix=".")

@client.command()
async def foo(ctx, params):
    await ctx.send(f"lorem ipsum")

assert 1 == 2

client.run(token)