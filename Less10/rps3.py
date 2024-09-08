import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    acceptedInput = {'1', '2', '3'}
    
    playerChoice = input("\nEnter...\n1 for rock, \n2 for paper or \n3 for Scissors:\n\n")
    
    if playerChoice in acceptedInput:
        player = int(playerChoice)
    else:
        print("Incorrect value")
        return play_rps()
        
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
        
    print("\nPlay again?")
    
    while True:
    
        playagain = input("\nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
            return play_rps()
    else:
            print("\nBYE BYE 👋👋👋")
            print("Thank you for playing!\n")
            sys.exit("Peace! ✌️")

play_rps()