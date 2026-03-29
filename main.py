import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Run the bot with the token (add your token to the .env file)
# bot.run(os.getenv('DISCORD_TOKEN'))
