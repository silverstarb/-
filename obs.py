import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)


client.run(os.environ['token'])

@bot.command()
async def 안녕(ctx):
await ctx.channel.send(f'{ctx.message.author.mention}님, 나도 안녕!'', reference=ctx.message)

@bot.command()
async def 안녕(ctx):
dm_channel = await ctx.message.author.create_dm()
await dm_channel.send(f'{ctx.message.author.mention}님, 나도 안녕!')

@bot.command()
async def 삭제(ctx):
await ctx.message.delete()
await ctx.channel.send('메세지를 삭제했어요.')

@bot.command()
async def 얼리기(ctx):
global isFrozen
if isFrozen:
await ctx.message.delete()
await ctx.channel.send('> 이미 채팅창이 얼어있습니다.')
else:
isFrozen = True
await ctx.message.delete()
await ctx.channel.send('> ' + ctx.author.name + '님이 채팅창을 얼렸습니다.')


