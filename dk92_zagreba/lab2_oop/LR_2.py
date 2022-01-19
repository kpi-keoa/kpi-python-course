from functools import total_ordering


class ElectricalComponent:
    def __init__(self, smd, local_name_in, developent_in):
        self.type = smd
        self.local_name = local_name_in
        self.development = developent_in

    def get_clectrical_component_info(self):
        return (
            f"Тип: {self.type}"
            f"\nИмя компонента в схеме: {self.local_name}"
            f"\nИмя производителя: {self.development}"
        )

    # Створення обьекта батька від якого буде наслідування


@total_ordering
class Resistor(ElectricalComponent):
    def __init__(self, smd, local_name, developent, denomination):
        super().__init__(smd, local_name, developent)
        self.denominatione = denomination

    def __eq__(self, other):
        return self.denominatione == other.denominatione

    def __lt__(self, other):
        return self.denominatione < other.denominatione

    def __le__(self, other):
        return self.denominatione <= other.denominatione

    def _repr_(self):
        return f"Игра была создана на {self.denominatione} игроко"

    def get_clectrical_component_info(self):
        return (
            f"{super().get_clectrical_component_info()} \n"
            f"Номинал {self.denominatione}\n"
        )


class Capacitor(ElectricalComponent):
    def __init__(self, smd, local_name, developent, capacity):
        super().__init__(smd, local_name, developent)
        self.capacity = capacity

    def __str__(self):
        return f"Емкость {self.capacity} Фарад"

    def get_clectrical_component_info(self):
        return f"{super().get_clectrical_component_info()} \nЕмкость {self.capacity} Фарад\n"


class Variable_Resistor(Resistor):
    def __init__(self, smd, local_name, developent, denomination, Turnovers):
        super().__init__(smd, local_name, developent, denomination)
        self.Turnovers = Turnovers

    def get_clectrical_component_info(self):
        return f"{super().get_clectrical_component_info()}Оборотов: {self.Turnovers}\n"


if __name__ == "__main__":
    print("Тест")

    R1 = Resistor("SMD", "R1", "Nikom", 160)
    print(R1.get_clectrical_component_info())

    C1 = Capacitor("DIP", "C1", "Radiomag", 0.24)
    print(C1.get_clectrical_component_info())

    R3 = Variable_Resistor("DIP", "R3", "Vishay", 8.2, 5)
    print(R3.get_clectrical_component_info())

    R2 = Resistor("SMD", "R2", "Vishay", 10)

    if R2 == R1:
        print(R2.local_name, "!=", R1.local_name)

    elif R1 >= R2:
        print(R1.local_name, ">=", R2.local_name)

    if R1 > R2:
        print(R1.local_name, ">", R2.local_name)
