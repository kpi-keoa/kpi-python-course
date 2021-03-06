a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def roots (a, b, c):
    """This function culculates the roots of quadratic equation.
    We have two possible roots if discriminant > 0, but if discriminant is 0 then we have only one 
    root. If discriminant is less then 0, there are no roots. To be simplier with getting the result
    roots are declared as an array"""

    d = b ** 2 - 4 * a * c

    if d > 0:
        x[0] = (-b + math.sqrt(d)) / (2 * a)
        x[1] = (-b - math.sqrt(d)) / (2 * a)
        print("x1 = %.1f \nx2 = %.1f" % (x[0], x[1]))
    elif d < 0:
        print("There are no roots")
    else:
        x[0] = (-b) / (2 * a)
        print("x = %.1f" % x[0])

roots (a, b, c)
