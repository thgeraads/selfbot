import binascii
import discord
from discord.ext import commands
import clipboard
from googletrans import Translator
import pyttsx3
import time
import zalgoify
import upsidedown
import requests
from gtts import gTTS   
import random
import urllib
# Reddit
import praw
r = praw.Reddit(
    client_id='yu6A-bY5XOQP1A',
    client_secret='VTDFOb27iJ3VGxIZLhUhsJLUO0Q',
    user_agent="zeehondiebot")

translator = Translator()

# bot / selfbot prefixes
bot = commands.Bot(command_prefix = "N/A")
prefix = "%!"

# stuff for regional
forbiddenchar = "1234567890!@#$%^&*(),./<>?;':[]{}-=_+`"
allowedchar = "abcdefghijklmnopqrstuvwxyz1234567890"
convert = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"}

async def regional(msg):
    newstring = ""
    content = msg.content.replace(f"{prefix}regional ", "")
    content = content.replace(" ", "").lower()
    for a in content:
        if a.upper() == "B":
            newstring = newstring + ":b:"
        elif a.upper() == "O":
            newstring = newstring + ":o:"
        else:
            newstring = newstring + f":regional_indicator_{a}:"
        try: 
            int(a)
            newstring = newstring + ":" + convert[a] + ":"
        except:
            pass    
    for b in forbiddenchar:
            if f":regional_indicator_{b}:" in newstring:
                newstring = newstring.replace(f":regional_indicator_{b}:", "")
    await msg.channel.send(newstring)
    await msg.delete()

async def avatar(msg):
    content = msg.content.replace(f"{prefix}avatar ", "")
    if content == "":
        await msg.channel.send(f":robot: {msg.author.mention}'s avatar:\n{msg.author.avatar_url}")
        await msg.delete()
    else:
        user = msg.mentions[0]
        await msg.delete()
        await msg.channel.send(f":robot: {user.mention}'s avatar:\n{user.avatar_url}")
    
        
            
    
async def userinfo(msg):
    await msg.channel.send(f":robot: Username: {msg.author.name}#{msg.author.discriminator}\nServer nickname: {msg.author.mention}\nAccount created on: {msg.author.created_at}\nAvatar: {msg.author.avatar_as(size=256)}")    
    await msg.delete()
    
async def guilds(msg):
    guildstring = ""
    for guilds in bot.guilds:
        guildstring = guildstring + f"{guilds.name}\n"
    await msg.channel.send(guildstring)
    
async def emote(msg):
    emotename = msg.content.replace(f"{prefix}emote ", "")
    for guilds in bot.guilds:
        for emote in guilds.emojis:
            if emote.name == emotename:
               await msg.channel.send(f"{emote.url}")
               await msg.delete()
               return
            else:
                pass
    await msg.channel.send(":robot: Emote not found.")
    
async def calc(msg):
    eq = msg.content.replace(f"{prefix}calc ", "")
    ans = eval(eq)
    await msg.channel.send(f":robot: {eq} = {ans}")
    await msg.delete()
    
async def translate(msg):
    try:
        pre = msg.content.replace(f"{prefix}translate ", "")
        toLang = pre.split(" ")[0]
        toText = pre[3:]
        post = translator.translate(toText, dest=toLang)
        await msg.channel.send(f":robot: {post.text}")
        await msg.delete()
    except:
        await msg.channel.send(":robot: Something went wrong translating, try again.")
        await msg.delete()
        
async def clap(msg):
    content = msg.content.replace(f"{prefix}clap ", "")
    await msg.channel.send(content.replace(" ", ":clap:"))
    await msg.delete()
    
async def sound(msg):
    engine = pyttsx3.init()
    engine.setProperty('rate', 3000)
    ctx = await bot.get_context(msg)
    voice_client = msg.author.voice.channel
    vc = await voice_client.connect()
    
    
    await msg.delete()
    if msg.content.replace(f"{prefix}sound ", "") == "whiff":
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="./sounds/whiff.mp3"))
        time.sleep(5)
        await msg.channel.send(":weary: 'k ill have a whiff.")
        await vc.disconnect()
    elif msg.content.replace(f"{prefix}sound ", "") == "pussy":
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="./sounds/pussy.mp3"))
        time.sleep(7)
        await msg.channel.send(":cat: Ow, my pussy!")
        await vc.disconnect()
    elif msg.content.replace(f"{prefix}sound ", "") == "sorting":
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="./sounds/sorting.mp3"))
        time.sleep(2)
        await msg.channel.send(":ok_hand: i got that blELUElUEBUELiUEELiiUEiLEiULUBElUiEB")
        await vc.disconnect()


async def zalgo(msg):
    content = msg.content.replace(f"{prefix}zalgo ", "")
    await msg.delete()
    await msg.channel.send(zalgoify.process(content))
        

async def flip(msg):
    content = msg.content.replace(f"{prefix}flip ", "")
    if content.startswith("upsidedown"):
        await msg.delete()
        await msg.channel.send(upsidedown.transform(content.replace("upsidedown", "")))
    elif content.startswith("reverse"):
        await msg.delete()
        await msg.channel.send(content.replace("reverse", "")[::-1])
        
