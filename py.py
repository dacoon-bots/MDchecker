import discord
import datetime
import os

datab={}

helpdata="""
`ㅁ지갑`
  - 내 <:makerdollar:686564265217360089>를 확인합니다.
`ㅁ지갑 <유저의 서버 별명 또는 멘션>`
  - 다른 사람의 <:makerdollar:686564265217360089>를 확인합니다.
"""
devoldata="""
`ㅁ지급 <액수> <유저의 서버 별명 또는 멘션>`
  - 유저에게 <:makerdollar:686564265217360089>를 지급합니다.
`ㅁ차감 <액수> <유저의 서버 별명 또는 멘션>`
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

    if message.content == "ㅁ지갑":
        embed = gnembed(str(get_md(message.author))+"<:makerdollar:686564265217360089>","", message)
        await message.channel.send(embed = embed)

    elif message.content.startswith("ㅁ지갑 "):
        if len(message.mentions) == 1:
            embed = gnembed(str(get_md(message.mentions[0]))+"<:makerdollar:686564265217360089>","", message)
            await message.channel.send(embed = embed)
        else:
            cnt=finduser(message.content[4:])
            if cnt == -1:
                await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message))
            elif cnt == -2:
                await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message))  
            else:
                embed = gnembed(str(get_md(cnt))+"<:makerdollar:686564265217360089>","", message)
                await message.channel.send(embed = embed)          

    if message.content.startswith("ㅁ지급 "):
        if len(message.mentions) == 1:
            add_md(message.mentions[0], int(message.content[4:].split()[0]))
            embed = gnembed("성공적으로 지급하였습니다.","", message)
            await message.channel.send(embed = embed)   
        else:
            cnt=finduser(message.content[4:].split()[1])
            if cnt == -1:
                await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message))
            elif cnt == -2:
                await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message))  
            else:
                add_md(cnt, int(message.content[4:].split()[0]))
                embed = gnembed("성공적으로 지급하였습니다.","", message)
                await message.channel.send(embed = embed)    

    if message.content.startswith("ㅁ차감 "):
        if len(message.mentions) == 1:
            add_md(message.mentions[0], -1*int(message.content[4:].split()[0]))
            embed = gnembed("성공적으로 차감하였습니다.","", message)
            await message.channel.send(embed = embed)   
        else:
            cnt=finduser(message.content[4:].split()[1])
            if cnt == -1:
                await message.channel.send(embed = gnembed("그 이름의 유저를 찾을 수 없습니다.","", message))
            elif cnt == -2:
                await message.channel.send(embed = gnembed("그 이름의 유저가 여러명 있습니다. 멘션으로 해주세요.","", message))  
            else:
                add_md(cnt, -1*int(message.content[4:].split()[0]))
                embed = gnembed("성공적으로 차감하였습니다.","", message)
                await message.channel.send(embed = embed) 



def gnembed(title, description, message):
    embed = discord.Embed(title = title, description = description, color = 0xffcc00, timestamp = datetime.datetime.utcnow())
    embed.set_footer(text = "MDv2", icon_url = app.user.avatar_url)
    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
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
            if member.display_name == name:
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

app.run(os.environ["BOT_TOKEN"])
