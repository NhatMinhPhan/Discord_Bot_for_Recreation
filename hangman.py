import requests
import json
from typing import List, Union

class HangmanData:
    current_guess = ''
    solution = ''
    hangman_lives = 6
    INITIAL_LIVES = 6
    is_ready = False
    incorrect_letters = []

    @staticmethod
    def is_finished() -> bool:
        """
        Returns if the ongoing game of hangman is finished by checking if the current guess matches the solution
        :return: a boolean value
        """
        return HangmanData.solution == HangmanData.current_guess

def fetch_word(length: int = -1) -> str:
    """
    Return a random word from Random Word API.
    If length >= 1, return a random word which is 'length' characters long.
    Otherwise, return a random word of any length.
    :param length: length of the word to be returned. If length <= 0, the word can be of any length.
    :return: a random word of string type
    """
    assert isinstance(length, int), 'length is not an int'
    if length >= 1:
        response = requests.get(f'https://random-word-api.herokuapp.com/word?length={length}').text
        return json.loads(response)[0]
    else:
        response = requests.get('https://random-word-api.herokuapp.com/word').text
        return json.loads(response)[0]

def fetch_words(quantity: int, word_length: int = -1) -> List[str]:
    """
    Return a list of random words from Random Word API.
    If length >= 1, return random words which is 'length' characters long.
    Otherwise, return random words of any length.
    :param quantity: the number of words to be returned
    :param word_length: length of the words to be returned. If length <= 0, the words can be of any length.
    :return: a list of words of string type
    """
    assert isinstance(quantity, int), 'quantity is not an int'
    assert isinstance(word_length, int), 'word_length is not an int'
    assert quantity > 0, 'quantity is not above 0'
    if word_length >= 1:
        response = requests.get(f'https://random-word-api.herokuapp.com/word?length={word_length}&number={quantity}').text
        return json.loads(response)
    else:
        response = requests.get(f'https://random-word-api.herokuapp.com/word?number={quantity}').text
        return json.loads(response)

def set_up(word_length: int = -1, *, startswith: Union[str, None] = None, endswith: Union[str, None] = None) -> None:
    """
    Set up a Hangman game and HangmanData to facilitate the game.
    :param word_length: length of the word to be guessed. If word_length <= 0, the word can be of any length.
    :param startswith: Keyword-only. The character or sequence of characters that the word must start with if it is not set to None.
    :param endswith: Keyword-only. The character or sequence of characters that the word must end with if it is not set to None.
    :return: None
    """
    assert isinstance(word_length, int), 'word_length is not an int'
    assert startswith is None or isinstance(startswith, str), 'startswith is neither None or a str'
    assert endswith is None or isinstance(endswith, str), 'endswith is neither None or a str'

    word = ''

    if startswith is None and endswith is None:
        word = fetch_word(word_length)
    elif startswith:
        while len(word) == 0 or word[0] == startswith:
            word = fetch_word(word_length)
    elif endswith:
        word = fetch_word(word_length)

    HangmanData.solution = word
    HangmanData.current_guess = '?' * len(word)
    HangmanData.is_ready = True
    HangmanData.hangman_lives = HangmanData.INITIAL_LIVES
    HangmanData.incorrect_letters.clear()

def guess(response: str) -> bool:
    """
    Determine if response is correct and adjust data accordingly.
    :param response: User's response
    :return: True if correct, False otherwise.
    """
    assert isinstance(response, str), 'response is not a str'
    response = response.strip() # Strips whitespace
    assert len(response) == 1, 'response is not 1 character long'
    assert response.isalpha(), 'response consists of a NON-alphabetical character'
    response = response.lower()
    if response in HangmanData.solution:
        start_index = -1
        while HangmanData.solution.find(response, start_index + 1) >= 0:
            start_index = HangmanData.solution.find(response, start_index + 1)
            HangmanData.current_guess = HangmanData.current_guess[:start_index] + response + \
                                        HangmanData.current_guess[start_index + 1:]
        if HangmanData.is_finished():
            HangmanData.is_ready = False
        return True

    else:
        HangmanData.hangman_lives -= 1
        if response not in HangmanData.incorrect_letters:
            HangmanData.incorrect_letters.append(response)
        if HangmanData.hangman_lives == 0:
            HangmanData.is_ready = False
        return False

"""
def set_up(word_length: int = -1, *, startswith: Union[str, None] = None, endswith: Union[str, None] = None) -> None:
    assert isinstance(word_length, int), 'word_length is not an int'
    assert startswith is None or isinstance(startswith, str), 'startswith is neither None or a str'
    assert endswith is None or isinstance(endswith, str), 'endswith is neither None or a str'

    word = ''

    if startswith is None and endswith is None:
        word = fetch_word(word_length)
    elif startswith:
        while len(word) == 0 or word[0] == startswith:
            word = fetch_word(word_length)
    elif endswith:
        word = fetch_word(word_length)

    HangmanData.solution = word
    HangmanData.current_guess = '*' * len(word)
    HangmanData.is_ready = True
    HangmanData.hangman_lives = HangmanData.INITIAL_LIVES
    HangmanData.incorrect_letters.clear()
    print(f'BEGIN: {HangmanData.current_guess}')
    print(f'You have {HangmanData.hangman_lives} lives left.')
"""
"""
def guess(response: str) -> bool:
    assert isinstance(response, str), 'response is not a str'
    response = response.strip() # Strips whitespace
    assert len(response) == 1, 'response is not 1 character long'
    assert response.isalpha(), 'response consists of a NON-alphabetic character'
    response = response.lower()
    if response in HangmanData.solution:
        start_index = -1
        while HangmanData.solution.find(response, start_index + 1) >= 0:
            start_index = HangmanData.solution.find(response, start_index + 1)
            HangmanData.current_guess = HangmanData.current_guess[:start_index] + response + \
                                        HangmanData.current_guess[start_index + 1:]
        if not HangmanData.is_finished():
            print(f'Correct! Now we have: {HangmanData.current_guess}')
        else:
            print(f'That\'s right! The answer is: \'{HangmanData.solution}\'!')
            HangmanData.is_ready = False
        return True

    else:
        HangmanData.hangman_lives -= 1
        HangmanData.incorrect_letters.append(response)
        if HangmanData.hangman_lives > 0:
            print(f'Incorrect! You now have {HangmanData.hangman_lives} lives left.')
            print(f'Incorrect letters: {HangmanData.incorrect_letters}')
        else:
            print(f'Incorrect! You\'re now out of lives!')
            print(f'The answer is \'{HangmanData.solution}\'!')
        return False
"""

"""
if __name__ == '__main__':
    set_up(5)
    while HangmanData.solution != HangmanData.current_guess and HangmanData.hangman_lives > 0:
        user_input = input('Guess: ')
        guess(user_input)
"""