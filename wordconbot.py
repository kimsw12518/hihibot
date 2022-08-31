# -*- coding: utf-8 -*-
import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("히히 라이트 온")
    await client.change_presence(status=discord.Status.online, activity=game)

channel="끝말잇기"
word="aaa"
wordlist=['가','나','다','라','마','바','사','아','자','차','카','타','파','하']
doo=['녀','녁','녂','녃','년','녅','녆','녇','녈','녉','녊','녋','녌','녍','녎','녏','념','녑','녒','녓','녔','녕','녖','녗','녘','녙','녚','녛','뇨','뇩','뇪','뇫','뇬','뇭','뇮','뇯','뇰','뇱','뇲','뇳','뇴','뇵','뇶','뇷','뇸','뇹','뇺','뇻','뇼','뇽','뇾','뇿','눀','눁','눂','눃','뉴','뉵','뉶','뉷','뉸','뉹','뉺','뉻','뉼','뉽','뉾','뉿','늀','늁','늂','늃','늄','늅','늆','늇','늈','늉','늊','늋','늌','늍','늎','늏','니','닉','닊','닋','닌','닍','닎','닏','닐','닑','닒','닓','닔','닕','닖','닗','님','닙','닚','닛','닜','닝','닞','닟','닠','닡','닢','닣','랴','략','랶','랷','랸','랹','랺','랻','랼','랽','랾','랿','럀','럁','럂','럃','럄','럅','럆','럇','럈','량','럊','럋','럌','럍','럎','럏','려','력','렦','렧','련','렩','렪','렫','렬','렭','렮','렯','렰','렱','렲','렳','렴','렵','렶','렷','렸','령','렺','렻','렼','렽','렾','렿','례','롁','롂','롃','롄','롅','롆','롇','롈','롉','롊','롋','롌','롍','롎','롏','롐','롑','롒','롓','롔','롕','롖','롗','롘','롙','롚','롛','료','룍','룎','룏','룐','룑','룒','룓','룔','룕','룖','룗','룘','룙','룚','룛','룜','룝','룞','룟','룠','룡','룢','룣','룤','룥','룦','룧','류','륙','륚','륛','륜','륝','륞','륟','률','륡','륢','륣','륤','륥','륦','륧','륨','륩','륪','륫','륬','륭','륮','륯','륰','륱','륲','륳','리','릭','릮','릯','린','릱','릲','릳','릴','릵','릶','릷','릸','릹','릺','릻','림','립','릾','릿','맀','링','맂','맃','맄','맅','맆','맇','라','락','띾','띿','란','랁','랂','랃','랄','랅','랆','랇','랈','랉','랊','랋','람','랍','랎','랏','랐','랑','랒','랓','랔','랕','랖','랗','래','랙','랚','랛','랜','랝','랞','랟','랠','랡','랢','랣','랤','랥','랦','랧','램','랩','랪','랫','랬','랭','랮','랯','랰','랱','랲','랳','로','록','롞','롟','론','롡','롢','롣','롤','롥','롦','롧','롨','롩','롪','롫','롬','롭','롮','롯','롰','롱','롲','롳','롴','롵','롶','롷','뢰','뢱','뢲','뢳','뢴','뢵','뢶','뢷','뢸','뢹','뢺','뢻','뢼','뢽','뢾','뢿','룀','룁','룂','룃','룄','룅','룆','룇','룈','룉','룊','룋','루','룩','룪','룫','룬','룭','룮','룯','룰','룱','룲','룳','룴','룵','룶','룷','룸','룹','룺','룻','룼','룽','룾','룿','뤀','뤁','뤂','뤃','르','륵','륶','륷','른','륹','륺','륻','를','륽','륾','륿','릀','릁','릂','릃','름','릅','릆','릇','릈','릉','릊','릋','릌','릍','릎','릏']
eum=['여','역','엮','엯','연','엱','엲','엳','열','엵','엶','엷','엸','엹','엺','엻','염','엽','엾','엿','였','영','옂','옃','옄','옅','옆','옇','요','욕','욖','욗','욘','욙','욚','욛','욜','욝','욞','욟','욠','욡','욢','욣','욤','욥','욦','욧','욨','용','욪','욫','욬','욭','욮','욯','유','육','윢','윣','윤','윥','윦','윧','율','윩','윪','윫','윬','윭','윮','윯','윰','윱','윲','윳','윴','융','윶','윷','윸','윹','윺','윻','이','익','읶','읷','인','읹','읺','읻','일','읽','읾','읿','잀','잁','잂','잃','임','입','잆','잇','있','잉','잊','잋','잌','잍','잎','잏','야','약','앾','앿','얀','얁','얂','얃','얄','얅','얆','얇','얈','얉','얊','얋','얌','얍','얎','얏','얐','양','얒','얓','얔','얕','얖','얗','여','역','엮','엯','연','엱','엲','엳','열','엵','엶','엷','엸','엹','엺','엻','염','엽','엾','엿','였','영','옂','옃','옄','옅','옆','옇','예','옉','옊','옋','옌','옍','옎','옏','옐','옑','옒','옓','옔','옕','옖','옗','옘','옙','옚','옛','옜','옝','옞','옟','옠','옡','옢','옣','요','욕','욖','욗','욘','욙','욚','욛','욜','욝','욞','욟','욠','욡','욢','욣','욤','욥','욦','욧','욨','용','욪','욫','욬','욭','욮','욯','유','육','윢','윣','윤','윥','윦','윧','율','윩','윪','윫','윬','윭','윮','윯','윰','윱','윲','윳','윴','융','윶','윷','윸','윹','윺','윻','이','익','읶','읷','인','읹','읺','읻','일','읽','읾','읿','잀','잁','잂','잃','임','입','잆','잇','있','잉','잊','잋','잌','잍','잎','잏','나','낙','낚','낛','난','낝','낞','낟','날','낡','낢','낣','낤','낥','낦','낧','남','납','낪','낫','났','낭','낮','낯','낰','낱','낲','낳','내','낵','낶','낷','낸','낹','낺','낻','낼','낽','낾','낿','냀','냁','냂','냃','냄','냅','냆','냇','냈','냉','냊','냋','냌','냍','냎','냏','노','녹','녺','녻','논','녽','녾','녿','놀','놁','놂','놃','놄','놅','놆','놇','놈','놉','놊','놋','놌','농','놎','놏','놐','놑','높','놓','뇌','뇍','뇎','뇏','뇐','뇑','뇒','뇓','뇔','뇕','뇖','뇗','뇘','뇙','뇚','뇛','뇜','뇝','뇞','뇟','뇠','뇡','뇢','뇣','뇤','뇥','뇦','뇧','누','눅','눆','눇','눈','눉','눊','눋','눌','눍','눎','눏','눐','눑','눒','눓','눔','눕','눖','눗','눘','눙','눚','눛','눜','눝','눞','눟','느','늑','늒','늓','는','늕','늖','늗','늘','늙','늚','늛','늜','늝','늞','늟','늠','늡','늢','늣','늤','능','늦','늧','늨','늩','늪','늫']
wordhist=[]

