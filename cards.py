# get_card()
import random

deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def get_card():
    """
    Parameter:
        none
    Return:
        <String> a random value from a list of a deck of cards' ranks
    """
    # print(random.choice(deck))
    return random.choice(deck)

# help(get_card)
# get_card()
