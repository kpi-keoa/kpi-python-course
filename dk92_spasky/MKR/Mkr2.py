import random
from array import *


class Cube_defolt():
    cube_edges = 6

    def __init__(self, edges=cube_edges, is_relollable=False):
        self.edges = edges
        self.is_relollable = is_relollable
        self.value_of_cube = 0


    def roll(self):
        if self.is_relollable == True or self.value_of_cube == 0:
            self.value_of_cube = random.randint(1, self.edges)
        return print (f'{self.value_of_cube}')

    def __str__(self):
        if self.value_of_cube == 0:
            return 'The cube was not thrown'
        else:
            return 'Value of cube is ',self.value_of_cube


    def __ne__(self, other):
        if self.value_of_cube != other.value_of_cube and self.value_of_cube != 0 and other.value_of_cube != 0:
            return 'The values ​​of the cubes not equivalent'
        else:
            return 'The condition is not met'


    def __eq__(self, other):
        if self.value_of_cube != 0 and other.value_of_cube != 0 and self.value_of_cube == other.value_of_cube:
            return 'The values ​​of the cubes are equivalent'
        else:
            return 'The condition is not met'



    def __lt__(self, other):
        if self.value_of_cube != 0 and other.value_of_cube != 0 and self.value_of_cube < other.value_of_cube :
            return f'{self.value_of_cube} < {other.value_of_cube}'
        else:
            return 'The condition is not met'


    @classmethod
    def handout(cls, X: int, Y: int):
        players_list = []
        for a in range(X * Y):
            players_list.append(Cube_defolt().roll())
        return players_list


class Cube_15(Cube_defolt):
        cube_edges = 15


class Cube_11(Cube_defolt):
        cube_edges = 11


if __name__ == '__main__':
    cbm = Cube_defolt()
    cbm.roll()


