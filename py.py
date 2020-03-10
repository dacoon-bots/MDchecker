import discord
import datetime
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
    if message.content == "MD 세팅":
        ax = 0
        for guild in app.guilds:
            if guild == message.guild:
                for member in guild.members:
                    if not app.get_user(member.id).bot:
                        try:
                            open(str(member.id)+'.makerdollar', 'r')
                        except:
                            open(str(member.id)+'.makerdollar', 'w').write('0')
                            ax+=1
        await message.channel.send(str(ax) + "명을 관리 명단에 추가시켰습니다.")
    if message.content == "내 MD":
        await message.channel.send("니 MD : "+open(str(message.author.id)+'.makerdollar').read())
        
app.run(os.environ["BOT_TOKEN"])
