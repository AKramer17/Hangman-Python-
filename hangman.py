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
        if len(letter) != 1 or letter != str(letter):   # Make sure user enters a letter
            print ("Invalid entry. Please enter a letter.")
        
        elif letter in hiddenWord:
            wordDash = letterFill

def letterFill(hiddenWord, wordDash, letter):
    result = ""
    for i in range(len(hiddenWord)):
        if hiddenWord[i] == letter:
            result = result + letter
        else:
            result = result + wordDash[i]
    return result

wordList = ["alligator", "astroid", "balloon", "balcony", "blinded", "character", "chamber",
"coin", "door", "double", "electric", "eraser", "essence", "family", "fire", "frog", "giant", 
"gigantic", "ghost", "haunted", "help", "hero", "hose", "igloo", "indigo", "jelly", "jump", 
"koala", "leaf", "lemon", "money", "monument", "nothing", "octagon", "orange", "pancakes",
"phone", "queen", "restroom", "radish", "salt", "savory", "triangle", "tunnel", "unicycle", 
"velvet", "violet", "winter", "xenophobe", "youth", "zebra"]
hiddenWord = random.choice(wordList)
hangman()