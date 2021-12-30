#!/usr/bin/env python3

from sys import argv, stderr

"""
This program performs operations with matrices. Available operations: adding matrices, multiplying matrices and writing to the main diagonal 1. The matrix is ​​filled with random numbers. The size of the matrix is ​​set from the console.
"""


funk = argv[1]
def sum_matrix(rov, collum):
    """ This function performs the assembly of matrices.

    Arguments:
        rov - the number of rows matrix is selected
        collum - the number of collumns matrix is selected

    Return:
        nome
    """

    X = []
    Y = []
    result = []

    read_matr(X, rov, collum)
    read_matr(Y, rov, collum)
    for i in range(len(X)):
        result.append([])
        for j in range(len(Y[0])):
            result[i].append(X[i][j] + Y[i][j])
    print(X, '\n', Y, '\n', result)


def read_matr(A, rov, collum):
    """ This function fills the matrix with random numbers.

    Arguments:
        A - matrix
        rov - the number of rows matrix is selected
        collum - the number of collumns matrix is selected

    Return:
        nome
    """

    import random
    for i in range(rov):
        A.append([])
        for j in range(collum):
            A[i] += [random.randint(1, 9)]


def multiplay(rov, collum, rov_1, collum_1):
    """ This function performs the multiplication of matrices.

    Arguments:
        rov - the number of rows of the first matrix is ​​selected
        collum - the number of collumns of the first matrix is ​​selected
        rov_1 - the number of rows of the second matrix is ​​selected
        collum_1 - the number of collumns of the second matrix is selected

    Return:
        nome
    """

    X = []
    Y = []
    result = []
    read_matr(X, rov, collum)
    read_matr(Y, rov_1, collum_1)
    for i in range(len(X)):
        result.append([])
        for j in range(len(Y[0])):
            result[i].append(int(0))
    for i in range(len(X)):

        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    print(X, '\n', Y, '\n', result)


def one_matrix(rov, collum):
    """ This function writes 1 to the main diagonal.

    Arguments:
        rov - the number of rows is selected
        collum - the number of collumns is selected

    Return:
        nome
    """
    X = []
    read_matr(X, rov, collum)
    for i in range(len(X)):
        for j in range(len(X[0])):
            if i == j:
                X[i][j] = 1
    print(X,)


if funk in('sum'):
    sum_matrix(int(argv[2]), int(argv[3]))
elif funk in ('one'):
    one_matrix(int(argv[2]), int(argv[3]))
elif funk in('mult'):
    multiplay(int(argv[2]), int(argv[3]), int(argv[3]), int(argv[3]))


"""
python3 -m timeit 'for i in range(10): print(i)'
5000 loops, best of 5: 39.3 usec per loop
python3 -m timeit 'i=0' 'while i < 10: print(i); i+=1'
5000 loops, best of 5: 39.5 usec per loop
"""
