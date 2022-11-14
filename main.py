import discord
from discord.ext import commands
import sys
import json
import os

client = commands.Bot(command_prefix="nft!")
client.remove_command("help")

@client.event
async def on_ready():
    data = read_json("punishment")
    client.punishments = data["ActivePunishmentS"]
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="NFT Advertisements"))
    print("Bot is Ready to Stop Some NFT Advertisements")

@client.event
async def on_message(message):
    member = message.author
    msg = message.content
    if message.author.bot:
        return
    if any(word in msg for word in blacklist):
        if message.guild.id in client.punishments:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: NFT Website.', inline=False)
            embed.set_footer(text="Punishment has been enables so the user has been banned")
            await message.channel.send(embed=embed)
            await message.delete()
            await message.author.ban(reason="[Auto by Anti-NFT Bot] NFT Advertisements")
            return
        else:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: NFT Website.', inline=False)
            await message.channel.send(embed=embed)
            await message.delete()
            return
    if any(word in msg for word in blacklist2):
        if message.guild.id in client.punishments:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"Hey {member.mention}, it seems like you are attempting to advertise a NFT based discord server. Well this server is protected by Anti-NFT Bot. Look at nft!nfttruth to find out the truth on NFTs", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: Discord Server', inline=False)
            embed.set_footer(text="If you are the owner of the server and believe this is a mistake and is Anti-NFT or not NFT based, contact the owner in our support server to appeal. (Avaliable in nft!info)")
            embed.set_footer(text="Punishment has been enables so the user has been banned")
            await message.channel.send(embed=embed)
            await message.delete()
            await message.author.ban(reason="[Auto by Anti-NFT Bot] NFT Advertisements")
            return
        else:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"Hey {member.mention}, it seems like you are attempting to advertise a NFT based discord server. Well this server is protected by Anti-NFT Bot. Look at nft!nfttruth to find out the truth on NFTs", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: Discord Server', inline=False)
            embed.set_footer(text="If you are the owner of the server and believe this is a mistake and is Anti-NFT or not NFT based, contact the owner in our support server to appeal. (Avaliable in nft!info)")
            await message.channel.send(embed=embed)
            await message.delete()
            return
    if any(word in msg for word in blacklist3):
        if message.guild.id in client.punishments:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: NFT Website.', inline=False)
            embed.set_footer(text="Punishment has been enables so the user has been banned")
            await message.channel.send(embed=embed)
            await message.delete()
            await message.author.ban(reason="[Auto by Anti-NFT Bot] NFT Advertisements")
            return
        else:
            embed = discord.Embed(title="NO NFT ADVERTISEMENTS ALLOWED", description=f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth", color=(40959))
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: NFT Website.', inline=False)
            await message.channel.send(embed=embed)
            await message.delete()
            return

    await client.process_commands(message)





@client.command()
async def help(ctx):
    embed = discord.Embed(title="Anti-Idiot Bot", description="Here is my entire Commands List", color=(40959))
    embed.add_field(name="GENERAL COMMANDS", value='nft!help - This message\nnft!ping - Checks my Latency\nnft!info - Information about the Bot\nnft!userinfo - Get information on a user to detect idiot status.\nnft!debug - See the settings enabled for your server.', inline=False)
    embed.add_field(name="ANTI-NFT", value='nft!nfttruth - Tells you the truth about NFTs\nnft!whatisanft - I share what a NFT is from Urban Dictionary', inline=False)
    embed.add_field(name="SETTINGS", value='nft!antinftenable - Enable the Anti-NFT system\nnft!antinftdisable - Disable the Anti-NFT system\nnft!antiidiotenable - If Idiots join your server, they will be banned\nnft!antiidiotdisable - Disables the Anti-Idiot System.\nnft!punishenable - Allow the bot to start banning members who sends NFT ad.\nnft!punishdisable - Disables the Punishment System.\nnft!setlogschannel - Set where you want the bot to send its logs too', inline=False)
    embed.add_field(name="DEVELOPER-ONLY COMMANDS", value='nft!restart - Reboots the bot and loads in the new commands/content.\nnft!watchstatus - Changes bot status to a watchstatus\nnft!listenstatus - Changes bot status to a Listening status\nnft!playstatus - Changes bot status to a playing status', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My Latency is: {round(client.latency * 1000)}ms')

@client.command()
async def info(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot", description="Information about the Anti-NFT discord bot.", color=(40959))
    embed.add_field(name="GENERAL", value='CREATOR: Idiot Creature Hater#2255', inline=False)
    embed.add_field(name="LINKS", value='Invite me: https://discord.com/api/oauth2/authorize?client_id=985998562573832262&permissions=1374390971590&scope=bot\nSupport Server: https://discord.gg/xTfAYs7Kyg\nSource Code: https://github.com/BadUserHater/AntiNFTBot', inline=False)
    embed.add_field(name="CREDITS/SOURCE", value='Orignal Creator: Idiot Creature Hater#2255\nOpen Source?: TRUE\nLicense: MIT\nSource Code: https://github.com/BadUserHater/AntiNFTBot', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def privacy(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot Privacy Policy", description="Last updated: July 23, 2022", color=(40959))
    embed.add_field(name="WHAT DATA DO YOU COLLECT", value='Anti-NFT Bot does not store any data by default, however if you use **nft!punishenable**, your server ID will be collected.', inline=False)
    embed.add_field(name="WHY IS THIS DATA NEEDED?", value='The data is needed so the bot knows if a member should be punished if they send a NFT Advertisement in your server.', inline=False)
    embed.add_field(name="HOW DO I REMOVE MY DATA?", value='To remove the server ID it collected, then execute **nft!punishdisable**. If you kick the bot before doing this, then please reach out to the owner of the bot to remove your data.', inline=False)
    embed.add_field(name="HOW MAY I CONTACT YOU FOR CONCERNS", value='Reach to use at our support server at: https://discord.gg/NpRbKaFmJU', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command()
async def nfttruth(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot", description="Here is the truth about NFTs", color=(40959))
    embed.add_field(name="NFTs IS CAUSING HARM TO THE ENVIRONMENT", value='NFTs are making a bad impact to the world. Learn more about the truth of NFTs here: https://rickorford.com/8-reasons-to-not-invest-in-nfts/', inline=False)
    await ctx.send(embed=embed)





@client.command()
@commands.has_permissions(administrator=True)
@commands.bot_has_permissions(ban_members=True)
async def punishenable(ctx):
    client.punishments.append(ctx.guild.id)
    data = read_json("punishment")
    data["ActivePunishmentS"].append(ctx.guild.id)
    write_json(data, "punishment")
    await ctx.send("The Punishment Module has been enabled. I will **now start** banning members if they send a NFT advertisement in this server")

@client.command()
@commands.has_permissions(administrator=True)
async def punishdisable(ctx):
    client.punishments.remove(ctx.guild.id)
    data = read_json("punishment")
    data["ActivePunishmentS"].remove(ctx.guild.id)
    write_json(data, "punishment")
    await ctx.send("The Punishment Module has been **disabled**. I will **no longer be** banning members if they send a NFT advertisement in this server")

@punishenable.error
async def punishenable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry but you need the **Administrator** permission to use this command')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Sorry but I need the **Ban Members** permission for this function to work.")
    else:
        raise error

@punishdisable.error
async def punishdisable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry but you need the **Administrator** permission to use this command')
    else:
        raise error

def read_json(filename):
    with open(f"./punishment.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"./punishment.json", "w") as file:
        json.dump(data, file, indent=4)

blacklist = ["crypto.com/nft", "opensea.io", "niftygateway.com", "launchmynft.co", "jump.trade", "rarible.com", "binance.com", "superrare.com", "async.art", "knownorigin.io", "blockchainappfactory.com", "eggheadz.io", "mee6.xyz/nft", "renewable-earth.club", "mother-nature.nft", "filab.io", "www.odysseydao.com", "theredapefamily.com", "orcania.io", "www.atomverse.club", "bunny-buddies.com", "www.flooz.world", "earclubnft.com", "svs.gg", "desperateapewives.com", "www.billionaireclubnft.com", "kurto.io", "xn--opnsea-4ua.app", "opensea.app", "www.alleycatunion.com", "www.teddytrex.io", "www.larvalabs.com", "boredapeyachtclub.com", "www.coolcatsnft.com", "cryptodadsnft.com", "www.lazylionsnft.com", "yuga.com", "otherside.xyz", "cryptopunks.app", "cannabispixie.co", "seadn.io", "highrunpokerclub.io", "davethedead.art", "tokensite.com"]

blacklist2 = ["discord.gg/mothernaturenft", "discord.gg/filab", "discord.gg/nft", "discord.gg/nfts", "discord.gg/nftpromo", "discord.gg/mollynft", "discord.gg/angryapesunitednft", "discord.gg/chaosclownz", "discord.gg/voodoo-warriors", "discord.gg/bvx", "discord.gg/flooz", "discord.gg/earc", "discord.gg/svsnft", "discord.gg/dapewives", "discord.gg/44vUJbEuE4", "discord.gg/vxajAY3YKt", "discord.gg/YzgjUUpmkf", "discord.gg/vvn2TkVXJw", "discord.gg/4Bya8nmpbC", "discord.gg/xX6SugCFBn", "discord.gg/z2bFtCJ8Tu", "discord.gg/pXCjGRxQaU", "discord.gg/ZeptbXM6S2", "discord.gg/nVqWPXeRXa", "discord.gg/uj3YZst", "discord.gg/FTERdSFCaf", "discord.gg/DsqPcJAYQT", "discord.gg/uweHDNdQrv", "discord.gg/xJnsPjAkDZ", "discord.gg/aSyjFg4jfP", "discord.gg/geZKHzWtu8", "discord.gg/FTTyyJ9Xu3", "discord.gg/gded98jmH8", "discord.gg/zJDRR5VKx4", "discord.gg/eGwdFsDKdh", "discord.gg/VWFtEpVc9Q", "discord.gg/75ArpFxPaF", "discord.gg/GJBVHbNfx7", "discord.gg/HxE754wj9r", "discord.gg/jKVr2UhNfr", "discord.gg/uzFfH3A4xy", "discord.gg/KyMMS7fuAP", "discord.gg/RZG9DgHZJX"]

blacklist3 = ["twitter.com/FourImmortals", "www.instagram.com/filabltd", "www.facebook.com/FILabOfficial", "twitter.com/FOURIMMORTALS", "twitter.com/eghz_nft", "instagram.com/atmvrs", "twitter.com/TheRedApeFamily", "twitter.com/theredapefamily", "www.instagram.com/theredapefamily", "www.youtube.com/c/TheRedApeFamily", "twitter.com/atomverseNFT", "twitter.com/theatomverse", "twitter.com/thebunnybuddies", "twitter.com/flooz_inc", "www.instagram.com/flooz.inc", "twitter.com/EARClubNFT", "twitter.com/svsnft", "twitter.com/DApeWives", "twitter.com/partyapebc", "www.instagram.com/billionaireclubnft", "www.linkedin.com/company/billionaireclubnft", "twitter.com/AlleyCatUnion", "twitter.com/PixeldustNFT", "twitter.com/TeddyTRexNFT", "twitter.com/TokyoGachaGirls", "www.instagram.com/AlleyCatUnion", "twitter.com/LazyLionsNFT", "www.instagram.com/lazylionsnft", "twitter.com/larvalabs", "www.youtube.com/channel/UCg2TFGt5LqBOSkEfeoP_shQ", "twitter.com/coolcatsnft", "twitter.com/BoredApeYC", "twitter.com/cryptopunksnfts", "twitter.com/HighRunPC", "twitter.com/MEE6NFT"]






botstaff = [757827467657478245]

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
@client.command()
async def restart(ctx):
    if ctx.author.id in botstaff:
        await ctx.send("Restarting... This may take some time.")
        restart_program()
    else:
        await ctx.send("This command can only be used by the bot developers")
        return




client.run("BOTTOKENHERE")
