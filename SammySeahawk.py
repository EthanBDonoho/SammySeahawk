import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    print('user joined')
    await member.channel.send('Hello ')
    print('Sent?')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="SammySeahawk", description="A helpful mascot", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="TheFudgems")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SammySeahawk", description="Here are some commands:", color=0xeee657)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NjQ3ODQzMjM1NjMyMzgxOTUy.Xdll2w.K7F1kGqPBHQ57LOuLGx_9qHzV1E')