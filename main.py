import discord
from discord.ext import commands
import requests

# Bot ayarları
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# API'den ördek resmi URL'sini al
def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

# !duck komutu
@bot.command(name="duck")
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Botu çalıştır
bot.run("BURAYA_BOT_TOKENİNİ_YAZ")