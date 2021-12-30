class Personage():
    def __init__(self, name, party, sex):
        self.name = name
        if sex == "man" or sex == "woman":
            self.sex = sex
        else:
            return "error: there can be no such sex"
        self.party = party

    def for_the(self):
        print("For the ", self.party)

class Mage(Personage):
    def __init__(self, name, party, sex, lvl):
        super().Personage.__init__(self, name, party, sex)
        if lvl.isdigit():
            self.lvl = lvl
        else:
            return "error: Level must be a number!"

    def spell(self):
        if lvl <= 5 :
            print("puck!")
        elif lvl > 5 and lvl <= 10:
            print("bang!")
        elif lvl > 10:
            print("trah! babah!!!!")

class Warrior(Personage):
    def __init__(self, name, party, sex, item):
        super().Personage.__init__(self, name, party, sex)
        if item == "sword" or item == "bow":
            self.item = item
        else:
            return "item = sword or bow"

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


