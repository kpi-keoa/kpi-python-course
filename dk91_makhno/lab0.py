import math

print("find area ...")
st = input()
if st == 'triancle':
        def area(a, b, c):
            p = (a + b + c) / 2
            ar = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("area of a triancle = ", ar)
elif st == 'square':
        def area(a):
            ar = a*a;
            print("area of a square = ", ar)
elif st == 'rectangle':
        def area(a, b):
            ar = a * b;
            print("area of a rectangle", ar)
elif st == 'circle':
        def area(r):
            ar = math.pi * r * r
            print("area of a circle", ar)
