from abc import ABC, abstractmethod


class ChessPiece(ABC):
    cord = ""

    def __str__(self):
        return "ChessPiece"

    def draw(self):
        """
        общий метод, который будут использовать
        все наследники этого класса
        """
        print("Drew a chess piece")

    @abstractmethod
    def move(self):
        """
        абстрактный метод, который будет необходимо,
        переопределять для каждого подкласса
        """
        pass


class Queen(ChessPiece):
    def __init__(self, side):
        if side == "black":
            self.cord = ""
        elif side == "white":
            self.cord = ""

    def __str__(self):
        return f"Queen on {self.cord}"

    def move(self, move):
        self.cord = move
        print(f"Moved Queen to {move}")


class Pawn(ChessPiece):
    def __init__(self, cord):
        self.cord = cord

    def __str__(self):
        return f"Pawn on {self.cord}"

    def move(self, move):
        self.cord = move
        print(f"Moved Pawn to {move}")


class Animal(ABC):
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old animal"

    def say(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age, gender="male"):
        super().__init__(name, age)
        self.gender = gender

    def __str__(self):
        return f"My name is {self.name}, I am {self.age} \
            years old {self.gender} mammal"

    def say(self):
        pass


class Cat(Mammal):
    def __init__(self, name, age, gender, color='black'):
        super().__init__(name, age, gender)
        self.color = color

    def __str__(self):
        return f'''My name is {self.name}, I am {self.age} years old
         {self.gender} {self.color} cat.'''

    def say(self):
        print("Meow!")


class Dog(Mammal):
    def __init__(self, name, age, gender, color='black'):
        super().__init__(name, age, gender)
        self.color = color

    def __str__(self):
        return f'''My name is {self.name}, I am {self.age} years old
         {self.gender} {self.color} dog.'''

    def say(self):
        print("Woof!")


def logic():
    my_cat = Cat("Lis", 2, "m", "white")
    print(my_cat)
    my_cat.say()
    my_dog = Dog("Trepp", 4, "m")
    print(my_dog)
    my_dog.say()
    white_queen = Queen("white")
    white_queen.move("e4")
    print(white_queen)


if __name__ == '__main__':
    logic()
