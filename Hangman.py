# Variables
word = "ANGULAR"
wordArray = list(word)
wordGuessed = 0
guesses = 6
wordSize = len(word)
shots = 0
guessed = 0


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
