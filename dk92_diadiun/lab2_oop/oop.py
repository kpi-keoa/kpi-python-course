import os

os.system('clear')


class Device:
    """Device class.
    Accepting parameters:
    - Model
    - Year
    - Generation
    - Pencil Connected
    - Battery charge
    """

    Model = ""
    Year = 0
    Generation = 0
    PencilConnected = False
    BatteryCharge = 0

    def __init__(self, Model="Unavailable", Year=0,
                 Generation=0, Pencil=False, Battery=0):
        """Device Class Constructor"""
        self.Model = Model
        self.Year = Year
        self.Generation = Generation
        self.PencilConnected = Pencil
        self.BatteryCharge = Battery

    def get_model(self):
        """Function prints device model, if available.
        Else prints unknown model
        """
        if(self.Model != "Unavailable\n"):
            print(self.Model)
        else:
            print("Unknown Model\n")

    def get_year(self):
        """Function prints device year, if available"""
        if (self.Year != 0):
            print(self.Model, "Device Year:", self.Year, "\n")

    def get_generation(self):
        """Function prints device generation, if available"""
        if (self.Model != "Unavailable" and self.Generation != 0):
            print(self.Model, "Device Generation:", self.Generation, "\n")

    def get_battery(self):
        """Function prints device battery charge, in %"""
        print(self.Model, "Battery Charge:", self.BatteryCharge, "%\n")

    def set_battery(self, newBatteryCharge):
        """Function sets new battery charge"""
        self.BatteryCharge = newBatteryCharge
        print(self.Model, "new battery charge:", self.BatteryCharge, "%\n")

    def __str__(self):
        DeviceLog = "Device Model: " + str(self.Model) + "\n"

        if(self.__class__.__name__ != "Pencil"):
            DeviceLog = DeviceLog + "Model Year: " + \
                        str(self.Year) + "\n"
        if(self.__class__.__name__ != "Laptop"):
            DeviceLog = DeviceLog + "Device Generation: " + \
                        str(self.Generation) + "\n"
        if(self.__class__.__name__ == "Tablet"):
            DeviceLog = DeviceLog + "Is Pencil Connected: " + \
                        str(self.PencilConnected) + "\n"
        DeviceLog = DeviceLog + "Battery Charge: " + \
                                str(self.BatteryCharge) + "%\n"
        return DeviceLog


class Laptop(Device):
    """Laptop Class.
    Accepting parameters:
    - Model
    - Year
    - Battery charge
    """

    def __init__(self, Model="Unavailable", Year=0, BatteryCharge=0):
        """Laptop Class Constructor"""
        self.Model = Model
        self.Year = Year
        self.Generation = 0
        self.PencilConnected = False
        self.BatteryCharge = BatteryCharge


class Tablet(Device):
    """Tablet Class.
    Accepting parameters:
    - Model
    - Generation
    - Year
    - Pencil Connected
    - Battery charge
    """

    def __init__(self, Model="Unavailable", Year=0, Generation=0,
                 PencilConnected=False, BatteryCharge=0):
        """Tablet Class Constructor"""

        self.Model = Model
        self.Year = Year
        self.Generation = Generation
        self.PencilConnected = PencilConnected
        self.BatteryCharge = BatteryCharge

    def get_pencil(self):
        """Function prints pencil connection status"""
        print(self.Model, "Pencil Connected:", self.PencilConnected, "\n")

    def set_pencil(self, newPencilConnected):
        """Function changes pencil connection status"""
        self.PencilConnected = newPencilConnected
        print(self.Model, "Pencil Now Connected?:", self.PencilConnected, "\n")


class Pencil(Device):
    """Pencil Class.
    Accepting parameters:
    - Generation
    - Battery Charge
    """

    def __init__(self, Model="Unavailable", Generation=0, BatteryCharge=0):
        """Pencil Class Constructor"""
        self.Model = Model
        self.Year = 0
        self.Generation = Generation
        self.PencilConnected = False
        self.BatteryCharge = BatteryCharge


if(__name__ == '__main__'):
    MacbookPro = Laptop("Macbook Pro", 2019, 75)
    IPadPro = Tablet("IPad Pro", 2016, 2, True, 98)
    IPadAir = Tablet("IPad Air", 2018, 3, False, 23)
    IPencil = Pencil("IPencil", 1, 100)

    MacbookPro.get_battery()
    IPadAir.get_generation()
    IPadPro.get_pencil()

    MacbookPro.set_battery(50)

    IPadAir.set_pencil(True)
    IPadAir.get_pencil()

    print(MacbookPro)
    print(IPadPro)
    print(IPadAir)
    print(IPencil)
