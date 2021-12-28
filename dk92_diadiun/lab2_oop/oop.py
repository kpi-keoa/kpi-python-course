import os
import sys

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

clear_screen()


class Device:
    """Device class.
    Accepting parameters:
    - model
    - year
    - generation
    - Pencil Connected
    - Battery charge
    """

    def __init__(self, model="Unavailable", year=0,
                 generation=0, Pencil=False, Battery=0):
        """Device Class Constructor"""
        self.model = model
        self.year = year
        self.generation = generation
        self.pencil_connected = Pencil
        self.battery_charge = Battery

    def get_model(self):
        """Function prints device model, if available.
        Else prints unknown model
        """
        if(self.model != "Unavailable\n"):
            print(self.model)
        else:
            print("Unknown model\n")

    def get_year(self):
        """Function prints device year, if available"""
        if (self.year != 0):
            print(self.model, "Device year:", self.year, "\n")

    def get_generation(self):
        """Function prints device generation, if available"""
        if (self.model != "Unavailable" and self.generation != 0):
            print(self.model, "Device generation:", self.generation, "\n")

    def get_battery(self):
        """Function prints device battery charge, in %"""
        print(self.model, "Battery Charge:", self.battery_charge, "%\n")

    def set_battery(self, newbattery_charge):
        """Function sets new battery charge"""
        self.battery_charge = newbattery_charge
        print(self.model, "new battery charge:", self.battery_charge, "%\n")

    def __str__(self):
        device_log = "Device model: " + str(self.model) + "\n"

        if(self.__class__.__name__ != "Pencil"):
            device_log = device_log + "model year: " + \
                        str(self.year) + "\n"
        if(self.__class__.__name__ != "Laptop"):
            device_log = device_log + "Device generation: " + \
                        str(self.generation) + "\n"
        if(self.__class__.__name__ == "Tablet"):
            device_log = device_log + "Is Pencil Connected: " + \
                        str(self.pencil_connected) + "\n"
        device_log = device_log + "Battery Charge: " + \
                    str(self.battery_charge) + "%\n"
        return device_log


class Laptop(Device):
    """Laptop Class.
    Accepting parameters:
    - model
    - year
    - Battery charge
    """

    def __init__(self, model="Unavailable", year=0, battery_charge=0):
        """Laptop Class Constructor"""
        self.model = model
        self.year = year
        self.generation = 0
        self.pencil_connected = False
        self.battery_charge = battery_charge


class Tablet(Device):
    """Tablet Class.
    Accepting parameters:
    - model
    - generation
    - year
    - Pencil Connected
    - Battery charge
    """

    def __init__(self, model="Unavailable", year=0, generation=0,
                 pencil_connected=False, battery_charge=0):
        """Tablet Class Constructor"""

        self.model = model
        self.year = year
        self.generation = generation
        self.pencil_connected = pencil_connected
        self.battery_charge = battery_charge

    def get_pencil(self):
        """Function prints pencil connection status"""
        print(self.model, "Pencil Connected:", self.pencil_connected, "\n")

    def set_pencil(self, newpencil_connected):
        """Function changes pencil connection status"""
        self.pencil_connected = newpencil_connected
        print(self.model, "Pencil Connected?:", self.pencil_connected, "\n")


class Pencil(Device):
    """Pencil Class.
    Accepting parameters:
    - generation
    - Battery Charge
    """

    def __init__(self, model="Unavailable", generation=0, battery_charge=0):
        """Pencil Class Constructor"""
        self.model = model
        self.year = 0
        self.generation = generation
        self.pencil_connected = False
        self.battery_charge = battery_charge


if(__name__ == '__main__'):
    macbook_pro = Laptop("Macbook Pro", 2019, 75)
    ipad_pro = Tablet("IPad Pro", 2016, 2, True, 98)
    ipad_air = Tablet("IPad Air", 2018, 3, False, 23)
    IPencil = Pencil("IPencil", 1, 100)

    macbook_pro.get_battery()
    ipad_air.get_generation()
    ipad_pro.get_pencil()

    macbook_pro.set_battery(50)

    ipad_air.set_pencil(True)
    ipad_air.get_pencil()

    print(macbook_pro)
    print(ipad_pro)
    print(ipad_air)
    print(IPencil)
