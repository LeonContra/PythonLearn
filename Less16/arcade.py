import sys
from rps import rps
from guess_number import guessNum

def arcade(name="Player"):
    
    print(f"\n{name}, welcome to the Arcade! 🎮\n")
    
    acceptedInput = {'1', '2', 'x', 'X'}
    
    def startArcade():
        
        playerChoice = input(f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess my number\nOr 'x' to exit the Arcade\n")
    
        if playerChoice not in acceptedInput:
            print(f"\n{name}, please enter a valid value of 1, 2, or x\n")
            return startArcade()
        else:
            decideGame(playerChoice)
    
    def decideGame(player):
        if(player == "1"):
            print("\nYou chose Rock Paper Scissors\n")
            rockPS = rps(name)
            rockPS()
        elif(player == "2"):
            print("\nYou chose Guess my Number\n")
            guessGame = guessNum(name)
            guessGame()
        else:
            print("\nGoodBye! 👋👋👋")
            print("\nThanks for stopping by the Arcade!\n")
            sys.exit(f"Peace {name}! ✌️")
        
        print(f"\n{name}, Hey there!, welcome back to the Arcade!\n")
        startArcade()
    
    startArcade()
    
    

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )
    

    args = parser.parse_args()

    arcade(args.name)