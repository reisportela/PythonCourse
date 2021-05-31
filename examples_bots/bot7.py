import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('1.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_ofsides + 1)))
        for  in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)
