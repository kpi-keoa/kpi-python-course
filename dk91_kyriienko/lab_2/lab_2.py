#!/usr/bin/env python3
import pics
import requests as req 


class Human:
    def __init__(self, name, surname, male, age=1):
        self.name = name
        self.surname = surname
        self.male = male
        if age > 0:
        	self.age = age
        else:
        	raise Exception("Enter correct age!")

    def __str__(self):
        return pics.h_logo

    def __eq__(self, other):
        if self.age == other.age:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.age != other.age:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

    def __le__(self, other):
        if self.age <= other.age:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.age >= other.age:
            return True
        else:
            return False

    def change_age(self, new_age):
    	self.age = new_age

    def whois(self):
        print(f'{self.name} {self.surname} is {self.male}, {self.age} yeras old!')


class Writer(Human):
    def __init__(self, name, surname, male, age, book):
        super().__init__(name, surname, male, age)
        self.book = book

    def __str__(self):
        return pics.book

    def whois(self):
        super().whois()
        print(f'Author of {self.book}')


class Singer(Human):
    def __init__(self, name, surname, male, age, song):
        super().__init__(name, surname, male, age)
        self.song = song

    def __str__(self):
        return pics.note

    def whois(self):
        super().whois()
        print(f'Author of {self.song}')


class Painter(Human):
    def __init__(self, name, surname, male, age, picture):
        super().__init__(name, surname, male, age)
        self.picture = picture

    def __str__(self):
	    return pics.mona

    def whois(self):
        super().whois()
        print(f'Author of {self.picture}')


if __name__ == '__main__':
    
    person_writer = Writer('Taras', 'Shevchenko', 'man', 1, 'Kobzar')

    person_writer.change_age(41)
    person_writer.whois()

    print(person_writer)

    person_painter = Painter('Leonardo', 'Da Vinchi', 'man', 51, 'Jakonda')
    person_paint = Painter('Ian', 'Vermeer', 'man', 50, 'Little street')

    person_painter.whois()

    print(person_painter)


    print(person_painter > person_paint)