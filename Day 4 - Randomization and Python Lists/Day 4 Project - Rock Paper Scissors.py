import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

print('Computer chose:')

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_input == computer_choice:
    print('Draw')
elif user_input == 0 and computer_choice == 2:
    print('You win')
elif user_input == 1 and computer_choice == 0:
    print('You win')
elif user_input == 2 and computer_choice == 1:
    print('You win')
else:
    print('You lose')

print("\nPress any key to exit...")
input()
