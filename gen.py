import discord
import random
import sqlite3
import asyncio
import traceback
import json
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.cooldowns import BucketType

#MySQL Calls 
conn = sqlite3.connect('account.db')
c = conn.cursor()

#Discord Command
prefix = "!"
TOKEN = "PUT TOKE HERE"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

#Calls
bot_developer = 'cracked.to/Kojixus'

#Cooldown command
_cd = commands.CooldownMapping.from_cooldown(1.0, 120.0, commands.BucketType.member)


#color
color = 0x8317FF

#Admin List - Insert the user id of the person here 
admin_list = []


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n------\nMy current prefix is: ! \n-----")
    await bot.change_presence(activity=discord.Game(name=f"Generating Accounts {bot.user.name}.\nUse ! to interacte with me!"))

#MYSQL
def create_table():
    conn = sqlite3.connect('accounts.db')
    c.execute('CREATE TABLE IF NOT EXISTS nordvpn(email TEXT, password TEXT)')
def create_table2():
    c.execute('CREATE TABLE IF NOT EXISTS hulu_accounts(email TEXT, password TEXT)')
def create_table3():
    c.execute('CREATE TABLE IF NOT EXISTS spotify(email TEXT, password TEXT)')
create_table()
create_table2()
create_table3()

#Commands
@bot.command()
async def info(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    members = len(guild.members)
    embed=discord.Embed(title="Buyer Info",color=color,inline=True)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="Members:",value=f"{members}",inline=True)
    embed.add_field(name="Developer",value=f"{bot_developer}",inline=True)
    embed.set_footer(text='Bot Info')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role("PUR YOUR STAFF ROLE HERE")
async def staffhelp(ctx):
    await ctx.send(f"{ctx.author.mention},sending you a the list of commands")
    embed = discord.Embed(title='List of Staff commands',description='The list of simple commands',color=color)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="!updateaccounts",value="Shows how and what accounts can be added",inline=False)
    embed.add_field(name="!removestock account_type",value="Removes stock from a certain account type",inline=False)
    embed.add_field(name="!info",value="Info",inline=False)
    embed.set_footer(text='List of Staff Commands')
    await ctx.author.send(embed=embed)

@bot.command()
async def help(ctx):
    await ctx.send(f"{ctx.author.mention}, I have sent you a DM showing my commands!")
    embed = discord.Embed(title = 'Help Commands',description = 'Here are some helpful commands to use',color=color)
    embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="!stock",value="Shows stock of accounts",inline=False)
    embed.add_field(name="!accounts",value="Shows the types of accounts that can be generated",inline=False)
    embed.set_footer(text='Help commands')
    await ctx.author.send(embed=embed)

@bot.command()
async def updateaccounts(ctx):
    await ctx.send(f"{ctx.author.mention}, I have sent you a DM showing commands how to add more accounts")
    embed = discord.Embed(title='Update Accounts',description='Command to Update Accounts',color=color)
    embed.set_author(name='Gen Info',icon_url='https:!!i.ibb.co!3MHXD2w!Profile-Page.jpg')
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="!addnordvpn",value="Format is !addnordvpn email:pass\nThis command can only add 1 account",inline=False)
    embed.add_field(name="!addbulknordvpn",value="Format is !addbulknordvpn \nemail:pass\nemail:pass (must be 10 lines)\nThis command can only add 10 accounts (no less or no more)",inline=False)
    embed.add_field(name="!addhulu",value="Format is !addhulu email:pass\nThis command can only add 1 account",inline=False)
    embed.add_field(name="!addbulkhulu",value="Format is !addbulkhulu \nemail:pass\nemail:pass (must be 10 lines)\nThis command can only add 10 accounts (no less or no more)",inline=False)
    embed.add_field(name="!addspotify",value="Format is !addspotify email:pass\nThis command can only add 1 account",inline=False)
    embed.add_field(name="!addbulkspotify",value="Format is !addbulkspotify \nemail:pass\nemail:pass (must be 10 lines)\nThis command can only add 10 accounts (no less or no more)",inline=False)
    embed.set_footer(text='Commands for Updating Accounts')
    await ctx.author.send(embed=embed)

