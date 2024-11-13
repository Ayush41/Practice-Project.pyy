# ROck Paper Scissors Game

import random
def play_game():
    options = ["rock","paper","scissors"]
    userChoice = input("Enter rock,paper or scissors :-").lower()
    computerChoice = random.choice(options)

    print(f"Computer Chooses :-{computerChoice}")
    