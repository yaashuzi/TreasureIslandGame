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

#User's option selection
user_option = input("You're on the island, yes... ik what you're thinking now, put that thinking to work and tell me... Where do you want to go?,\nLeft or Right? ").lower()

#Option right or anything else
if user_option == 'right':
    print("You got blinded by a spell... You fell into a hole.\nGame Over.")

#option left
elif user_option == 'left':
    print("You're Safe, There's an ocean infront of you... Swim or Wait??")
    left_option = input('Swim or Wait?').lower()

    if left_option == 'swim':
        print("You thought you made the right call, as you're swimming to the island, 3 sharks came from below and starts to circle around you and you're cooked... \nGame Over.")

    # option door select
    elif left_option == 'wait':
        door_option = input("You can't swim through ocean like that, you made the right call to wait, and 3 magical door faded in front of you which is leaking a white light, you don't know where it goes, which door you picking?\nRed, Blue or Yellow?").lower()
        #red
        if door_option == 'red':
            print("You entered the red door... the door closed on you and fire starts melting you from below... ,\nIt's Game Over.")
        #blue
        elif door_option == 'blue':
            print("You're favourite color must be blue... Eaten by beasts,\nGame Over.")
        #yellow
        elif door_option == 'yellow':
            print("You Won!, You found the treasure!")
        else:
            print("I SAID!, RED, BLUE or YELLOW!")

else:
    print("Invalid Option. Please try again.")

#if multiple output allowed; use if + if
#if single output allowed; use if + elif