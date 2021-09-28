import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Gravity Destroyers"))

@bot.event
async def on_command_error(ctx,error):
    if ctx.message.content == ".pinghelp":
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("It seems like you have missed an arguement in the command. Remember to `.pinghelp @personwhoisaskingforhelp`")
            await asyncio.sleep(3)
            await ctx.message.delete()
    
@commands.command()
async def ping(ctx):
    await ctx.send("pong")

@commands.command()
async def cj(ctx):
    await ctx.send("CJ, da man")
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_partyparrot')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_scrollupfast')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_dealwithit')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_party')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_vibingcat')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_tilt')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_zoom')
    await ctx.send(str(emoji))
    await asyncio.sleep(1)
    emoji = discord.utils.get(bot.emojis, name='cj_colors')
    await ctx.send(str(emoji))

@commands.command()
async def emojis(ctx):
    for emoji in ctx.guild.emojis:
        await ctx.send(emoji.name)

@commands.command()
async def pinghelp(ctx, usermention):
    message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    name = ctx.author.mention
    content = message.content
    returns = f"{name} has requested a Helper Ping for: '{content}' which was sent by {usermention}\n All in favour react with <:greentick:875244017833639956>"
    #await ctx.send(returns)
    await ctx.message.reply(returns)
    await ctx.message.add_reaction('<:greentick:875244017833639956>')

instagram = 871911275926519828
reddit = 867599777743372299
channelCounter = 0
@bot.event
async def on_message(message):
    

    await bot.process_commands(message)
    global channelCounter
    channelCounter +=1
    if message.channel.id == instagram and channelCounter == 1:
        await message.channel.send("We have a new IG post. <@&883230758658011148>")
    #channelCounter = 0

    
    if message.channel.id == reddit and channelCounter == 1:
        await message.channel.send("We have a new Reddit post. <@&870509092974759946>")
    channelCounter = 0
    

bot.add_command(ping)
bot.add_command(pinghelp)
bot.add_command(cj)
bot.add_command(emojis)