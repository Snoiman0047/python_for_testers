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


def init_game():
    import random
    print('Welcome to the Cows and Bulls Game!\n'
          'I will generate a number, and you have to guess the numbers one digit at a time.\n'
          'For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.\n'
          'The game ends when you get 4 bulls!\n'
          'Type exit at any prompt to exit.')
    return True, [''], '{0:04d}'.format(random.randint(0, 9999))


def get_guess(guess_log):
    guess_log.append(input('\nGuess the number: '))
    return guess_log


def calc_cow_bull(guess, answer):
    cow, bull = 0, 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            cow += 1
        if guess[i] in answer:
            bull += 1
    return cow, bull - cow


def start_game():
    playing, guess_log, answer = init_game()
    while playing:
        guess_log = get_guess(guess_log)
        if guess_log[-1] == 'exit':
            break
        cow, bull = calc_cow_bull(guess_log[-1], answer)
        if cow == 4:
            print(f'Your are right! After {len(guess_log) - 1} guess/es you finally get it!\n'
                  f'Your guessing history {guess_log[1:]}')
            play = input('\n\nCome on, streaming with me on another game? ')
            if play.lower() == 'y' or play.lower() == 'yes':
                print('\n' * 6)
                start_game()
        else:
            print(f"Your guess isn't quite right, try again.\n{cow} cows, {bull} bulls")


start_game()
