from random import randrange


def diceRoll():
    dice = [1, 2, 3, 4, 5, 6]
    number = randrange(6)
    return dice[number]


repeat = "Y"

while repeat == "Y":
    print(diceRoll())
    repeat = input("Play again? (y/n): ").upper()
