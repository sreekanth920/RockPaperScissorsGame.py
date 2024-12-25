import random

print("WELCOME TO ROCK PAPER SCISSORS")

opt = ("rock", "paper", "scissors")

while True:
    player = None
    computer = random.choice(opt)
    while player not in opt:
        player = input("Enter your choice (rock, paper or scissors): ").lower()
        if player not in opt:
            print("Enter a valid option")

    print(f'Computer Choice is {computer}')
    print(f'Your Choice is {player}')

    # Determine the outcome
    if player == computer:
        print("Ties")
    elif player == 'rock' and computer == 'scissors':
        print("You Win")
    elif player == 'scissors' and computer == 'paper':
        print("You Win")
    elif player == 'paper' and computer == "rock":
        print("You Win")
    else:
        print("You Lose..!")
    play_again = input("Want to play again (yes or no): ").lower()
    if play_again == 'no':
        print("Thanks for playing..")
        break
