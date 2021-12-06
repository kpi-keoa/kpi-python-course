#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val1", type=int, help='First value')
parser.add_argument("val2", type=int, help='Second value')
args = parser.parse_args()


def gcd(val1: int, val2: int):
    """Calculate the greatest common divisor of val1 and val2.

    Args:
        val1 (int): The value of the first argument.
        val2 (int): The value of the second argument.

    Returns:
        The greatest common divisor.
    """
    while val1 != val2:
        if val1 > val2:
            val1 -= val2
        else:
            val2 -= val1
    return val1


def lcm(val1: int, val2: int):
    """Calculate the least common multiple of val1 and val2.

    Args:
        val1 (int): The value of the first argument.
        val2 (int): The value of the second argument.

    Returns:
        The least common multiple.
    """
    mul = val1 * val2
    return print(mul // gcd(val1, val2))


lcm(args.val1, args.val2)
