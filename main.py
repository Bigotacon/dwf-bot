import requests
# bot.py
import os
import random
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

    
def parse_product(product):
    url = f"https://dwarvenforge.com/products/all?page={product}.js"
    details = requests.get(url).json()
    quantity = details['variants'][0]['inventory_quantity']
    return quantity

TOKEN = "MTAwNDE1MDQzNTM3MzkyMDM0Ng.GhVTaq.bs2v5-VcdF96o8cs7Mgv0QLUG4Q02L2rbQe-yw"
bot = commands.Bot(command_prefix='!')

@bot.command(name='product', help='gets details for DwF product')
async def fetch_inv(ctx, product_handle: str):
    url = f"https://dwarvenforge.com/products/{product_handle}.js"
    details = requests.get(url).json()
    qty = details['variants'][0]['inventory_quantity']
    await ctx.send(qty)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
   
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
   
bot.run(TOKEN)