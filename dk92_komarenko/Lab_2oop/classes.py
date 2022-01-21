class Transport:
    """
    class Transport - parent class of all transport
                      characteristics: brand, model, max_speed, mass
                      example: Transport("Nissan", "Almera", "188", "1600", "4")
    """
    def __init__(self, brand, model, max_speed, mass):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.mass = mass
        self.speed = 0

    def __str__(self):
        return (f"Brand: {self.brand}\tModel: {self.model}\tMaxSpeed: {self.max_speed}\tMass: {self.mass}")

    def move(self, speed):
        if speed in range(0, int(self.max_speed)):
            self.speed = speed
        else:
            print("Error speed : ", self.brand, self.model,
                  "can't drive with speed ", speed, " km/h",
                  "maximum speed = ", self.max_speed)
            self.speed = 0

    def print_speed(self):
        print("  --> ", self.brand, self.model, "drive with speed ", self.speed, " km/h")

class Automotive(Transport):
    """
    class Automotive - child class of automotive transport
                       characteristics: brand, model, max_speed, mass, wheels
                       example: Automotive("BMW", "X5", "210", "2500", "4")
    """

    def __init__(self, brand, model, max_speed, mass, wheels):
        super().__init__(brand, model, max_speed, mass)
        self.wheels = wheels

    def __str__(self):
        return super().__str__() + "\tWheels: {}".format(self.wheels)


class Aircraft(Transport):
    """
    class Aircraft - child class of aviation transport, contain airplane and helicopters
                     characteristics: brand, model, max_speed, mass, group
                     example: Aircraft("Boeing", "773", 1200, 5300, "Airplane")
    """

    def __init__(self, brand, model, max_speed, mass, group):
        super().__init__(brand, model, max_speed, mass)
        self.group = group

    def __str__(self):
        return super().__str__() + "\tGroup: {}".format(self.group)


class Boat(Transport):
    """
    class Boat - child class of boat transport, contain boats and submarines
                 characteristics: brand, model, max_speed, mass, propeller
                 example: Boat("Yamaha", "G5", 45, 450, 1)
    """

    def __init__(self, brand, model, max_speed, mass, propeller):
        super().__init__(brand, model, max_speed, mass)
        self.propeller = propeller

    def __str__(self):
        return super().__str__() + "\tPropeller: {}".format(self.propeller)


class Train(Transport):
    """
    class Train - child class of railway transport
                  characteristics: brand, model, max_speed, mass, propeller
                  example: Train("Hyundai", "Rotem", 170, 48000, "electro")
    """
    def __init__(self, brand, model, max_speed, mass, engine):
        super().__init__(brand, model, max_speed, mass)
        self.engine = engine

    def __str__(self):
        return super().__str__() + "\tEngine: {}".format(self.engine)

def print_transport(transport):
    for item in transport:
        print(item)
        if item.speed > 0 :
            item.print_speed()

def main():
    """Demonstrate a create different classes of transport"""
    print("Module start as a script\n","-"*30)
    print(main.__doc__, '\n', "-"*30)
    print("Description:")
    print(Transport.__doc__)
    print(Automotive.__doc__)
    print(Aircraft.__doc__)
    print(Boat.__doc__)
    print(Train.__doc__)

    transport = [Automotive("BMW", "X5", "210", "2500", "4"),
                 Automotive("Audi", "T8", "220", "1900", "4"),
                 Aircraft("Boeing", "773", 1200, 5300, "Airplane"),
                 Boat("Yamaha", "G5", 45, 450, 1),
                 Train("Hyundai", "Rotem", 170, 48000, "electro")]

    print("List of all transport:")
    print("-"*30, "\n")
    print_transport(transport)    


if __name__ == '__main__':
    main()
