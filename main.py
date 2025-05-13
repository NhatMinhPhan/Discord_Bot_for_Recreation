import discord
import os # default module
from dotenv import load_dotenv
from discord import app_commands
import counting
import admin
from typing import List

load_dotenv() # load all the variables from the env file
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)
MY_GUILD = discord.Object(id = os.getenv('MY_SERVER'))

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1367793365344849991))
    print(f"{client.user} is ready and online!")

@tree.command(
    name="hey",
    description="Say hey to the bot!",
    guild=MY_GUILD
)
async def hello(interaction):
    await interaction.response.send_message("Hey!")

@tree.command(
    name="counting_mode",
    description="Check the status of the counting mode (ON/OFF)",
    guild=MY_GUILD
)
async def get_counting_mode(interaction):
    response = "Counting mode is currently "
    response += "ON" if counting.CountingData.counting_mode else "OFF"
    response += "."
    await interaction.response.send_message(response)

@tree.command(
    name="toggle_counting",
    description="Toggle the status of the counting mode (ON/OFF) (Admins-only)",
    guild=MY_GUILD
)
async def toggle_counting_command(interaction):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if not roles_are_set:
        return
    # Check if the user has one of the admin roles set for the bot:
    member_is_admin = False
    for role in interaction.user.roles:
        if role in admin.AdminData.admin_roles:
            member_is_admin = True
            break
    if not member_is_admin:
        # Send a private message to the user
        await interaction.response.send_message(
            'This command cannot be carried out because you do not have one of the admin roles set for this bot.',
            ephemeral = True
        )
        return

    response = toggle_counting()
    await interaction.response.send_message(response)

@tree.command(
    name="one_number_per_user",
    description="Check the status of the one_number_per_user setting for counting (ON/OFF)",
    guild=MY_GUILD
)
async def get_one_number_per_user(interaction):
    response = "ONE_NUMBER_PER_USER is currently "
    response += "ON" if counting.CountingData.one_number_per_user else "OFF"
    response += "."
    await interaction.response.send_message(response)

@tree.command(
    name="toggle_one_number_per_user",
    description="Toggle the status of the one_number_per_user setting for counting (ON/OFF) (Admins-only)",
    guild=MY_GUILD
)
async def toggle_one_number_per_user(interaction):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if not roles_are_set:
        return
    # Check if the user has one of the admin roles set for the bot:
    member_is_admin = False
    for role in interaction.user.roles:
        if role in admin.AdminData.admin_roles:
            member_is_admin = True
            break
    if not member_is_admin:
        # Send a private message to the user
        await interaction.response.send_message(
            'This command cannot be carried out because you do not have one of the admin roles set for this bot.',
            ephemeral=True
        )
        return

    counting.CountingData.toggle_one_number_per_user()
    response = "ONE_NUMBER_PER_USER has been turned "
    response += "ON" if counting.CountingData.one_number_per_user else "OFF"
    response += "."
    await interaction.response.send_message(response)

@tree.command(
    name="counting_lives",
    description="Check the number of lives remaining before the counting game is reset",
    guild=MY_GUILD
)
async def get_counting_lives(interaction):
    response = f"You now have {counting.CountingData.current_lives} lives remaining."
    await interaction.response.send_message(response)

@tree.command(
    name="counting_info",
    description="Return all information about the counting game",
    guild=MY_GUILD
)
async def get_counting_info(interaction):
    response = f"CURRENT LIVES: {counting.CountingData.current_lives}\n"
    response += f"CURRENT INTEGER: {counting.CountingData.current_int}\n"
    response += f"MAX LIVES: {counting.CountingData.max_lives}\n"
    response += f"COUNTING HIGH SCORE: {counting.CountingData.max_int}\n"
    response += "ONE NUMBER PER USER: "
    response += "On" if counting.CountingData.one_number_per_user else "Off"
    await interaction.response.send_message(response)

@tree.command(
    name="counting_high_score",
    description="Check the high score achieved in the counting game",
    guild=MY_GUILD
)
async def counting_high_score(interaction):
    response = f"COUNTING HIGH SCORE: {counting.CountingData.current_lives}"
    await interaction.response.send_message(response)

