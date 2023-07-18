# Importing time, random and words modules
import random
import time
from words import word_list


def get_word():
    """"
    Returns a random word from the word list
    """
    word = random.choice(word_list)
    return word.lower()


def hangman(word):
    """
    The main function of the game. Time module makes
    the game more pleasing to play.
    """
    
    # Welcoming the user
    name = input("What is your name? ")
    print(f"Hello, {name}. Time to play hangman!")

    # Here we set the secret
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    turns = 8

    # Setting up the game
    time.sleep(1)
    print("There is no special characters or numbers in the secret word.")
    print("Start guessing...")
    print(display_hangman(turns))
    print("Secret word: " + word_completion)
    print("\n")
    time.sleep(0.5)

    # Create a while loop and check if the turns are more than zero
    while not guessed and turns > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():

            # If player puts a letter that is already guessed
            if guess in guessed_letters:
                print("You already guessed the letter. \
                      Guessed letters:", formatted_letters_list)
                time.sleep(0.5)
            
            # If the guessed word is not found in the secret word
            elif guess not in word:
                formatted_letters_list = " ".join(guessed_letters)
                print(guess, "is not in the word. \
                      Guessed letters:", formatted_letters_list)
                turns -= 1
                guessed_letters.append(guess)
                time.sleep(0.5)
