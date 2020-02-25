import random

def hangman():
    print "Welcome to Hangman!"
    wordDash = "_" *len(theWord)


wordList = ["alligator", "astroid", "balloon"]
theWord = random.choice(wordList)
hangman()