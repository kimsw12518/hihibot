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
                return str("`{}` ????????? ???????????? ?????????????????????".format(str(input)))
            else:
                self.memo.append(input)
                return str("`{}` ????????? ????????? ?????????????????????".format(str(input)))
        else:
            return str("`!?????? ?????? (??????,????????? ??????)\n!?????? ??????`")




a=[]

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("?????????... ??????????")
    print(f"a???, {bot.user}??? ???????????????")
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!????????? "))

hihi=0

@bot.command()
async def ??????(ctx):
    await ctx.send("{} ??????".format(ctx.message.author.mention))

@bot.command()
async def ??????(ctx,order='1'):
    global hihi
    string="???"
    if order=='??????':
        hihi=0
        string = ''.join([string, '??? ?????? ?????? ??????.'])
    elif order=='??????':
        string = '?????? ?????? ????????? {0}.'.format(hihi+1)
    else:
        order=int(order)
        hihi = hihi + order
        for i in range(0,hihi):
            r=randint(0,5)
            if r==0:
                string=''.join([string,'???'])
            elif r==1:
                string=''.join([string,'???'])
            else:
                string = ''.join([string, '???'])
    await ctx.send(f"{string}")

@bot.command()
async def ?????????(ctx):
    await ctx.send("!??????, !??????, !clear, !??????, !??????, !?????????, !???????????????, !??????, !??????, !??????, !??????")

@bot.command()
async def ??????(ctx):
    await ctx.send("(??????????????????? ?????????")

@bot.command()
async def ??????(ctx):
    await ctx.send(":coffin:")

@bot.command()
async def ????????????(ctx):
    await ctx.send(" :man_cartwheeling: \n:hole: :manual_wheelchair::man_golfing:")

@bot.command()
async def ??????(ctx):
    await ctx.send("?????????\n??????\n??????\n??????\n?????????\n????????? ??????\n???????????? ??????\n???????????? ??????\n?????????")

@bot.command()
async def ?????????(ctx):
    await ctx.send(":{0}:".format(dice[randint(0,5)]))

@bot.command()
async def ??????(ctx):
    await ctx.send(":thinking:")

@bot.command()
async def ??????(ctx,order='d'):
    test=0
    i=0
    for i in range(0, len(a), 1):
        if str(ctx.guild) in a[i].server:
            test = 1
            break
    if test == 0:
        a.append(Server(str(ctx.guild)))
        i=len(a)-1
    if order=='??????':
        if a[i].cardleft!=0:
            card=a[i].Card()
            embed=discord.Embed(title=f"{carddeck[card][0]}",description=f"{carddeck[card][1]}",color=0x00ddff)
            embed.add_field(name=f"{ctx.message.author.name}??? ??????",value=f"{a[i].cardleft}??? ??????")
            await ctx.send(f"{ctx.message.author.mention}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("?????? ?????????...")
    elif order=='??????':
        a[i].Cardreset()
        await ctx.send(":spades: :arrows_counterclockwise: :diamonds:\n:hearts: :black_joker: :clubs:")
    else:
        await ctx.send("`!?????? ??????\n!?????? ??????`")

@bot.command()
async def ???????????????(ctx,order='d'):
    test=0
    i=0
    for i in range(0, len(a), 1):
        if str(ctx.guild) in a[i].server:
            test = 1
            break
    if test == 0:
        a.append(Server(str(ctx.guild)))
        i=len(a)-1
    if order=="??????":
        if a[i].rusrulplaying==0:
            if ctx.message.author.name in a[i].rusrulplayer:
                a[i].rusrulplayer.remove(ctx.message.author.name)
                string = "\n".join(a[i].rusrulplayer)
                await ctx.send(f"{ctx.message.author.name} ??????!\n```????????? ??????\n{string}```")
            else:
                if len(a[i].rusrulplayer)==5:
                    await ctx.send(f"?????? ?????? ?????????;;")
                else:
                    a[i].rusrulplayer.append(ctx.message.author.name)
                    string="\n".join(a[i].rusrulplayer)
                    await ctx.send(f"??????????????? {ctx.message.author.name} ??????!\n```????????? ??????\n{string}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} ?????? ????????????...")
            return
    if order=="??????":
        string = " v.s ".join(a[i].rusrulplayer)
        await ctx.send(f"{string}") #???????????? ????????????
        a[i].rusrulplaying = 1
        bullet = randint(0, 5)
        print(bullet)
        curpl=randint(0, len(a[i].rusrulplayer))
        while len(a[i].rusrulplayer)>1:
            bullet = randint(0, 5)
            for t in range(0, 5):
                sleep(1)
                curpl=curpl+1 % len(a[i].rusrulplayer)
                await ctx.send("{} ??????".format(a[i].rusrulplayer[t % 2]))
                if bullet == t:
                    sleep(0.5)
                    await ctx.send("???!")
                    sleep(1)
                    await ctx.send(f"{a[i].rusrulplayer[t]} ??????!")
                    a[i].rusrulplayer.remove(a[i].rusrulplayer[t])
                    break
                else:
                    sleep(0.5)
                    await ctx.send("???...")
            if len(a[i].rusrulplayer) != 1:
                await ctx.send("reloading...")
        await ctx.send(f"{a[i].rusrulplayer[0]} ??????!")
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
                await ctx.send("?????? {0}?????? ???????????? ?????????????????????.".format(amount))
                data = f"{now()}/{ctx.guild} ????????? {ctx.channel} ?????? {ctx.message.author.name} {ctx.message.author.mention} {str(amount)}\n"
                f.write(data)
                f.close()
                sleep(2)
                await ctx.channel.purge(limit=1)
            else:
                await ctx.send("```50??? ????????? ???????????? ????????? ??? ????????????.(????????????)```".format(amount))
        except:
            await ctx.send("...????????????")
    else:
        await ctx.send("`!clear (?????????)\n*????????? ????????? ????????? ???????????????.`")

@bot.command()
async def ??????(ctx,order="d",*string: str):
    test=0
    i=0
    if order=="??????":
        for i in range(0,len(a),1):
            if str(ctx.guild) in a[i].server:
                test=1
                await ctx.send(a[i].Memo(string))
                return
        if test==0:
            a.append(Server(str(ctx.guild)))
            await ctx.send(a[len(a)-1].Memo(string))
    elif order=="??????":
        for i in range(0,len(a),1):
            if str(ctx.guild) in a[i].server:
                test=1
                if str(a[i].memo)=='[]':
                    await ctx.send("?????????...?????????????")
                else:
                    await ctx.send("`{0}`".format(str(a[i].memo)))
                return
        if test == 0:
            await ctx.send("?????????...?????????????")
    else:
        await ctx.send("`!?????? ?????? (??????,????????? ??????)\n!?????? ??????`")

#@bot.command()
#async def ????????????(ctx):



bot.run("token")

#????????? ????????? ctx.guild
#????????? ????????? ctx.channel
