"""Main file"""
import os
import discord
from dotenv import load_dotenv

from controller.music_controller import MusicController

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    """Bot connected to Discord
    """
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """On message event
    """
    if message.author == client.user:
        return

    if message.content.startswith("#"):
        full_command = message.content[1:].split(" ")
        if len(full_command) > 0:
            command = full_command[0]
            del full_command[0]
            params = full_command

            function = get_function_command(command)(client, message)
            function.load(params)

def get_function_command(command):
    """Get function from string command

    Args:
        command (str): main command

    Returns:
        class: instance class
    """
    controllers = {
        "music": MusicController
    }
    return controllers.get(command, lambda: None)

client.run(os.getenv('TOKEN'))
