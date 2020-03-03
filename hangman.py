import random

def hangman():
    print ("Welcome to Hangman!")
    wordDash = "_" *len(hiddenWord)
    numGuesses = 0
    remainingGuesses = 9 - numGuesses

    while remainingGuesses != 0:
        print (wordDash)
        print ("Remaining guesses: " + remainingGuesses)

        letter = input("Guess: ")
        if len(letter) != 1 or letter != str(letter): #Make sure user enters a letter
            print ("Invalid entry. Please enter a letter.")
        
        elif letter in hiddenWord:
            wordDash = letterFill

def letterFill(hiddenWord, wordDash, letter):
    for i in range(len(hiddenWord)):
        if hiddenWord[i] == letter:

wordList = ["alligator", "astroid", "balloon"] #To be extended
hiddenWord = random.choice(wordList)
hangman()