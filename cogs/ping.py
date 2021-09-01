import discord
from discord.ext import commands

class ping(commands.Cog):

   def __init__(self,client):
     self.client = client
   
   
   @commands.command()
   async def pinger(self,ctx):
     await ctx.send(f'Latency is: {round(self.client.latency * 1000)}ms')

def setup(client):
  client.add_cog(ping(client))