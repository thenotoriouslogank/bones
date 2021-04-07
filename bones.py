# !/usr/bin/python3

"""Rolls a number[X] of dice[d] of an arbitrary number of sides[Y].

Syntax: XdY [eg, 4d20]

(C) 2021 Logan Aker, Salem, Virginia
Released under GNU Public License (GPL)
email logan.aker1989@gmail.com

"""

import time
import random
import sys


def main():
    """Tracks simulated dice rolls.

    Keyword arguments: NOT YET IMPLEMENTED.
    """
    dice_bag()
    time.sleep(.75)
#   sums()
    yes_or_no("Would you like to roll again?")

def dice_bag():
    """Take user input and convert it into dice and roll counts."""
    die = input('Which die would you like to roll? ')
    rolls = input('How many dice do you want to roll? ')
#  dice = sum(rolls)
    print('Rolling ' + str(rolls) + 'd' + str(die))
    time.sleep(float(rolls) * .01)
    results(die, rolls)



# def sums(dice):
    # total =
    # basically just add all of the values we got together here
    # print("TOTAL: " + total)

def results(die, rolls):
    """Calculate dice rolls and print them to the console."""
    i = 1
    while i < (int(rolls) + 1):
        pips = str(random.randint(1, int(die)))
        print("-----------------------")
        print("Roll Number " + str(i) + "   |   " + pips)
        print(i, int(pips))
        i = i + 1


def yes_or_no(question):
    while "The answer is invalid":
        reply = str(raw_input(question + " (y/n): ")).lower().strip()
        if reply[:1] == "y":
            print("Restarting. . . ")
            time.sleep(2.5)
            main()
        if reply[:1] == "n":
            print("Goodbye!")
            time.sleep(2.5)
            sys.exit()

# TODO Write docstrings.
# TODO Create parameters for dice (to hit, for damage, etc.)
# TODO Perhaps work on implementing full-scale combat tracking?
# Here is my original thinking for how parameters might work:
# mod = input("Parameters")
#
# tohit, group, bonus, dmg
# I think I just treat these params as different functions entirely, right?
# Like the 'basic' command is just xdy, but the others can be manupulated
# further.
# TODO Create functionality to either print to console or to a log file.


if __name__ == '__main__':
    main()

sys.exit()
