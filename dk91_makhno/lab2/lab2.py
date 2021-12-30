class Personage():
    def __init__(self, name, party, gender):
        self.name = name
        self.gender = gender
        self.party = party

    def for_the(self):
        print("For the ", self.party)

class Mage(Personage):
    def __init__(self, name, party, gender, lvl):
        Personage.__init__(self, name, party, gender)
        self.lvl = lvl

    def spell(self):
        if lvl <= 5 :
            print("puck!")
        elif lvl > 5 and lvl <= 10:
            print("bang!")
        elif lvl > 10:
            print("trah! babah!!!!")

class Warrior(Personage):
    def __init__(self, name, party, gender, item):
        Personage.__init__(self, name, party, gender)
        self.item = item

    def attack(self):
        if item == "sword" :
            print("hit!")
        elif lvl == "bow":
            print("shot!")




def main():
    h = Personage("bebra", "Horde", "man")
    h.for_the()
    war = Warrior("bebra", "Horde", "man", "sword")
    war.attack()
    mag = Mage("bebra", "Horde", "man", 25)
    war.spell()


if __name__ == '__main__':
    main()