async def stealavatar(msg):
    await msg.delete()
    url = msg.author.avatar_url
    getAvatar = requests.get(url)
    open("./avatar/current.png", "wb").write(getAvatar.content)
    try:
        content = msg.content.replace(f"{prefix}stealavatar ", "")
        user = bot.get_user(content.replace("<@", "").replace(">", ""))
        member = msg.mentions[0]
        url = member.avatar_url
        getAvatar = requests.get(url)
        open("avatar.png", "wb").write(getAvatar.content)
    except:
        msg.channel.send(":robot: Something went wrong getting the users avatar. Try again.")
    test = open("avatar.png")
    bruh = open("avatar.png", "rb").read()
    await bot.user.edit(password="<password>", avatar=bruh)
    
async def restore(msg):
    restore = open("./avatar/current.png", "rb").read()
    await bot.user.edit(password="<password>", avatar=restore)
    
async def inshallah(msg):
    await msg.delete()
    await msg.channel.send("https://cdn.discordapp.com/attachments/764225931644502026/768108721875583006/tenor.gif")


async def reddit(msg):
    import datetime
    """Fetch a random post from a subreddit. Usage: ?reddit <sub>"""
    subname = msg.content.replace(f"{prefix}reddit ", "")

    submission = r.subreddit(f"{subname}").random()
    posttime = submission.created_utc
    realtime = datetime.datetime.utcfromtimestamp(
        posttime).strftime('%Y-%m-%d %H:%M:%S')
    redditembed = discord.Embed(
        title=submission.title,
        url=submission.url,
        color=0x7ac5c9)
    redditembed.set_image(url=submission.url)
    redditembed.set_footer(text="r/" + subname + " | " + realtime)
    await msg.channel.send(embed=redditembed)
    await msg.delete()

    
    
    # await msg.channel.send("This subreddit might be private or non-existant.")
    
async def tts(msg):
    speechtext = msg.content.replace(f"{prefix}tts ", "")
    engine = pyttsx3.init()
    engine.setProperty('rate', 89000)
    theText = speechtext
    tts = gTTS(text=theText, lang='en')
    tts.save("./sounds/audio_out.mp3")
    with open("./sounds/audio_out.mp3", "rb") as fp:
        audio = discord.File(fp, filename="tts.mp3")
    await msg.channel.send(file=audio)
    await msg.delete()
    
async def r34call(msg):
    import os
    if os.path.isfile('./image/porn.jpg'):
        os.remove('./image/porn.jpg')
    terms = msg.content.replace(f"{prefix}r34 ", "")
    base_url = "https://r34-json-api.herokuapp.com/posts?limit=100"
    complete_url = base_url + "&tags=" + str(terms)
    try:
        response = requests.get(complete_url)
    except BaseException:
        msg.channel.send(":robot: Something went wrong.")
    res = response.json()
    number = random.randint(0, 100)
    image = res[number]["file_url"]
    url = image
    urllib.request.urlretrieve(url, './image/porn.jpg')
    
    with open("./image/porn.jpg", "rb") as fp:
        porn = discord.File(fp, "porn.jpg")
        fp.close()
    await msg.channel.send(file=porn)
    await msg.delete()
    

    
@bot.event
async def on_message(msg):
    if msg.author.id == 464733215903580160:
        if msg.content.startswith(f"{prefix}regional"):
            await regional(msg)
        elif msg.content.startswith(f"{prefix}avatar"):
            await avatar(msg)
        elif msg.content.startswith(f"{prefix}userinfo"):
            await userinfo(msg)
        elif msg.content.startswith(f"{prefix}guilds"):
            await guilds(msg)
        elif msg.content.startswith(f"{prefix}emote"):
            await emote(msg)
        elif msg.content.startswith(f"{prefix}calc"):
            await calc(msg)
        elif msg.content.startswith(f"{prefix}translate"):
            await translate(msg)
        elif msg.content.startswith(f"{prefix}clap"):
            await clap(msg)
        elif msg.content.startswith(f"{prefix}caps"):
            await caps(msg)          
        elif msg.content.startswith(f"{prefix}sound"):
            await sound(msg)
        elif msg.content.startswith(f"{prefix}zalgo"):
            await zalgo(msg)
        elif msg.content.startswith(f"{prefix}flip"):
            await flip(msg)
        elif msg.content.startswith(f"{prefix}stealavatar"):
            await stealavatar(msg)
        elif msg.content.startswith(f"{prefix}restore"):
            await restore(msg)
        elif msg.content.startswith(f"{prefix}inshallah"):
            await inshallah(msg)
        elif msg.content.startswith(f"{prefix}tts"):
            await tts(msg)
        
        elif msg.content.startswith(f"{prefix}reddit"):
            await reddit(msg)
        elif msg.content.startswith(f"{prefix}r34"):
            await r34call(msg)
        elif msg.content.startswith(f"{prefix}"):
            await msg.channel.send(":robot: Command not found.")
            
bot.run("<token>", bot = False)