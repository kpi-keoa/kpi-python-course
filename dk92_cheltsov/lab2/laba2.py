#!/usr/bin/env python3

class SourceOfV:
    def __init__(self, voltage):
        self.volts=voltage


class Battery(SourceOfV):
    def __init__ (self, size, voltage):
        super().__init__(voltage)
        self.size=size

    def __str__(self):
        return (
            f"Bettery format {self.size}, "
            f"Bettery voltage {self.volts} "
        )

class Accumulator(Battery):
    def __init__ (self, voltage, size, capacity):
        super().__init__(size, voltage)
        self.C=capacity

    def __lt__(self, other):
        return (self.C * self.volts) < (other.C * other.volts)
    def __gt__(self, other):
        return (self.C * self.volts) > (other.C * other.volts)

    def __str__(self):
        return (
            f"Accumulator format {self.size}, "
            f"Accumulator capacity = {self.C}Ah, {self.volts}V, Max {self.C * self.volts}Wh "
        )

class PowerSupply(SourceOfV):
    def __init__ (self, current, voltage, efficiency):
        super().__init__(voltage)
        self.Amps = current
        self.efficiency = efficiency

    def __repr__(self):
        return (
            f"Power supply = {self.Amps}A, {self.volts}V, Max {self.Amps * self.volts}W, "
            f"Power supply efficiency = {self.efficiency}% "
        )

if __name__ == "__main__":
    def _demo_():
        print("demo")
        bat = Battery('AA', 1.5)
        print(bat.size, ",  ", bat.volts, "V, ", bat)
        accum = Accumulator(3.7, 32900, 5)
        print(accum.C, "Ah, ", accum.volts, "V, ", accum)
        PS = PowerSupply(300, 12, 93)
        print(PS.Amps, "A, ", PS.volts, "V, ", PS)

        accum2 = Accumulator(7.4, 32900, 5)
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

    
    
