import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot(intents = discord.Intents(messages=True, message_content=True))

class BotData:
    counting_mode = False

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(len(message.content))
    msg = message.content.strip()

    if msg.startswith('$dbless_counting'):
        response = "Counting mode is currently "
        response += "ON" if BotData.counting_mode else "OFF"
        response += "."
        await message.channel.send(response)

    if msg.startswith('$dbless_toggle_counting'):
        response = toggle_counting()
        await message.channel.send(response)


def toggle_counting():
    BotData.counting_mode = not BotData.counting_mode
    response = "Counting mode has been turned "
    response += "ON" if BotData.counting_mode else "OFF"
    response += "."
    return response

bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token