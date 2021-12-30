import operator as op
import os
import sys
import time
import re

if sys.platform == 'linux':
    def clear_screen():
        print('\033[H\033[2J', end='')
else:
    def clear_screen():
        os.system('cls')

clear_screen()

operator_map = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv
}


def Calculator(to_calc, num_list, mode):
    """
    Function for calculating the specified string.

    Arguments:
    - The string to be calculated
    - List of numbers that make up the string
    - The cycle to be used. 1 - for, 2 - while
    """
    list_idx = 1
    calc_result = int(num_list[0])

    start_time = time.time()
    if mode == 1:
        for cnt in range(len(to_calc)):
            for op, func in operator_map.items():
                if to_calc.find(op, cnt, cnt + 1) != -1:
                    calc_result = func(
                        calc_result, int(num_list[list_idx]))
                    list_idx += 1
    if mode == 2:
        cnt = 0
        while cnt < len(to_calc):
            for op, func in operator_map.items():
                if to_calc.find(op, cnt, cnt + 1) != -1:
                    calc_result = func(
                        calc_result, int(num_list[list_idx]))
                    list_idx += 1
            cnt += 1

    if mode == 1:
        print(" Время выполнения for %0.5f миллисекунд" % (
            (time.time() - start_time) * 1000))
    elif mode == 2:
        print(" Время выполнения while %0.5f миллисекунд" % (
            (time.time() - start_time) * 1000))

    return calc_result


def data_input():
    """
    The function accepts data for further processing in the program
    - You can set arguments from the command line
    - Can be set directly during program execution
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Что там посчитать?:")


in_str = data_input()

os.system('clear')
print("Результат:", Calculator(in_str, re.split(
    '\+|\-|\*|\/', in_str), 1))  # Передача аргументов как позиционных
print("Результат:", Calculator(in_str, re.split(
    '\+|\-|\*|\/', in_str), 2))  # Передача аргументов как позиционных

# Как ключевых
# print("Результат:", Calculator(num_list=re.split(
#   '\+|\-|\*|\/', in_str), to_calc=in_str, mode=1))
