# /usr/local/bin/python3 /Users/NazarDiadiun/Desktop/Calculator.py "24 + 46"

import sys
import time
import re

def Calculator(ToCalculate, NumbersList, Mode):
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
    if Mode == 2:
        print(" Время выполнения while %0.5f миллисекунд" % ((time.time() - start_time) * 1000))

    return CalculationResult

while True:

    # Если переданы аргументы через командную строку
    if len(sys.argv) > 1:
    # В строку, для дальнейших операций, заносим первый аргумент
        InputString = sys.argv[1]
    # Если аргументов не передали
    else:
    # Запрашиваем у пользователя
        InputString = input("Что там посчитать?:");

    
    # Передача аргументов как позиционных
    print("Результат:", Calculator(InputString, re.split('\+|\-|\*|\/', InputString), 1))
    print("Результат:", Calculator(InputString, re.split('\+|\-|\*|\/', InputString), 2))

    # Как ключевых
    # print("Результат:", Calculator(NumbersList=re.split('\+|\-|\*|\/', InputString), ToCalculate=InputString, Mode=1))


    break
