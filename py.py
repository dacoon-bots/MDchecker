import discord
import datetime
import random
import os

datab={}
manager={493659299609051136,534145145109741569}

helpdata="""
`ㅁ지갑`
  - 내 <:makerdollar:686564265217360089>를 확인합니다.
`ㅁ지갑 <유저의 서버 별명 또는 멘션>`
  - 다른 사람의 <:makerdollar:686564265217360089>를 확인합니다.
`ㅁ송금 <금액> <유저의 서버 별명 또는 멘션>`
  - 다른 사람에게 <:makerdollar:686564265217360089>를 보냅니다.
`ㅁ돈벌기 <금액>`
  - 100<:makerdollar:686564265217360089>~200<:makerdollar:686564265217360089>사이의 금액을 법니다.
  - 쿨타임 10분
`ㅁ도박 <금액>`
  - 10%확률로 3배를 받습니다.
  - 20%확률로 2배를 받습니다.
  - 70%확률로 돈을 모두 잃습니다.
  - 쿨타임 5분
`ㅁ도둑질 <유저의 서버 별명 또는 멘션>`
  - 40%확률로 1000<:makerdollar:686564265217360089>~2000<:makerdollar:686564265217360089>사이의 돈을 훔쳐옵니다.
  - 30%확률로 실패합니다.
  - 30%확률로 메이커에게 걸려 1000<:makerdollar:686564265217360089>~2000<:makerdollar:686564265217360089>를 벌금으로 냅니다.
  - 쿨타임 10분
`ㅁ랭킹`
  - 랭킹을 확인한다.
"""
devoldata="""
`ㅁ지급 <금액> <유저의 서버 별명 또는 멘션>`
  - 유저에게 <:makerdollar:686564265217360089>를 지급합니다.
`ㅁ차감 <금액> <유저의 서버 별명 또는 멘션>`
  - 유저에게 <:makerdollar:686564265217360089>를 차감합니다.
"""

app = discord.Client()

