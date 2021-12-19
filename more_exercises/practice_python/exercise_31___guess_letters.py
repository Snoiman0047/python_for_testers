"""
Create software that will play the "Cows and Bulls" game with the user. The game works like this:
Randomly create a 4-digit number. Ask the user to guess a 4-digit number. For each digit that-
The user guessed right in the right place, he has a "cow". For each digit the user guessed
In the right place is a "bull." Each time the user guesses, tell him how many
They have "cows" and "bulls." Once the user guesses the correct number, the game is over.
Keep track of the guesses the user makes throughout the game and tell the user at the end
his guess history and of course the number of guesses.
(https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html - question link)
"""

import re
import random


def create_list(sentence):
    guess_list = ['_' for i in range(len(sentence))]
    return modify_list(guess_list, ' ', sentence)


def modify_list(result, guess, answer):
    """
    Print all the key in dict.

    Arguments:
    result -- a list of the show pattern word.
    guess -- the letter of user's guess.
    answer -- the answer of word

    Returns:
    result -- the list of word after modified.

    """
    if guess in answer:
        index_list = [x.start() for x in re.finditer(guess, answer)]
        for i in index_list:
            result[i] = guess
    else:
        print(f"Oops, letter '{guess}' is not in the word")
    print(''.join(result))
    return result


def win(word_list):
    """
    Check the user has guessed the right word or not.

    Arguments:
    word_list -- the word list.

    Returns:
    True/False -- return True if the word has been guessed right also return false.
    """
    if '_' not in word_list:
        return True
    else:
        return False


def random_sentence(_file_name):
    with open(_file_name, "r") as _file:
        lines = _file.readlines()
        sentences = [line.rstrip() for line in lines]
    return (random.choice(sentences))[:-1]


def start_game():
    play = 'y'
    while play.lower() == 'y' or play.lower() == 'yes':
        print(f'\nWelcome to Hangman!\n')
        right_answer = random_sentence('sentences')
        guess_list = create_list(right_answer)
        guess_count = 0
        while True:
            guess = input('Guess your letter: ')
            guess_count += 1
            guess_list = modify_list(guess_list, guess, right_answer)
            if win(guess_list):
                print(f'\nYou win! ({guess_count} guesses)')
                break
        play = input('\n\nCome on, streaming with me on another game? ')

start_game()
