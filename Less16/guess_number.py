import sys
import random
from enum import Enum

def guessNum(name='PlayerOne'):
    
    game_count = 0
    player_wins = 0

    def play_guessNum():
        nonlocal name
        nonlocal player_wins

        acceptedInput = {'1', '2', '3'}
        
        playerChoice = input(f"\n{name}, can you guess which number I'm thinking of? I'll make it easy, choose 1, 2, or 3\n\n")
        
        if playerChoice in acceptedInput:
            player = int(playerChoice)
        else:
            print(f"{name}, I said 1, 2, 3. I'm trying to make it easy for ya.")
            return play_guessNum()
            
        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print(f"\n{name}, you chose {player}.\n")
        print(f"I was thinking of the number {computer}...\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
        
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you guessed right! Congrats!"
            else:
                return f"👺 Yikes. Looks like you guessed wrong. Too bad, {name}"
        
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1    

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s Wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay again, {name}?")
        
        while True:
        
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
                return play_guessNum()
        else:
                print("\nBYE BYE 👋👋👋")
                print("Thank you for playing!\n")
                #sys.exit(f"Peace {name}! ✌️")
            
    return play_guessNum



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
    
    guess_number = guessNum(args.name)
    guess_number()

