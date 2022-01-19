#!/usr/bin/env python3

""" This module is calculate a arithmetic operations for triangle."""

import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ab', type=float, help='The first leg')
parser.add_argument('ac', type=float, help='The second leg')

group = parser.add_mutually_exclusive_group()
group.add_argument('--farea', help='For calculate area of triangle',
                   action='store_true')
group.add_argument('--fperim',
                   help='For calculate perimeter of triangle',
                   action='store_true')
group.add_argument('--fhypot',
                   help='For calculate hypotenuse of triangle',
                   action='store_true')
args = parser.parse_args()


def input_args():
    """Function for input args from keyboard

    Returns:
        ab (float): The value of the first leg.
        ac (float): The value of the second leg.
    """
    # input from command line
    ab = input("Length of the 1 leg: ")
    ac = input("Length of the 2 leg: ")
    # convert to float
    ab = float(ab)
    ac = float(ac)

    return ab, ac


def calc_hypotenuse(ab, ac):
    """Function for calculate hypotenuse of the triangle

    Args:
        ab (float): The value of the first leg.
        ac (float): The value of the second leg.
    Returns:
        bc (float): Hypotenuse of the triangle.
    """
    bc = math.sqrt(ab**2 + ac**2)
    return bc


def calc_area(ab, ac):
    """Function for calculate area of the triangle

    Args:
        ab (float): The value of the first leg.
        ac (float): The value of the second leg.
    Returns:
        s (float): Area of the triangle.
    """
    s = (ab * ac) / 2
    return s


def calc_perimeter(ab, ac):
    """Function for calculate perimeter of the triangle

    Args:
        ab (float): The value of the first leg.
        ac (float): The value of the second leg.
    Returns:
        p (float): Perimeter of the triangle.
    """
    bc = calc_hypotenuse(ab, ac)
    p = ab + ac + bc
    return p


def choice(ab, ac):
    """Function for manual choice of operation,
        calculate arithmetic operation for triangle.

    Args:
        ab (float): The value of the first leg.
        ac (float): The value of the second leg.
    Returns:
        The result of calculated operations.
    """
    calc_choice = input("\nChoice the calculate function:\n"
                        "type A - calculate Area of triangle,\n"
                        "type P - calculate Perimeter of triangle\n"
                        "type H - calculate Hypotenuse of triangle\n")
    if calc_choice.upper() == 'A':
        print("The area of the triangle : %.2f" % calc_area(ab, ac))
    elif calc_choice.upper() == 'P':
        print("Perimeter of a triangle : %.2f" % calc_perimeter(ab, ac))
    elif calc_choice.upper() == 'H':
        print("Hypotenuse of a triangle : %.2f" % calc_hypotenuse(ab, ac))
    else:
        print("Bye. See you later.")
        return 1


def calc():
    """Function for calculate arithmetic operation for triangle,
        use arguments from argparse"""
    if args.farea:
        print("The area of the triangle : %.2f \n"
              % calc_area(args.ab, args.ac))
    elif args.fperim:
        print("Perimeter of a triangle : %.2f \n"
              % calc_perimeter(args.ab, args.ac))
    elif args.fhypot:
        print("Hypotenuse of a triangle : %.2f \n"
              % calc_hypotenuse(args.ab, args.ac))
    else:
        print('You have not typed a valid operator.')

    while 1:
        # Add choice() function for make a choice of operation
        ab, ac = input_args()
        if choice(ab, ac):
            break


if __name__ == '__main__':
    calc()