from queue import PriorityQueue

func = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list.

A = 1
B = 0


func.put((1, A*B))
func.put((2, A))

while func:
    if A*B == 1:
        print(func.get(), "ONE")
    if A == 1:
        print(func.get(), "TWO")
    if ((A != 1)&(B != 1)):
        print("FAIL")
