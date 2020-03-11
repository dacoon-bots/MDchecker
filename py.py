import discord
from datetime import timedelta
import datetime
import random
import os

helped="""`ㅁ지갑` : 현재 내 MD를 확인합니다.
`ㅁ지갑 <멘션>` : 유저의 MD를 확인합니다.
`ㅁ지급 <돈> <멘션> `: 유저에게 MD를 지급합니다. (메이커만 가능)
`ㅁ차감 <돈> <멘션>` : 유저에게 MD를 차감합니다. (메이커만 가능)
`ㅁ도박 <돈>` : 도박을 합니다. 45% 확률로 돈을 돌려받고, 40% 확률로 모든 돈을 잃고, 10% 확률로 2배로 받고, 5% 확률로 5배로 받습니다. 100MD 이상 걸 수 있습니다.
`ㅁ송금 <돈> <멘션>` : 유저에게 MD를 보냅니다.
`ㅁ돈벌기` : 1시간마다 사용할 수 있으며 1000<:makerdollar:686564265217360089>~2000<:makerdollar:686564265217360089>를 법니다.
`ㅁ출석체크` : 하루에 한번 1000<:makerdollar:686564265217360089>를 받습니다.
`ㅁ도둑질 <멘션>` : 40% 확률로 1<:makerdollar:686564265217360089>~1000<:makerdollar:686564265217360089>를 훔쳐오고 60% 의 확률로 1<:makerdollar:686564265217360089>~1000<:makerdollar:686564265217360089>를 벌금으로 냅니다.
`ㅁ랭킹` : <:makerdollar:686564265217360089>를 많이 가진 순서대로 1위부터 20위까지 나열합니다.
"""

app = discord.Client()

@app.event
async def on_ready():
    print("Log in to next -> ", end = "")
    print(app.user.name, end = " : ")
    print(app.user.id)
    print("===============")


