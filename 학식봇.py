import discord, asyncio, datetime, time
from discord.ext import commands, tasks
from random import *

app = commands.Bot(command_prefix='밍')

# 테스트 서버 #
테스트서버 = 832286544496033843
테스트채팅 = 914897810153930833
# 메--창 서버
메창서버 = 808742146391801856
메창재획알림방 = 878999964351606784
# 이슬
이슬서버 = 815553588843118622
이슬재획알림방 = 914890809768304720

alarmLst = [] 
alarmLst2 = []
alarmInfo = {}
alarmInfo['alarmOn'] = False


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ' + app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.online, activity=None)
    await app.get_guild(이슬서버).get_channel(이슬재획알림방).send('학식봇 재시작!')
    alarmLst2.append(39)
    del alarmLst[:]
    alarmLst.append(29)
    alarmLst.append(59)
    if not alarmInfo['alarmOn']:
        alarmInfo['alarmOn'] = True
        루프.start()

# TODO: 경뿌 알림이( 29분 59분)
@tasks.loop(seconds=1)
async def 루프():
    cur = datetime.datetime.now()
    curSec = cur.second
    curMin = cur.minute
    curHour = cur.hour + 9
    curDay = cur.day
    if curHour >= 24:
        curHour -= 24
        curDay += 1
    if curMin in alarmLst:
        if curSec == 0:
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'{curMin}분!', tts=True)
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'{curMin}분!', tts=True)
            return
        if curSec == 30:
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'30초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'{curMin}분!', tts=True)
            return
        if curSec == 50:
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'10초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'{curMin}분!', tts=True)
            return
    if (curMin in alarmLst2) and (curHour % 2 == 0):
        if curSec == 0:
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'{curMin}분! 이벤트 버프 ', tts=True)
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'{curMin}분! 이벤트 버프 ', tts=True)
            return
        if curSec == 30:
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'이벤트 버프 30초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'이벤트 버프 30초 전 ({curMin+1}분)', tts=True)
            return
        if curSec == 50:
            await app.get_guild(이슬서버).get_channel(이슬재획알림방).send(f'이벤트 버프 10초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(메창재획알림방).send(f'이벤트 버프 10초 전 ({curMin+1}분)', tts=True)
            return

@app.command()
async def 추첨(ctx, *input):
    length = len(input)
    await ctx.send(f'{input} {length}명 중 당첨자는...')
    micro = datetime.datetime.now().microsecond
    random = micro % length
    await ctx.send(f'## {(input[random]).replace(",","")} ## ({micro} % {length} = {random})')

@app.command()
async def 여러명(ctx, *input):
    selectedPeople = []
    length = len(input) - 1
    n = int(input[0])
    people = list(input[1:])
    
    if(n < length):
        await ctx.send(f'{people} {length}명 중 당첨자는...')
        for i in range(n):
            random = datetime.datetime.now().microsecond % (length - i)
            selectedPeople.append(people.pop(random))
        await ctx.send(selectedPeople)

    else:
        await ctx.send(f'뽑는 사람({n})이 사람 수({length})보다 작아야합니다..!')

@app.command()
async def 읽어(ctx, *input):
    await ctx.send(' '.join(input), tts=True)

app.run('ODc4Njc2NzYxODUwODA2MzUy.YSEpgQ.9QodKdVKGt5jinZNwxEUkkhsn-I')
# heroku logs --tail --app maplestory-bot