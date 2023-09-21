SOURCE CODE FOR THE ANTI-NFT BOT
CREATED BY: Idiot Creature Hater#2255 on Discord.

WARNING: THIS SOURCE CODE HAS BEEN DISCONTINUED! IF YOU WISH TO SELF-HOST THIS BOT, YOU ARE ON YOUR OWN!

THIS CODE HAS BEEN REWRITTEN FOR DISCORD.PY 2.0 AS DISCORD.PY 1.7.x MAY HAVE STOPPED WORKING IN 2023.

Anti-NFT bot is a open source discord.py bot that stops links to NFT websites, blocks phrases relating to NFT advertising, and
even NFT based discord servers. Can also remove messages containing links to many NFT marketplaces.
This version also lets you set in your server if you want the bot to auto-ban members who sends NFT advertisements or not.

NOTE: To use this source code, you need the Message content intent, if your bot is unverified, then turn it on in the developer portal

================================================
SETUP:
- Fork or download this source code
- Go to https://discord.com/developers/applications and create a discord bot application, create a bot, and copy its discord bot token if you have not already done so
- Enable the Message Content Intent.
- client.run("BOTTOKENHERE") where BOTTOKENHERE is your Discord Bot Token that you got from the Discord developer portal (Located at the bottom of the code)
- client = commands.Bot(command_prefix = "nft!") where nft! would be the prefix you want
- SETTING UP STAFF
>>>> Towards the bottom, head to botstaff = [757827467657478245]
>>>> In the botstaff brackets, replace 757827467657478245 with the discord user ids of your staff you want to control the bot.
>>>> To have more then one, seperate each user id with a comma and space. EXAMPLE: botstaff = [757827467657478245, 672273762892251136, 972161452133728256]
- Invite your bot to the server
>>>> When you invite the bot, the permissions needed at minimum is: Read Messages, Send Messages, Manage Messages, View Channel History, and Embed Links
>>>> For the punishment option, Ban Members and Manage Roles permissions is required as well.

With the json files, you don't need to touch them.

=================================================
HOW THE BOT WORKS + EXTRA INFO

We are constantly updating the detection system to be able to stop Pro NFT Advertisements
like stopping NFT market websites and NFT project discord servers.

How it works is we have 3 lists at the botton seperated with a comma and space.
blacklist = Regular NFT websites
blacklist2 = Pro NFT Discord Servers (Like NFT project servers)
blacklist3 = NFT project social media pages

CURRENT ISSUES: You can't remove the logs data from command, you have to manually remove your server id/channel id from the logs.json file

=================================================

WARNING: THERE IS LITERALLY NO GUARENTEES OR WARRENTIES IF YOU DECIDE TO SELF-HOST THIS BOT. IF YOU DO, WE WILL NOT BE HELD RESPONSIBLE OR LIABLE FOR
DAMAGES INCLUDING BUT LIMITED TO: LOSS OF PROFITS, COMMERCIAL DAMAGES, etx. IF YOU DO SELF HOST THIS BOT, WE EXPECT YOU TO HAVE ENOUGH KNOWLEDGE IN
DISCORD.PY AND PYTHON. WE WILL NOT HELP YOU SET UP THE BOT UP EITHER! USE AT YOUR OWN RISK!
IT IS ADVISED TO USE THE ORIGNAL BOT:
https://discord.com/oauth2/authorize?client_id=985998562573832262&permissions=277295262918&scope=bot%20applications.commands

LICENSE: We are using the MIT license so you can do whatever you want with this source code.
Crediting me is also advised.

=================================================
ORIGNAL LINKS:
ORIGNAL BOT: https://discord.com/oauth2/authorize?client_id=985998562573832262&permissions=277295262918&scope=bot%20applications.commands
SUPPORT SERVER: https://discord.gg/NpRbKaFmJU
WEBSITE: https://meowbahhbotsite.glitch.me

DEVELOPER'S LINKS (You can support me just by following me)
YOUTUBE CHANNEL: https://www.youtube.com/c/TheIdiotCreatureHater
TWITTER: https://twitter.com/BadUserHater
GITHUB: https://github.com/BadUserHater
GAMEJOLT: https://gamejolt.com/@IdiotCreatureHater
DISCORD SERVER: https://discord.gg/nVs4rCNwyc
SUBREDDIT: https://www.reddit.com/r/BadUserHaters/
TIKTOK: https://www.tiktok.com/@theidiotcreaturehater

IdiotAI API is made by Idiot Creature Hater Studios 2022-2023
Idiot Creature Hater Studios 2021-2023