@app.event
async def on_ready():
    print("Login complete\n")
    game = discord.Game("베타 테스트 중입니다. 현재 갱신된 데이터는 정식 버전때 모두 날아갑니다.")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):

    if not(message.author.id in datab):
        create_md(message.author.id)

    if message.content == "ㅁ도움":
        embed = gnembed("MDv2봇 도움말","", message.author)
        embed.add_field(name="MD 관련 커맨드", value=helpdata, inline=False)
        embed.add_field(name="메이커&개발자 전용 커맨드", value=devoldata, inline=False)
        await message.channel.send(embed = embed)

    if message.content == "ㅁ지갑":
        embed = gnembed(str(get_md(message.author))+"<:makerdollar:686564265217360089>","", message.author)
        await message.channel.send(embed = embed)

    elif message.content.startswith("ㅁ지갑 "):
        if len(message.mentions) == 1:
            embed = gnembed(str(get_md(message.mentions[0]))+"<:makerdollar:686564265217360089>","", message.mentions[0])
            await message.channel.send(embed = embed)
        else:
            cnt=finduser(message.content[4:])
            if cnt == -1:
                await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message.author))
            elif cnt == -2:
                await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message.author))  
            else:
                embed = gnembed(str(get_md(cnt))+"<:makerdollar:686564265217360089>","", cnt)
                await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ지급 "):
        if message.author.id in manager:
            if len(message.mentions) == 1:
                add_md(message.mentions[0], int(message.content[4:].split()[0]))
                embed = gnembed("성공적으로 지급하였습니다.","", message.author)
                await message.channel.send(embed = embed)   
            else:
                cnt=finduser(message.content[4:].split()[1])
                if cnt == -1:
                    await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message.author))
                elif cnt == -2:
                    await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message.author))  
                else:
                    add_md(cnt, int(message.content[4:].split()[0]))
                    embed = gnembed("성공적으로 지급하였습니다.","", message.author)
                    await message.channel.send(embed = embed)    
        else:
            embed = gnembed("매니저가 아닙니다.","", message.author)
            await message.channel.send(embed = embed)   

    if message.content.startswith("ㅁ차감 "):
        if message.author.id in manager:
            if len(message.mentions) == 1:
                add_md(message.mentions[0], -1*int(message.content[4:].split()[0]))
                embed = gnembed("성공적으로 차감하였습니다.","", message.author)
                await message.channel.send(embed = embed)   
            else:
                cnt=finduser(message.content[4:].split()[1])
                if cnt == -1:
                    await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message.author))
                elif cnt == -2:
                    await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message.author))  
                else:
                    add_md(cnt, -1*int(message.content[4:].split()[0]))
                    embed = gnembed("성공적으로 차감하였습니다.","", message.author)
                    await message.channel.send(embed = embed) 
        else:
            embed = gnembed("매니저가 아닙니다.","", message.author)
            await message.channel.send(embed = embed)   

    if message.content.startswith("ㅁ송금 "):
        if int(message.content[4:].split()[0])>0:
            if get_md(message.author) >= int(message.content[4:].split()[0]):
                if len(message.mentions) == 1:
                    add_md(message.mentions[0], int(message.content[4:].split()[0]))
                    add_md(message.author, -1*int(message.content[4:].split()[0]))
                    embed = gnembed("성공적으로 송금하였습니다.","", message.author)
                    await message.channel.send(embed = embed)   
                else:
                    cnt=finduser(message.content[4:].split()[1])
                    if cnt == -1:
                        await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message.author))
                    elif cnt == -2:
                        await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message.author))  
                    else:
                        add_md(cnt, int(message.content[4:].split()[0]))
                        add_md(message.author, -1*int(message.content[4:].split()[0]))
                        embed = gnembed("성공적으로 송금하였습니다.","", message.author)
                        await message.channel.send(embed = embed)    
            else:
                await message.channel.send(embed = gnembed("돈은 0보다 크게 입력해 주세요.", "", message.author))
        else:
            await message.channel.send(embed = gnembed("돈이 부족합니다.",str(int(message.content[4:].split()[0])-get_md(message.author))+"<:makerdollar:686564265217360089>가 더 필요합니다.", message.author))

    if message.content == "ㅁ돈벌기":
        if ablework(message.author):
            cost=random.randint(100,200)
            add_md(message.author,cost)
            worked(message.author)
            embed = gnembed(str(cost)+"<:makerdollar:686564265217360089>를 벌었습니다.","", message.author)
            await message.channel.send(embed = embed)
        else:
            embed = gnembed(str(waitminute(message.author)[0])+"분 "+str(waitminute(message.author)[1])+"초 후에 다시 벌 수 있습니다.","", message.author)
            await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ도박"):
        if ablecas(message.author):
            cost=int(message.content[4:])
            add_md(message.author, -1*cost)
            cast(message.author)
            randomd=10
            if randomd==1:
                add_md(message.author, 3*cost)
                await message.channel.send(embed = gnembed("10%확률로 3배를 돌려받았습니다.","", message.author))
            elif 2<=randomd<=3:
                add_md(message.author, 2*cost)
                await message.channel.send(embed = gnembed("20%확률로 2배를 돌려받았습니다.","", message.author))
            else:
                await message.channel.send(embed = gnembed("70%확률로 돈을 잃었습니다.","", message.author))
        else:
            embed = gnembed(str(caswait(message.author)[0])+"분 "+str(caswait(message.author)[1])+"초 후에 다시 도박할 수 있습니다.","", message.author)
            await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ도둑질"):
        if ablest(message.author):
            if len(message.mentions)>0:
                target=message.mentions[0]
            else:
                target=finduser(message.content[5:])
            if target==-1 or target==-2:
                can = random.randint(1,10)
                st(message.author)
                if 1<=can<=4:
                    cost=random.randint(1,2000)
                    mine=get_md(target)
                    if mine<=cost:
                        embed = gnembed("전 재산인 "+str(mine)+"<:makerdollar:686564265217360089>를 훔쳤습니다.","", message.author)
                        add_md(target, -1*mine)
                        add_md(message.author, mine)
                        await message.channel.send(embed = embed)
                    else:
                        embed = gnembed(str(cost)+"<:makerdollar:686564265217360089>를 훔쳤습니다.","", message.author)
                        add_md(target, -1*cost)
                        add_md(message.author, cost)
                        await message.channel.send(embed = embed)

                elif 5<=can<=7:
                    embed = gnembed("도둑질에 실패하였습니다.","", message.author)
                    await message.channel.send(embed = embed)
                else:
                    mine=get_md(message.author)
                    cost=random.randint(1,2000)
                    if mine<=cost:
                        embed = gnembed("도둑질을 하다 메이커에게 걸려 전 재산인 "+str(mine)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.","", message.author)
                        add_md(message.author, -1*mine)
                        await message.channel.send(embed = embed)
                    else:
                        embed = gnembed("도둑질을 하다 메이커에게 걸려 "+str(cost)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.","", message.author)
                        add_md(message.author, -1*cost)
                        await message.channel.send(embed = embed)
            else:
                embed = gnembed("그런 사람이 없거나 여러명입니다. 멘션으로 해주세요.","", message.author)
                await message.channel.send(embed = embed)
        else:
            embed = gnembed(str(stwait(message.author)[0])+"분 "+str(stwait(message.author)[1])+"초 후에 다시 도둑질할 수 있습니다.","", message.author)
            await message.channel.send(embed = embed)
            
    if message.content == "ㅁ랭킹":
        am=[]
        for x in datab.keys():
            am.append([datab[x][0], x])
        count=min(20, len(datab))
        for x in range(count):
            for y in range(count-1):
                if am[y][0]<am[y+1][0]:
                    z=am[y]
                    am[y]=am[y+1]
                    am[y+1]=z
        strs=""
        for x in range(count):
            strs+=str(x+1)+"위 : "+message.guild.get_member(am[x][1]).display_name+"("+str(am[x][0])+"<:makerdollar:686564265217360089>)\n"
        await message.channel.send(embed = gnembed("랭킹",strs, message.author))

def gnembed(title, description, author):
    embed = discord.Embed(title = title, description = description, color = 0xffcc00, timestamp = datetime.datetime.utcnow())
    embed.set_footer(text = "MDv2", icon_url = app.user.avatar_url)
    embed.set_author(name = author.display_name, icon_url = author.avatar_url)
    return embed
def get_md(user):
    global datab
    if user.id in datab:
        return datab[user.id][0]
    else:
        create_md(user.id)
        return datab[user.id][0]
def add_md(user, money):
    global datab
    if user.id in datab:
        datab[user.id][0]+=money
    else:
        create_md(user.id)
        datab[user.id][0]+=money
def finduser(name):
    cnt, idm = 0, 0
    for guild in app.guilds:
        for member in guild.members:
            if member.display_name.startswith(name):
                if cnt == 0:
                    cnt = 1
                    idm = member.id
                else:
                    return -2
    if cnt == 0:
        return -1
    return app.get_user(idm)
def create_md(idd):
    global datab
    datab[idd]=[]
    datab[idd].append(1000)
    datab[idd].append("no")
    datab[idd].append("no")
    datab[idd].append("no")

def ablework(user):
    global datab
    if datab[user.id][1]=="no":
        return True
    elif datab[user.id][1]+datetime.timedelta(minutes=10)<=datetime.datetime.utcnow()+datetime.timedelta(hours=9):
        return True
    else:
        return False
def worked(user):
    global datab
    datab[user.id][1]=datetime.datetime.utcnow()+datetime.timedelta(hours=9)
def waitminute(user):
    global datab
    a = datab[user.id][1].minute + 10 - datetime.datetime.utcnow().minute
    b = datab[user.id][1].second - datetime.datetime.utcnow().second
    if b<0: a,b=a-1,b+60
    if a<0: a+=60
    return [a,b]

def ablecas(user):
    global datab
    if datab[user.id][2]=="no":
        return True
    elif datab[user.id][2]+datetime.timedelta(minutes=5)<=datetime.datetime.utcnow()+datetime.timedelta(hours=9):
        return True
    else:
        return False
def cast(user):
    global datab
    datab[user.id][2]=datetime.datetime.utcnow()+datetime.timedelta(hours=9)
def caswait(user):
    global datab
    a = datab[user.id][2].minute + 5 - datetime.datetime.utcnow().minute
    b = datab[user.id][2].second - datetime.datetime.utcnow().second
    if b<0: a,b=a-1,b+60
    if a<0: a+=60
    return [a,b]

def ablest(user):
    global datab
    if not(user.id in datab):
        create_md(user.id)
    if datab[user.id][3]=="no":
        return True
    elif datab[user.id][3]+datetime.timedelta(minutes=10)<=datetime.datetime.utcnow()+datetime.timedelta(hours=9):
        return True
    else:
        return False
def st(user):
    global datab
    datab[user.id][3]=datetime.datetime.utcnow()+datetime.timedelta(hours=9)
def stwait(user):
    global datab
    a = datab[user.id][3].minute + 10 - datetime.datetime.utcnow().minute
    b = datab[user.id][3].second - datetime.datetime.utcnow().second
    if b<0: a,b=a-1,b+60
    if a<0: a+=60
    return [a,b]

app.run(os.environ["BOT_TOKEN"])
