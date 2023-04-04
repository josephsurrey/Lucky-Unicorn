""" Written by Joseph Surrey, 4/04/2023
Instructions function for Lucky Unicorn game
"""

# import information from other files
from setup import *
from get_valid_input import get_valid_input
from start_round import start_round


def instructions():
    print("Welcome to Lucky Unicorn\n"
          "By playing this game you are supporting Doctors without Borders")
    played_before = get_valid_input("Have you played this game before? (Y/N)", str, ["Y", "N", "NO", "YES"], True, 0, 0)
    if played_before == "Y" or played_before == "YES":
        start_round()
    else:
        print(INSTRUCTIONS)
        start_round()
