This is a rough draft for README.md

This is a bot which is not reliant on any use of a database and is programmed for practice and non-professional purposes.
This bot facilitates activities comprising of counting, hangman and rock paper scissors.

Enter /help for commands.

NOTE: The .env file was accidentally committed, and therefore all the data contained thereof have been reset, removed or revoked.

__________________________________________________________________________________________
## COMMANDS
## General:
    `/help`: Get available commands from this bot
    `/hey`: Say hey to the bot!
    `/hello`: Say hello to the bot!
    
## Administrative:
    `/get_admin_roles`: Get a list of the admin roles for this server (Admins-only)
    `/update_admin_roles`: Update admin roles for this bot with names (Admins-only if admin roles for this bot have been set)
    `/reset_admin_roles`: Reset admin roles for this bot (Admins-only if admin roles for this bot have been set)
    
## Counting (only works in #counting channel):
    `/counting_mode`: Check the status of the counting mode (ON/OFF)
    `/toggle_counting`: Toggle the status of the counting mode (ON/OFF) (Admins-only)
    `/one_number_per_user`: Check the status of the one_number_per_user setting for counting (ON/OFF)
    `/toggle_one_number_per_user`: Toggle the status of the one_number_per_user setting for counting (ON/OFF) (Admins-only)
    `/counting_lives`: Check the number of lives remaining before the counting game is reset
    `/counting_info`: Return all information about the counting game
    `/counting_high_score`: Check the high score achieved in the counting game
    `/set_max_lives_to <positive-integer>` : Set the number of max counting lives to a certain positive integer (Admins-only)
    
## Hangman (only works in #hangman channel):
    `/new_hangman <Optional: word-length>`: Create or reset a new hangman game played only in #hangman
    `/hangman_guess <letter>`: Guess a letter for an ongoing game of hangman only in #hangman if there is one
    `/end_hangman`: Terminate any ongoing game of hangman. This works only in #hangman.
    `/hangman_progress`: Show the used letters and the answer so far for the current game of hangman
    
## Rock paper scissors:
    `/rps-cast <move (rock, paper, scissors or corresponding emoji)>`: Play rock paper scissors with the bot!
__________________________________________________________________________________________
© Nhat Minh Phan, 2025
