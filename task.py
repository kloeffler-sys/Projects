print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1= input('You are at a crossroads, which way would you like to turn? type "left" or "right": ')


if choice1 == 'left':
   choice2= input("You come across a lake with an island in the middle will you 'wait' for a boat or 'swim' across?: ")
   if choice2 == 'wait':
        choice3=input("after boating to the island, you find three doors in a cliff \
    will you enter the 'red', 'yellow, or 'blue' one?")

        if choice3 == 'blue':
            print("You open the blue door to a hungry group of lions,\
    there is a moment of silence before they leap at you, game over.")

        elif choice3 == 'red':
            print("You walk into the red door expecting treasure, \
    but it was a door to the magma pool in the island and you fell in. Game over.")

        elif choice3 == 'yellow':
            print("You genius! the yellow door made of gold was the vault door!\
     you found the riches! game over.")

        else:
            print("You decide to try to make a different door in the cliff,\
     and then God smites you for being so foolish, game over.")
   else:
        print("While Swimming, you feel something brush past your leg, \
    then you are drug under. Game over.")
else:
    print("you fall down a hole, game over")