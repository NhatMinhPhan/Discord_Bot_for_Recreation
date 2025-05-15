import random
from typing import Tuple

def generate_move() -> str:
    """
    Generate a random move in rock paper scissors.
    :return: 'rock', 'paper' or 'scissors'
    """
    move_int = random.randint(1, 3)
    match move_int:
        case 1:
            return 'rock'
        case 2:
            return 'paper'
        case 3:
            return 'scissors'

def interpret_move(move: str) -> str:
    """
    Interpret the player's move/input and return the interpretation accordingly.
    :param move: 'rock', 'paper', 'scissors', any legible variations thereof and emojis corresponding to them
    :return: 'rock', 'paper', 'scissors', or 'invalid'
    """
    assert isinstance(move, str), 'move is not a string'
    move = move.strip().lower()
    if move == 'rock' or move == 'paper' or move == 'scissors':
        return move

    rock_emojis = {'🪨', '🗿'}
    paper_emojis = {'📄', '📝', '📃', '📜', '🗒', '📋', '📑'}
    scissors_emojis = {'✂️'}

    if move in rock_emojis:
        return 'rock'
    elif move in paper_emojis:
        return 'paper'
    elif move in scissors_emojis:
        return 'scissors'
    return 'invalid'

def compare_moves(a: str, b: str) -> str:
    """
    Compare moves between a and b
    :param a: 'rock', 'paper', or 'scissors'
    :param b: 'rock', 'paper', or 'scissors'
    :return: 'a' if a wins, 'b' if b wins, 'neither' otherwise
    """
    valid_inputs = {'rock', 'paper', 'scissors'}
    assert a in valid_inputs, 'a is not a valid input'
    assert b in valid_inputs, 'b is not a valid input'
    if a == b:
        return 'neither'

    if a == 'rock':
        if b == 'scissors':
            return 'a'
        elif b == 'paper':
            return 'b'
    elif a == 'paper':
        if b == 'rock':
            return 'a'
        elif b == 'scissors':
            return 'b'
    elif a == 'scissors':
        if b == 'paper':
            return 'a'
        elif b == 'rock':
            return 'b'

def versus_computer(player_move: str) -> Tuple[str, str]:
    """
    Compare moves between the player and the computer.
    If the player wins, return True.
    Return False otherwise.
    :param player_move: the player's move as a string value (text or emoji)
    :return: A tuple of 'player' if the player wins, or 'computer' if the computer wins, or 'neither' otherwise, followed by the computer's move
    """
    player: str = interpret_move(player_move)
    computer: str = generate_move()

    result = compare_moves(player, computer)
    match result:
        case 'neither':
            return 'neither', computer
        case 'a':
            return 'player', computer
        case 'b':
            return 'computer', computer

if __name__ == '__main__':
    move = ''
    while move != 'quit':
        move = input('Next move: ')
        if move == 'quit':
            break
        res = versus_computer(move)
        match res[0]:
            case 'neither':
                print(f'Computer played: {res[1]}\nA tie!')
            case 'player':
                print(f'Computer played: {res[1]}\nYou won!')
            case 'computer':
                print(f'Computer played: {res[1]}\nComputer won!')