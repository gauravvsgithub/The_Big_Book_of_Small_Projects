# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


def game():
    print("""
        Bagels, a deductive logic game.
        By Al Sweigart al@inventwithpython.com
        I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say:    That means:
          Pico         One digit is correct but in the wrong position.
          Fermi        One digit is correct and in the right position.
          Bagels       No digit is correct.
        I have thought up a number.
         You have 10 guesses to get it.
    """)
    game_life = True

    # game loop
    while game_life:

        correct = False
        remaining_chances = MAX_GUESSES
        secret_num = get_secret_num()
        print('secret_num= ',secret_num)
        while remaining_chances and not correct:
            guess = input('> ')
            if guess == secret_num:
                print('You got it!')
                correct = True
                print('Do you want to play it again? (yes or no)')
                choice = input('> ')
                if choice == 'no':
                    game_life = False
            else:
                print('Try again!')
        print('Thanks for playing the game!')


if __name__ == '__main__':
    game()