@bot.command()
async def removestock(ctx, type):
    if ctx.message.author.id in admin_list:
        if type == "nordvpn":
            delete = "nordvpn"
        elif type == "hulu":
            delete = "hulu_accounts"
        elif type == "spotify":
            delete = "spotify"
        else:
            embed=discord.Embed(title="Your Request Failed",description="Please provide a valid account type",color=color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Request Failed')     
            await ctx.send(embed=embed)
        c.execute(f"DELETE FROM {delete}")
        conn.commit()
        embed=discord.Embed(title="Your request is successful",description=f"Successfully removed stock from {type}",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Successful')     
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Your Request Failed",description="You do not have permission to remove stock",color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Request Failed')     
        await ctx.send(embed=embed)
@tasks.loop(minutes=2)
async def post_loop():
    await bot.wait_until_ready()
    server = bot.get_guild(change me) 
    channel = bot.get_channel(change me)
    await channel.purge(limit=99)
    c.execute("SELECT count(*) from nordvpn")
    stock = c.fetchall()
    c.execute("SELECT count(*) from hulu_accounts")
    stock2 = c.fetchall()
    c.execute("SELECT count(*) from spotify")
    stock3 = c.fetchall()
    embed = discord.Embed(title='Current Stock',description='List of all Accounts and current stock',color=color)
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.set_author(name='Gen Info')
    embed.add_field(name="NordVPN:",value=f"{stock[0][0]}",inline=True)
    embed.add_field(name="Hulu:",value=f"{stock2[0][0]}",inline=True)
    embed.add_field(name="Spotify:",value=f"{stock3[0][0]}",inline=True)
    embed.set_footer(text='Accounts')
    await channel.send(embed=embed)
my_loop.start()
check_loop.start()

@bot.command()
async def stock(ctx):
    c.execute("SELECT count(*) from nordvpn")
    stock = c.fetchall()
    c.execute("SELECT count(*) from hulu_accounts")
    stock2 = c.fetchall()
    c.execute("SELECT count(*) from spotify")
    stock3 = c.fetchall()
    embed = discord.Embed(title='Current Stock',description='List of all Accounts and current stock',color=color)
    embed.set_author(name='Account Gen Stock')
    embed.add_field(name="NordVPN:",value=f"{stock[0][0]}",inline=True)
    embed.add_field(name="Hulu:",value=f"{stock2[0][0]}",inline=True)
    embed.add_field(name="Spotify:",value=f"{stock3[0][0]}",inline=True)
    embed.set_footer(text='Accounts Stock')
    await ctx.send(embed=embed)

#channel where accounts will be able to generate from put channel id 
channel_generated[]

@bot.command()
@commands.has_role(PUT PREMIUM ROLE HERE)
async def accounts(ctx)
    await ctx.send(f"{ctx.author.mention}, Check your DM's we've sent you the commands")
    embed = discord.Embed(title='Current Accounts',description='List of all Accounts commands',color=color)
    embed.set_author(name='Accounts that can be Generated')
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="hulu",value="!hulu will send you a hulu account",inline=True)
    embed.add_field(name="nordvpn",value="!nordvpn will send you a nordvpn account",inline=True)
    embed.add_field(name="spotify",value="!spotify will send you a spotify account",inline=True)
    embed.set_footer(text='Current Accounts')
    await ctx.author.send(embed=embed)

###########################################################################################################################
#directtv Command 
###########################################################################################################################
@bot.command()
@commands.has_role("Premium")
async def spotify(ctx):
        if ctx.channel.id in channel_generated:
            c.execute("SELECT count(*) from spotify")
            stock = c.fetchall()
            if stock[0][0] == 0:
                embed=discord.Embed(title="Failed to Generate",description=f"There is currently no stock for spotify, try again later when a restock is announced!",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Check your DM's! We have sent you your generated account!",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
                c.execute('SELECT * FROM spotify ORDER BY RANDOM() LIMIT 1')
                data = c.fetchall()
                embed  = discord.Embed(title="Spotify Account generated",description=(f"Your account details are\n**Email/user:** {data[0][0]}\n**Password:** {data[0][1]}\n**Combo:** {data[0][0]}:{data[0][1]}"),color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                c.execute("DELETE FROM spotify WHERE password=?", (data[0][1],))
                conn.commit()
                await ctx.author.send(embed=embed)
                await ctx.author.send(f"{data[0][0]}:{data[0][1]}")
                account_log = discord.Embed(title="Spotify account generated",description=f"Account with the following info:\nEmail: {data[0][0]}\nPassword: {data[0][1]} has been generated",color=color)
                account_log.set_footer(text=f"Generated by {ctx.author} | Discord ID: {ctx.author.id}")
                server = bot.get_guild(change me)
                channel = server.get_channel(change me)
                await channel.send(embed=account_log)
        else:
            embed = discord.Embed(title="Failed request",description="You cannot use that command in this channel",color=color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Account Generator')
            await ctx.send(embed=embed)
@bot.command()
async def addspotify(ctx, account):
    email = account.split(":")[0]
    password = account.split(":")[1]
    if ctx.author.id in admin_list:
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email}','{password}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added spotify account with the details:\n Email/username: {email}\nPassword: {password}"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
        logger = discord.Embed(title="Spotify account added",description=f"The following account was added:\n{email}:{password}",color=color)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add spotify accounts"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
@bot.command()
async def addbulkspotify(ctx, account, account2, account3, account4, account5, account6, account7, account8, account9, account10): #account3, account4, account5, account6, account7, account8, account9, account 10):
    email = account.split(":")[0]
    password = account.split(":")[1]
    email2 = account2.split(":")[0]
    password2 = account2.split(":")[1]
    email3 = account3.split(":")[0]
    password3 = account3.split(":")[1]
    email4 = account4.split(":")[0]
    password4 = account4.split(":")[1]
    email5 = account5.split(":")[0]
    password5 = account5.split(":")[1]
    email6 = account6.split(":")[0]
    password6 = account6.split(":")[1]
    email7 = account7.split(":")[0]
    password7 = account7.split(":")[1]
    email8 = account8.split(":")[0]
    password8 = account8.split(":")[1]
    email9 = account9.split(":")[0]
    password9 = account9.split(":")[1]
    email10 = account10.split(":")[0]
    password10 = account10.split(":")[1]
    if ctx.author.id in admin_list:
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email}','{password}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email2}','{password2}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email3}','{password3}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email4}','{password4}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email5}','{password5}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email6}','{password6}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email7}','{password7}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email8}','{password8}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email9}','{password9}')")
        conn.commit()
        c.execute(f"INSERT INTO spotify (email, password) VALUES('{email10}','{password10}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added spotify accounts to database"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
        logger = discord.Embed(title="Spotify accounts added",description=f"The following accounts were added\n{email}:{password}\n{email2}:{password2}\n{email3}:{password3}\n{email4}:{password4}\n{email5}:{password5}\n{email6}:{password6}\n{email7}:{password7}\n{email8}:{password8}\n{email9}:{password9}\n{email10}:{password10}",color=color)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add spotify accounts"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
###########################################################################################################################
#hulu Command 
###########################################################################################################################
@bot.command()
@commands.has_role("Premium")
async def hulu(ctx):
        if ctx.channel.id in channel_generated:
            c.execute("SELECT count(*) from hulu_accounts")
            stock = c.fetchall()
            if stock[0][0] == 0:
                embed=discord.Embed(title="Failed to Generate",description=f"There is currently no stock for hulu, try again later when a restock is announced!",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Check your DM's! We have sent you your generated account!",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
                c.execute('SELECT * FROM hulu_accounts ORDER BY RANDOM() LIMIT 1')
                data = c.fetchall()
                embed = discord.Embed(title="Hulu Account generated",description=(f"Your account details are\n**Email/user:** {data[0][0]}\n**Password:** {data[0][1]}\n**Combo:** {data[0][0]}:{data[0][1]}"),color=color)
                c.execute("DELETE FROM hulu_accounts WHERE password=?", (data[0][1],))
                conn.commit()
                await ctx.author.send(embed=embed)
                await ctx.author.send(f"{data[0][0]}:{data[0][1]}")
                account_log = discord.Embed(title="Hulu account generated",description=f"Account with the following info:\nEmail: {data[0][0]}\nPassword: {data[0][1]} has been generated",color=color)
                account_log.set_footer(text=f"Generated by {ctx.author} | Discord ID: {ctx.author.id}")
                account_log.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                server = bot.get_guild(change me)
                channel = server.get_channel(733511079535312928)
                await channel.send(embed=account_log)
        else:
            embed = discord.Embed(title="Failed request",description="You cannot use that command in this channel",color=color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Account Generator')
            await ctx.send(embed=embed)
@bot.command()
async def addhulu(ctx, account):
    email = account.split(":")[0]
    password = account.split(":")[1]
    if ctx.author.id in admin_list:
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email}','{password}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added a hulu account with the details:\n Email/username: {email}\nPassword: {password}"),color=color)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)
        logger = discord.Embed(title="Hulu account added",description=f"The following account was added:\n{email}:{password}",color=color)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add hulu accounts"),color=color)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)
@bot.command()
async def addbulkhulu(ctx, account, account2, account3, account4, account5, account6, account7, account8, account9, account10): #account3, account4, account5, account6, account7, account8, account9, account 10):
    email = account.split(":")[0]
    password = account.split(":")[1]
    email2 = account2.split(":")[0]
    password2 = account2.split(":")[1]
    email3 = account3.split(":")[0]
    password3 = account3.split(":")[1]
    email4 = account4.split(":")[0]
    password4 = account4.split(":")[1]
    email5 = account5.split(":")[0]
    password5 = account5.split(":")[1]
    email6 = account6.split(":")[0]
    password6 = account6.split(":")[1]
    email7 = account7.split(":")[0]
    password7 = account7.split(":")[1]
    email8 = account8.split(":")[0]
    password8 = account8.split(":")[1]
    email9 = account9.split(":")[0]
    password9 = account9.split(":")[1]
    email10 = account10.split(":")[0]
    password10 = account10.split(":")[1]
    if ctx.author.id in admin_list:
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email}','{password}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email2}','{password2}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email3}','{password3}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email4}','{password4}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email5}','{password5}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email6}','{password6}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email7}','{password7}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email8}','{password8}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email9}','{password9}')")
        conn.commit()
        c.execute(f"INSERT INTO hulu_accounts (email, password) VALUES('{email10}','{password10}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added hulu accounts to database"),color=color)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)
        logger = discord.Embed(title="Hulu accounts added",description=f"The following accounts were added\n{email}:{password}\n{email2}:{password2}\n{email3}:{password3}\n{email4}:{password4}\n{email5}:{password5}\n{email6}:{password6}\n{email7}:{password7}\n{email8}:{password8}\n{email9}:{password9}\n{email10}:{password10}",color=color)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add hulu accounts"),color=color)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)
