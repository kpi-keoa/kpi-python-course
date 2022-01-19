import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("figure", type=str, help='What shape area do you want to find?')
parser.add_argument("-a", "--action", help='Сhoose action!(div or mul)', default ="multiplication")

args = parser.parse_args()

def area_triancle(a, b, c):
    """function for calculating the area of a triangle

    Args:
        a (int): side a
        b (int): side b
        c (int): side c

    Returns:
        float: area triancle
    """
    p = (a + b + c) / 2
    ar = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("area of a triancle = ", ar)
    return ar

def area_square(a):
    """function for calculating the area of a square

    Args:
        a (int): side a

    Returns:
        float: area square
    """
    ar = a*a;
    print("area of a square = ", ar)
    return ar

def area_rectangle(a, b):
    """function for calculating the area of a rectangle

    Args:
        a (int]: side a
        b (int): side b

    Returns:
        float: area rectangle
    """
    ar = a * b;
    print("area of a rectangle", ar)
    return ar

def area_circle(r):
    """function for calculating the area of a circle

    Args:
        r (int): radius

    Returns:
        float: area circle
    """
    ar = math.pi * r * r
    print("area of a circle", ar)
    return ar

def division(ar):
    """division of area by number

    Args:
        ar (float): area
    """
    a = int(input("How much to divide?"))
    print(ar / a)

def multiplication(ar):
    """multiplication of area by number

    Args:
        ar ([type]): [description]
    """
    a = int(input("How much to multiply?"))
    print(a * ar)



if args.figure == 'triancle':
    a = int(input("a ="))
    b = int(input("b ="))
    c = int(input("c ="))
    ar = area_triancle(a, b, c)
elif args.figure == 'square':
    a = int(input("a ="))
    ar = int(area_square(a))
elif args.figure == 'rectangle':
    a = int(input("a ="))
    b = int(input("b ="))
    ar = area_rectangle(a, b)  
elif args.figure == 'circle':
    r = int(input("r ="))
    ar = area_circle(r)
if args.action == 'div':
    division(ar)
elif args.action == 'div':
    multiplication(ar)
            