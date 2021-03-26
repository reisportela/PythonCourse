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
from discord.ext import commands
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

    thesun = [
        'a1',
        'a2',
        (
            'a3, '
            'a4'
        ),
        'a5',
    ]

    if message.content == 'what':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == 'as':
        response = random.choice(thesun)
        await message.channel.send(response)
    
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    if message.content == 'weare':
        response = 'estou a dormir'
        await message.channel.send(response)

client.run(TOKEN)
