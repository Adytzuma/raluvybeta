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
import json


bot = commands.Bot(command_prefix=';;')
logging.basicConfig(level='INFO')
bot.load_extension("cogs.admin")
bot.load_extension("cogs.youtube")
#bot.load_extension("cogs.sound")
bot.load_extension("cogs.music")

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
        


                     
"""                    


@bot.event
async def on_member_join(member):
     with open("welcome.json", "r") as f:
        data = json.load(f)
     welcome = data['message'].replace("{server}", member.guild.name).replace("{user}", member.mention).replace("{membercount}", str(member.guild.member_count)) 
     try:
        if data['guild'] == member.guild.id:
             await bot.get_guild(data['guild']).get_channel(data['channel']).send(welcome)
        else:
             return
     except:
        pass

     
@bot.command(aliases=["welcomemessage", "welcomemsg", "joinmsg", "joinmessage", "welcome-message", "join-message", "welcome-msg", "join-msg"])
@commands.has_permissions(manage_guild=True)
async def welcome(ctx, *, message=None):
     error = "**Please use `,welcome <#channel> <message>`\n\n{user} = mention user\n{server} = server name\n{membercount} = member count**"
     if message is None:
        return await ctx.send(error)
     try:
        with open("welcome.json", "r") as f:
             read = json.load(f)
        if read['guild'] == ctx.guild.id:
             if read['guild']['channel'] == message.channel.id:
                await ctx.send(f"I'm on {message.channel.id}. Did you know? Type `--remove` for remove it and recreate it")
        else:
          with open("welcome.json", "w") as f:
             json.dump(data, f)
             data = {}
             data['guild'] = ctx.guild.id
             data['guild']['channel'] = message.channel.id
             data['guild']['message'] = message
             await ctx.send(f"**:white_check_mark: Done! I will send it on {message.channel.mention}!** :wink:")
     except:
        return

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def emoji(ctx, owo: discord.Emoji=None):
    a = random.choice(bot.emojis)
    if owo is None:
      return await ctx.send(a)
    else:
      try:
         uwu = bot.get_emoji(bot.guilds.emojis)
         if uwu == owo:
              await ctx.send(uwu)
         else:
              await ctx.send("**That emoji is not found on the bot! Try again with `,emoji`!**")
      except:
         return


@bot.command(aliases=['nickname'])
async def nick(ctx, member: discord.Member=None, *, uwu):
     try:
        if member is None:
          member = ctx.author
        owo = member.id
        if ctx.author.guild_permissions == 'manage_nickname' is True:
          await ctx.guild.get_member(owo).edit(nick=uwu)
          return await ctx.message.add_reaction('\U00002705')
        else:
          if ctx.author.guild_permissions == 'change_nickname' is True:
               await ctx.guild.get_member(ctx.author.id).edit(nick=uwu)
               return await ctx.message.add_reaction('\U00002705')
          else:
               await ctx.message.add_reaction('\U0000274c')
     except discord.Forbidden as owo:
        return await ctx.send(f"**Ops... I can't change because:**\n`{owo}`")

"""


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    t = await ctx.send(':ping_pong: | Pong!, Calculating...')
    await asyncio.sleep(1)
    await t.edit(content=f':ping_pong: | **Pong!** `{ctx.bot.latency * 1000:,.0f}MS`')

bot.run('NDkyMzcxODk2MzM2Mzg0MDE4.Do-y9Q.1F7gVsNEbBYw-Ca3sDFvi4H618I')
