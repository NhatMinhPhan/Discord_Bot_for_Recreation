import discord

class CountingData:
    current_lives = 3
    current_int = 1
    max_lives = 3
    max_int = 0

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

async def process_counting_messages(channel: discord.TextChannel, latest_message: discord.Message=None):
    """ Takes a counting channel """
    assert channel.name.strip().lower() == 'counting', "Channel's name is not called 'counting'"
    if latest_message == None:
        latest_message = channel.last_message
    msg = latest_message.content.strip()
    if msg.split(' ', 1)[0].isdigit():
        if int(msg.split(' ', 1)[0]) == CountingData.current_int:
            if CountingData.max_int < CountingData.current_int:
                CountingData.max_int = CountingData.current_int
                await latest_message.add_reaction('✅')
            else:
                await latest_message.add_reaction('☑️')
            CountingData.current_int += 1
        else:
            await latest_message.add_reaction('❌')
            if CountingData.current_lives > 0:
                CountingData.current_lives -= 1
                await channel.send(
                    f'Incorrect number! The next number is {CountingData.current_int}. You have {CountingData.current_lives} left.',
                    reference=latest_message)
            else:
                CountingData.reset_lives()
                CountingData.reset_current_int()
                await channel.send(
                    f'Incorrect number! You\'ve used all your lives, so start it all over! The next number is {CountingData.current_int}!',
                    reference=latest_message)