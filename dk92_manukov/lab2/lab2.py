#!/usr/bin/env python
import os
import sys

print("This program is a demonstration of my knowledge about classes, metods and OOP.")

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

class laptop
    """Class laptop include: Brand, Year, Solution"""

    brand = ""
    year = 0
    solution = ""

    def __init__(self, brand = "Undefined", solution = "Undefined", year = 0):
        """laptop class constructor"""
        self.brand = brand
        self.year = year
        self.solution = solution

    def get_brand(self):
        """function prints laptop's brand if define."""
        if(self.brand != "Undefined\n"):
            print(self.brand)
        else:
            print("Undefined brand\n")

    def get_solution(self):
        """Function prints laptop's solution, if define"""
        if (self.solution != "Undefined\n"):
            print("Laptop's solution: ", self.solution, "\n")

    def get_year(self):
        """function prints laptop's year, if define"""
        if (self.year != 0):
            print(self.brand, "Laptop's year:", self.year, "\n")

    def __str__(self):
        lap = "Laptop's brand: " + str(self.brand) + "\n"
        lap = lap + "Laptop's solution: " + str(self.solution) + "\n"
        lap = lap + "Laptop's year: " + str(self.year) + "\n"
        return lap

class ultrabook(laptop)

    """Ultrabook class included: brand, solution, year"""

    def __init__(self, brand = "Undefined", solution = "Undefined", year = 0):
        """Ultrabook class constructor"""
        self.brand = brand
        self.solution = solution
        self.year = year

class makbook(ultrabook)

    """Makbook class included: brand(only Apple), solution, year"""

    def __init__(self, brand = "Apple", solution = "Undefined", year = 0):
        """Makbook class constructor"""
        self.brand = "Apple"
        self.solution = solution
        self.year = year

class netbook(laptop)

    """Netbook class included: brand, solution, year"""

    def __init__(self, brand = "Undefined", solution = "Undefined", year = 0):
        """Netbook class constructor"""
        self.brand = brand
        self.solution = solution
        self.year = year

if(__name__ == '__main__'):
    AcerAspire3 = netbook("Acer Aspire 3", "1920*1080", 2020)
    HPPavilion = ultrabook("HP Pavilion", "2560 × 1440", 2021)
    Makbook = makbook("Apple Makbook Pro 16", 2020)

    Makbook.set_solution("3072*1920")
    Makbook.get_pencil()

    print(AcerAspire3)
    print(HPPavilion)
    print(Makbook)
