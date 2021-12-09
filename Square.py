print("1-Площадь прямоугольника, 2-Площадь квадрата")
figure = input("Выберите фигуру: ")
 
if figure == '1':
    print("Длины сторон прямоугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Площадь: %.2f" % (a * b))
elif figure == '2':
    print("Сторона квадрата:")
    a = float(input("a = "))
    s = a * a
    print("Площадь: %.2f" % s)
else:
    print("Ошибка")
