import discord
import os
from discord.ext import commands, tasks

# Sets the activity of the bot to what the user wants
thing = discord.Activity(type=discord.ActivityType.listening, name="Something")

# client is created that allows the bot to be called with commands
client = commands.Bot(command_prefix='&',activity=thing,status=discord.Status.online)

# Loads cogs into the bot
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
# Unloads cogs from the bot
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
# Loads a cog that you wish
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# Authenticates your bot by checking the token provided by Discord
client.run(os.getenv('bookish_token'))
