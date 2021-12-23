
from functools import total_ordering
class Component:
    def temperature(self, t):
        self.temp = t


@total_ordering
class Resistor(Component):
    def __init__(self, ohm, t):
        self.ohm = ohm
        self.temperature(t)

    def __eq__(self, other):
        return self.ohm == other.ohm

    def __lt__(self, other):
        return self.ohm < other.ohm

    def __repr__(self):  # меняет отображение в системе
        return f"Резистор нежен для добавления сопротивления в {self.ohm} Om"


class Сapaсitor(Component):
    def __init__(self, Far, t):
        self.far = Far
        self.temperature(t)

    def __str__(self):  # меняет отображение при вызове принт
        return f"Конденсатор нужен для добавления емкости в {self.far} Фарад"


class CapacitorSMD(Сapaсitor):
    def __init__(self, Far, t, tip):
        self.far = Far
        self.temperature(t)
        self.tipe = tip


if __name__ == "__main__":

    def _demonstrate_():
        print("\nДемонстрация роботы")
        rezist = Resistor(500, 20)
        print(rezist.ohm, "ohm", rezist.temp, "t", rezist)
        cap = Сapaсitor(50, 20)
        print(cap.far, "Farad", cap.temp, "t", cap)
        cap_smd = CapacitorSMD(10, 240, 8163)
        print(cap_smd.far, "Farad", cap_smd.temp, "t", cap_smd.tipe, "tip", cap_smd)
        rezist_2 = Resistor(500, 20)
        if rezist_2 == rezist:
            print("==")
        if rezist_2 <= rezist:
            print(">=")
        if rezist_2 == rezist:
            print("<=")

        rezist_2.om = 1000

        if rezist_2 != rezist:
            print("!=")
        if rezist_2 > rezist:
            print(">")
        rezist_2.om = 1
        if rezist_2 < rezist:
            print("<")


if __name__ == "__main__":
    print("Етот код не выполняеться при вызове скрипта из другого кода")
    _demonstrate_()
