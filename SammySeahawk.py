# Author: Ethan Donoho
# Date: 12/19
# Purpose: General use discord bot for UNCW server

# Import discord library

import discord
from discord import Member
from discord.ext import commands

# Assigns prefix bot checks for

bot = commands.Bot(command_prefix='~')

# Bot attempts log in, prints success in console

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Bot assigns members role on server join

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Seahawks")
    await Member.add_roles(member, role)

# Command to Change members role

@bot.command()
async def role(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await Member.add_roles(member, role)


# WIP Bot greets user on server join

# @bot.event
# async def on_member_join(member):
#    print('user joined')
#    await member.channel.send('Hello ')
#    print('Sent?')

# Command to display bot info

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="SammySeahawk", description="Version 1.0 of a helpful mascot", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="TheFudgems")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

# Removes default bot help message

bot.remove_command('help')

# Custom bot help message

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SammySeahawk", description="Here are some commands:", color=0xeee657)
    embed.add_field(name="~info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="~help", value="Gives this message", inline=False)
    embed.add_field(name="~role", value="Sets your role", inline=False)

    await ctx.send(embed=embed)

# Unique token assignment to allow bot to log in

bot.run('NjQ3ODQzMjM1NjMyMzgxOTUy.Xdll2w.K7F1kGqPBHQ57LOuLGx_9qHzV1E')