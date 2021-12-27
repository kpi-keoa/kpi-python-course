import math
tip = input("Введіть назву фігури = ")

if tip == "Трикутник":
    a = float(input("Розмір сторони   a = "))
    b = float(input("Розмір сторони b = "))
    c = float(input("Розмір сторони c = "))
    p = (a + b + c) / 2
    s = math.sqrt((p * (p - a) * (p - b) * (p - c)))

elif tip == "прямокутник":
    a = float(input("Розмір сторони a = "))
    b = float(input("Розмір сторони b = "))
    s = a * b
elif tip == "круг":
    r = float(input("Радіус круга r = "))
    s = math.pi * (r ** 2)

print(s)
