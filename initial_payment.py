""" Written by Joseph Surrey, 4/04/2023
Initial payment function for Lucky Unicorn game
"""

from get_valid_input import get_valid_input
from start_round import start_round


def initial_payment():
    balance = get_valid_input("How much would you like to play Lucky Unicorn with? ($1 - $10) ",
                              float, [], False, 1, 10)
    start_round(balance)
