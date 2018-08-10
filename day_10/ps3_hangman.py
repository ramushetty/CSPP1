
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import os 

import random

WORDLIST_FILENAME = os.path.join("words.txt")

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    o_o = ''
    for j in secretWord:
        if j in lettersGuessed:
            o_o += j
        else:
            o_o += '_'
    return o_o



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    s_t = string.ascii_lowercase
    r_e = ""
    for i in s_t:
        if i not in lettersGuessed:
            r_e = r_e+i
    return r_e
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after ea ch guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord), "letters long.")
    print("---------------------")
    flag = False
    mx = len(secretWord)+5
    lettersGuessed=[]
    while mx!=0:
        print("You have",mx, "guesses left.")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        gu=input("please guess a letter :")
        mx = mx-1
        lettersGuessed.append(gu)
        if gu in getAvailableLetters(lettersGuessed):
            print(getGuessedWord(secretWord, lettersGuessed))
        else:
            print(getGuessedWord(secretWord, lettersGuessed))
        if gu not in secretWord:
            print("oops! not in my word:",getGuessedWord(secretWord,lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed) is True:
            flag = True
    if flag is True:
        print("good guess: ", getGuessedWord(secretWord, lettersGuessed))
        print("congratulations, you won!")
    else:
        print ("sorry you ran out of guesses . the word was ", secretWord)


 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord="apple"
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
