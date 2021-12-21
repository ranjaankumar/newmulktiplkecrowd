import discord
from discord.ext import commands
import random
import asyncio
from discord import Webhook, RequestsWebhookAdapter
pat=[]


vedantu = Webhook.from_url("https://discord.com/api/webhooks/922673692205539388/26QGscVp2hvE2mZUlOwATX_RVA-FZaLEgdI3PmUWtA-woECwWEbktlCA4DaIMj2swcz5",adapter=RequestsWebhookAdapter())
hq = Webhook.from_url("https://discord.com/api/webhooks/922697024380485662/CZmwkLkIMlXURtDtZFJhP8FdRFhsazrhsOCE4_80Hsd1vFM-ssyAJaFRqK-q3UKmP9mT",adapter=RequestsWebhookAdapter())
swagbucks = Webhook.from_url("https://discord.com/api/webhooks/922698885003091989/ce3TsfFrOFxCS4Nj5nFzE0QrqNTVhsxenN2yLeyN8I8GpdcLqsCJhk0eQzAUL_JmJKSJ",adapter=RequestsWebhookAdapter())

token = "OTA3NjM2MTIyNjgxNzUzNjIw.YYqEAg.XrBltIs25SwcS3axOqh2UkJ18aI "
techds = ""
bot =commands.Bot(command_prefix=techds)

ch=""

@bot.event
async def on_ready():
	print("Online")
	
@bot.command(name="1")
async def o(ctx):
	m=ctx.message.author
	if ctx.message.channel.id == 920855533077020765:  #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918012951791796335:  #stardom_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 921037549206663229:  #daynite_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 918730322789662760:  #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 920849694303850517:  #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
        
		
	if ctx.message.channel.id == 893400610957832202:  #daynite_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 919540946037772318:  #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 922147520128368670:  #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918134314456191027:  #stardom_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 893400509803819028:  #daynite_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922023255005601875:  #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :one:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922713009795788800:  #smart_hq
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
			
		
	if ctx.message.channel.id == 918730322789662760:  #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
		
	if ctx.message.channel.id == 920849694303850517:  #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
		
	if ctx.message.channel.id == 920855533077020765:  #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 893400610957832202:  #dayniye_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 922147520128368670:  #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 919540946037772318:  #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918134314456191027:  #stardom_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 893400509803819028:  #dayniye_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922023255005601875:  #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922713009795788800:  #smart_hq
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
		
		
	if ctx.message.channel.id == 918730322789662760: #pheonix_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 920849694303850517: #smart_vedantu
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		vedantu.send(embed=embed)
		
	if ctx.message.channel.id == 920855533077020765: #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 893400610957832202: #dayniye_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 922147520128368670: #pheonix_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 919540946037772318: #smart_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 918134314456191027: #stardom_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 893400509803819028: #dayniye_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922023255005601875: #pheonix_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)
		
	if ctx.message.channel.id == 922713009795788800: #smart_hq
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		hq.send(embed=embed)


bot.run(token)
