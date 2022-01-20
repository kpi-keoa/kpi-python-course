
from dataclasses import dataclass

@dataclass
class dice:
    faces: int = 6
    value: int = None
    is_rerollable:bool = False
    
    def __init__(self, faces: int = 6, value: int = None, is_rerollable:bool = False):
        self.faces = faces
        self.value = value
        self.is_rerollable = is_rerollable

    def roll(self, val):
        #return self.value = random.randint(1, 6)
        if(not self.is_rerollable):
            self.value = val
            self.is_rerollable = True
            return self.value
        if(self.is_rerollable):
            print("ERROR dice are alredy rolled")
            return -1
    
    def __lt__(self, other):
        if(not self.is_rerollable):
            print("ERROR first dice not roll!")
            return 0
        if(not other.is_rerollable):
            print("ERROR second dice not roll!")
            return 0
        return self.value < other.value

    def __lt__(self, other):
        if(not self.is_rerollable):
            print("ERROR first dice not roll!")
            return 0
        if(not other.is_rerollable):
            print("ERROR second dice not roll!")
            return 0
        return self.value > other.value

    def __str__(self):
        if(self.value == None):
            return f"""
                     _____ 
                    /____/|
                   |     ||
                   |  ?  ||
                   |_____|/
                                           """
        return f"""
                     _____ 
                    /____/|
                   |     ||
                   |  {self.value}  ||
                   |_____|/
                                           """



if __name__ == "__main__":
    def _demo_():
        print("_______DEMO dice_______")
        d1 = dice()
        print(d1.value)
        print(d1)
        
        d1.roll(5)
        print(d1)

        d2 = dice()

        if(d1 > d2):
            print("first playr win")

        if(d1 < d2):
            print("second playr win")
        
        d2.roll(4)
        print(d2)

        if(d1 > d2):
            print("first playr win")

        if(d1 < d2):
            print("second playr win")

        

if __name__ == "__main__":
    _demo_()
    
