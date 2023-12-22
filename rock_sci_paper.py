import random

print("(1)-> Rock\n(2)-> Scissors\n(3)-> Paper")

computerChoice = random.randint(1, 3)

while True:
    try:
        x = input("Select your choice of rock, paper, or scissors:")
        userChoice=int(x)
        break
    except ValueError:
        print("This'll be int type")


if userChoice in [1, 2, 3]:
    if computerChoice == 1:
        print("The computer chose rock.")
    elif computerChoice == 2:
        print("The computer chose scissors.")
    elif computerChoice == 3:
        print("The computer chose paper.")

    if userChoice == 1:
        print("You chose rock.")
    elif userChoice == 2:
        print("You chose scissors.")
    elif userChoice == 3:
        print("You chose paper.")

    if computerChoice == 1 and userChoice == 2:
        print("Computer (Rock) wins!\n")
    elif computerChoice == 1 and userChoice == 3:
        print("You (Paper) wins!\n")
    elif computerChoice == 2 and userChoice == 3:
        print("Computer(Scissors) wins!\n")
    elif computerChoice == 2 and userChoice == 1:
        print("You(Rock) wins!\n")
    elif computerChoice == 3 and userChoice == 1:
        print("Computer(Paper) wins!\n")
    elif computerChoice == 3 and userChoice == 2:
        print("You (Scissors) wins!\n")
    else:
        print("It's a tie! Play again.\n")
else:
    print("Geçerli bir işlem giriniz.")

