#!/usr/bin/env python3

import math
from sys import argv, stderr
tip = argv[1]

"""This program calculates the area.

        Figures:
            triangle,
            rectangle,
            circle,
    Also sums the area of ​​two given triangles.

        Example:
            $ python Lab1.py <arg1>, <arg2>, <arg3>, <arg4> ...
            <arg1> - a shape type,
            <arg2>, <arg3>, <arg4> ... - values.

    If the data is incorrect, an error is displayed on the screen.
"""

def triangle(side_a, /, side_b, *, side_c):

    """
    The function calculates the area of ​​a triangle.

        Args:
            side_a(int): Values ​​for side length a.
            side_b(int): Values ​​for side length b.
            side_c(int): Values ​​for side length c.

        Returns:
            float: square of triangle.
    """

    print('figure = triangle ')
    print('side size a =', side_a)
    print('side size b =', side_b)
    print('side size c =', side_c)
    per = (side_a + side_b + side_c) / 2
    square = math.sqrt((per * (per - side_a) * (per - side_b) * (per - side_c)))
    print(f'area of {tip} = {square}')
    return (square)


def rectangle(side_b=0, side_a=0):

    """
    The function calculates the area of ​​a rectangle.

     Args:
        side_a(int): Values ​​for side length a.
        side_b(int): Values ​​for side length b.
    """

    print('figure = rectangle ')
    print('side size a=', side_a)
    print('side size b=', side_b)
    square = side_a * side_b
    print(f'area of {tip} = {square}')


def circle(radius=int(argv[2])):

    """
     The function calculates the area of ​​a circle.

     Args:
        radius(int): radius value
    """

    print('figure = circle ')
    print('Радіус круга=', radius)
    square = math.pi * (radius ** 2)
    print(f'area of {tip} = {square}')


def sum_triangle(side_a, side_b, /, side_c, side_d, *, side_e, side_f):
    first = triangle(int(argv[2]), int(argv[3]), side_c=int(argv[4]))
    second = triangle(int(argv[5]), int(argv[6]), side_c=int(argv[7]))
    suma = first + second
    print(f'suma triangle = {suma}')

    """
    The function adds the area of ​​two user-defined triangles

     Args:
        side_a(int): Values ​​for side length a first triangle
        side_b(int): Values ​​for side length b first triangle
        side_c(int): Values ​​for side length c first triangle
        side_d(int): Values ​​for side length a second triangle
        side_e(int): Values ​​for side length b second triangle
        side_f(int): Values ​​for side length c second triangle
    """

if tip in ('t', 'tri', 'triangle'):
    triangle(int(argv[2]), int(argv[3]), side_c=int(argv[4]))

elif tip in ('r', 'rec', 'rectangle'):
    rectangle(side_b=int(argv[2]), side_a=int(argv[3]))

elif tip in ('c', 'cir', 'circle'):
    circle(radius=int(argv[2]))

elif tip in ('s', 'suma'):
    sum_triangle(int(argv[2]), int(argv[3]), int(argv[4]),
    int(argv[5]), side_e=int(argv[6]), side_f=int(argv[7]))

else:
    stderr.write('ERROR, Not found')
