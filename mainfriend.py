import discord
from discord.ext import commands
import random
import asyncio
from discord import Webhook, RequestsWebhookAdapter
pat=[]


hook = Webhook.from_url("https://discord.com/api/webhooks/922673692205539388/26QGscVp2hvE2mZUlOwATX_RVA-FZaLEgdI3PmUWtA-woECwWEbktlCA4DaIMj2swcz5",adapter=RequestsWebhookAdapter())

token = "OTA3NjM2MTIyNjgxNzUzNjIw.YYqEAg.XrBltIs25SwcS3axOqh2UkJ18aI"
techds = ""
bot =commands.Bot(command_prefix=techds)

ch=""

@bot.event
async def on_ready():
	print("Online")
	
@bot.command(name="1")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 918012951791796335:
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		#hook.send("1")
	if ctx.message.channel.id == 921037549206663229:	
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		#hook.send("1")
		

@bot.command(name="2")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 918012951791796335:
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		#hook.send("1")		
	
	
	if ctx.message.channel.id == 921037549206663229:
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		#hook.send("1")		
	
	
@bot.command(name="3")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 918012951791796335:
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hook.send(embed=embed)
		#hook.send("1")


bot.run(token)
