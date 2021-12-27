#!/usr/bin/env python3
import os

class Machinery:
    """Machinery class.
    parameters:
    -Ear of production
    -Price
    -Producing country
    -Volume
    -Power
    -Diagonal
    -Processor
    -Video card
    """


    ear_of_production = 0
    price = 0
    producing_country = ""
    volume = 0
    power = 0
    diagonal = 0
    processor = ""
    video_card = ""

    def __init__(self, ear = 0, price = 0,
                 country = "unknown",volume = 0,
                 power = 0, diagonal = 0, processor = "unknown",
                 video_card = "unknown"):
        """Machinery class constructor"""
        self.ear_of_production = ear
        self.price = price
        self.producing_country = country
        self.volume = volume
        self.power = power
        self.diagonal = diagonal
        self.processor = processor
        self.video_card = video_card


    def print_ear(self):
        """The method displays the year and country"""
        if(self.ear_of_production != "unknown" and elf.producing_country != "unknown"):
            print("The device is made in ", self.ear_of_production,
                  " in country ", self.producing_country, "\n")
        else:
            print("Unknown\n")

    def print_price(self):
        """Displays the price of the product"""
        if(self.price != 0):
            print("The price of the device: ", self.price, "\n")
        else:
            print("Unknown\n")

    def change_price(self, new_price):
        """Changes the price and outputs the price"""
        self.price = new_price
        print("New price for the product: ", self.price, "\n")

    def __str__(self):
        device = "The device is made in: " + str(self.ear_of_production) + \
        " in country " + str(self.producing_country) + "price - " + str(self.price) + \
        "\n"

        if(self.__class__.__name__ == "Microwave"):
            device = device + "Microwave volume: " + str(self.volume) + \
        " power: " + str(self.power) + "\n"

        if(self.__class__.__name__ == "Tv"):
            device = device + "Diagonal of the monitor: " + str(self.diagonal) + "\n"

        if(self.__class__.__name__ == "Leptop"):
            device = device + "Laptop processor: " + str(self.processor) + \
        " video card: " + str(self.video_card) + "\n"

        return device

class Microwave(Machinery):

    def __init__(self, ear = 0, price = 0,
                 country = "unknown",volume = 0,
                 power = 0):
        self.ear_of_production = ear
        self.price = price
        self.producing_country = country
        self.volume = volume
        self.power = power

    def print_power(self):
        """Outputs microwave power"""
        print("Microwave power: ", self.power, "\n")



class Tv(Machinery):

    def __init__(self, ear = 0, price = 0,
                 country = "unknown", diagonal = 0):
        self.ear_of_production = ear
        self.price = price
        self.producing_country = country
        self.diagonal = diagonal

    def print_diagonal(self):
        """Displays the diagonal of the monitor"""
        print("Diagonal TV: ", self.diagonal, "\n")

class Leptop(Machinery):
    def __init__(self, ear = 0, price = 0,
                 country = "unknown",volume = 0,
                 power = 0, diagonal = 0, processor = "unknown",
                 video_card = "unknown"):
        self.ear_of_production = ear
        self.price = price
        self.producing_country = country
        self.processor = processor
        self.video_card = video_card

    def print_processor(self):
        """Displays which processor in the laptop"""
        print("This laptop has a processor: ", self.processor, "\n")


if(__name__ == '__main__'):
    mirta = Microwave(2020, 1400, "Korea", 6, 1300)
    soni = Tv(2019, 5000, "Japan", 40)
    acer = Leptop(2018, 50000, "Ukraine", "intel", "nvidia")

    soni.print_price()
    acer.change_price(40000)


    print(mirta)
    print(soni)
    print(acer)

