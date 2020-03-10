import discord
from datetime import timedelta
import datetime
import random
import os


app = discord.Client()

@app.event
async def on_ready():
    print("Log in to next -> ", end = "")
    print(app.user.name, end = " : ")
    print(app.user.id)
    print("===============")


@app.event
async def on_message(message):
    if message.content == "서버 세팅":
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
        await message.channel.send(str(ax) + "명을 관리 명단에 추가시켰습니다.")

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
                    embed = discord.Embed(title = "5% 확률로 건 돈의 3배를 돌려 받으셨습니다.", color = 0x9966ff, timestamp = datetime.datetime.utcnow())
                    embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
                    embed.set_footer(text = "MD관리봇", icon_url = app.user.avatar_url)
                    await message.channel.send(embed = embed)
                    open(str(message.author.id)+'.makerdollar','w').write(str(has+cost*2))

app.run(os.environ["BOT_TOKEN"])