@tree.command(
    name="set_max_lives_to",
    description="Set the number of max counting lives to a certain positive integer (Admins-only)",
    guild=MY_GUILD
)
@app_commands.describe(new_max_lives='The new number of max lives')
async def set_max_lives_to(interaction, new_max_lives: str):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if not roles_are_set:
        return
    # Check if the user has one of the admin roles set for the bot:
    member_is_admin = False
    for role in interaction.user.roles:
        if role in admin.AdminData.admin_roles:
            member_is_admin = True
            break
    if not member_is_admin:
        # Send a private message to the user
        await interaction.response.send_message(
            'This command cannot be carried out because you do not have one of the admin roles set for this bot.',
            ephemeral=True
        )
        return

    try:
        new_max = int(new_max_lives)
        if new_max <= 0: # Terminate if new_max is not positive
            await interaction.response.send_message(
                f'Argument {new_max_lives} is not above 0.\nThis command has not been fulfilled.'
            )
            return

        # If current lives > max lives, reset lives
        if counting.CountingData.current_lives > counting.CountingData.max_lives:
            counting.CountingData.set_max_lives_and_reset(new_max)
        else: # Simply set max_lives to new_max
            counting.CountingData.set_max_lives(new_max)
        response = f"MAX LIVES has been set to {new_max}"
        await interaction.response.send_message(response)
    except ValueError:
        await interaction.response.send_message(
            f'Argument {new_max_lives} cannot be parsed.\nThis command has not been fulfilled.'
        )


@tree.command(
    name="get_admin_roles",
    description="Gets a list of the admin roles for this server",
    guild=MY_GUILD
)
async def get_admin_roles(interaction):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if not roles_are_set:
        return

    admin_roles = admin.AdminData.admin_roles
    admin_roles_names: List[str] = [role.name for role in admin_roles]

    response = f"Admin roles for this bot: {admin_roles_names}"
    await interaction.response.send_message(response)

@tree.command(
    name="update_admin_roles",
    description="Update admin roles for this bot by following the slash command with the names of such roles (Admins-only if admin roles for this bot have been set)",
    guild=MY_GUILD
)
@app_commands.describe(args='Names of the admin roles to be set for this bot')
async def update_admin_roles(interaction, *args: str):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if roles_are_set:
        # Check if the user has one of the admin roles set for the bot:
        member_is_admin = False
        for role in interaction.user.roles:
            if role in admin.AdminData.admin_roles:
                member_is_admin = True
                break
        if not member_is_admin:
            # Send a private message to the user
            await interaction.response.send_message(
                'This command cannot be carried out because you do not have one of the admin roles set for this bot.',
                ephemeral=True
            )
            return

    try:
        admin.AdminData.admin_roles = list(
            admin.get_roles_by_names(client.get_guild(int(os.getenv('MY_SERVER'))), *args)
        )
    except AssertionError:
        print('update_admin_roles: the guild argument is not a Guild object')
        await interaction.response.send_message(
            'This command cannot be carried out because: the guild argument is not a Guild object'
        )
    else: # When there is no error
        response = 'Admin roles for this bot have been updated!'
        admin_roles = admin.AdminData.admin_roles
        admin_roles_names: List[str] = [role.name for role in admin_roles]

        response += f"Updated admin roles: {admin_roles_names}"
        await interaction.response.send_message(response)

@tree.command(
    name="reset_admin_roles",
    description="Reset admin roles for this bot (Admins-only if admin roles for this bot have been set)",
    guild=MY_GUILD
)
async def reset_admin_roles(interaction):
    # This is admins-only, so the following checks if admin roles for this bot have been set or not
    roles_are_set = admin_roles_are_set(interaction)
    if roles_are_set:
        # Check if the user has one of the admin roles set for the bot:
        member_is_admin = False
        for role in interaction.user.roles:
            if role in admin.AdminData.admin_roles:
                member_is_admin = True
                break
        if not member_is_admin:
            # Send a private message to the user
            await interaction.response.send_message(
                'This command cannot be carried out because you do not have one of the admin roles set for this bot.',
                ephemeral=True
            )
            return

    admin.AdminData.admin_roles.clear()


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.channel.name.strip().lower() == 'counting' and counting.CountingData.counting_mode:
        await counting.process_counting_messages(message.channel, message)

def toggle_counting():
    counting.CountingData.counting_mode = not counting.CountingData.counting_mode
    response = "Counting mode has been turned "
    response += "ON" if counting.CountingData.counting_mode else "OFF"
    response += "."
    return response

async def admin_roles_are_set(interaction) -> bool:
    """
    Checks if admin roles for this bot are set.
    :param: interaction: Interaction passed as an argument for a slash command
    :return: boolean value for whether admin roles are set for this bot
    """
    admin_roles = admin.AdminData.admin_roles
    if len(admin_roles) == 0:
        response = 'Admin roles for this bot are not set yet.'
        response += '\nPlease use the command /update_admin_roles to set admin roles for this bot so that admins-only commands work.'
        await interaction.response.send_message(response)
        return False
    return True

if __name__ == '__main__':
    client.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token