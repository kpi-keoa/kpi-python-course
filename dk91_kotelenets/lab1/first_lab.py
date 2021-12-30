#!/usr/bin/env python3

"""This module is responsible for arithmetic operations."""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number1', type=float, help='The first number')
parser.add_argument('number2', type=float, help='The second number')

group = parser.add_mutually_exclusive_group()
group.add_argument('--fadd', help='For addition', action='store_true')
group.add_argument('--fsub', help='For substration', action='store_true')
group.add_argument('--fmult', help='For multiplication', action='store_true')
group.add_argument('--fdiv', help='For division', action='store_true')

args = parser.parse_args()


def welcome():
    """Return the greeting."""
    print('Welcome to Calculator')


def calculate(number1: float, number2: float):
    """Do the operations between number1 and number2 and show the result.

    Args:
        number1 (float): The value of the first argument.
        number2 (float): The value of the second argument.
    Returns:
        The result of arithmetic operations.
    """
    if args.fadd:
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif args.fsub:
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif args.fmult:
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif args.fdiv:
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    else:
        print('You have not typed a valid operator.')

    # Add again() function to calculate() function
    again()


def again():
    """Do the user survey."""
    calc_again = input("""
Do you want to calculate again?
Please type Y for YES or N for NO.
""")

    if calc_again.upper() == 'Y':
        calculate(args.number1, args.number2)
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


welcome()

calculate(args.number1, args.number2)
