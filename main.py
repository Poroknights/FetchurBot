import fandom
import discord
from datetime import datetime
from discord import Embed
client = discord.Client()

async def get_fetchur(message):
    fandom.set_wiki("hypixel-skyblock")
    page = fandom.page(title = "Fetchur")
    daily = page.section("Current Request")
    item = daily[daily.find(")")+1:]
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    fEmbed = discord.Embed(title = item, description = "Today's item Fetchur needs is " + item + " " + current_time + " UTC +1", color = 0xBA55D3)
    await message.channel.send(embed = fEmbed)

@client.event
async def on_message(message):

    if message.author == client.user:
            return

    if message.content.startswith("*fetchur") or message.content.startswith("*f"):
        await get_fetchur(message)

client.run("token")
