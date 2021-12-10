print('Limit area: ', end='')
l=int(input())
a=float(input("Enter the area of the object1: "))
b=float(input("Enter the area of the object2 (not less 2): "))
c=float(input("Enter the area of the object3 (not less 3): "))
while True:
    s = a + b + c
    if s <= l:
        if b < 2:
            print('Object2 area less than 2')
            break
        elif c < 3:
            print('Object3 area less than 3')
            break
        else:
            print('The area will be enough.')
            break
    else:
        print('The area of ​​the objects exceeds the allowable area!')
        break
