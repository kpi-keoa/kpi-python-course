import random
from array import *


class cube:
    """
    Klas cube
     `` roll '' - rolls a die. At the same time, it sets the value of how the dice fell.
    And it returns the same value.  Provide that after rolling the die cannot be rolled
    again if, upon initialization, is_rerollable (default False) is not set to True.
     `` handout`` - `` classmethod``, which creates M cubes for N players
    Special (dunder-) methods for comparing two cubes. You can only compare cubes that
    have already been abandoned.
    """

    def __init__(self, edge_in=6, is_rerollable_in=False):
        self.edge = edge_in
        self.is_rerollable = is_rerollable_in
        self.thrown = False
        self.meaning = self.edge + 1

    def roll(self):
        if self.thrown == False or self.is_rerollable == True:
            self.meaning = random.randint(1, self.edge)
            self.thrown = True
        return self.meaning

    def __str__(self):
        if self.thrown == False:
            self.roll()
        return (f"    ////////////\n  //       // //\n////////////  //\n",)
        "//        //  //\n//   {self.meaning}    //  //\n//        ////\n",
        "////////////\n{self.edge, self.is_rerollable, self.thrown, self.meaning}"

    def __eq__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning == other.meaning
        else:
            return -1

    def __ne__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning != other.meaning
        else:
            return -1

    def __lt__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning < other.meaning
        else:
            return -1

    def __gt__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning > other.meaning
        else:
            return -1

    def __le__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning <= other.meaning
        else:
            return -1

    def __ge__(self, other):
        if self.thrown == True and other.thrown == True:
            return self.meaning >= other.meaning
        else:
            return -1

    @classmethod
    def handout(self, M: int, N: int):
        player_list = []
        for a in range(M * N):
            player_list.append(cube().roll())
        return player_list


class cube11(cube):
    def __init__(self, edge_in=11, is_rerollable_in=False):
        self.edge = edge_in
        self.is_rerollable = is_rerollable_in


class cube15(cube):
    def __init__(self, edge_in=15, is_rerollable_in=False):
        self.edge = edge_in
        self.is_rerollable = is_rerollable_in


if __name__ == "__main__":
    """
    A game for 2 players, throwing dice, summing up points and then comparing.
    """
    a = cube()
    b = cube()
    print(">=", a >= b)
    print("<=", a >= b)
    print(a)
    print(">=", a >= b)
    print("<=", a >= b)

    print(b)
    print(">=", a >= b)
    print("<=", a >= b)
    M = 5
    N = 2
    while True:
        plist = a.handout(M, N)
        print(plist)
        result1 = 0
        result2 = 0

        for i in range(5):
            result1 = result1 + plist[i]
            result2 = result2 + plist[i + 5]
        print("result1", result1)
        print("result2", result2)
        if result1 == result2:
            print("Ничья")
        elif result1 > result2:
            print("игрок 1 победил")
        elif result1 < result2:
            print("игрок 2 победил")
        input("Press Enter to continue game...")