@app.event
async def on_message(message):
    if message.content == "ㅁ세팅":
        ax = 0
        for guild in app.guilds:
            if guild == message.guild:
                for member in guild.members:
                    if not app.get_user(member.id).bot:
                        try:
                            open(str(member.id)+'.makerdollar', 'r')
                        except:
                            open(str(member.id)+'.makerdollar', 'w').write('1000')
                            open(str(member.id)+'.work', 'w').write('nowork')
                            open(str(member.id)+'.check', 'w').write('nocheck')
                            open(str(member.id)+'.steal', 'w').write('nosteal')
                            open('list.txt', 'a').writelines("\n"+str(member.id))
                            ax+=1
        await message.channel.send(str(ax) + "명이 세팅 되었습니다.")

    if message.content == "ㅁ지갑":
        embed = discord.Embed(title = open(str(message.author.id)+'.makerdollar', 'r').read() + "<:makerdollar:686564265217360089>", color = 0xffc830, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

    elif message.content.startswith("ㅁ지갑"):
        embed = discord.Embed(title = open(str(message.mentions[0].id)+'.makerdollar', 'r').read() + "<:makerdollar:686564265217360089>", color = 0xffc830, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.mentions[0].display_name, icon_url = message.mentions[0].avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ지급"):
        if message.author.id != 493659299609051136:
            embed = discord.Embed(title = "메이커만 사용 가능합니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            if len(message.mentions) != 1:
                embed = discord.Embed(title = "멘션을 해주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                try:
                    ti = int(open(str(message.mentions[0].id)+'.makerdollar','r').read())+int(message.content[4:].split(' ')[0])
                except:
                    embed = discord.Embed(title = "얼마를 지급할지 입력해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                else:
                    open(str(message.mentions[0].id)+'.makerdollar','w').write(str(ti))
                    embed = discord.Embed(title = "지급 완료!", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ차감"):
        if message.author.id != 493659299609051136:
            embed = discord.Embed(title = "메이커만 사용 가능합니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            if len(message.mentions) != 1:
                embed = discord.Embed(title = "멘션을 해주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                try:
                    ti = int(open(str(message.mentions[0].id)+'.makerdollar','r').read())-int(message.content[4:].split(' ')[0])
                except:
                    embed = discord.Embed(title = "얼마를 차감할지 입력해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                else:
                    open(str(message.mentions[0].id)+'.makerdollar','w').write(str(ti))
                    embed = discord.Embed(title = "차감 완료!", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ도박"):
        try:
            cost=int(message.content[4:])
        except:
            embed = discord.Embed(title = "돈을 입력해주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            has=int(open(str(message.author.id)+'.makerdollar', 'r').read())
            if has<cost:
                embed = discord.Embed(title = "돈이 없어요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            elif cost<100:
                embed = discord.Embed(title = "돈은 100보다 큰 값으로 입력해주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                open(str(message.author.id)+'.makerdollar','w').write(str(has-cost))
                d=random.randint(1, 100)
                if 1<=d<=40:
                    embed = discord.Embed(title = "40% 확률로 건 돈을 잃으셨습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                if 41<=d<=85:
                    embed = discord.Embed(title = "45% 확률로 건 돈을 돌려 받으셨습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has))
                if 86<=d<=95:
                    embed = discord.Embed(title = "10% 확률로 건 돈의 2배를 돌려 받으셨습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has+cost))
                if 96<=d<=100:
                    embed = discord.Embed(title = "5% 확률로 건 돈의 5배를 돌려 받으셨습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has+cost*4))

    if message.content == "ㅁ도움":
        embed = discord.Embed(title = "명령어가 작동을 안 할시 `ㅁ세팅`을 입력해 주세요.", description = helped, color = 0xffc830, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ송금"):
        try:
            cost=int(message.content[4:].split(' ')[0])
        except:
            embed = discord.Embed(title = "얼마를 보낼 지 입력해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            has=int(open(str(message.author.id)+'.makerdollar', 'r').read())
            if has<cost:
                embed = discord.Embed(title = "돈이 없어요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            elif cost<0:
                if has<cost:
                    embed = discord.Embed(title = "0MD보다 큰 금액만 보낼 수 있습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
            else:
                open(str(message.author.id)+'.makerdollar', 'w').write(str(has-cost))
                z=str(int(open(str(message.mentions[0].id)+'.makerdollar', 'r').read())+cost)
                open(str(message.mentions[0].id)+'.makerdollar', 'w').write(z)
                embed = discord.Embed(title = "송금 했습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)

    if message.content == "ㅁ돈벌기":
        worked=open(str(message.author.id)+'.work').read()
        if worked=="nowork":
            mon=random.randint(1000, 2000)
            has=int(open(str(message.author.id)+'.makerdollar','r').read())
            open(str(message.author.id)+'.makerdollar','w').write(str(has+mon))
            time=datetime.datetime.now()
            haha=str(time.year)+' '+str(time.month)+' '+str(time.day)+' '+str(time.hour)+' '+str(time.minute)+' '+str(time.second)
            open(str(message.author.id)+'.work','w').write(haha)
            embed = discord.Embed(title = "일을 해서 "+str(mon)+"<:makerdollar:686564265217360089>를 벌었습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            timf=worked.split(' ')
            tim=[]
            for x in range(len(timf)):
                tim.append(int(timf[x]))
            if datetime.datetime.utcnow()+timedelta(hours=9)>=datetime.datetime(year=tim[0],month=tim[1],day=tim[2],hour=tim[3],minute=tim[4],second=tim[5])+timedelta(hours=1):
                mon=random.randint(20, 100)
                has=int(open(str(message.author.id)+'.makerdollar','r').read())
                open(str(message.author.id)+'.makerdollar','w').write(str(has+mon))
                time=datetime.datetime.utcnow()+timedelta(hours=9)
                haha=str(time.year)+' '+str(time.month)+' '+str(time.day)+' '+str(time.hour)+' '+str(time.minute)+' '+str(time.second)
                open(str(message.author.id)+'.work','w').write(haha)
                embed = discord.Embed(title = "일을 해서 "+str(mon)+"MD를 벌었습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                timd=datetime.datetime(year=tim[0],month=tim[1],day=tim[2],hour=tim[3],minute=tim[4],second=tim[5])+datetime.timedelta(hours=1)
                embed = discord.Embed(title = str(timd.month)+'월 '+str(timd.day)+'일 '+str(timd.hour)+'시 '+str(timd.minute)+'분 '+str(timd.second)+'초 부터 일을 할 수 있습니다.', color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)

    if message.content == "ㅁ출석체크":
        checked = open(str(message.author.id)+'.check', 'r').read()
        time=datetime.datetime.utcnow()+timedelta(hours=9)
        if checked=="nocheck":
            has=int(open(str(message.author.id)+'.makerdollar','r').read())
            open(str(message.author.id)+'.makerdollar','w').write(str(has+1000))
            haha=str(time.year)+' '+str(time.month)+' '+str(time.day)
            open(str(message.author.id)+'.check','w').write(haha)
            embed = discord.Embed(title = "출석체크를 해서 1000<:makerdollar:686564265217360089>를 벌었습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        elif int(checked.split()[0])==time.year and int(checked.split()[1])==time.month and int(checked.split()[2])==time.day:
            embed = discord.Embed(title = "내일 다시 시도해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            has=int(open(str(message.author.id)+'.makerdollar','r').read())
            open(str(message.author.id)+'.makerdollar','w').write(str(has+1000))
            haha=str(time.year)+' '+str(time.month)+' '+str(time.day)
            open(str(message.author.id)+'.check','w').write(haha)
            embed = discord.Embed(title = "출석체크를 해서 1000<:makerdollar:686564265217360089>를 벌었습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)

    if message.content.startswith("ㅁ도둑질"):
        stole=open(str(message.author.id)+'.steal','r').read()
        time=datetime.datetime.utcnow()+timedelta(hours=9)
       
        if stole=="nosteal":
            haha=str(time.year)+' '+str(time.month)+' '+str(time.day)+' '+str(time.hour)+' '+str(time.minute)+' '+str(time.second)
            open(str(message.author.id)+'.steal','w').write(haha)
            if len(message.mentions)==1:
                goed=random.randint(1,5)
                cost=random.randint(1, 1000)
                if goed<=2:
                    hasb=int(open(str(message.mentions[0].id)+'.makerdollar','r').read())
                    if cost>=hasb:
                        embed = discord.Embed(title = "상대방의 전 재산인 "+str(hasb)+"<:makerdollar:686564265217360089>를 훔쳐 버렸습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                        await message.channel.send(embed = embed)
                        open(str(message.mentions[0].id)+'.makerdollar','w').write('0')
                        hasg=int(open(str(message.author.id)+'.makerdollar','r').read())+hasb
                        open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
                    else:
                        embed = discord.Embed(title = str(cost)+"<:makerdollar:686564265217360089>를 훔쳐 버렸습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                        await message.channel.send(embed = embed)
                        hasg=int(open(str(message.mentions[0].id)+'.makerdollar','r').read())-cost
                        open(str(message.mentions[0].id)+'.makerdollar','w').write(str(hasg))
                        hasg=int(open(str(message.author.id)+'.makerdollar','r').read())+cost
                        open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
                else:
                    hasb=int(open(str(message.author.id)+'.makerdollar','r').read())
                    if cost>=hasb:
                        embed = discord.Embed(title = str(random.randint(1, 1000))+"<:makerdollar:686564265217360089>를 훔치려다 메이커에게 걸려 전 재산인 "+str(hasb)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                        await message.channel.send(embed = embed)
                        open(str(message.author.id)+'.makerdollar','w').write("0")
                    else:
                        embed = discord.Embed(title = str(random.randint(1, 1000))+"<:makerdollar:686564265217360089>를 훔치려다 메이커에게 걸려 "+str(cost)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                        await message.channel.send(embed = embed)
                        hasg=int(open(str(message.author.id)+'.makerdollar','r').read())-cost
                        open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
            else:
                embed = discord.Embed(title = "도둑질할 사람을 멘션해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
        else:
            tim=stole.split()
            timd=datetime.datetime(year=int(tim[0]),month=int(tim[1]),day=int(tim[2]),hour=int(tim[3]),minute=int(tim[4]),second=int(tim[5]))+datetime.timedelta(minutes=10)
            if timd<=datetime.datetime.utcnow()+timedelta(hours=9):
                haha=str(time.year)+' '+str(time.month)+' '+str(time.day)+' '+str(time.hour)+' '+str(time.minute)+' '+str(time.second)
                open(str(message.author.id)+'.steal','w').write(haha)
                if len(message.mentions)==1:
                    goed=random.randint(1,5)
                    cost=random.randint(1, 1000)
                    if goed<=2:
                        hasb=int(open(str(message.mentions[0].id)+'.makerdollar','r').read())
                        if cost>=hasb:
                            embed = discord.Embed(title = "상대방의 전 재산인 "+str(hasb)+"<:makerdollar:686564265217360089>를 훔쳐 버렸습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                            await message.channel.send(embed = embed)
                            open(str(message.mentions[0].id)+'.makerdollar','w').write('0')
                            hasg=int(open(str(message.author.id)+'.makerdollar','r').read())+hasb
                            open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
                        else:
                            embed = discord.Embed(title = str(cost)+"<:makerdollar:686564265217360089>를 훔쳐 버렸습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                            await message.channel.send(embed = embed)
                            hasg=int(open(str(message.mentions[0].id)+'.makerdollar','r').read())-cost
                            open(str(message.mentions[0].id)+'.makerdollar','w').write(str(hasg))
                            hasg=int(open(str(message.author.id)+'.makerdollar','r').read())+cost
                            open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
                    else:
                        hasb=int(open(str(message.author.id)+'.makerdollar','r').read())
                        if cost>=hasb:
                            embed = discord.Embed(title = str(random.randint(1, 1000))+"<:makerdollar:686564265217360089>를 훔치려다 메이커에게 걸려 전 재산인 "+str(hasb)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                            await message.channel.send(embed = embed)
                            open(str(message.author.id)+'.makerdollar','w').write("0")
                        else:
                            embed = discord.Embed(title = str(random.randint(1, 1000))+"<:makerdollar:686564265217360089>를 훔치려다 메이커에게 걸려 "+str(cost)+"<:makerdollar:686564265217360089>를 벌금으로 냈습니다.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                            await message.channel.send(embed = embed)
                            hasg=int(open(str(message.author.id)+'.makerdollar','r').read())-cost
                            open(str(message.author.id)+'.makerdollar','w').write(str(hasg))
                else:
                    embed = discord.Embed(title = "도둑질할 사람을 멘션해 주세요.", color = 0xffc830, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(title = str(timd.month)+'월 '+str(timd.day)+'일 '+str(timd.hour)+'시 '+str(timd.minute)+'분 '+str(timd.second)+'초 부터 도둑질을 할 수 있습니다.', color = 0xffc830, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)

    if message.content == "ㅁ랭킹":
        lists=open('list.txt','r').read().split('\n')
        del(lists[0])
        listed=[]
        for x in lists:
            listed.append([int(x), int(open(x+'.makerdollar','r').read())])
        for x in range(len(listed)):
            for y in range(len(listed)-1):
                if listed[y][1]<listed[y+1][1]:
                    a=listed[y]
                    listed[y]=listed[y+1]
                    listed[y+1]=a
        strs=""
        for x in range(min(20,len(listed))):
            strs+=str(x+1)+"위 : "+app.get_user(int(listed[x][0])).display_name+"("+str(listed[x][1])+"<:makerdollar:686564265217360089>)\n"
        embed = discord.Embed(title = "1위부터 20위까지의 순위입니다.", description=strs, color = 0xffc830, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

app.run(os.environ["BOT_TOKEN"])
