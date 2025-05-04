import discord
import os # default module
from dotenv import load_dotenv
from discord import app_commands

load_dotenv() # load all the variables from the env file
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)

class BotData:
    counting_mode = False

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1367793365344849991))
    print(f"{client.user} is ready and online!")

@tree.command(
    name="hey",
    description="Say hey to the bot!",
    guild=discord.Object(id = 1367793365344849991)
)
async def hello(interaction):
    await interaction.response.send_message("Hey!")

@tree.command(
    name="counting_mode",
    description="Check the status of the counting mode (ON/OFF)",
    guild=discord.Object(id = 1367793365344849991)
)
async def get_counting_mode(interaction):
    response = "Counting mode is currently "
    response += "ON" if BotData.counting_mode else "OFF"
    response += "."
    await interaction.response.send_message(response)

@tree.command(
    name="toggle_counting",
    description="Toggle the status of the counting mode (ON/OFF)",
    guild=discord.Object(id = 1367793365344849991)
)
async def toggle_counting_command(interaction):
    response = toggle_counting()
    await interaction.response.send_message(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(len(message.content))
    msg = message.content.strip()

    if msg.startswith('$dbless_counting'):
        response = "Counting mode is currently "
        response += "ON" if BotData.counting_mode else "OFF"
        response += "."
        await message.channel.send(response, reference=message)

    if msg.startswith('$dbless_toggle_counting'):
        response = toggle_counting()
        await message.channel.send(response, reference=message)


def toggle_counting():
    BotData.counting_mode = not BotData.counting_mode
    response = "Counting mode has been turned "
    response += "ON" if BotData.counting_mode else "OFF"
    response += "."
    return response

client.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token