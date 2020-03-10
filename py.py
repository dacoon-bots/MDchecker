import discord
from datetime import timedelta
import datetime
import random
import os 

helped="""`$지갑` : 현재 내 MD를 확인합니다.
`$지급` <돈> <멘션> : 유저에게 MD를 지급합니다. (메이커만 가능)
`$차감` <돈> <멘션> : 유저에게 MD를 차감합니다. (메이커만 가능)
`$도박` <돈> : 도박을 합니다. 40%확률로 모든 돈을 잃고, 45%확률로 돈을 돌려받고, 10%확률로 2배로 받고, 5%확률로 5배로 받습니다. 100MD 이상 걸 수 있습니다.
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
    if message.content == "$세팅":
        ax = 0
        for guild in app.guilds:
            if guild == message.guild:
                for member in guild.members:
                    if not app.get_user(member.id).bot:
                        try:
                            open(str(member.id)+'.makerdollar', 'r')
                        except:
                            open(str(member.id)+'.makerdollar', 'w').write('1000')
                            ax+=1
        await message.channel.send(str(ax) + "명이 세팅 되었습니다.")

    if message.content == "$지갑":
        embed = discord.Embed(title = "너에겐 " + open(str(message.author.id)+'.makerdollar', 'r').read() + "MD가 있다!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

    if message.content.startswith("$지급"):
        if message.author.id != 493659299609051136:
            embed = discord.Embed(title = "응 메이커만 가능해~", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            if len(message.mentions) != 1:
                embed = discord.Embed(title = "돈을 누구한테 줄지 멘션해 줘!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                try:
                    ti = int(open(str(message.mentions[0].id)+'.makerdollar','r').read())+int(message.content[4:].split(' ')[0])
                except:
                    embed = discord.Embed(title = "뭔가가 잘못됬어...", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                else:
                    open(str(message.mentions[0].id)+'.makerdollar','w').write(str(ti))
                    embed = discord.Embed(title = "지급 완료!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)

    if message.content.startswith("$차감"):
        if message.author.id != 493659299609051136:
            embed = discord.Embed(title = "응 메이커만 가능해~", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            if len(message.mentions) != 1:
                embed = discord.Embed(title = "돈을 누구한테 차감할지 멘션해 줘!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                try:
                    ti = int(open(str(message.mentions[0].id)+'.makerdollar','r').read())-int(message.content[4:].split(' ')[0])
                except:
                    embed = discord.Embed(title = "뭔가가 잘못됬어...", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                else:
                    open(str(message.mentions[0].id)+'.makerdollar','w').write(str(ti))
                    embed = discord.Embed(title = "차감 완료!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)

    if message.content.startswith("$도박"):
        try:
            cost=int(message.content[4:])

        except:
            embed = discord.Embed(title = "값을 입력해 줘!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
            embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
            embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            has=int(open(str(message.author.id)+'.makerdollar', 'r').read())
            if has<cost:
                embed = discord.Embed(title = "돈이 없어요.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            elif cost<100:
                embed = discord.Embed(title = "돈은 100보다 큰 값으로 입력해줘!", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                await message.channel.send(embed = embed)
            else:
                open(str(message.author.id)+'.makerdollar','w').write(str(has-cost))
                d=random.randint(1, 100)
                if 1<=d<=40:
                    embed = discord.Embed(title = "40% 확률로 건 돈을 잃으셨습니다.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                if 41<=d<=85:
                    embed = discord.Embed(title = "45% 확률로 건 돈을 돌려 받으셨습니다.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has))
                if 86<=d<=95:
                    embed = discord.Embed(title = "10% 확률로 건 돈의 2배를 돌려 받으셨습니다.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has+cost))
                if 96<=d<=100:
                    embed = discord.Embed(title = "5% 확률로 건 돈의 5배를 돌려 받으셨습니다.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has+cost*4))

    if message.content == "$도움":
        embed = discord.Embed(title = "명령어가 작동을 안 할시 `$세팅`을 입력해 주세요.", description = helped, color = 0x9966ff, timestamp = datetime.datetime.utcnow())
        embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
        embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
        await message.channel.send(embed = embed)

app.run(os.environ["BOT_TOKEN"])
