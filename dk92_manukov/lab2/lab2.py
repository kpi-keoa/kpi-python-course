#!/usr/bin/env python

"""This program is a demonstration of my knowledge
about classes, metods and OOP."""

class Cars:
    """First class, basis functions"""

    def __init__(self, mark, model = 'unknown', country = 'Unknown'):
        self.mark = mark
        self.model = model
        self.country = country

    def __str__(self):
        """Base __str__"""

        carslog = "Car's mark is " + str(self.mark) + ".\n"
        carslog = carslog + "Model is " + str(self.model) + ".\n"
        if(self.country == 'Unknown'):
            self.country = 'unknown country'
        carslog = carslog + "It create in " + self.country + ".\n"
        return carslog

class Type(Cars):
    """This class uses heredity"""

    def __init__(self, mark, model = 'unknown', country = 'Unknown', type = 'Unknown'):
        Cars.__init__(self, mark, model, country)
        self.type = type

    def __str__(self):
        if(self.type == 'Unknown'):
            self.type = 'unknown fuel'
        carslog = Cars.__str__(self) + "This car use " + self.type + " to move.\n"
        return carslog

class Wd(Type):
    """This class uses method super heredity, property with setter and incapsulation"""

    def __init__(self, mark, model='unknown', country='Unknown', type='Unknown', __drive='Unknown'):
        super().__init__(mark, model, country, type)
        self.__drive = __drive

    def __str__(self):
        self.__drive = self.__drive.capitalize()
        carslog = super().__str__()
        if(self.__drive == 'Front'):
            carslog = super().__str__() + "Just use gas pedal to return control!\n"
        elif(self.__drive == 'Rear'):
            carslog = super().__str__() + "Just use gas pedal to return taste of life!\n"
        return carslog

    @property
    def drive(self):
        print(f"\n\n {self.__drive} \n\n")

    @drive.setter
    def drive(self, new):
        self.__drive = str(new)

if(__name__ == '__main__'):
    """Test-code-part"""

    zaz = Type('ZAZ', 'Vida', 'Ukraine', 'something')
    bentley = Wd('Bentley', 'Bentayga', 'UK', 'oil', 'rear')
    maybach = Wd('Maybach', 'Zeppelin', 'Deutchland', 'electricity')

    print(maybach)

    maybach.drive = "front"
    maybach.drive

    print(zaz)
    print(bentley)
    print(maybach)
