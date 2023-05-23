import discord
from discord.ext import commands
import requests, random
from load_dotenv import load_dotenv
import os

load_dotenv('secrets/.env')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

api_key = os.getenv("API_KEY")
token = os.getenv("TOKEN")


# Command to fetch and display a random cat image URL
@bot.command()
async def cat(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        cat_data = response.json()
        if cat_data:
            cat_image_url = random.choice(cat_data)['url']
            await ctx.send(cat_image_url)
        else:
            await ctx.send('No cat image found.')
    else:
        await ctx.send('Failed to fetch cat image.')

@bot.event
async def on_message(message):
    if '🐱' in message.content:
        cat_image_url = get_random_cat_image()
        if cat_image_url:
            await message.channel.send(cat_image_url)
        else:
            await message.channel.send('Failed to get a cat image. Meow!')

    await bot.process_commands(message)

def get_random_cat_image():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        cat_data = response.json()
        if cat_data:
            cat_image_url = cat_data[0]['url']
            return cat_image_url
    return None

# Event handling
# Verify cmd ctx
@bot.command()
async def my_command(ctx):
    # Command code here
    await ctx.send("Command executed!")

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected and ready.')

@bot.event
async def on_connect():
    print(f'{bot.user.name} is connected to the server.')

@bot.event
async def on_disconnect():
    print('Bot has disconnected from the server.')

@bot.event
async def on_error(event, *args, **kwargs):
    print(f'Error occurred: {args[0]}')

@bot.event
async def on_command_error(ctx, error):
    print(f'Command error: {error}')


bot.run(token)