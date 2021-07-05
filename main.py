import os
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "g.", description = "GlaxiBot")

@bot.event
async def on_ready():
	print('''   ▄██████▄   ▄█          ▄████████ ▀████    ▐████▀  ▄█  ▀█████████▄   ▄██████▄      ███     
             ███    ███ ███         ███    ███   ███▌   ████▀  ███    ███    ███ ███    ███ ▀█████████▄ 
             ███    █▀  ███         ███    ███    ███  ▐███    ███▌   ███    ███ ███    ███    ▀███▀▀██ 
            ▄███        ███         ███    ███    ▀███▄███▀    ███▌  ▄███▄▄▄██▀  ███    ███     ███   ▀ 
           ▀▀███ ████▄  ███       ▀███████████    ████▀██▄     ███▌ ▀▀███▀▀▀██▄  ███    ███     ███     
             ███    ███ ███         ███    ███   ▐███  ▀███    ███    ███    ██▄ ███    ███     ███     
             ███    ███ ███▌    ▄   ███    ███  ▄███     ███▄  ███    ███    ███ ███    ███     ███     
             ████████▀  █████▄▄██   ███    █▀  ████       ███▄ █▀   ▄█████████▀   ▀██████▀     ▄████▀   
             ▀                                                                               
			 ''')
	await bot.change_presence(activity=discord.Game(name="g.help  v_1.0"))



@bot.command()
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)







bot.run("ODYwNDg1NDE1NTU5MTAyNTA1.YN77fg.24BuCHWfTsntODGrjWTLYsVJZyc")
