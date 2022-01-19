class Transport:
    """class transport """
    def __init__(self, brand, model, maxSpeed, mass):
        self.brand = brand
        self.model = model
        self.maxSpeed = maxSpeed
        self.mass = mass

    def __str__(self):
        return ("Brand: {}\tModel: {}\tMaxSpeed: {}\tMass: {}"
                .format(self.brand, self.model,  self.maxSpeed, self.mass))


class Automotive(Transport):
    def __init__(self, brand, model, maxSpeed, mass, wheels):
        Transport.__init__(self, brand, model, maxSpeed, mass)
        self.wheels = wheels

    def __str__(self):
        return super().__str__() + "\tWheels: {}".format(self.wheels)


class Aircraft(Transport):
    def __init__(self, brand, model, maxSpeed, mass, group):
        Transport.__init__(self, brand, model, maxSpeed, mass)
        self.group = group

    def __str__(self):
        return super().__str__() + "\tGroup: {}".format(self.group)


class Boat(Transport):
    def __init__(self, brand, model, maxSpeed, mass, propeller):
        Transport.__init__(self, brand, model, maxSpeed, mass)
        self.propeller = propeller

    def __str__(self):
        return super().__str__() + "\tPropeller: {}".format(self.propeller)


class Train(Transport):
    def __init__(self, brand, model, maxSpeed, mass, engine):
        Transport.__init__(self, brand, model, maxSpeed, mass)
        self.engine = engine

    def __str__(self):
        return super().__str__() + "\tEngine: {}".format(self.engine)


def main():
    print('Module start as a script\n--------------------------------')
    transport = [Automotive("BMW", "X5", "180", "2300", "4"),
                 Aircraft("Boeing", "773", 1200, 5300, "Airplane"),
                 Boat("Yamaha", "G5", 45, 450, 1),
                 Train("Hyundai", "Rotem", 170, 48000, "electro")]
    for item in transport:
        print(item)
        print()


if __name__ == '__main__':
    main()
