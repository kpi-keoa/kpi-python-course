from random import randint
from functools import total_ordering


@total_ordering
class pCube():
    default_edges = 6

    def __init__(self, edges=default_edges, is_rerollable=False):
        '''Конструктор. edges - кількість сторін куба, за замовчуванням 6. is_rerollable - можливісь перекидати куб, за замовчуванням False'''
        self.edges = edges
        self.is_rerollable = is_rerollable
        self.num = 0


    def roll(self):
        '''Кидає куб, якщо ще не кинутий або is_rerollable==True. Поверне значення яке випало або яке було, якщо куб був вже кинутий'''
        if self.num == 0 or self.is_rerollable:
            self.num = randint(1, self.edges)
        return self.num


    @classmethod
    def handout(cls, m, n):
        '''Поверне список розмірностю n, де кожен елемент - список розмірностю m кожен елемент котрого є екземпляр класа'''
        return [[cls()] * m] * n


    def __str__(self):
        '''Поверне стан куба'''
        if self.num == 0:
            return 'Куб ще не бросали.'
        else:
            return f'Випало {self.num} із {self.edges}'
    

    def __eq__(self, other):
        '''Порівняння на рівність. Поверне истину якщо оба куба були вже кинуті та випало однакове значення.'''
        return self.num != 0 and other.num != 0 and self.num == other.num


    def __lt__(self, other):
        '''Порівняння на менший. Поверне истину якщо оба куба були вже кинуті та на першому випало менше значення.'''
        return self.num != 0 and other.num != 0 and self.num < other.num

class elCube(pCube):
    default_edges = 11
    pass


class fivCube(pCube):
    default_edges = 15
    pass


def play(playersC):
    '''сиграти для щадоної кількості гравців'''
    cubes = pCube.handout(1, int(playersC))
    pwc = list(zip(cubes, range(1, int(playersC+1))))
    print(pwc)
    for i in pwc:
        print(f'Ігрок №{i[1]} бросає куб. ')
        i[0][0].roll()
        print(f'{str(i[0][0])}\n')
    print(f'Вийграв ігрок №{max(pwc)[1]}')


if __name__ == '__main__':
    play(10)
