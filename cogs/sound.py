import discord
from discord.ext import commands

error = "You must be connected to a voice channel"

class sound:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(invoke_without_command = True)
    async def fart(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/fart.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U0001f4a8')
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True)
    async def fortnite(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/fortnite.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            emoji = self.bot.get_emoji(495616375394664463)
            await ctx.message.add_reaction(emoji)
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True)
    async def illuminati(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/illuminati.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U0001f53a')
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True, aliases=['john-cena', 'johncena'])
    async def john(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/john.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U0001f60e')
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True, aliases=['ohohohmygod', 'ohmygod', 'ohohmygod'])
    async def omg(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/omg.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U0001f631')
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True, aliases=['sad-violin', 'sadviolin'])
    async def sad(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/sad.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U0001f641')
        else:
            await ctx.send(error)

    

    @commands.command(invoke_without_command = True, aliases=['windowsXP', 'winxp', 'windowsxp'])
    async def winXP(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/winXP.wav")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U00002705')
        else:
            await ctx.send(error)

    @commands.command(invoke_without_command = True, aliases=['whatthefuck', 'what-the-fuck', 'whattheheck'])
    async def wtf(self, ctx):
        if ctx.author.voice != None:
            try:
                await ctx.author.voice.channel.connect()
            except discord.ClientException:
                pass

            source = discord.FFmpegPCMAudio("data/sound/wtf.mp3")

            try:
                ctx.voice_client.play(source)
            except discord.ClientException:
                await ctx.send("Already playing audio.")
                return
            await ctx.message.add_reaction('\U00002049')
        else:
            await ctx.send(error)

    @commands.command(aliases = ["leave", "end", "disconnect"])
    async def stop(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()
            await ctx.message.add_reaction('\U0001f4e4')
        else:
            await ctx.send(f"{self.bot.user.name} is not currently in a voice channel")


def setup(bot):
    bot.add_cog(sound(bot))
