#! /usr/bin/env python3
"""Area calculator"""
def standard(b,c):
    """Compliance check function."""
    if b < 2:
        print('Object2 area less than 2')
    else:
        print('Object2 comply with the standard.')
    if c < 3:    
        print('Object3 area less than 3')
    else:
        print('Object3 comply with the standard.')

import argparse
parser = argparse.ArgumentParser()
"""Positional arguments"""
parser.add_argument('l', type=int, help='Limit area')
parser.add_argument('a', type=float, help='Enter the area of the object1')
parser.add_argument('b', type=float, help='Enter the area of the object2 (not less 2)')
parser.add_argument('c', type=float, help='Enter the area of the object2 (not less 3)')
args = parser.parse_args()
standard(args.b, args.c)
s = args.a + args.b + args.c
if s <= args.l:
    print('The area will be enough.')
else:
    print('The area of the objects exceeds the allowable area!')
