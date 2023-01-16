import discord
import random

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("The bot is ready")
    print("------------------------")
    

@client.event
async def on_message(message):
    #kui bot ise kirjutas
    if message.author == client.user:
        return

    if "!hello" in message.content:
        await message.channel.send('Hello!')

    if "!anime" in message.content:
        await message.channel.send("https://myanimelist.net/animelist/sttellage")
    
    if "moshi" in message.content:
        await message.channel.send("Kas te räägite must taga? :(")

    if "!kivi" in message.content:
        kaigud = ["kivi", "paber", "kaarid"]
        kaik = random.choice(kaigud)

        if kaik == "kivi":
            await message.channel.send(kaik)
            await message.channel.send("Viik!\nwow okei, proovime uuesti")
            
        elif kaik == "paber":
            await message.channel.send(kaik)
            await message.channel.send("Minu võit! hehe ez :3")

        elif kaik == "kaarid":
            await message.channel.send(kaik)
            await message.channel.send("Sina võitsid!!\nok, teeme veel ühe")

    if "!paber" in message.content:
        kaigud = ["kivi", "paber", "kaarid"]
        kaik = random.choice(kaigud)

        if kaik == "paber":
            await message.channel.send(kaik)
            await message.channel.send("Viik!\nwow okei, proovime uuesti")

        elif kaik == "kivi":
            await message.channel.send(kaik)
            await message.channel.send("Sina võitsid?!\nmh, teeme best out of five!")

        elif kaik == "kaarid":
            await message.channel.send(kaik)
            await message.channel.send("Minu võit! gg ez")

    if "!käärid" in message.content:
        kaigud = ["kivi", "paber", "kaarid"]
        kaik = random.choice(kaigud)

        if kaik == "paber":
            await message.channel.send(kaik)
            await message.channel.send("Sina võitsid!? ära loe mu mõtteid :c")

        elif kaik == "kaarid":
            await message.channel.send(kaik)
            await message.channel.send("Viik! Peame veel ühe tegema!")

        elif kaik == "kivi":
            await message.channel.send(kaik)
            await message.channel.send("Minu võit! get good, kid")

client.run("MTA2NDI2MDU5MTg3MjY1NTM4MQ.GrRm72.zl8nPSBFNpI8RB3I-aWggvhtWpRBGu2222mSj0")

