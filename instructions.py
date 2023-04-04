""" Written by Joseph Surrey, 4/04/2023
Instructions function for Lucky Unicorn game
"""

# import information from other files
from setup import *
from get_valid_input import get_valid_input
from initial_payment import initial_payment


def instructions():
    # welcome message
    print("Welcome to Lucky Unicorn\n"
          "By playing this game you are supporting Doctors without Borders")
    # ask if user has played before
    played_before = get_valid_input("Have you played this game before? (Y/N)", str, ["Y", "N", "NO", "YES"], True)
    if played_before == "Y" or played_before == "YES":
        initial_payment()
    else:
        # print instructions if the user has not played before
        print(INSTRUCTIONS)
        # run initial_payment
        initial_payment()
