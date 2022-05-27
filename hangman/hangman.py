import random
from time import sleep
from hangman_wordlist import wordlist
from hangman_art import logo, stages


print(logo)

print('Welcome to Hangman Game!')
answer = 'y'
while answer == 'y':
    print('Let me think of a word...')
    sleep(2.5)
    chosen_word = random.choice(wordlist)
    print(f'The word contains {len(chosen_word)} letters.')
    spaces = ['_'] * len(chosen_word)
    print(*spaces)
    lives = 7
    guessed = 0
    while lives != 0 and guessed != len(chosen_word):
        guess = input('Guess a letter: ')
        sleep(1)
        if guess in set(chosen_word):
            for i in range(0, len(chosen_word)):
                if chosen_word[i] == guess:
                    spaces[i] = guess
                    guessed += 1
            print(*spaces)
        else:
            lives -= 1
            print(stages[lives])
    else:
        if guessed == len(chosen_word):
            answer = input(f'Congratulations, you won!\nWanna try again? y/n ')
        elif lives == 0:
            answer = input(f'Sorry, you lost. The word was {chosen_word}.\nWanna try again? y/n ')
