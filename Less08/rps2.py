import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

acceptedInput = {'1', '2', '3'}

playagain = True

while playagain:
    
    playerChoice = input("\nEnter...\n1 for rock, \n2 for paper or \n3 for Scissors:\n\n")

    player = int(playerChoice) if playerChoice in acceptedInput else sys.exit("Input must be a number")
        

    if player < 1 or player > 3: 
        sys.exit("You must enter 1, 2, or 3")
        
    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player ==  1 and computer == 3:
        print("🎉 You win!")
    elif player ==  2 and computer == 1:
        print("🎉 You win!")
    elif player ==  3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😑 You tied.")
    else:
        print("👺 Python wins...")
        
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\nBYE BYE 👋👋👋")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Peace! ✌️")