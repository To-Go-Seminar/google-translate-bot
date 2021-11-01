import discord
from googletrans import Translator

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = discord.Client()
translator = Translator()

@client.event
async def on_ready():
	print('--------------')
	print('ログインしました')
	print(client.user.name)
	print(client.user.id)
	print('--------------')

@client.event
async def on_message(message):
	if message.author.bot:
		return

	if message.content.startswith('!translate'):
		say = message.content
		say = say[10:]
		if say.find('-') == -1:
			str = say
			detect = translator.detect(str)
			befor = detect.lang
			if befor == 'ja':
				convert = translator.translate(str, src=befor, dest='en')
				embed = discord.Embed(title='result', color=0xFFFFFF)
				embed.add_field(name='Befor', value=str)
				embed.add_field(name='After', value=convert.text, inline=False)
				await message.channel.send(embed=embed)
			else:
				convert = translator.translate(str, src=befor, dest='ja')
				embed = discord.Embed(title='result', color=0xFFFFFF)
				embed.add_field(name='Befor', value=str)
				embed.add_field(name='After', value=convert.text, inline=False)
				await message.channel.send(embed=embed)
		else:
			trans, str = list(say.split('='))
			befor, after = list(trans.split('-'))
			convert = translator.translate(str, src=befor, dest=after)
			embed = discord.Embed(title='result', color=0xFFFFFF)
			embed.add_field(name='Befor', value=str)
			embed.add_field(name='After', value=convert.text, inline=False)
			await message.channel.send(embed=embed)

	if message.content.startswith('!detect'):
		say = message.content
		s = say[8:]
		detect = translator.detect(s)
		m = 'この文字列の言語は ' + detect.lang + ' です。'
		await message.channel.send(m)

client.run(token)