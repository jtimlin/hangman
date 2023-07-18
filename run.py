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