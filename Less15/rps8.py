import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    
    game_count = 0
    player_wins = 0
    python_wins = 0
    game_ties = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_ties
        
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        acceptedInput = {'1', '2', '3'}
        
        playerChoice = input(f"\n{name}, please enter...\n1 for rock, \n2 for paper or \n3 for Scissors:\n\n")
        
        if playerChoice in acceptedInput:
            player = int(playerChoice)
        else:
            print(f"{name}, please enter a valid input of 1, 2, or 3")
            return play_rps()
            
        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            nonlocal game_ties
        
            if player ==  1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player ==  2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player ==  3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                game_ties += 1
                return "😑 You tied."
            else:
                python_wins += 1
                return f"👺 Python wins...\nsorry {name}"
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1    

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(f"\nPython Wins: {python_wins}")
        print(f"\nTied Games: {game_ties}")

        print(f"\nPlay again, {name}?")
        
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
                sys.exit(f"Peace {name}! ✌️")
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )
    
    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

