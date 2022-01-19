import math
import array

RO = 7800 #kg/m3
AURUM = 149

radius = input ("\n Write the radius of your fantastic planet in km: ")
radius = int(radius)

print ("\n Square of your planet is: ", 4 * math.pi * math.pow(radius,2), "square kilometers")

distance = input ("\n Write the distance between your planet and Dyson sphere in astronomical unit (1, 2, etc): ")
equal = int(distance * AURUM)

dsquare = 4 * math.pi * math.pow(equal,2)

print ("\n Square of your Dyson sphere is: ", dsquare, "* 10^9 square kilometers")

while True:
    try:
        thickin = int(input ("\n Write the thickness of Dyson sphere in m (1 - 10): "))
        if 1 <= thickin <= 10:

            Vsp = 4/3 * math.pi * (radius * 10 ** 3) ** 3 - 4/3 * math.pi * (radius - (thickin ** 3))
            print ("\n The Volume of your Dyson square is", Vsp, "cubic kilometers")
            break
        else:
            raise ValueError
    except ValueError:
        print ("\n Sorry, but you make a mistake")
        continue

print ("\n So, your Dyson spehere will weigh", RO * Vsp, "10^6 gramm or 10^2 * ton \n")






