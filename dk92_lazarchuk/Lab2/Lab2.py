import math

class Figure():
    def __init__(self):
        self.name = 'none'
    def __str__(self):
        return f'class: {self.name}'
    def __repr__(self):
        return 'Figure()'
    def area(self):
        return 0


class Circuit(Figure):
    def __init__(self, radius):
        self.name = 'Circuit'
        self.radius = radius
    def __str__(self):
        return f'class: {self.name} with radius: {self.radius}'
    def __repr__(self):
        return f'Circuit({self.radius})'
    def area(self):
        return float(self.radius)*float(self.radius)*math.pi


class Rectangle(Figure):
    def __init__(self, w, h):
        self.name = 'Rectangle'
        self.widht = w
        self.height = h
    def __str__(self):
        return f'class: {self.name} with widht: {self.widht} and height: {self.height}'
    def __repr__(self):
        return f'Rectangle({self.widht}, {self.height})'
    def area(self):
        return float(self.widht)*float(self.height)


class Squart(Rectangle):
    def __init__(self, a):
        self.name = 'Squart'
        self.widht = a
        self.height = a
    def __str__(self):
        return f'class: {self.name} with edge: {self.widht}'
    def __repr__(self):
        return f'Squart({self.widht})'

def test():
    tes = [Figure(), Circuit(5), Rectangle(3,4), Squart(6)]
    for i in tes:
        print(f'{str(i)} and area: {i.area()}')


if __name__ == "__main__":
    test()
