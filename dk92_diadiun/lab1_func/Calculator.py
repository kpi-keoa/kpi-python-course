# /usr/local/bin/python3 /Users/NazarDiadiun/Desktop/Calculator.py "24 + 46"

import os
import sys
import time
import re

os.system('clear')

def Calculator(ToCalculate, NumbersList, Mode):
    """ Функция для просчёта указанной строки.

    Принимает на вход три аргумента:
        - Строку, которая должна быть просчитана
        - Список чисел, из которых состоит строка
        - Цикл, который будет использован. 1 - for, 2 - while
    
    Возвращает результат счёта.
    """
    ListIndex = 1
    CalculationResult = int(NumbersList[0])

    start_time = time.time()
    if Mode == 1:
        for Counter in range(len(ToCalculate)):
            if ToCalculate.find('+', Counter, Counter + 1) != -1:
                CalculationResult += int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('-', Counter, Counter + 1) != -1:
                CalculationResult -= int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('*', Counter, Counter + 1) != -1:
                CalculationResult *= int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('/', Counter, Counter + 1) != -1:
                CalculationResult /= int(NumbersList[ListIndex])
                ListIndex += 1
    if Mode == 2:
        Counter = 0
        while Counter < len(ToCalculate):
            if ToCalculate.find('+', Counter, Counter + 1) != -1:
                CalculationResult += int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('-', Counter, Counter + 1) != -1:
                CalculationResult -= int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('*', Counter, Counter + 1) != -1:
                CalculationResult *= int(NumbersList[ListIndex])
                ListIndex += 1
            if ToCalculate.find('/', Counter, Counter + 1) != -1:
                CalculationResult /= int(NumbersList[ListIndex])
                ListIndex += 1
            Counter += 1


    if Mode == 1:
        print(" Время выполнения for %0.5f миллисекунд" % ((time.time() - start_time) * 1000))
    elif Mode == 2:
        print(" Время выполнения while %0.5f миллисекунд" % ((time.time() - start_time) * 1000))

    return CalculationResult


def data_input():
    """Функция принимает данные для дальнейшей обработки в програме
        - Можно получить аргументы из командной строки
        - Можно задать непосредственно во время выполнения программы
    """
    # Если переданы аргументы через командную строку
    if len(sys.argv) > 1:
    # В строку, для дальнейших операций, заносим первый аргумент
        return sys.argv[1]
    # Если аргументов не передали
    else:
    # Запрашиваем у пользователя
        return input("Что там посчитать?:")


InputString = data_input()

os.system('clear')
    
    # Передача аргументов как позиционных
print("Результат:", Calculator(InputString, re.split('\+|\-|\*|\/', InputString), 1))
print("Результат:", Calculator(InputString, re.split('\+|\-|\*|\/', InputString), 2))

    # Как ключевых
    # print("Результат:", Calculator(NumbersList=re.split('\+|\-|\*|\/', InputString), ToCalculate=InputString, Mode=1))

