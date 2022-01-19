import random


class Dice:

    pretty_dict = {1: "---------\n|       |\n|   o   |\n|       |\n---------",
                   2: "---------\n|  o    |\n|       |\n|    o  |\n---------",
                   3: "---------\n|  o    |\n|   o   |\n|    o  |\n---------",
                   4: "---------\n|  o o  |\n|       |\n|  o o  |\n---------",
                   5: "---------\n|  o o  |\n|   o   |\n|  o o  |\n---------",
                   6: "---------\n|  o o  |\n|  o o  |\n|  o o  |\n---------"}

    result = None
    locked = False

    def __init__(self, num: int = 6, is_rerollable: bool = False) -> None:
        self.num = num
        self.is_rerollable = is_rerollable

    def roll(self) -> int:
        """Сформировать результат кубика.

        Вернуть число грани
        """
        self.result = random.randint(1, self.num)
        if not self.is_rerollable:
            self.locked = True
        return self.result

    @classmethod
    def handout(cls, M: int, N: int) -> str:
        """Провести игру в кости

        M - количество игроков
        N - количество костей у игрока
        """
        users_dice = {}
        for i in range(M):
            users_dice.update({i: []})
            for _ in range(N):
                users_dice[i].append(Dice())
        for i in range(N):
            print(f"{i + 1} round:")
            users_dice[0][i].roll()
            users_dice[1][i].roll()
            if (users_dice[0][i] == users_dice[1][i]):
                print("draw")
            elif (users_dice[0][i] > users_dice[1][i]):
                print("first player win")
            else:
                print("second player win")

    def __lt__(self, other) -> bool:
        if self.result and other.result:
            return self.result < other.result

    def __le__(self, other) -> bool:
        if self.result and other.result:
            return self.result <= other.result

    def __eq__(self, other) -> bool:
        if self.result and other.result:
            return self.result == other.result

    def __ne__(self, other) -> bool:
        if self.result and other.result:
            return self.result != other.result

    def __gt__(self, other) -> bool:
        if self.result and other.result:
            return self.result > other.result

    def __ge__(self, other) -> bool:
        if self.result and other.result:
            return self.result >= other.result

    def pretty_dunder(self) -> str:
        """Красивый вывод грани кубика."""
        if self.result:
            return self.pretty_dict[self.result]


class ElvDice(Dice):
    def __init__(self, num: int = 11, is_rerollable: bool = False) -> None:
        self.num = num
        self.is_rerollable = is_rerollable

    def pretty_dunder(self) -> str:
        return "Sorry not avaliable"


class FifDice(Dice):
    def __init__(self, num: int = 15, is_rerollable: bool = False) -> None:
        self.num = num
        self.is_rerollable = is_rerollable

    def pretty_dunder(self) -> str:
        return "Sorry not avaliable"


if __name__ == "__main__":
    f_dice = Dice()
    s_dice = Dice()
    print("first_playe: dice roll")
    f_dice.roll()
    print(f_dice.pretty_dunder())
    print("second_playe: dice roll")
    s_dice.roll()
    print(s_dice.pretty_dunder())
    if (f_dice == s_dice):
        print("draw")
    elif (f_dice > s_dice):
        print("first player win")
    else:
        print("second player win")
    Dice.handout(2, 3)
