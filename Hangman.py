# imports
from os import system, name

# Variables
wordGuessed = 0
guesses = 6
shots = 0
guessed = 0
word = input("Enter a word to guess: ").upper()
wordSize = len(word)
wordArray = list(word)
if name == 'nt':
    system('cls')
else:
    system('clear')


# Functions
def search(le):
    for letter in wordArray:
        if le == letter:
            print("Letter Find!")
            index = wordArray.index(letter)
            del wordArray[index]
            global shots
            shots += 1
            global guessed
            guessed = 1
            break
    if guessed == 0:
        global guesses
        guesses -= 1
        print("No letter found :(\n\n-1 Life")
    guessed = 0


# Main
print("Welcome to the hangman\nYou have 5 guesses")
while wordGuessed == 0:
    if shots < wordSize:
        letterInput = input("Try to guess the word. Insert a letter: ").upper()
        search(letterInput)
        if shots == wordSize:
            wordGuessed = 1
            print("You guessed the word! " + word)
        if guesses == 0:
            print("You Lose :(")
            break
