import random
from words import words 
import string

def get_valid_word(words): #funciton to randomly choose word from the list with no space or dash
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters  = set() #what the user has guessed already


    #getting user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter) 
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already guessed that character. Please try again.')

    else:
        print('Invalid character. Please try again')


hangman()