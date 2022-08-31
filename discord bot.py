import discord
from discord.ext import commands
from time import sleep
from random import *
import pickle
from datetime import datetime

dice=['one','two','three','four','five','six']
carddeck=[[":spades: **A**","**A of Spades**"],[":spades: **2**","**2 of Spades**"],[":spades: **3**","**3 of Spades**"],[":spades: **4**","**4 of Spades**"],[":spades: **5**","**5 of Spades**"],[":spades: **6**","**6 of Spades**"],[":spades: **7**","**7 of Spades**"],[":spades: **8**","**8 of Spades**"],[":spades: **9**","**9 of Spades**"],[":spades: **10**","**10 of Spades**"],[":spades: **J**","**J of Spades**"],[":spades: **Q**","**Q of Spades**"],[":spades: **K**","**K of Spades**"],[":diamonds: **A**","**A of Diamonds**"],[":diamonds: **2**","**2 of Diamonds**"],[":diamonds: **3**","**3 of Diamonds**"],[":diamonds: **4**","**4 of Diamonds**"],[":diamonds: **5**","**5 of Diamonds**"],[":diamonds: **6**","**6 of Diamonds**"],[":diamonds: **7**","**7 of Diamonds**"],[":diamonds: **8**","**8 of Diamonds**"],[":diamonds: **9**","**9 of Diamonds**"],[":diamonds: **10**","**10 of Diamonds**"],[":diamonds: **J**","**J of Diamonds**"],[":diamonds: **Q**","**Q of Diamonds**"],[":diamonds: **K**","**K of Diamonds**"],[":hearts: **A**","**A of Hearts**"],[":hearts: **2**","**2 of Hearts**"],[":hearts: **3**","**3 of Hearts**"],[":hearts: **4**","**4 of Hearts**"],[":hearts: **5**","**5 of Hearts**"],[":hearts: **6**","**6 of Hearts**"],[":hearts: **7**","**7 of Hearts**"],[":hearts: **8**","**8 of Hearts**"],[":hearts: **9**","**9 of Hearts**"],[":hearts: **10**","**10 of Hearts**"],[":hearts: **J**","**J of Hearts**"],[":hearts: **Q**","**Q of Hearts**"],[":hearts: **K**","**K of Hearts**"],[":clubs: **A**","**A of Clubs**"],[":clubs: **2**","**2 of Clubs**"],[":clubs: **3**","**3 of Clubs**"],[":clubs: **4**","**4 of Clubs**"],[":clubs: **5**","**5 of Clubs**"],[":clubs: **6**","**6 of Clubs**"],[":clubs: **7**","**7 of Clubs**"],[":clubs: **8**","**8 of Clubs**"],[":clubs: **9**","**9 of Clubs**"],[":clubs:10**","**10 of Clubs**"],[":clubs: **J**","**J of Clubs**"],[":clubs: **Q**","**Q of Clubs**"],[":clubs: **K**","**K of Clubs**"],[":spades: :diamonds: **JOKER** :hearts: :clubs:",":black_joker:"],[":spades: :diamonds: **BLACK JOKER** :hearts: :clubs:",":clown:"]]

def now():
    a= datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    return a

class Server:
    def __init__(self,*aaa):
        self.server=aaa
        self.cardleft=54
        self.cardused=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.memo=[]
        self.rusrulplaying=0
        self.rusrulplayer=[]

    def Card(self):
        if self.cardleft>0:
            self.cardleft=self.cardleft-1
            while True:
                x=randint(0,53)
                if self.cardused[x]==0:
                    self.cardused[x]=1
                    return x

    def Cardreset(self):
        self.cardleft=54
        self.cardused = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def Memo(self,input):
        input=list(map(str,input))
        input="_".join(input)
        if input != '':
            if input in self.memo:
                self.memo.remove(input)
                return str("`{}` 내역이 메모에서 제거되었습니다".format(str(input)))
            else:
                self.memo.append(input)
                return str("`{}` 내역이 메모에 추가되었습니다".format(str(input)))
        else:
            return str("`!메모 편집 (추가,제거할 내용)\n!메모 내역`")




a=[]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("여기가... 어디요?")
    print(f"aㅏ, {bot.user}요 안심하세요")
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!명령어 "))

hihi=0

@bot.command()
async def 안녕(ctx):
    await ctx.send("{} ㅎㅇ".format(ctx.message.author.mention))

@bot.command()
async def 히히(ctx,order='1'):
    global hihi
    string="히"
    if order=='리셋':
        hihi=0
        string = ''.join([string, '히 스택 리셋 완료.'])
    elif order=='스택':
        string = '현재 히히 스택은 {0}.'.format(hihi+1)
    else:
        order=int(order)
        hihi = hihi + order
        for i in range(0,hihi):
            r=randint(0,5)
            if r==0:
                string=''.join([string,'힣'])
            elif r==1:
                string=''.join([string,'ㅎ'])
            else:
                string = ''.join([string, '히'])
    await ctx.send(f"{string}")

@bot.command()
async def 명령어(ctx):
    await ctx.send("!안녕, !흠터, !clear, !카드, !메모, !주사위, !러시안룰렛, !히히, !빅맥, !안해, !관짝")

@bot.command()
async def 안해(ctx):
    await ctx.send("(╯°□°）╯︵ ┻━┻")

@bot.command()
async def 관짝(ctx):
    await ctx.send(":coffin:")

@bot.command()
async def 나이스샷(ctx):
    await ctx.send(" :man_cartwheeling: \n:hole: :manual_wheelchair::man_golfing:")

