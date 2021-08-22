import discord, asyncio, datetime, time
from discord.ext import commands, tasks

app = commands.Bot(command_prefix='알림')

# 테스트 서버
# serverId = 832286544496033843
# chattingId = 832286544496033846
# 야영지 서버
serverId = 540930626505932800
chattingId = 878736864633315358
#chattingId = 710809428450082876 음성채팅방 대화방

alarmLst = [] 
alarmRunningLst = [] 
alarmInfo = {}
alarmInfo['alarmOn'] = True
alarmInfo['alarmCnt'] = 0

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ' + 'app.user.name')
    print('connection was successful')
    await app.change_presence(status=discord.Status.online, activity=None)
    await app.get_guild(serverId).get_channel(chattingId).send(f'학식봇 등장! 현재 분({datetime.datetime.now().minute}분 같은거)는 넣지 마세요.. 고장납니다 ㅠㅠ)')

# TODO: 경뿌 알림이( 29분 59분)
@tasks.loop(seconds=1)
async def 루프():
    curSec = datetime.datetime.now().second
    curMin = datetime.datetime.now().minute
    if(curMin in alarmLst):
        if curSec > 1:
            alarmLst.remove(curMin)
            await app.get_guild(serverId).get_channel(chattingId).send(f'이미 {curMin}분 이야!', tts=True)
            time.sleep(61-curSec)
            alarmLst.append(curMin)
        else:
            alarmLst.remove(curMin)
            await app.get_guild(serverId).get_channel(chattingId).send(f'{curMin}분!', tts=True)
            time.sleep(29)
            await app.get_guild(serverId).get_channel(chattingId).send(f'30초 전 ({curMin+1}분)', tts=True)
            time.sleep(20)
            await app.get_guild(serverId).get_channel(chattingId).send(f'10초 전 ({curMin+1}분)', tts=True)
            alarmLst.append(curMin)
            time.sleep(11)

@app.command()
async def 추가(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num not in alarmLst:
            if num > -1 and num < 60:
                alarmLst.append(num)
                alarmLst.sort()
            else:
                await ctx.send(f'{num}는 숫자 범위가 맞지 않습니다(0~59)')
    await ctx.send(alarmLst)

@app.command()
async def 제거(ctx, *input):
    for elem in input:
        num = (int)(elem)
        if num in alarmLst:
            alarmLst.remove(num)
    await ctx.send(alarmLst)

@app.command()
async def 다제거(ctx):
    del alarmLst[:]
    await ctx.send(alarmLst)

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
async def 지금(ctx):
    await ctx.send(f'{datetime.datetime.now().minute}분 {datetime.datetime.now().minute}초야!')

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