@client.event
async def on_message(message):
    global channel
    global word
    global wordlist
    global wordhist
    aa=str(message.channel)
    if aa==channel:
        if message.content.startswith(word):
            if message.content not in wordhist:
                word=message.content+"-"
                word=word[-2]
                if word in doo:
                    await message.channel.send(f"> {word}({eum[doo.index(word)]})_____")
                else:
                    await message.channel.send(f"> {word}_____")
                wordhist.append(message.content)
            
        if message.content.startswith("~리셋"):
            word= wordlist[random.randint(0,13)]
            if word in doo:
                await message.channel.send(f"> {word}({eum[doo.index(word)]})_____")
            else:
                await message.channel.send(f"> {word}_____")

        if message.content.startswith("~기록"):
            await message.channel.send(f"{wordhist}")

        if word in doo and message.content.startswith(eum[doo.index(word)]):
            if message.content not in wordhist:
                word = message.content + "-"
                word = word[-2]
                if word in doo:
                    await message.channel.send(f"> {word}({eum[doo.index(word)]})_____")
                else:
                    await message.channel.send(f"> {word}_____")
                wordhist.append(message.content)
            

client.run("Njk0Mzk0MTg2NjEwNTA3ODE3.XvDBmA.vsWbn_bCNZKB71gwrSEPBZKfy3s")