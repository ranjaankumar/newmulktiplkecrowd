import discord
from discord.ext import commands
import random
import asyncio
from discord import Webhook, RequestsWebhookAdapter
pat=[]


vedantu = Webhook.from_url("https://discord.com/api/webhooks/922673692205539388/26QGscVp2hvE2mZUlOwATX_RVA-FZaLEgdI3PmUWtA-woECwWEbktlCA4DaIMj2swcz5",adapter=RequestsWebhookAdapter())
hq = Webhook.from_url("https://discord.com/api/webhooks/922673692205539388/26QGscVp2hvE2mZUlOwATX_RVA-FZaLEgdI3PmUWtA-woECwWEbktlCA4DaIMj2swcz5",adapter=RequestsWebhookAdapter())
swagbucks = Webhook.from_url("https://discord.com/api/webhooks/922673692205539388/26QGscVp2hvE2mZUlOwATX_RVA-FZaLEgdI3PmUWtA-woECwWEbktlCA4DaIMj2swcz5",adapter=RequestsWebhookAdapter())

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
	if ctx.message.channel.id == 918012951791796335:  #stardom_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #daynite_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
        if ctx.message.channel.id == 921037549206663229:  #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #daynite_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #stardom_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #daynite_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #smart_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)

@bot.command(name="2")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 918012951791796335:  #stardom_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
				
	
	
	if ctx.message.channel.id == 921037549206663229:  #dayniye_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
			
		
	if ctx.message.channel.id == 918012951791796335:  #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
		
	if ctx.message.channel.id == 918012951791796335:  #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
		
	if ctx.message.channel.id == 918012951791796335:  #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #dayniye_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #stardom_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #dayniye_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #smart_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
	
	
@bot.command(name="3")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 918012951791796335: #stardom_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229: #dayniye_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
		
	if ctx.message.channel.id == 918012951791796335: #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #dayniye_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #stardom_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #dayniye_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335: #smart_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)


bot.run(token)
