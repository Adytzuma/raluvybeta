import discord
import random
import datetime
import traceback
import aiohttp
import asyncio
from discord import opus
import async_timeout
from random import randint
from discord.ext import commands
from asyncio import sleep
import logging
import os
from discord import opus
import json
import discord
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL

bot = commands.Bot(command_prefix=';;')
logging.basicConfig(level='INFO')
bot.load_extension("cogs.admin")
bot.load_extension("cogs.sound")
bot.load_extension("cogs.music")
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
load_opus_lib()

@bot.event
async def on_ready():
     game = discord.Game("lmao")
     await bot.change_presence(activity=game)
     print(f"Bot is now online on {len(bot.guilds)} servers!")

@bot.event
async def on_command_error(ctx, error):
    if ctx.author.bot is True:
        return
    await ctx.send(error)

@bot.command(aliases=['userstatus', 'user-status', 'statususer', 'status-user'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def status(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
    if member.status.name == 'online':
          a = "<:online:536240817602560010> Online"
    if member.status.name == 'idle':
          a = "<:idle:536240817522868224> Idle"
    if member.status.name == 'dnd':
          a = "<:dnd:536240817531125760> DND"
    if member.status.name == 'offline':
          a = "<:offline:536240817552228385> Offline"
    if member.is_on_mobile():
          if member.mobile_status.name == 'online':
             b = "<:online:536240817602560010> Online"
          if member.mobile_status.name == 'idle':
             b = "<:idle:536240817522868224> Idle"
          if member.mobile_status.name == 'dnd':
             b = "<:dnd:536240817531125760> DND"
          if member.mobile_status.name == 'offline':
             b = "<:offline:536240817552228385> Offline"
    else:
       b = "This user is not on mobile."
    if member.desktop_status.name == 'online':
             c = "<:online:536240817602560010> Online"
    if member.desktop_status.name == 'idle':
             c = "<:idle:536240817522868224> Idle"
    if member.desktop_status.name == 'dnd':
             c = "<:dnd:536240817531125760> DND"
    if member.desktop_status.name == 'offline':
             c = "<:offline:536240817552228385> Offline"
    if member.web_status.name == 'online':
             d = "<:online:536240817602560010> Online"
    if member.web_status.name == 'idle':
             d = "<:idle:536240817522868224> Idle"
    if member.web_status.name == 'dnd':
             d = "<:dnd:536240817531125760> DND"
    if member.web_status.name == 'offline':
             d = "<:offline:536240817552228385> Offline"

    embed = discord.Embed(title=f"{member.name}'s status", color=discord.Color.blue())
    embed.add_field(name="Status", value=a)
    embed.add_field(name="User mobile status", value=b, inline=True)
    embed.add_field(name="User desktop status", value=c, inline=True)
    embed.add_field(name="User web status", value=d, inline=True)
    await ctx.send(embed=embed)
        

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    t = await ctx.send(':ping_pong: | Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

bot.run(os.getenv("TOKEN"))
