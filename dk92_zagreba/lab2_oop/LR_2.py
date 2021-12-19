
class komponent:
    def temperature (self, t):
        self.temp=t


class rezistor(komponent): 
    def __init__ (self, om, t):
        self.om=om
        self.temperature(t)

    def __eq__(self, other):
        return self.om == other.om
    def __ne__(self, other):
        return self.om != other.om
    def __lt__(self, other):
        return self.om < other.om
    def __gt__(self, other):
        return self.om > other.om
    def __le__(self, other):
        return self.om <= other.om
    def __ge__(self, other):
        return self.om >= other.om

    def __repr__(self):#меняет отображение в системе
        return f"Резистор нежен для добавления сопротивления в {self.om} Om"



class capasitor(komponent):
    def __init__ (self, Far, t):
        self.far=Far
        self.temperature(t)
    def __str__(self):#меняет отображение при вызове принт
        return f"Конденсатор нужен для добавления емкости в {self.far} Фарад"

class capasitor_smd(capasitor):
    def __init__ (self, Far, t, tip):
        self.far=Far
        self.temperature(t)
        self.tipe=tip


if __name__ == "__main__":
    def _demonstrate_():
        print("\nДемонстрация роботы")
        rezist = rezistor(500, 20)
        print(rezist.om, "om", rezist.temp,"t", rezist)
        cap = capasitor(50, 20)
        print(cap.far, "Farad", cap.temp,"t", cap)
        cap_smd = capasitor_smd(10, 240, 8163)
        print(cap_smd.far, "Farad", cap_smd.temp,"t", cap_smd.tipe,"tip", cap_smd)
        rezist_2 = rezistor(500, 20)
        if(rezist_2 == rezist):
            print("==")
        if(rezist_2 <= rezist):
            print(">=")
        if(rezist_2 == rezist):
            print("<=")

        rezist_2.om=1000

        if(rezist_2 != rezist):
            print("!=")
        if(rezist_2 > rezist):
            print(">")
        rezist_2.om=1
        if(rezist_2 < rezist):
            print("<")





if __name__ == "__main__":
    print("etod kod ne vipolnaetsa pri vizove ckripta iz drugogo koda")
    _demonstrate_()


   
