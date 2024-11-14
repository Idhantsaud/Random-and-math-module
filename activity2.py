import random

while True:
    user_int = input("Enter one of the choices (rock, paper,scissors)")

    actions = ["rock", "paper", "scissors"]
    computer = random.choice(actions)
    print(f"You have selected {user_int}\n")
    print(f"Computer has selected {computer}\n")

    if user_int == computer:
        print("Tie")
    elif user_int == "rock":
        if computer == "scissors":
            print("You won")
        else:
            print("you lost")
    
    elif user_int == "paper":
        if computer == "rock":
            print("You won")
        else:
            print("You lost")
    elif user_int == "scissors":
        if computer == "paper":
            print("You win")
        else:
            print("You lost")
    PlayAgain = input("play again ? (y/n)")
    if PlayAgain == "n":

        break
    