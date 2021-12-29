class Tank:
    """This class implements a text game about tanks."""
    
    __NAME, __LVL, __HEALTH, __DMG, __SPEED = 'Noname', 1, 100, 1, 15
    __slots__ = ['__name', '__lvl', '__health', '__dmg', '__speed']


    def __init__(self):
        self.__name = Tank.__NAME
        self.__lvl = Tank.__LVL
        self.__health = Tank.__HEALTH
        self.__dmg = Tank.__DMG
        self.__speed = Tank.__SPEED


    def __str__(self):
        return 'Name: {} \nLvl: {} \nHealth: {} \nDmg: {} \nSpeed: {}'.format(self.__name, self.lvl, self.health, self.dmg, self.speed)


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def lvl(self):
        return self.__lvl


    @lvl.setter
    def lvl(self, lvl_val):
        self.__lvl += Tank.__typeTest(lvl_val)
        if self.__lvl >= 10: self.__lvl = 10

    
    @property
    def health(self):
        return self.__health


    @health.setter
    def health(self, health_val):
        self.__health += Tank.__typeTest(health_val)
        if self.__health >= 100: self._health = 100
        elif self.__health <= 0: print("Tank destroyed") 

    
    @property
    def dmg(self):
        return self.__dmg


    @dmg.setter
    def dmg(self, dmg_val):
        self.__dmg += Tank.__typeTest(dmg_val)
        if self.__dmg >= 30: self.__dmg = 30


    @property
    def speed(self):
        return self.__speed


    @speed.setter
    def speed(self, speed_val):
        self.__speed += Tank.__typeTest(speed_val)


    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ('Must be int')


class Medium_tank(Tank):
    def __init__(self):
        Tank.__init__(self)
        self.name = 'medium_tank'
        self.dmg = 15
        self.speed = -6


class Heavy_tank(Tank):
    def __init__(self):
        Tank.__init__(self)
        self.name = 'heavy_tank'
        self.dmg = 25
        self.speed = -10


def main():
    obj_2 = Medium_tank()
    obj_3 = Heavy_tank()
    print("Your tank characteristics:")
    print(obj_2)
    print("Enemy tank characteristics:")
    print(obj_3)
    while True:
        num = int(input("Your tank is ready to attack! \nPress 1 if you want to shoot or 2 if you want to make an alliance: "))
        if num == 1 or num == 2: break
        else: print("Error, choose 1 or 2") 

    while obj_3.health > 0 and obj_2.health > 0:
        if num == 1:
            obj_3.health = -16
            print("Enemy armor is damaged!")
            obj_2.health = -26
            print("Your tank is damaged!")

            if obj_3.health <= 0: 
                print("Tank", obj_3.name, "destroyed")
                break
            elif obj_2.health <=0: 
                print("Tank", obj_2, "destroyed")
                break
        elif num == 2:
            print("Congratulations, you have an ally! You did the right thing.")
            break


if __name__ == '__main__':
    main()