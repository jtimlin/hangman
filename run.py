# Importing time, random and words modules
import random
import time
from words import word_list
from hangman_structure import display_hangman


def get_word():
    """"
    Returns a random word from the word list
    """
    word = random.choice(word_list)
    return word.lower()


def user_welcome():
    """
    This function allows user to
    type their name only with letters.
    """
    username = None

    while True:
        print("Welcome to Hangman game!")
        username = input("What is your name? ")
        
        if not username.isalpha():
            print("Username must be alphabets only.")
            continue
        else:
            print(f"Hello, {username}. Time to play!")
            break


def play_again():
    """
    This function prompts the user to decide whether they want
    to play again. If the user inputs 'y' or 'Y', the game
    will start over. Otherwise, it will shut down.
    """
    play = None

    while True:
        play = input("Play again? (Y/N) ").lower()
        
        if play == "y":
            main()
        else:
            print(f"You have left the game.")
            exit()


def hangman(word):
    """
    The main function of the game. Time module makes
    the game more pleasing to play.
    """

    # Here we set the secret
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    turns = 8
    letters_word = list(word)

    # Setting up the game
    time.sleep(1)
    print("There is no special characters or numbers in the secret word.")
    print("Start guessing...")
    print(display_hangman(turns))
    print("Secret word: " + word_completion)
    print('The word has {} letters.'.format(len(letters_word)))
    print("\n")
    time.sleep(0.5)

    # Create a while loop and check if the turns are more than zero
    while not guessed and turns > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():

            # If player puts a letter that is already guessed
            if guess in guessed_letters:
                print("You already guessed the letter.")
                formatted_letters_list = ", ".join(guessed_letters)
                print("Guessed letters:", formatted_letters_list)
                time.sleep(0.5)

            # If the guessed letter is NOT found in the secret word
            elif guess not in word:
                formatted_letters_list = ", ".join(guessed_letters)
                print(guess, "is not in the word.")
                print("Guessed letters:", formatted_letters_list)
                turns -= 1
                guessed_letters.append(guess)
                time.sleep(0.5)

            # If the guessed letter IS found in the secret word
            else:
                print(f"\033[1;32;40mGood job, {guess} is in the word!\033[0m")
                formatted_letters_list = ", ".join(guessed_letters)
                print("Guessed letters:", formatted_letters_list)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, char in enumerate(word) if char == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                time.sleep(0.5)

        # If the player guesses the whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                time.sleep(0.5)
            elif guess != word:
                print(guess, "is not the word.")
                turns -= 1
                guessed_words.append(guess)
                time.sleep(0.5)
            else:
                guessed = True
                word_completion = word

        # If the player guesses a number, a special character
        # or a word that is wrong length.
        else:
            print("Not a single letter or words length")
            print("is not the same as the secret word.")
            time.sleep(0.5)
        print(display_hangman(turns))
        print("Secret word: " + word_completion)
        print("\n")

    # If the player wins or loses
    if guessed:
        print("\033[1;32;40mCongrats, you guessed the word! You win!\033[0m")
        play_again()
    else:
        print("\033[1;31;40mSorry, you ran out of turns.\033[0m")
        print(f"\033[1;31;40mThe word was {word}. Maybe next time!\033[0m")
        play_again()


def main():
    """
    The main function of the game
    """
    word = get_word()
    user_welcome()
    hangman(word)


# checks if the executed file is the main program and run the main function
if __name__ == "__main__":
    main()
