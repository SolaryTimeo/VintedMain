from webserver import keep_alive

import os
import time
import requests
import discord
from discord.ext import commands
from table2ascii import table2ascii

output = table2ascii(header=["Noms :", "Nike", "Zara", "Adidas", "Lacoste"],
                     body=[["ID :", "53", "12", "14", "304"],
                           ["Status :", "OK", "OK", "OK", "WIP"]],
                     footer=["By Timeo", "", "", "", ""])
"""
key = "https://www.vinted.be/vetements?price_from=0&currency=EUR&price_to=60&brand_id[]=53&catalog[]=5"
@client.event
async def on_message(message, author, mention):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        
        await message.channel.send(message.author.mention + "Hello")
"""

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # No infinite bot loops
    if message.author == client.user:
        return
    if message.content.startswith('!start'):
        mention = message.author.mention

        response = f"Salut {mention}, Bienvenue ! \nSi vous souhaitez lancer le bot écrivez : !vinted"
        await message.channel.send(response)
    if message.content.startswith('!vinted'):
        mention = message.author.mention

        response = f"{mention}, INFORMATION : \n\n-------------------------------\nTrier par marque : (!marques pour voir les marques dispo)\nTrier par prix : \nTrier par mots-clés : chaussures, t-shirt,...\n-------------------------------\nVous pouvez ajouter tous les arguments possibles\nExemple : \"!vintedstart 53 150 chaussures\""
        await message.channel.send(response)
    if message.content.startswith('!marques'):
        mention = message.author.mention
        await message.channel.send(
            f"{mention}, Les marques actuellement disponibles :\n\n```\n{output}\n```"
        )


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)
