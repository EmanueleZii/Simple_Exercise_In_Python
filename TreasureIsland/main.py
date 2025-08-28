Treasure= '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************


'''

print(Treasure)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")

if answer == "left":
    print("GameOver you fell into a trap.")
elif answer == "right":
    print("You went right. You found a swim!")
    if input("Do you want to swim or wait? Type 'swim' or 'wait'") == "swim":
        print("GameOver you were attacked by a trout.")
    else:
        print("You waited and found a three Door!")
        if input("Do you want to open the door or go back? Type 'open' or 'back'") == "open":
            print("Congratulations! You found the treasure!")
        else:
            print("You went back and fell into a trap.")
else:
    print("Invalid choice. Please type 'left' or 'right'.")

