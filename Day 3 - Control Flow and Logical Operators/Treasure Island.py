print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_step = input('You have found an intersection, to your left, you can see in the distance an ominous body of water and to the right, you can see a thick jungle. You must choose: left or right?')
if first_step == 'left':
    second_step = input('You come closer to the body of water and find that it is a seemingly shallow river. You are unsure whether to swim or wait for someone to come, hopefully with a boat. You must choose: swim or wait? ')
    if second_step == 'wait':
        third_step = input('You wait and wait and seemingly no one will come...nor hear you. Until out of the blue water a mysterious figure offers you a ride accrooss the river. You accept the offer. On the other side you can see in the distance a temple with 3 doors, one red, one blue and one yellow. Which one do you believe holds the treasure: red, blue or yellow?')
        if third_step == 'red':
            print('You attempt to open the red door. It is heavy. You push and push and with each attempt you feel the door budge and the brigness from within shines. You manage to almost open the door fully when you start to feel the heat. You keep pushing, your flesh starting to hurt. The door is almost open... You hear a loud roar and before you can look around a giant ball of fire swallows you whole.\nGame over.')
        elif third_step == 'blue':
            print('You attempt to open the blue door. It is heavy. You push and push and with each attempt you feel the door opening a bit more. You start to hear noise from inside, could it be, another adventurer, or the sound of air passing trough. You keep pushing, the sound becomes louder. The door is almost open... You hear a loud roar and before you can look around a pack of wild beasts leap towards you.\nGame over.')
        elif third_step == 'yellow':
            print('You attempt to open the yellow door. It is heavy. You push and push and with each attempt you feel the door opening a bit more. With the last bit of your strength you open the door just enough to pass trough. Exhausted, but with high morale you attempt to traverse the temple. After a few minutes of walking you start to hear the flickering of a fire. In the distance, you can almost see a glow. What could it be. A few meters more and you are presented with the golden light of the coveted treasure.\nCongratulations! You win! ')
        else:
            print('You decide adventure is not for you, not after you took that arrow to the knee all those years ago.\nGame over.')
    else:
        print('You attempt to cross the river. You swim for a few minuts and hear something strangebehind you. You turn around hoping to meet a friendly fish, however what you see is a hungry trout. The trout observes you for a second and with lightning fast attack it kills you.\nGame over.')
else:
    print('You attempt to pass trough the jungle, however you fall in a hidden trap and meet your demise.\nGame Over.')

print("\nPress any key to exit...")
input()