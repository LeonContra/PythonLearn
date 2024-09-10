import sys
import random
from enum import Enum

def rps():
    
    game_count = 0
    player_wins = 0
    python_wins = 0
    game_ties = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_ties
        
        
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
            nonlocal player_wins
            nonlocal python_wins
            nonlocal game_ties
        
            if player ==  1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player ==  2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player ==  3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                game_ties += 1
                return "😑 You tied."
            else:
                python_wins += 1
                return "👺 Python wins..."
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1    

        print("\nGame count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nPython Wins: " + str(python_wins))
        print("\nTied Games: " + str(game_ties))

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
    return play_rps

play = rps()

play()