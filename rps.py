import sys
import random
from enum import Enum

class rps(Enum):
    Rock = 1
    Paper =2
    Stone = 3

print("welcome to rock paper scissor Game....!")
print("1. Rock \n2. Paper\n3. Scissors")
playerchoice = int(input("Enter your choice:"))

print(playerchoice)

if playerchoice < 1 or playerchoice >= 3 :
    sys.exit("you must enter valid options. ")

computerchoice = random.randint(1,3)
print(computerchoice)



print("you chose : " + str(rps(playerchoice)).replace('rps.',''))
print("computer chose : " + str(rps(computerchoice)).replace('rps.',''))

if playerchoice == 1 and computerchoice == 3:
    print("You win...👑")
elif playerchoice == 2 and computerchoice == 1:
     print("You win...👑")
elif playerchoice == 3 and computerchoice == 2:
     print("You win...👑")
elif playerchoice == computerchoice :
     print("Tie Game...😊")

else :
    print("computer Win, You Lose...😒")