import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Choose a number between the following list: 1-Rock, 2-Paper, #-Scissors: ")

playerChoice = int(playerChoice)

# User Input check
if playerChoice < 1 or playerChoice > 3:
    print("Error: You should choose between 1 and 3!")
else:
    # Develo the game Logic through if/elif/else
    computerChoice = random.randint(1, 3)
    print(computerChoice, computerChoice)   

    if playerChoice == computerChoice:
        print("Its a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")  
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")   
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")               