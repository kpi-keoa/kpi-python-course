#!/usr/bin/evn python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('action', type=str)
parser.add_argument('-n', '--name', type=str, default='first')
parser.add_argument('-c', '--count', type=int, default=5)


args = parser.parse_args()

student = {'first': 1,
           'second': 2,
           'third': 3
           }


def find(name):
    """function for finding a number by name
    Args:
        name (str): student name
    Returns:
        print number the student and new list
    """
    print(student[name],'- with 100')


def set(name, count):
    """function to set any number by name
    Args:
        name (str): student name
        count (int): student number
    Returns:
        print action and new list
    """
    count = int(count)
    print(student[name], '=>', count)
    student[name] = count


def add(name, count):
    """function to adds any number to number by name
    Args:
        name (str): student name
        count (int): student number
    Returns:
        print action and new list
    """
    count = int(count)
    print(student[name], '+', count,'=', student[name]+count)
    student[name] += count


if args.action == 'find':
    find(args.name)
elif args.action == 'set':
    set(args.name, args.count)
elif args.action == 'add':
    add(args.name, args.count)
elif args.action != 'print':
    print('Not corect action')

print('list:', student)