@bot.command()
async def 빅맥(ctx):
    await ctx.send("빵뚜껑\n양파\n피클\n치즈\n양상추\n특별한 소스\n순쇠고기 패티\n순쇠고기 패티\n참깨빵")

@bot.command()
async def 주사위(ctx):
    await ctx.send(":{0}:".format(dice[randint(0,5)]))

@bot.command()
async def 흠터(ctx):
    await ctx.send(":thinking:")

@bot.command()
async def 카드(ctx,order='d'):
    test=0
    i=0
    for i in range(0, len(a), 1):
        if str(ctx.guild) in a[i].server:
            test = 1
            break
    if test == 0:
        a.append(Server(str(ctx.guild)))
        i=len(a)-1
    if order=='뽑기':
        if a[i].cardleft!=0:
            card=a[i].Card()
            embed=discord.Embed(title=f"{carddeck[card][0]}",description=f"{carddeck[card][1]}",color=0x00ddff)
            embed.add_field(name=f"{ctx.message.author.name}의 카드",value=f"{a[i].cardleft}장 남음")
            await ctx.send(f"{ctx.message.author.mention}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("다시 섞어라...")
    elif order=='섞기':
        a[i].Cardreset()
        await ctx.send(":spades: :arrows_counterclockwise: :diamonds:\n:hearts: :black_joker: :clubs:")
    else:
        await ctx.send("`!카드 뽑기\n!카드 섞기`")

@bot.command()
async def 러시안룰렛(ctx,order='d'):
    test=0
    i=0
    for i in range(0, len(a), 1):
        if str(ctx.guild) in a[i].server:
            test = 1
            break
    if test == 0:
        a.append(Server(str(ctx.guild)))
        i=len(a)-1
    if order=="참가":
        if a[i].rusrulplaying==0:
            if ctx.message.author.name in a[i].rusrulplayer:
                a[i].rusrulplayer.remove(ctx.message.author.name)
                string = "\n".join(a[i].rusrulplayer)
                await ctx.send(f"{ctx.message.author.name} 쫄튀!\n```참여자 명단\n{string}```")
            else:
                if len(a[i].rusrulplayer)==5:
                    await ctx.send(f"사람 너무 많아요;;")
                else:
                    a[i].rusrulplayer.append(ctx.message.author.name)
                    string="\n".join(a[i].rusrulplayer)
                    await ctx.send(f"러시안룰렛 {ctx.message.author.name} 참가!\n```참여자 명단\n{string}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} 아직 안끝났다...")
            return
    if order=="시작":
        string = " v.s ".join(a[i].rusrulplayer)
        await ctx.send(f"{string}") #여기부터 갈아엎자
        a[i].rusrulplaying = 1
        bullet = randint(0, 5)
        print(bullet)
        curpl=randint(0, len(a[i].rusrulplayer))
        while len(a[i].rusrulplayer)>1:
            bullet = randint(0, 5)
            for t in range(0, 5):
                sleep(1)
                curpl=curpl+1 % len(a[i].rusrulplayer)
                await ctx.send("{} 격발".format(a[i].rusrulplayer[t % 2]))
                if bullet == t:
                    sleep(0.5)
                    await ctx.send("탕!")
                    sleep(1)
                    await ctx.send(f"{a[i].rusrulplayer[t]} 탈락!")
                    a[i].rusrulplayer.remove(a[i].rusrulplayer[t])
                    break
                else:
                    sleep(0.5)
                    await ctx.send("틱...")
            if len(a[i].rusrulplayer) != 1:
                await ctx.send("reloading...")
        await ctx.send(f"{a[i].rusrulplayer[0]} 우승!")
        a[i].rusrulplayer = []
        a[i].rusrulplaying = 0
    

@bot.command()
async def clear(ctx, amount : int=0):
    if amount>0:
        try:
            if amount<=50:
                f=open("log.txt",'a')
                await ctx.channel.purge(limit=1)
                await ctx.channel.purge(limit=amount)
                await ctx.send("최근 {0}개의 메시지를 제거하였습니다.".format(amount))
                data = f"{now()}/{ctx.guild} 서버의 {ctx.channel} 채널 {ctx.message.author.name} {ctx.message.author.mention} {str(amount)}\n"
                f.write(data)
                f.close()
                sleep(2)
                await ctx.channel.purge(limit=1)
            else:
                await ctx.send("```50개 이상의 메시지를 삭제할 수 없습니다.(악용방지)```".format(amount))
        except:
            await ctx.send("...권한내놔")
    else:
        await ctx.send("`!clear (자연수)\n*봇에게 관리자 권한이 필요합니다.`")

@bot.command()
async def 메모(ctx,order="d",*string: str):
    test=0
    i=0
    if order=="편집":
        for i in range(0,len(a),1):
            if str(ctx.guild) in a[i].server:
                test=1
                await ctx.send(a[i].Memo(string))
                return
        if test==0:
            a.append(Server(str(ctx.guild)))
            await ctx.send(a[len(a)-1].Memo(string))
    elif order=="내역":
        for i in range(0,len(a),1):
            if str(ctx.guild) in a[i].server:
                test=1
                if str(a[i].memo)=='[]':
                    await ctx.send("메모가...없는데요?")
                else:
                    await ctx.send("`{0}`".format(str(a[i].memo)))
                return
        if test == 0:
            await ctx.send("메모가...없는데요?")
    else:
        await ctx.send("`!메모 편집 (추가,제거할 내용)\n!메모 내역`")

#@bot.command()
#async def 슬롯머신(ctx):



bot.run("token")

#서버의 이름은 ctx.guild
#채널의 이름은 ctx.channel
