This is a Discord bot which is not reliant on databases and is programmed for practice and non-professional purposes.
This bot facilitates activities comprising of counting, hangman and rock paper scissors.

Enter /help for commands.

The following libraries and packages are crucial in this bot's operations, all of which were installed via the Python PIP:
_Discord.py, requests,_ and _python-dotenv_. The [Random Word API](https://random-word-api.herokuapp.com/home) is also integrated for the hangman features.

### Instructions
1. Install the libraries above: _Discord.py, requests,_ and _python-dotenv_.
2. Once all the libraries above are installed, an .env file is to be created, which must include the following information:
- DISCORD_TOKEN: the token of the Discord bot for which the Python scripts are to run
- MY_SERVER: the ID of the Discord server in which the Discord bot runs
3. Ensure all the Python scripts and the .env file must be in the same directory.
4. Run [main.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/main.py). And that's it!

### Description of individual files
- [main.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/main.py): The file to be executed, containing slash commands and other information relating to the setup of the Discord bot.
- [admin.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/admin.py): The script dealing with setting up and managing administrator roles for admins-only slash commands.
- [counting.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/counting.py): The script that processes counting messages, which originate only from the #counting channel.
- [hangman.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/hangman.py): The script that facilitates games of hangman, whose functions are called only by messages from the #hangman channel.
- [rockpaperscissors.py](https://github.com/NhatMinhPhan/Discord_Bot_for_Recreation/blob/db637f08f70c37aaed770f3d2eb3de232d29d254/rockpaperscissors.py): The script that allows the Discord bot to engage in a game of rock paper scissors, in response to the original message which invokes the bot. Unlike counting.py and hangman.py, all of the slash commands that start with rock paper scissors can be used anywhere in the server.

__________________________________________________________________________________________
# Slash Commands
## General
    `/help`: Get available commands from this bot
    `/hey`: Say hey to the bot!
    `/hello`: Say hello to the bot!
    
## Administrative
    `/get_admin_roles`: Get a list of the admin roles for this server (Admins-only)
    `/update_admin_roles`: Update admin roles for this bot with names (Admins-only if admin roles for this bot have been set)
    `/reset_admin_roles`: Reset admin roles for this bot (Admins-only if admin roles for this bot have been set)
    
## Counting (only works in #counting channel)
    `/counting_mode`: Check the status of the counting mode (ON/OFF)
    `/toggle_counting`: Toggle the status of the counting mode (ON/OFF) (Admins-only)
    `/one_number_per_user`: Check the status of the one_number_per_user setting for counting (ON/OFF)
    `/toggle_one_number_per_user`: Toggle the status of the one_number_per_user setting for counting (ON/OFF) (Admins-only)
    `/counting_lives`: Check the number of lives remaining before the counting game is reset
    `/counting_info`: Return all information about the counting game
    `/counting_high_score`: Check the high score achieved in the counting game
    `/set_max_lives_to <positive-integer>` : Set the number of max counting lives to a certain positive integer (Admins-only)
    
## Hangman (only works in #hangman channel)
    `/new_hangman <Optional: word-length>`: Create or reset a new hangman game played only in #hangman
    `/hangman_guess <letter>`: Guess a letter for an ongoing game of hangman only in #hangman if there is one
    `/end_hangman`: Terminate any ongoing game of hangman. This works only in #hangman.
    `/hangman_progress`: Show the used letters and the answer so far for the current game of hangman
    
## Rock paper scissors
    `/rps-cast <move (rock, paper, scissors or corresponding emoji)> <ephemeral (If True, the message will only be seen by you)>`: Play rock paper scissors with the bot!
__________________________________________________________________________________________
© Nhat Minh Phan, 2025
