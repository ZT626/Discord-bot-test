import discord
from discord.ext import commands

# You need discord.py to run the program do pip install discord if you haven't already! ^

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
 print('The Sweatshops are waiting!')

# add a text file with the token inside it and name it token.txt.gitignore when wanting to run the program

with open("token.txt.gitignore") as file:
 token = file.read()

bot.run(token)