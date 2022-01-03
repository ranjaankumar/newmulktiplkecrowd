import discord
from discord.ext import commands
import random
import asyncio
from discord import Webhook, RequestsWebhookAdapter
pat=[]


vedantu = Webhook.from_url("https://discord.com/api/webhooks/927618423595368460/ILPemTzfIdNddo5rVNg_HR5Gbr69R-VRoiUpeSHseuolFlOxIKqnF_IDN7XYmbIJiPE_",adapter=RequestsWebhookAdapter())
hq = Webhook.from_url("https://discord.com/api/webhooks/927619855136477224/IFJyNwhUiisRa1pct0TaqBvZrjmu0zwjtshJnVVQl_Zo8yYzNwUKNgpV4kDfG-azwegf",adapter=RequestsWebhookAdapter())
swagbucks = Webhook.from_url("https://discord.com/api/webhooks/927618593464664084/xOKYMiXrAPp6cq0ZLdGg1sls1DKK8GJxQ1hbvE4Uj00PuOCOBAowww8nR4IxwR7PWHkG",adapter=RequestsWebhookAdapter())

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
	if ctx.message.channel.id == 924645053987713085:  #stardom_swagbucks
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
		
        
		
	if ctx.message.channel.id == 926894350015819887:  #daynite_swagbucks
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
		
		
	if ctx.message.channel.id == 924645053987713085:  #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :two:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 926894350015819887:  #dayniye_swagbucks
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
		
	if ctx.message.channel.id == 924645053987713085: #stardom_swagbucks
		embed=discord.Embed(description="**Went With Option** :three:",color=discord.Colour.random())
		embed.set_author(name=f"{m.name}#{m.discriminator}", icon_url=m.avatar_url)
		swagbucks.send(embed=embed)
		
	if ctx.message.channel.id == 926894350015819887: #dayniye_swagbucks
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
