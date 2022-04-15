import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)


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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
#run.py
import discord

client = discord.Client()  

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content == '$hello': # 만약 채팅이 '안녕'라면
        await message.channel.send('Hello!') # 나도안녕!라고 보내기

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")
     
@bot.command()
async def join(ctx)
	if ctx.author.voice and ctx.author.voice.channel:
    	channel = ctx.author.voice.channel
    	await channel.connect()
    else:
    	await ctx.send("음성채널 없음")  

@bot.command()
async def leave(ctx):
	await bot.voice_clients[0].disconnect()
         
client.run(os.environ['token'])
  
client.run('token')