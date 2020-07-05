import discord
from discord.ext import commands
import JsonManager

bot = commands.Bot(command_prefix=JsonManager.getPrefix())

colore = ["blue"]

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(activity=discord.Activity(name=JsonManager.getActivity(), type=discord.ActivityType.watching))

@bot.command()
async def embed(ctx, *args):
    if len(args) >= 1:
        if str(args[0]) in colore:
            embed = discord.Embed(title=args, colour=discord.Colour(args[0]))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=' '.join(args), description=ctx.message.author.name)
            await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        embed = discord.Embed(title='pd', colour=discord.Color.red())
        
        await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(JsonManager.getChannel("welcome"))
    await channel.send(str(JsonManager.getMessage("join_message")).replace("%member%", member.name)) 
    await member.add_roles(discord.utils.get(member.guild.roles, name=JsonManager.getRole("new")))

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(JsonManager.getChannel("welcome"))
    await channel.send(str(JsonManager.getMessage("leave_message")).replace("%member%", member.name))
    

@bot.event
async def on_raw_reaction_add(payload):
    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    if payload.channel_id == JsonManager.getChannel("rule"):
        print(payload.emoji.name)
        if payload.emoji.name == "✅":
            await member.add_roles(discord.utils.get(bot.get_guild(payload.guild_id).roles, name=JsonManager.getRole("member")))
        if payload.emoji.name == "❌":
            await member.kick()

bot.run(JsonManager.getToken())