###########################################################################################################################
#Hulu Command 
###########################################################################################################################
###########################################################################################################################
#NordVpn Command 
###########################################################################################################################
@bot.command()
@commands.has_role("Premium")
async def nordvpn(ctx):
        if ctx.channel.id in channel_generated:
            c.execute("SELECT count(*) from nordvpn")
            stock = c.fetchall()
            if stock[0][0] == 0:
                embed=discord.Embed(title="No stock!",description=f"There is currently no stock for Nordvpn, please try again when a restock is announced.",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="I've sent you the account details! Check your DM's!",color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                await ctx.send(embed=embed)
                c.execute('SELECT * FROM nordvpn ORDER BY RANDOM() LIMIT 1')
                data = c.fetchall()
                embed = discord.Embed(title="NordVPN Account generated",description=(f"Your account details are\n**Email/user:** {data[0][0]}\n**Password:** {data[0][1]}\n**Combo:** {data[0][0]}:{data[0][1]}"),color=color)
                embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                embed.set_footer(text='Account Generator')
                c.execute("DELETE FROM nordvpn WHERE password=?", (data[0][1],))
                conn.commit()
                await ctx.author.send(embed=embed)
                await ctx.author.send(f"{data[0][0]}:{data[0][1]}")
                account_log = discord.Embed(title="NordVPN account generated",description=f"Account with the following info:\nEmail: {data[0][0]}\nPassword: {data[0][1]} has been generated",color=color)
                account_log.set_footer(text=f"Generated by {ctx.author} | Discord ID: {ctx.author.id}")
                account_log.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
                server = bot.get_guild(change me)
                channel = server.get_channel(733511079535312928)
                await channel.send(embed=account_log)
        else:
            embed = discord.Embed(title="Failed request",description="You cannot use that command in this channel",color=color)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            await ctx.send(embed=embed)
@bot.command()
async def addnordvpn(ctx, account):
    email = account.split(":")[0]
    password = account.split(":")[1]
    if ctx.author.id in admin_list:
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email}','{password}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added a nordVPN account with the details:\n Email/username: {email}\nPassword: {password}"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
        logger = discord.Embed(title="NordVPN account added",description=f"The following account was added:\n{email}:{password}",color=color)
        logger.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add nordVPN accounts"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
