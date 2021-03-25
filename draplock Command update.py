import asyncio
import json
import os
import discord
from discord import Guild, TextChannel
from discord.ext import commands

import random
import re

from datetime import datetime, timedelta


bot = commands.Bot(command_prefix='=', intents=discord.Intents.all(), case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    print(f"Wir sind als '{bot.user}' mit der ID {bot.user.id} eingeloggt")



#########################################
if not os.path.isfile("blackliste.json"):
    data = {"blackliste": []}
    with open("blackliste.json", "w") as neu:
        json.dump(data, neu)

@bot.event
async def on_message(message):
    if not message.author.bot:
        ctx = await bot.get_context(message, cls=commands.Context)
        if ctx.command is not None:
            await bot.process_commands(message)
        else:
            content = message.content.lower()
            with open('blackliste.json', "r") as file:
                liste = json.load(file)["blackliste"]
            if liste:
                for i in liste:
                    if i in content:
                        await message.delete()
                        await message.channel.send(f'{message.author.mention}!'
                                                   f'Diese wort Ist __VERBOTEN__!', delete_after=5)
                        break


"""------------------------------------Commands------------------------------------"""


@bot.command(name="add")
async def add(ctx, *, word: str):
    with open("blackliste.json", "r") as f:
        conf = json.load(f)
    if word.lower() in conf["blackliste"]:
        await ctx.channel.send(f"`{word}` ist bereits in der Blacklist.", delete_after=2)
    else:
        conf["blackliste"].append(word.lower())
        with open("blackliste.json", "w") as f:
            json.dump(conf, f)
        await ctx.channel.send(f"`{word}` wurde zu der blacklist geaddet.", delete_after=4)


@bot.command(name="remove")
async def remove(ctx, *, word: str):
    with open("blackliste.json", "r") as f:
        conf = json.load(f)
    if word.lower() in conf["blackliste"]:
        conf["blackliste"].remove(word)
        await ctx.channel.send(f"`{word}` Wurde von der Blacklist entfent.", delete_after=2)
    else:
        await ctx.channel.send(f"`{word}` ist nicht in der Blacklist.", delete_aft
        
@bot.command()
async def pun(ctx):
    witz = ['Herr Doktor ich komm mir so unglaublich überflüssig vor.\n Dr: Der Nächste bitte!',
            'Geht eine schwangere Frau in eine Bäckerei und sagt: "Ich krieg ein Brot." \n Darauf der Bäcker: "Sachen gibts!',
            'Was steht auf dem Grabstein eines Mathematikers? \n "Damit hat er nicht gerechnet."',
            'Wenn ein Yogalehrer seine Beine senkrecht nach oben streckt und dabei furzt, welche Yoga Figur stellt er da? \n Eine Duftkerze',
            'Gestern erzählte ich meinem Freund, dass ich schon immer dieses Ding aus Harry Potter reiten wollte.\n "einen Besen?"\n "nein, Hermine."',
            'Zwei Schnecken unterhalten sich.Sagt die erste Schnecke:\n „Meine Frau hat mich letzten Sommer verlassen. Sie ist einfach zusammen mit den Kindern weggegangen. Und weißt du, was das schlimmste ist?”\nDie zweite Schnecke zuckt mit den Schultern: „Nö, was den?” \n Die erste Schnecke zeigt auf die Straße: „Ich kann sie immer noch in der Kurve sehen."',
            'Was vermisst eine Schraube am meisten? Einen Vater',
            'Der Vater sagt zum Sohn: Sohn, ich muss dir was sagen. Du wurdest adoptiert.\nSagt der Sohn: WAS! Ich will sofort meine echten Eltern kennenlernen.\nDarauf der Vater: Wir sind deine echten Eltern! Und jetzt mach dich fertig, du wirst in 20 Minuten abgeholt.',
            'Geht ein Panda über die Straße. Bam....Bus!Was sagt ein Haifisch, wenn er einen Surfer sieht?\n"Das ist aber nett serviert, so mit Frühstücksbrettchen."',
            'Wie verbrennt man ganz schnell 900 Kalorien?\nIndem man die Pizza im Ofen vergisst.',
            'Was sagt das eine Streichholz zum anderen Streichholz?\nKomm, lass uns durchbrennen',
            'Was macht ein Pirat am Computer?\nEr drückt die Enter-Taste',
            'Was ist grün und steht vor der Tür?\nKlopfsalat',
            'Ich habe einen Joghurt fallen gelassen. Er war nicht mehr haltbar.',
            'Sie: „Und was ist so dein Lieblingsfilm?“\nEr: „Tesafilm ist ein echt guter Streifen.“',
            'Wentler: **Egal**',
            'Zwei Männer in tiefsinnigem Bargespräch.\n"Wenn ich mit deiner Frau schlafe, sind wir dann Feinde?"\n"Nein."\n"Sind wir dann Freunde?"\n"Nein."\n"Was sind wir dann?"\n"Quitt."']
    embed = discord.Embed(title="Witz",
                          description=random.choice(witz),
                          color=0x128c1b)
    embed.set_thumbnail(url="https://media.tenor.com/images/99338a98580194539b4ecbcbc1ade726/tenor.gif")
    await ctx.send(embed=embed)


@bot.command(aliases=['münze', 'flipcoin'])
async def coin(ctx):
    embed = discord.Embed(title="Münze",
                          description='Ich werfe die Münze...',
                          color=0xeebb17)
    mess = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    muenz = [':coin: Ich habe geworfen und es kam: **Kopf**',
             ':coin: Ich habe geworfen und es kam: **Zahl**']
    embed_new = discord.Embed(title="Münze",
                              description=random.choice(muenz),
                              color=0xeebb17)
    await mess.edit(embed=embed_new)


@bot.command()
async def Orakel(ctx, *, question):
    responses = [
        "Es ist sicher.",
        "Es ist entschieden, so.",
        "Ohne Zweifel.",
        "Ja auf jeden Fall.",
        "Sie können sich darauf verlassen.",
        "Das wird nicht so richtig sein.",
        "Auf keinen Fall.",
        "Sie können sich nicht darauf verlassen.",
        "Wäre mir das nicht so sicher."]
    embed = discord.Embed(title="Orakel",
                          description='Ich werde dir es sagen...',
                          color=0xeebb17)
    mess = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    embed = discord.Embed(title="Das Orakel❔",
                          description=f'Frage: `{question}`\nAntwort: `{random.choice(responses)}`',
                          color=ctx.author.color)
    await mess.edit(embed=embed)

######################################

@bot.command(aliases=['start', 'g'])
@commands.has_permissions(manage_guild=True)
async def giveaway(ctx):
    await ctx.send("Wähle den Channel, wo das Giveaway gestartet werden soll.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg1 = await bot.wait_for('message', check=check, timeout=30.0)

        channel_converter = discord.ext.commands.TextChannelConverter()
        try:
            giveawaychannel = await channel_converter.convert(ctx, msg1.content)
        except commands.BadArgument:
            return await ctx.send("Dieser Channel existiert nicht?")

    except asyncio.TimeoutError:
        await ctx.send("Du hast zu lange gebraucht, nächstes mal schneller!")

    if not giveawaychannel.permissions_for(ctx.guild.me).send_messages or not giveawaychannel.permissions_for(
            ctx.guild.me).add_reactions:
        return await ctx.send(
            f"Bot hat nicht die Rechte, um das Giveaway zu machen: {giveawaychannel}\n **Rechte benötigt:** ``Add reactions | Send messages.``")

    await ctx.send("Wie viele Gewinner sollen Gewinnen?")
    try:
        msg2 = await bot.wait_for('message', check=check, timeout=30.0)
        try:
            winerscount = int(msg2.content)
        except ValueError:
            return await ctx.send("Du hast keine Anzahl von Gewinnern angegeben. Bitte versuche es erneut.")

    except asyncio.TimeoutError:
        await ctx.send("Du hast zu lange gebraucht, nächtes mal schneller!")

    await ctx.send("Wie lange soll das Giveaway gehen?")
    try:
        since = await bot.wait_for('message', check=check, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send("Du hast zu lange gebraucht, nächste mal schneller!")

    seconds = ("s", "sec", "secs", 'second', "seconds")
    minutes = ("m", "min", "mins", "minute", "minutes")
    hours = ("h", "hour", "hours")
    days = ("d", "day", "days")
    weeks = ("w", "week", "weeks")
    rawsince = since.content

    try:
        temp = re.compile("([0-9]+)([a-zA-Z]+)")
        if not temp.match(since.content):
            return await ctx.send("Du hast keine Zeiteinheit angegeben. Bitte versuche es erneut.")
        res = temp.match(since.content).groups()
        time = int(res[0])
        since = res[1]

    except ValueError:
        return await ctx.send("Du hast keine Zeiteinheit angegeben. Bitte versuche es erneut.")

    if since.lower() in seconds:
        timewait = time
    elif since.lower() in minutes:
        timewait = time * 60
    elif since.lower() in hours:
        timewait = time * 3600
    elif since.lower() in days:
        timewait = time * 86400
    elif since.lower() in weeks:
        timewait = time * 604800
    else:

        return await ctx.send("Du hast keine Zeiteinheit angegeben. Bitte versuche es erneut.")

    await ctx.send("Wie soll der Preis sein??")
    try:
        msg4 = await bot.wait_for('message', check=check, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.send("Du hast zu lange gebraucht, nächtes mal schneller!")

    futuredate = datetime.utcnow() + timedelta(seconds=timewait)
    embed1 = discord.Embed(color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
                           title=f"🎉GIVEAWAY🎉\n`{msg4.content}`", timestamp=futuredate,
                           description=f'Reagiere mit 🎉 um Teilzunehmen!\nErstellt von: {ctx.author.mention}')

    embed1.set_footer(text=f"Giveaway wird enden")
    msg = await giveawaychannel.send(embed=embed1)
    await msg.add_reaction("🎉")
    await asyncio.sleep(timewait)
    message = await giveawaychannel.fetch_message(msg.id)
    for reaction in message.reactions:
        if str(reaction.emoji) == "🎉":
            users = await reaction.users().flatten()
            if len(users) == 1:
                return await msg.edit(embed=discord.Embed(title="Niemand hat das Giveaway gewonnen."))
    try:
        winners = random.sample([user for user in users if not user.bot], k=winerscount)
    except ValueError:
        return await giveawaychannel.send("Nicht genügend Teilnehmer")
    winnerstosend = "\n".join([winner.mention for winner in winners])

    win = await msg.edit(embed=discord.Embed(title="GEWINNER",
                                             description=f"Herzlichen Glückwunsch {winnerstosend}, du hast **{msg4.content}** gewonnen!",
                                             color=discord.Color.blue()))


# Reroll command, used for chosing a new random winner in the giveaway
@bot.command()
@commands.has_permissions(manage_guild=True)
async def reroll(ctx):
    async for message in ctx.channel.history(limit=100, oldest_first=False):
        if message.author.id == bot.user.id and message.embeds:
            reroll = await ctx.fetch_message(message.id)
            users = await reroll.reactions[0].users().flatten()
            users.pop(users.index(bot.user))
            winner = random.choice(users)
            await ctx.send(f"Der Neue Gewinner ist {winner.mention}")
            break
    else:
        await ctx.send("Hier gibt es keine Giveaways.")

# Umfrage command

@bot.command(name="poll")
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *args):
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="NEUE UMFRAGE",
            description=f"{poll_title}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Umfrage erstellt by: {ctx.message.author} • Reagiere zum voten"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
        
        
#ping command

@bot.command()
async def ping(ctx):
  latency = client.latency
  embed=discord.Embed(description=f':ping_pong: | Der aktuelle ping vom bot ist {round(bot.latency*1000)} ms!', color=0x07edde)
  await ctx.send(embed=embed)
  
  
 #userinfo command
 
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
 
    embed = discord.Embed(title=f"Userinfo von {ctx.author.name}", color=0xeba834)
 
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Angefordert von {ctx.author.name}", icon_url=ctx.author.avatar_url)
 
    embed.add_field(name="Name", value=member, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
 
    if member.bot == True:
        embed.add_field(name="Bot?", value="Ja", inline=True)
    else:
        embed.add_field(name="Bot?", value="Nein", inline=True)
 
    embed.add_field(name=f"Rollen ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=True)
    embed.add_field(name="Höchste Rolle", value=member.top_role.mention, inline=True)
 
    await ctx.message.delete()
    await ctx.send(embed=embed)
    
 
#tempchanel

#servers.json inhalt 

#{

#}

tempchannels = []
admins = [Admin id]


if os.path.isfile("channels.json"):
    with open('channels.json', encoding='utf-8') as f:
        channels = json.load(f)
else:
    channels = {}
    with open('channels.json', 'w') as f:
        json.dump(channels, f, indent=4)


@bot.command(pass_context=True)
async def addtempchannel(ctx, channelid):
    if ctx.author.bot:
        return
    if ctx.author.guild_permissions.administrator:
        if channelid:
            for vc in ctx.guild.voice_channels:
                if vc.id == int(channelid):
                    if str(ctx.channel.guild.id) not in channels:
                        channels[str(ctx.channel.guild.id)] = []
                    channels[str(ctx.channel.guild.id)].append(int(channelid))
                    with open('channels.json', 'w') as f:
                        json.dump(channels, f, indent=4)
                    await ctx.send("{} ist nun ein JoinHub".format(vc.name))
                    return
            await ctx.send("{} ist kein Voicechannel".format(channelid))
        else:
            await ctx.send("Bitte gebe eine ChannelID an")
    else:
        await ctx.send("Du brauchst das Recht Administrator um das zu tun")


@bot.command(pass_context=True)
async def removetempchannel(ctx, channelid):
    if ctx.author.bot:
        return
    if ctx.author.guild_permissions.administrator:
        if channelid:
            guildS = str(ctx.channel.guild.id)
            channelidI = int(channelid)
            for vc in ctx.guild.voice_channels:
                if vc.id == int(channelid):
                    if channels[guildS]:
                        if channelidI in channels[guildS]:
                            channels[guildS].remove(channelidI)
                            with open('channels.json', 'w') as f:
                                json.dump(channels, f, indent=4)
                                await ctx.send("{} ist kein JoinHub mehr".format(vc.name))
                                return
                        else:
                            await ctx.send("Dieser Channel existiert hier nicht")
                            return
            await ctx.send("Du besitzt noch keine JoinHubs")
        else:
            await ctx.send("Keine Channelid angegeben")
    else:
        await ctx.send("Du brauchst das Recht Administrator um das zu tun")


@bot.command(pass_context=True)
async def info(ctx):
    if ctx.author.bot:
        return
    if ctx.author.id in admins:
        membercount = 0
        guildcount = 0
        for guild in client.guilds:
            membercount += guild.member_count
            guildcount += 1
        embed = discord.Embed(title='Informationen', description=f'Der Bot ist derzeit auf {guildcount-1} anderen '
                                                                 f'Servern und sieht {membercount} Members.',
                              color=0xfefefe)
        await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def leave(ctx, serverid):
    if ctx.author.bot:
        return
    if ctx.author.id in admins:
        guild = client.get_guild(serverid)
        if guild:
            await ctx.channel.send(f'{guild.name} geleaved.')
            await guild.leave()
        else:
            await ctx.channel.send(f'Keine Guild mit der ID {serverid} gefunden.')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel:
        if isTempChannel(before.channel):
            bchan = before.channel
            if len(bchan.members) == 0:
                await bchan.delete(reason="No member in tempchannel")
    if after.channel:
        if isJoinHub(after.channel):
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            overwrite.move_members = True
            name = "│⏳ {}".format(member.name)
            output = await after.channel.clone(name=name, reason="Joined in joinhub")
            if output:
                tempchannels.append(output.id)
                await output.set_permissions(member, overwrite=overwrite)
                await member.move_to(output, reason="Created tempvoice")



async def getChannel(guild, name):
    for channel in guild.voice_channels:
        if name in channel.name:
            return channel
    return None


def isJoinHub(channel):
    if channels[str(channel.guild.id)]:
        if channel.id in channels[str(channel.guild.id)]:
            return True
    return False


def isTempChannel(channel):
    if channel.id in tempchannels:
        return True
    else:
        return False
        
        
 #mod zeug
 
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await bot.kick(member)
    await ctx.send(f'{member.mention} Wurde Gekickt für den grund: {reason}')

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} Wurde mit dem Bannhammer Gebannt für den grund: {reason}')


@bot.command()
@commands.has_permissions(ban_members=True)
async def idban(ctx, member, *, reason=None):
    member = await bot.fetch_user(int(member))
    await ctx.guild.ban(member, reason=reason)
    e = discord.Embed(description=f'Username:{member.name} \nUser ID: {member.id}',
                              color=0x0000FF)
    e.set_author(name=f"User wurde idgebant von {ctx.message.author}",
                 icon_url="https://cdn.discordapp.com/attachments/735638856883240970/752595705822183535/730905.png")
    await ctx.send(embed=e)


@bit.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member = None, reason=None):
        if member == None:
            return await ctx.send("**Invalid Syntax:** =softban (user) (reason)`")
        if member.top_role >= ctx.author.top_role:
            await ctx.send(f"⛔ DU kannst **{member}** auf grund deiner rolle.")
            return
        if member.top_role >= ctx.me.top_role:
            await ctx.send("⛔ Meine höchste Rolle ist niedriger oder gleich der höchsten Rolle des Mitglieds.")
        await ctx.guild.ban(member, delete_message_days=5, reason=reason)
        await ctx.guild.unban(member)
        await ctx.send(f"👌 {member.mention} Wurde erfolgreich gesoftbant ")


#-----------------------------------#   

###########################################################

bot.run('Dein Token')
