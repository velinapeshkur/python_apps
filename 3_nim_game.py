from random import randint
from time import sleep


def easy_level(sticks):
    if sticks > 3:
        return randint(1, 3)
    return randint(1, sticks)


def hard_level(sticks):
    if sticks >= 5:
        if 1 <= sticks % 5 <= 3:
            return sticks % 5
        return 1
    return sticks - 1


print('This is a game called Nim, in which you can play against your computer. '
      f'\nThe rules are simple: '
      f'\nYou have 10 sticks. A player must pick up from 1 to 3 sticks during each move.'
      f'\nWhoever picks up the last stick loses. Are you ready to start? (y/n)')
answer = input()
while answer == 'y':
    sticks = 10
    n = 1
    sleep_time = 1.2
    level = input('Choose difficulty level: (e-easy, h-hard)\n')
    while level != 'e' and level != 'h':
        level = input('Wrong input. Please enter "e" or "h": ')
    while sticks > 0:
        print(f'You have {sticks} sticks left.')
        if n % 2 == 1:
            my_move = int(input('Your move! Enter the number of sticks: '))
            while my_move > 3 or my_move == 0:
                my_move = int(input('Wrong number! Please enter the number between 1 and 3: '))
            sticks -= my_move
            n += 1
        else:
            if level == 'e':
                pc_move = easy_level(sticks=sticks)
            else:
                pc_move = hard_level(sticks=sticks)
            print('PC move: ', end='', flush=True)
            sleep(sleep_time)
            sleep_time += 1
            print(pc_move)
            sticks -= pc_move
            n += 1
    else:
        print('You have 0 sticks left')
        if n % 2 == 0:
            print('Sorry, PC wins :(')
        else:
            print('Congratulations, you win!')
    answer = input('Would you like to play again? (y/n)\n')
else:
    print('See you next time!')
