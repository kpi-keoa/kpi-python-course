#!/usr/bin/env python3
from statistics import median
from sys import argv
from sys import stderr


def avgg(agrs):
    """
    average the list
    Args:
        args(list): input sequence
    Returns:
        float: sequence mean 
        
    """
    return sum([float(i) for i in agrs]) / len(agrs)


def medd(agrs): 
    """
    median the list
    Args:
        agrs(list): input sequence
    Returns:
        float: median sequence 
        
    """
    return median([float(i) for i in agrs])


i_d = []


if(len(argv) < 3):
    for iii in range(100):
        sw = input()
        if(sw == 'avg'):
            print(f'average: {avgg(i_d)}')
            break
        elif(sw == 'med'):
            print(f'median: {medd(i_d)}')
            break
        else:
            i_d.append(float(sw))
else:
    try:
        if(argv[1] == 'avg'):
            print(f'average: {avgg(argv[2:])}')
        elif(argv[1] == 'med'):
            print(f'median: {medd(argv[2:])}')
        else:
            i_d.append(float(sw))
    except Exception as e:
        print(f'Detected critical error: {e} \n argv: {argv}', file=stderr)
