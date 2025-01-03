from art import logo, vs
from game_data import data
import random
import os 

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):

    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
try_again = True

while game_should_continue:

    account_a = account_b

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        score = 0
            
        try_again_input = input(f"Do you want to try again? Press 'Y' or 'N'. ").lower()

        if try_again_input == "n":
            try_again == False
            game_should_continue = False
            exit()
        elif try_again_input == "y":
            game_should_continue = True
