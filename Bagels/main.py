# My solution (might not be perfect, open to suggestions)

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num() -> str:
    all_nums = list('0123456789')
    random.shuffle(all_nums)
    secret_num = ''
    for i in range(0, NUM_DIGITS):
        secret_num += all_nums[i]
    return secret_num

def get_clues(secret_num: str, guess: str):
    result = []
    has_bagels = True
    for i in range(0, NUM_DIGITS):
        if secret_num[i] in guess:
            has_bagels = False
            if secret_num[i] == guess[i]:
                result.append('Fermi')
            else:
                result.append('Pico')
    if has_bagels:
        result.append('Bagels')

    return result


def game():
    print('''Bagels, a deductive logic game.
     By Al Sweigart al@inventwithpython.com
     
     I am thinking of a {}-digit number with no repeated digits.
     Try to guess what it is. Here are some clues:
     When I say:    That means:
     Pico         One digit is correct but in the wrong position.
     Fermi        One digit is correct and in the right position.
     Bagels       No digit is correct.
     
     For example, if the secret number was 248 and your guess was 843, the
     clues would be Fermi Pico.'''.format(NUM_DIGITS))
    game_life = True

    # game loop
    while game_life:
        correct = False
        remaining_chances = MAX_GUESSES
        secret_num = get_secret_num()
        print('I have thought up a number.')
        # secret_num = '962'
        # print('secret_num= ',secret_num)
        while remaining_chances and not correct:
            print('remaining_chances: {}'.format(remaining_chances),end='\n')
            guess = input('> ')
            if len(guess) > NUM_DIGITS or len(guess) < NUM_DIGITS:
                print('Please enter a number of {} digits.'.format(NUM_DIGITS), 'Try again!\n')
            elif guess == secret_num:
                print('You got it!')
                correct = True
                print('Do you want to play it again? (yes or no)\n')
                choice = input('> ')
                if choice == 'no':
                    game_life = False
            else:
                clues = get_clues(secret_num, guess)
                for clue in clues:
                    print(clue, end=' ')
                print()

            remaining_chances-=1
        if remaining_chances == 0:
            print('Do you want to play again? (yes or no)')
            play = input('> ')
            if play == 'no':
                game_life = False
    print('Thanks for playing the game!')


if __name__ == '__main__':
    game()
