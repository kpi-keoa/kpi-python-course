#!/usr/bin/env python3


class tank:
    def __init__(self, title, nation, level, crew_num):
        self.description = (title, nation, level, crew_num)
        self.title = title
        self.nation = nation
        self.level = level
        self.crew_num = crew_num


    def __str__(self):
        return 'Title: {} \t Species: {} \t Level {} \t Crew_num: {}'.format(self.title, self.nation, self.level, self.crew_num)

    
    def __len__(self):
        return(len(self.title))
    

class light_tank(tank):
    def speed(self):
        print(self.title + ' is light tank')

class medium_tank(light_tank):
    def medium_armour(self):
        print(self.title + ' is medium tank')


class heavy_tank(medium_tank):
    def heavy_armour(self):
        print(self.title + ' is heavy tank')


class sp_artillery(tank):
    def weapon(self):
        print(self.title + ' is artillery')


class at_sp_artillery(tank):
    def howitzer(self): 
        print(self.title + ' is anti-tank self-propelled gun')


def main():
    tank1 = light_tank('LT432', 'Soviet', '8', '3')
    tank2 = medium_tank('T-34', 'Soviet', '5', '5')
    tank4 = heavy_tank('IS-7', 'Soviet', '10', '6')
    tank5 = sp_artillery('SU-8', 'Soviet', '6', '5')
    tank6 = at_sp_artillery('SU-152', 'Soviet', '7', '5')
    print(tank1)
    print(len(tank1))
    tank1.speed()
    print(tank2)
    tank2.medium_armour()
    print(tank4)
    tank4.heavy_armour()
    print(tank5)
    tank5.weapon()
    print(tank6)
    tank6.howitzer()


if __name__ == '__main__':
    main()