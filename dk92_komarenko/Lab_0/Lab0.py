import math
 
AB = input("Length of the 1 leg: ")
AC = input("Length of the 2 leg : ")
 
AB = float(AB)
AC = float(AC)
 
BC = math.sqrt(AB**2 + AC**2)
 
S = (AB * AC) / 2
P = AB + AC + BC
 
print("The area of the triangle : %.2f" % S)
print("Perimeter of a triangle : %.2f" % P)