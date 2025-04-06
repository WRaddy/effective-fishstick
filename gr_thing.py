import pytesseract
from PIL import Image
import pyautogui
import discord
from dotenv import load_dotenv
import os
import io
from time import sleep

# Load environment variables from .env file
load_dotenv()

sleep(3)
screenshot = pyautogui.screenshot()

text = pytesseract.image_to_string(screenshot)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # Get channel ID and bot token from environment variables
    channel_id = int(os.getenv('CHANNEL_ID'))  # Convert to int
    channel = client.get_channel(channel_id)  
    if channel:
        await channel.send(f"Here's the OCR output:\n\n{text}")
    await client.close()

# Run the bot using the token from the .env file
client.run(os.getenv('DISCORD_TOKEN'))
