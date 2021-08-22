import discord, asyncio, datetime, time
from discord.ext import commands, tasks

app = commands.Bot(command_prefix='알림')

# 테스트 서버
테스트서버 = 832286544496033843
일반채팅 = 832286544496033846
# 야영지 서버
야영지서버 = 540930626505932800
재획알림방 = 878736864633315358
# 메--창 서버
메창서버 = 808742146391801856
재획알리미 = 878999964351606784

alarmLst = [] 
alarmLst2 = [] 
alarmInfo = {}
alarmInfo['alarmOn'] = False


@app.event
async def on_ready():
    print('다음으로 로그인합니다: ' + app.user.name)
    print('connection was successful')
    await app.change_presence(status=discord.Status.online, activity=None)
    await app.get_guild(테스트서버).get_channel(일반채팅).send('학식봇 재시작!')
    # await app.get_guild(야영지서버).get_channel(재획알림방).send('학식봇 재시작!')
    # await app.get_guild(메창서버).get_channel(재획알리미).send('학식봇 재시작!')
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
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'{curMin}분!', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'{curMin}분!', tts=True)
            return
        if curSec == 30:
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'30초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'30초 전 ({curMin+1}분)', tts=True)
            return
        if curSec == 50:
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'10초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'10초 전 ({curMin+1}분)', tts=True)
            return
    if (curMin in alarmLst2) and (curHour % 2 == 0):
        if curSec == 0:
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'{curMin}분! 이벤트 버프 ', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'{curMin}분! 이벤트 버프 ', tts=True)
            return
        if curSec == 30:
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'이벤트 버프 30초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'이벤트 버프 30초 전 ({curMin+1}분)', tts=True)
            return
        if curSec == 50:
            await app.get_guild(야영지서버).get_channel(재획알림방).send(f'이벤트 버프 10초 전 ({curMin+1}분)', tts=True)
            await app.get_guild(메창서버).get_channel(재획알리미).send(f'이벤트 버프 10초 전 ({curMin+1}분)', tts=True)
            return

@app.command()
async def 추가(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num not in alarmLst and num not in alarmLst2:
            if num > -1 and num < 60:
                alarmLst.append(num)
                alarmLst.sort()
            else:
                await ctx.send(f'{num}는 숫자 범위가 맞지 않습니다(0~59)')
    await ctx.send(alarmLst)

@app.command()
async def 추가2(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num not in alarmLst and num not in alarmLst2:
            if num > -1 and num < 60:
                alarmLst2.append(num)
                alarmLst2.sort()
            else:
                await ctx.send(f'{num}는 숫자 범위가 맞지 않습니다(0~59)')
    await ctx.send(alarmLst2)

@app.command()
async def 제거(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num in alarmLst:
            alarmLst.remove(num)
    await ctx.send(alarmLst)

@app.command()
async def 제거2(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num in alarmLst2:
            alarmLst2.remove(num)
    await ctx.send(alarmLst2)

@app.command()
async def 다제거(ctx):
    del alarmLst[:]
    await ctx.send(alarmLst)

@app.command()
async def 다제거2(ctx):
    del alarmLst2[:]
    await ctx.send(alarmLst2)

@app.command()
async def 켜기(ctx):
    if not alarmInfo['alarmOn']:
        alarmInfo['alarmOn'] = True
        루프.start()
        await ctx.send("알림이 켜졌습니다!")
    else:
        await ctx.send("이미 알림이 켜져있어..!")

@app.command()
async def 끄기(ctx):
    if alarmInfo['alarmOn']:
        alarmInfo['alarmOn'] = False
        루프.cancel()
        await ctx.send("알림이 꺼졌습니다..!")
    else:
        await ctx.send("이미 알림이 꺼져있어..!")

@app.command()
async def 켰니(ctx):
    if alarmInfo['alarmOn']:
        await ctx.send('응 켰어')
    else :
        await ctx.send('아니 껐어')

@app.command()
async def 껐니(ctx):
    if alarmInfo['alarmOn']:
        await ctx.send('아니 켰어')
    else :
        await ctx.send('응 껐어')

@app.command()
async def 리스트(ctx):
    if(len(alarmLst) == 0):
        await ctx.send('등록된 알람이 없엉..')
    await ctx.send(f'{alarmLst}에 울려!')

@app.command()
async def 리스트2(ctx):
    if(len(alarmLst2) == 0):
        await ctx.send('등록된 알람이 없엉..')
    await ctx.send(f'{alarmLst2}에 울려!')

@app.command()
async def 지금(ctx):
    cur = datetime.datetime.now()
    curSec = cur.second
    curMin = cur.minute
    curHour = cur.hour + 9
    curDay = cur.day
    if curHour >= 24:
        curHour -= 24
        curDay += 1
    await ctx.send(f'{curDay}일 {curHour}시 {curMin}분 {curSec}초야!')

@app.command()
async def 재획용(ctx):
    del alarmLst[:]
    alarmLst.append(29)
    alarmLst.append(59)
    await ctx.send('재획용 29분 59분 알림이야!')
    if not alarmInfo['alarmOn']:
        # await ctx.send('알람이 꺼져있어! (#알림켜기#)')
        alarmInfo['alarmOn'] = True
        루프.start()
        await ctx.send("알림이 켜졌습니다!")
        # 함수 안에 함수 넣는 방법 아시는 분..?

app.run('ODc4Njc2NzYxODUwODA2MzUy.YSEpgQ.9QodKdVKGt5jinZNwxEUkkhsn-I')