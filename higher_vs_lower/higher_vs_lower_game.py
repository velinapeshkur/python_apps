import os
import random
from art import logo, vs
from game_data import data


def generate_options(option_a):
    if option_a is None:
        option_a = random.randint(0, len(data) - 1)
    option_b = random.randint(0, len(data) - 1)
    while option_b == option_a or data[option_a]['follower_count'] == data[option_b]['follower_count']:
        option_b = random.randint(0, len(data) - 1)
    return option_a, option_b


def compare_two(option_a, option_b):
    if data[option_a]['follower_count'] > data[option_b]['follower_count']:
        right_choice = 'A'
    else:
        right_choice = 'B'
    print(f"Compare A: {data[option_a]['name']}, {data[option_a]['description']} from {data[option_a]['country']}")
    print(vs)
    print(f"Against B: {data[option_b]['name']}, {data[option_b]['description']} from {data[option_b]['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    while user_choice not in ('A', 'B'):
        user_choice = input(f"Sorry, there is no option '{user_choice}'. Please type 'A' or 'B': ").upper()
    return user_choice == right_choice


def play_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    score = 0
    option_a, option_b = generate_options(option_a=None)
    is_right = compare_two(option_a=option_a, option_b=option_b)
    while is_right:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}")
        option_a, option_b = generate_options(option_a=option_b)
        is_right = compare_two(option_a=option_a, option_b=option_b)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        if_continue = input('Would you like to play again? (y/n): ')
        if if_continue == 'y':
            play_game()


play_game()
