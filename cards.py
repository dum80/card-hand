# get_card()
import random

def get_card():
    """
    Parameter:
        none
    Return:
        <String> a random value from a list of a deck of cards' ranks
    """
    deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    return random.choice(deck)
