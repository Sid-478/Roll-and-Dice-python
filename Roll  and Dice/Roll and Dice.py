import random
number = ""
while number != "quit":
    dice = random.randint(1, 6)
    number = int(input("Guess number: "))
    if number == dice:
        print("Bingo! You won!")
    elif number == "quit":
        break
    else:
        print("You lost!")
