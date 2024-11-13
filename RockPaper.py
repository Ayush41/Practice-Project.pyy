# ROck Paper Scissors Game

import random
def play_game():
    options = ["rock","paper","scissors"]
    userChoice = input("Enter rock,paper or scissors :-").lower()
    computerChoice = random.choice(options)

    print(f"Computer Chooses :-{computerChoice}")

    if userChoice == computerChoice:
        print("OOH! Its a Draw")
     # Check for win conditions
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "paper" and computerChoice == "rock") or \
         (userChoice == "scissors" and computerChoice == "paper"):
        print("Hoooooooo! You Won!")
    else:
        print("You Loose")
    
play_game()