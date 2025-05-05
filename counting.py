import discord

class CountingData:
    current_lives: int = 3
    current_int: int = 1
    max_lives: int = 3
    max_int: int = 0
    one_number_per_user: bool = False
    message_with_last_int: discord.Message = None


    @staticmethod
    def reset_lives():
        CountingData.current_lives = CountingData.max_lives

    @staticmethod
    def reset_current_int():
        CountingData.current_int = 1

    @staticmethod
    def set_max_lives(new_max_lives: int):
        CountingData.max_lives = new_max_lives

    @staticmethod
    def set_max_lives_and_reset(new_max_lives: int):
        """ Set max lives and reset current lives. """
        CountingData.set_max_lives(new_max_lives)
        CountingData.reset_lives()

    @staticmethod
    def toggle_one_number_per_user():
        CountingData.one_number_per_user = not CountingData.one_number_per_user

async def process_counting_messages(channel: discord.TextChannel, latest_message: discord.Message=None):
    """ Takes a counting channel """
    assert channel.name.strip().lower() == 'counting', "Channel's name is not called 'counting'"
    if latest_message is None:
        latest_message = channel.last_message
    msg = latest_message.content.strip()

    # If one_number_per_user is True
    if CountingData.one_number_per_user and CountingData.current_int > 1 and msg.split(' ', 1)[0].isdigit() and \
            (CountingData.message_with_last_int and
                    CountingData.message_with_last_int.author == latest_message.author):
        await latest_message.add_reaction('❌')
        if CountingData.current_lives - 1 > 0:
            CountingData.current_lives -= 1
            await channel.send(
                f'No user can count twice in a row!\nYou have {CountingData.current_lives} lives left.',
                reference=latest_message)
        else:
            CountingData.reset_lives()
            CountingData.reset_current_int()
            await channel.send(
                f'No user can count twice in a row!\nYou\'ve used all your lives, so start it all over!\nThe next number is {CountingData.current_int}!',
                reference=latest_message)
        return # This is not a valid message in this case

    # If one_number_per_user is False or a different user has the newest number
    if msg.split(' ', 1)[0].isdigit():
        if int(msg.split(' ', 1)[0]) == CountingData.current_int:
            if CountingData.max_int < CountingData.current_int:
                CountingData.max_int = CountingData.current_int
                await latest_message.add_reaction('✅')
            else:
                await latest_message.add_reaction('☑️')
            CountingData.current_int += 1
            CountingData.message_with_last_int = latest_message
        else:
            await latest_message.add_reaction('❌')
            if CountingData.current_lives - 1 > 0:
                CountingData.current_lives -= 1
                await channel.send(
                    f'Incorrect number!\nThe next number is {CountingData.current_int}.\nYou have {CountingData.current_lives} lives left.',
                    reference=latest_message)
            else:
                CountingData.reset_lives()
                CountingData.reset_current_int()
                await channel.send(
                    f'Incorrect number!\nYou\'ve used all your lives, so start it all over!\nThe next number is {CountingData.current_int}!',
                    reference=latest_message)

