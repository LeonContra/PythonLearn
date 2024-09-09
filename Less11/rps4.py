import sys
import random
from enum import Enum

game_count = 0

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

    def decide_winner(player, computer):
        if player ==  1 and computer == 3:
            return "🎉 You win!"
        elif player ==  2 and computer == 1:
            return "🎉 You win!"
        elif player ==  3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😑 You tied."
        else:
            return "👺 Python wins..."
    
    game_result = decide_winner(player, computer)
    
    print(game_result)
    
    global game_count
    game_count += 1    

    print("\nGame count: " + str(game_count))

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