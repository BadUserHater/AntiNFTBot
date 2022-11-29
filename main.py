import discord
from discord.ext import commands
import asyncio
import sys
import json
import os

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=commands.when_mentioned_or('nft!'), intents=intents)
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
            embed.add_field(name="CASE DETAILS", value=f'NFT Advertiser Mention: {member.mention}\nNFT Advertising Type: NFT Social Media Page.', inline=False)
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
    embed = discord.Embed(title="Anti-NFT Bot", description="Here is my entire Commands List", color=(40959))
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

if "__main__" == __name__:
    with open("blacklist.txt", "r") as f:
        blacklist = f.read().splitlines()

if "__main__" == __name__:
    with open("blacklist2.txt", "r") as f:
        blacklist2 = f.read().splitlines()

if "__main__" == __name__:
    with open("blacklist3.txt", "r") as f:
        blacklist3 = f.read().splitlines()





client.run("BOTTOKENHERE")
