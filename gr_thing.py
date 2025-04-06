import pytesseract
from PIL import Image
import pyautogui
import discord
import io
from time import sleep

sleep(3)
screenshot = pyautogui.screenshot()

text = pytesseract.image_to_string(screenshot)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    channel = client.get_channel(1358501640659013776)  
    if channel:
        await channel.send(f"Here's the OCR output:\n\n{text}")
    await client.close()

# Run the bot
client.run('MTI4NTM1NDgwMDAzMjEyMDg2Mw.GZ7QWe.TwNS0qCoQG805jimYdiAoozKwK--Y0jGP-O1UA')
