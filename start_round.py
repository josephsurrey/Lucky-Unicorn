""" Written by Joseph Surrey, 4/04/2023
Start round function for Lucky Unicorn game
"""

# import information from other files
from setup import *
from get_valid_input import get_valid_input
from generate_token import generate_token


def start_round(balance):
    # prompt user to press enter to start
    get_valid_input("Press enter to start: ", str, [""])
    # subtract the price of the round from the user's balance
    balance -= ROUND_PRICE
    # generate token
    generate_token(balance)
