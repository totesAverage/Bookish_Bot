import discord
from discord.ext import commands
import youtube_dl

# Creates music cog so that the bot can find it
class music(commands.Cog):

  # Initiates the cog so that it will run
  def __init__(self,client):
    self.client = client
    
  # Makes the bot join the voice channel. It will check if there is anyone in the voice channel first, it cannot join unless a user is in the voice channel.
  @commands.command(aliases=['j'],help='This command will make the bot join the voice channel')
  async def join(self,ctx):
    if ctx.author.voice is None:
      await ctx.send("Please join a voice channel first!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      ctx.voice_client.move_to(voice_channel)
      
  # Allows you to disconnect the bot from the voice channel
  @commands.command(aliases=['dc'],help='This command will make the bot disconnect from the voice channel')
  async def leave(self,ctx):

    try:
      await ctx.voice_client.disconnect()
    except:
      await ctx.send("Bookish isn't in the voice channel!")

  # Allows you to play music from YouTube. It uses both yt_downloader and FFmpeg. yt_downloader downloads the file and FFmpeg converts it to a usable mpeg file to play. 
  @commands.command(aliases=['p'],help='This command will make the bot play music')
  async def play(self,ctx,url: str):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

  # Pauses the music bot
  @commands.command(aliases=['ps'],help='This command pauses the music')
  async def pause(self,ctx):
    if ctx.voice_client.is_playing():
      ctx.voice_client.pause()
      await ctx.send("Paused!⏸️")
    else:
      await ctx.send("Currently no audio is playing!")

  # Resumes the music bot
  @commands.command(aliases=['r'],help='This command resumes the music')
  async def resume(self,ctx):
    if ctx.voice_client.is_playing():
      await ctx.send("Music is already playing!")
    else:
      ctx.voice_client.resume()
      await ctx.send("Resume!▶️")

# It sets up the music cog for use. Very important
def setup(client):
  client.add_cog(music(client))
