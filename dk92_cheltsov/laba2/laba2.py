#!/usr/bin/env python3

class source_of_V:
    def voltage (self, v):
        self.volts=v


class battery(source_of_V):
    def __init__ (self, size, v):
        self.size=size
        self.voltage(v)

    def __str__(self):
        return f"Bettery format {self.size}"


class accumulator(source_of_V):
    def __init__ (self, capacity, v):
        self.C=capacity
        self.voltage(v)

    def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
    def __gt__(self, other):
        return (self.C * self.volts) > (other.C * other.volts)

    def __repr__(self):
        return f"Accumulator capacity = {self.C}Ah, {self.volts}V, Max {self.C * self.volts}W"

class power_supply(source_of_V):
    def __init__ (self, current, v):
        self.A=current
        self.voltage(v)

    def __str__(self):
        return f"Power supply = {self.A}A, {self.volts}V, Max {self.A * self.volts}Wh"


if __name__ == "__main__":
    def _demo_():
        print("demo")
        bat = battery('AA', 1.5)
        print(bat.size, ",  ", bat.volts, "V, ", bat)
        accum = accumulator(5, 3.7)
        print(accum.C, "Ah, ", accum.volts, "V, ", accum)
        PS = power_supply(300, 12)
        print(PS.A, "A, ", PS.volts, "V, ", PS)

        accum2 = accumulator(5, 7.4)
        print("\n1", accum, "\n2", accum2)
        
        if(accum2 < accum):
            print("first bigger")
        if(accum2 > accum):
            print("second bigger")

        accum2.C=2
        print("\n1", accum, "\n2", accum2)
        
        if(accum2 < accum):
            print("first bigger")
        if(accum2 > accum):
            print("second bigger")
        

if __name__ == "__main__":
    print("This code do not rum from call from another code")
    _demo_()

    
    
