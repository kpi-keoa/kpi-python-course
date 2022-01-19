#!/usr/bin/env python

import os
import sys
from random import randint

"""This program realizes roll of cube."""

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

class Cuberoll():
    default_sides = 6

    def __init__(self, sides=default_sides, is_rerollable=False):
        """Construct. Attributes: sides, is_rerollable."""

        self.sides = sides
        self.is_rerollable = is_rerollable
        self.num = 0

    def roll(self):
        """Roll the cube and return number."""

        if self.num == 0 or self.is_rerollable:
            self.num = randint(1, self.sides)
        return self.num

    @classmethod
    def handout(cls, m, n):
        """Return list."""

        return [[cls()] * m] * n

    def __str__(self):
        """Cube state."""

        if self.num == 0:
            return 'Cube is waiting.'
        else:
            return f'Cube give {self.num} from {self.sides}'

class Elevencube(Cuberoll):
    default_sides = 11
    pass

class Fifteencube(Cuberoll):
    default_sides = 15
    pass

def play(cuberoll_players):
    """Play for order number of players"""

    cubes = Cuberoll.handout(1, int(cuberoll_players))
    pwc = list(zip(cubes, range(1, int(cuberoll_players+1))))
    max = 0
    for i in pwc:
        i[0][0].num = 0
        i[0][0].roll()
        print(f'Player number {i[1]} do his step.')
        print(f'{str(i[0][0])}\n')
        if(max < i[0][0].num):
            max = i[0][0].num
            max_num = i[1]
    print(f'Won player, whose points = {max}. His number is {max_num}')

if __name__ == '__main__':

    play(3)
    play(5)
