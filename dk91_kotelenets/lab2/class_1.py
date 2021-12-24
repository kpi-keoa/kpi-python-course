class Creature:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return 'Name: {} \t Species: {} \t Age: {}'.format(self.name, self.species, self.age)

    def __add__(self, other):
        return self.name + other

    def __len__(self):
        return len(self.name)


class Animal(Creature):
    def sleep(self):
        print(self.name + ' is sleeping')


class Pet(Creature):
    def play(self):
        print(self.name + ' is playing')


class Dog(Animal, Pet):
    def bark(self):
        print(self.name + ' is barking')


class Cat(Animal, Pet):
    def feedme(self):
        print(self.name + ' wants to eat')


def main():
    sobaka = Dog('Buddy', 'Dog', 5)
    print(sobaka)
    print(sobaka + ' is a americal bulldog')
    print(len(sobaka))
    sobaka.sleep()
    sobaka.play()
    sobaka.bark()


if __name__ == '__main__':
    main()
