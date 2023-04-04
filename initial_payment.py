""" Written by Joseph Surrey, 4/04/2023
Initial payment function for Lucky Unicorn game
"""

# import information from other files
from get_valid_input import get_valid_input
from start_round import start_round
from setup import *


def initial_payment():
    balance = get_valid_input(f"How much would you like to play Lucky Unicorn with? (${ROUND_PRICE} - ${MAX_SPEND}) ",
                              float, [], False, ROUND_PRICE, MAX_SPEND)
    start_round(balance)