@bot.command()
async def addbulknordvpn(ctx, account, account2, account3, account4, account5, account6, account7, account8, account9, account10): #account3, account4, account5, account6, account7, account8, account9, account 10):
    email = account.split(":")[0]
    password = account.split(":")[1]
    email2 = account2.split(":")[0]
    password2 = account2.split(":")[1]
    email3 = account3.split(":")[0]
    password3 = account3.split(":")[1]
    email4 = account4.split(":")[0]
    password4 = account4.split(":")[1]
    email5 = account5.split(":")[0]
    password5 = account5.split(":")[1]
    email6 = account6.split(":")[0]
    password6 = account6.split(":")[1]
    email7 = account7.split(":")[0]
    password7 = account7.split(":")[1]
    email8 = account8.split(":")[0]
    password8 = account8.split(":")[1]
    email9 = account9.split(":")[0]
    password9 = account9.split(":")[1]
    email10 = account10.split(":")[0]
    password10 = account10.split(":")[1]
    if ctx.author.id in admin_list: #CALLS FOR ADMIN LIST
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email}','{password}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email2}','{password2}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email3}','{password3}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email4}','{password4}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email5}','{password5}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email6}','{password6}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email7}','{password7}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email8}','{password8}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email9}','{password9}')")
        conn.commit()
        c.execute(f"INSERT INTO nordvpn (email, password) VALUES('{email10}','{password10}')")
        conn.commit()
        embed = discord.Embed(title="Request Successful",description=(f"Successfully added NordVPN accounts to database"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)
        logger = discord.Embed(title="NordVPN accounts added",description=f"The following accounts were added\n{email}:{password}\n{email2}:{password2}\n{email3}:{password3}\n{email4}:{password4}\n{email5}:{password5}\n{email6}:{password6}\n{email7}:{password7}\n{email8}:{password8}\n{email9}:{password9}\n{email10}:{password10}",color=color)
        logger.set_footer(text=f"Added by {ctx.author} | Discord ID: {ctx.author.id}")
        logger.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        server = bot.get_guild(change me)
        channel = bot.get_channel(change me)
        await channel.send(embed=logger)
    else:
        embed = discord.Embed(title="Request failed",description=("You do not have permission to add nordVPN accounts"),color=color)
        embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.set_footer(text='Account Generator')
        await ctx.send(embed=embed)
###########################################################################################################################
#No Cooldown Command 
###########################################################################################################################
@bot.check
async def cooldown_check(ctx):
    bucket = _cd.get_bucket(ctx.message)
    retry_after = bucket.update_rate_limit()
    role = ctx.guild.get_role(change me) #Put your no cooldown role here
    g = ["help","stock","staffhelp","accounts","removestock","info","updateaccounts","addnordvpn","addbulknordvpn","addhulu","addbulkhulu","addspotify","addbulkspotify"]
    if ctx.command.name in g:
        ctx.command.reset_cooldown(ctx)
    elif ctx.message.author.id in admin_list:
        ctx.command.reset_cooldown(ctx)
    elif role in ctx.author.roles:
        ctx.command.reset_cooldown(ctx)
    elif retry_after:
            embed=discord.Embed(title="Your on a Cooldown",description=f"Please wait before using another command, please try again in {int(retry_after)} seconds",color =color)
            embed.set_author(name=f'{ctx.author}',icon_url=f'{ctx.author.avatar_url}',)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text='Account Generator')
            await ctx.send(embed=embed)
            embed.timestamp = datetime.datetime.utcnow()
            raise commands.CommandOnCooldown(bucket, retry_after)
    return True
###########################################################################################################################
#TOKEN DO NOT REMOVE OR FUCK WITH DUMB CUNTS, THANKS HONEYS
###########################################################################################################################
bot.run(TOKEN)