#!/usr/bin/env python
import os
import sys
from random import randint
from functools import total_ordering

print("This program is my credit work, that realizes roll of cube.")

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

@total_ordering
class Cuberoll():
    default_sides = 6

    def __init__(self, sides=default_sides, is_ rerollable=False):
        """Construct. Attributes: sides, is_ rerollable."""
        self.sides = sides
        self.is_ rerollable = is_ rerollable
        self.num = 0


    def roll(self):
        """Roll the cube and return number."""
        if self.num == 0 or self.is_ rerollable:
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


    def __eq__(self, other):
        """As like as next method - compare."""
        return self.num != 0 and other.num != 0 and self.num == other.num


    def __lt__(self, other):
        return self.num != 0 and other.num != 0 and self.num < other.num

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
    print(pwc)
    for i in pwc:
        print(f'Player number {i[1]} do his step.')
        i[0][0].roll()
        print(f'{str(i[0][0])}\n')
    print(f'Won player, whose number = {max(pwc)[1]}')

if __name__ == '__main__':

    play(3)

    play(5)
