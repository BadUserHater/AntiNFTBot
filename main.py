import discord
from discord.ext import commands
import asyncio
import sys
import random
import json

client = commands.Bot(command_prefix = "nft!")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="NFT Advertisements."))
    print("Bot Ready")

@client.event
async def on_message(message):
    member = message.author
    if message.author.bot:
        return
    if client.user.id != message.author.id:
        if 'crypto.com/nft' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'opensea.io' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'niftygateway.com' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'www.launchmynft.co' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'www.jump.trade' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'rarible.com' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'www.binance.com' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'superrare.com' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'async.art' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'knownorigin.io' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'www.blockchainappfactory.com' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'eggheadz.io' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'mee6.xyz/nft' in message.content:
            await message.channel.send(f"HEY {member.mention} NO NFT ADVERTISEMENTS IS ALLOWED HERE. NFTS are causing harm to the world. Learn more at nft!nfttruth")
            await message.delete()
        if 'buy my nft' in message.content:
            await message.channel.send(f"Are you trying to advertise your NFT {member.mention}? They are really stupid and causes harm to the world, look at nft!nfttruth to find out more.")
            await message.delete()
        if 'buy my NFT' in message.content:
            await message.channel.send(f"Are you trying to advertise your NFT {member.mention}? They are really stupid and causes harm to the world, look at nft!nfttruth to find out more.")
            await message.delete()
        
    await client.process_commands(message)





@client.command()
async def help(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot", description="Here is my entire Commands List", color=(40959))
    embed.add_field(name="GENERAL COMMANDS", value='nft!help - This message\nnft!ping - Checks my Latency\nnft!info - Information about the Bot\nnft!privacy - Checks my privacy Policy\nnft!nfttruth - Tells you the truth about NFTs', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My Latency is: {round(client.latency * 1000)}ms')

@client.command()
async def info(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot", description="Information about the NFT discord bot.", color=(40959))
    embed.add_field(name="GENERAL", value='CREATOR: Idiot Creature Hater#2255', inline=False)
    embed.add_field(name="LINKS", value='Invite me: https://discord.com/api/oauth2/authorize?client_id=985998562573832262&permissions=274879310912&scope=bot\nSupport Server: https://discord.gg/NpRbKaFmJU\nSource Code: https://github.com/BadUserHater/AntiNFTBot', inline=False)
    embed.add_field(name="SOURCE CODE STATUS", value='Open Source?: TRUE\nOrignal Creator: Idiot Creature Hater#2255\nLicense: MIT\nSource Code: https://github.com/BadUserHater/AntiNFTBot', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nfttruth(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot", description="Here is the truth about NFTs", color=(40959))
    embed.add_field(name="NFTs CAUSES HARM TO THE ENVIRONMENT", value='NFTs are making a bad impact to the world. Learn more about the truth of NFTs here: https://rickorford.com/8-reasons-to-not-invest-in-nfts/', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def privacy(ctx):
    embed = discord.Embed(title="ANTI-NFT Bot Privacy Policy", description="Last updated: July 4, 2022", color=(40959))
    embed.add_field(name="WHAT DATA DO YOU COLLECT", value='Anti-NFT Bot does not log, collect, or store any data. Once you invite the bot to your server, it is ready to search for any NFT advertisement links or any phrases relating to NFT advertisements.', inline=False)
    embed.add_field(name="HOW MAY I CONTACT YOU FOR CONCERNS", value='Reach to use at our support server at: https://discord.gg/NpRbKaFmJU', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()





client.run("BOTTOKENHERE")
