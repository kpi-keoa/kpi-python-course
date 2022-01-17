# Tamagotchi

import os, platform
from random import randrange

if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

class Pet(object):
    pets = []
    pets_names = []
    total_amount = 0

    excitement_reduce = 3
    excitement_warning = 3
    excitement_max = 10
    food_reduce = 2
    food_warning = 3
    food_max = 10
    vocab = ["Mommy", "Hello"]

    def __init__(self, name):
        self.name = name
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]
        Pet.pets.append(self)
        Pet.total_amount += 1
        Pet.pets_names.append(name)

    def __clock_tick(self):
        self.excitement -= 1
        self.food -= 1

    def mood(self):
        mood_is = None
        if self.food > self.food_warning and self.excitement > self.excitement_warning:
            mood_is = "happy"
        elif self.food < self.food_warning:
            mood_is = "hungry"
        else:
            mood_is = "borred"
        return mood_is

    def __str__(self):
        return "I am " + self.name + "and I feel " + self.mood()

    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        print(f"Hi, I am {self.name} and I feel {self.mood()} now")
        print(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()

    def eat(self, food = 0):
        print("Mmm... Thank you!:)")
        meal = randrange(self.food, self.food_max)
        self.food += meal
        
        if self.food < 0:
            self.food = 0
            print("I am still hungry!")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I am full!")
        self.__clock_tick()
        
    def play(self):
        fun = randrange(self.excitement, self.excitement_max)
        print("Wowww!!!")       
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("I am bored.")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("I am so happy!")
        self.__clock_tick()

    def pet_death(self):
        if self.food < 0:
            print(f"{self.name} is died:(")
    def pet_sleep(self):
        if self.excitement < excitement_warning:
            print(f"{self.name} is tired")
        if self.excitement == 0:
            print(f"Tshh... {self.name} is sleeping")

def get_pet():
    pet_name = input("Name your pet: ").title().strip()
    pet = Pet(pet_name)
    input("Hello! I am " + pet.name + "\nPress Enter to start..")
    return pet

def status():
    print("Total pets now:", Pet.total_amount)

def main():
    name_of_pet = input("Name your pet: ").title().strip()

    #Create a new pet
    my_pet = Pet(name_of_pet)
    input("Hello! I am " + my_pet.name + "\nPress Enter to start..")

    choice = None
        
    while choice != "0":
        menu = ("""
            Main menu:

            0 - Quit
            1 - Get new pet
            2 - Number of pets
            3 - Choose a pet""")
        print(menu)
        choice = input("Your choice: ")

        if choice == "0":
            sure = input("Are you sure you wanna quit? (Y/N)")
            if sure.upper() == "Y":
                print("Goodbye!")
            elif sure.upper() == "N":
                choice == "0"
        
        elif choice == "1":
            new_pet = get_pet()
        elif choice == "2":
            status()
            
            get_new_pet = input("Do you want to get one more pet? (Y/N)")
            if get_new_pet.upper() == "Y":
                get_pet()
            elif get_new_pet.upper() == "N":
                sure_quit = input("Do you want to quit? (Y/N)")
                if sure_quit.upper() == "N":
                    print(menu)
                    choice = input("Your choice: ")
                else:
                    choice = "0"
            else:
                print(menu)
                
        elif choice == "3":
            choose_the_pet = input("Input pet name: ").title().strip()
            if choose_the_pet not in Pet.pets_names:
                print("You don't have such a pet!")
                choose_the_pet = input("Input pet name: ").title().strip()
            else:
                print("""
                Select the action:
                            
                1 - Talk to pet
                2 - Feed the pet
                3 - Play with a pet
                4 - Teach the pet""")
                choice = input("Your choice: ")

                if choice == "1":
                    my_pet.talk()
                elif choice == "2":
                    my_pet.eat()
                elif choice == "3":
                    my_pet.play()
                elif choice == "4":
                    new_word = input("Write the word: ")
                    my_pet.teach(new_word)
                else:
                    print("No such item on the menu")

        else:
            print("No such item on the main menu")

if __name__ == '__main__':
    main()
    input("Push Enter for Exit")
