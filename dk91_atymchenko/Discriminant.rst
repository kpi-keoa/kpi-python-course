import math
print("The quadratic equation has the format ax^2 + bx + c = 0\nPlease enter your coeficients")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c
print("Discriminant D = %.1f" % d)
 
if d > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.1f \nx2 = %.1f" % (x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = %.1f" % x)
else:
    print("There are no roots")
