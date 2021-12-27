#!/usr/bin/env python
import os

print("This program is a simple calculator. Use next commands to:")
print(" 1 - addition\n 2 - subtraction\n 3 - multiplication\n 4 - division")

x = 0
y = 0
function = 0

def input_(msg):
    """User input function and control"""
    global function
    z = input(msg)
    if not z.isdecimal():
        if not z.lstrip('-').isdigit(): return input_("You didn't write the number. Please try again: ")
    function = int(z)
    if 1 <= int(z) <= 4: return function
    return input_("You use undefined command. Please enter another command: ")
print(input_("Print command's number what you need: "))

os.system('clear')

def input_(msg):
    """User input the first argument and control"""
    global x
    z = input(msg)
    x = int(z)
    if not z.isdecimal():
        if not z.lstrip('-').isdigit(): return input_("You didn't write the number. Please try again: ")
    else: return x
print(input_("Print the first number what you need: "))

os.system('clear')

def input_(msg):
    """User input the second argument and control"""
    global y
    z = input(msg)
    y = int(z)
    if not z.isnumeric():
        if not z.lstrip('-').isdigit(): return input_("You didn't write the number. Please try again: ")
    else: return y
print(input_("Print the second number what you need: "))

os.system('clear')

if function == 1: print("Sum " + str(x) + " and " + str(y) + " is " + str(x+y))
elif function == 2: print("Subtraction " + str(x) + " and " + str(y) + " is " + str(x-y))
elif function == 3: print("Multiply " + str(x) + " and " + str(y) + " is " + str(x*y))
elif function == 4: print("Division " + str(x) + " and " + str(y) + " is " + str(x/y))
