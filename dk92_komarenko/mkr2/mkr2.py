#!/usr/bin/env python3

""" This module for calculate distance and middle point."""

import math
import argparse

class Point:
    """class Point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("Point x, y = {}, {}"
                .format(self.x, self.y))


parser = argparse.ArgumentParser()
parser.add_argument('point', nargs='+', type=float, help='the coordinate of point')

group = parser.add_mutually_exclusive_group()
group.add_argument('--dist', help='For calculate distance',
                   action='store_true')
args = parser.parse_args()


def calc_middle(point1, point2):
    """Function for calculate middle point

    Args:
        point1 (object Point): The first point.
        point2 (object Point): The second point.
    Returns:
        point3 (object Point): the middle point.
    """
    point3 = Point ((point1.x + (point1.x - point2.x)/2),
    (point1.y + (point1.y - point2.y)/2))
    return point3


def calc_distance(point1, point2):
    """Function for calculate distance between point1 and point2

    Args:
        point1 (object Point): The first point.
        point2 (object Point): The second point.
    Returns:
        distance (float): the distance.
    """
    distance = math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    return distance


def calc():
    """Function for calculate distance and middle point,
        use arguments from argparse"""
    if len(args.point) > 3:
        count = len(args.point)
        i = count

        if args.dist:
            while i >= 4:
                point_a = Point(args.point[count - i], args.point[count - i + 1])
                point_b = Point(args.point[count - i + 2], args.point[count - i + 3])
                i -= 4
                print("\nThe distance from middle point to point1 and point2 : %.2f "
                  % calc_distance(point_a, point_b))
        else:
            while i >= 4:
                point_a = Point(args.point[count - i], args.point[count - i + 1])
                point_b = Point(args.point[count - i + 2], args.point[count - i + 3])
                i -= 4
                middle_point = calc_middle(point_a, point_b)
                print(f"\nThe middle point between point1 and point2 : {middle_point}")
    else:
        print('You have not typed a valid points.')

if __name__ == '__main__':
    calc()