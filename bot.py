# https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal
# https://discord.com/developers/applications/
# bot.py
# pip3 install discord
# pip3 install -U python-dotenv
# conda install -c conda-forge discord.py
# conda install -c conda-forge python-dotenv

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv('1.env')
TOKEN = os.getenv('DISCORD_TOKEN')
##GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'está a chover, :(',
    ]

    if message.content == 'ola':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)
