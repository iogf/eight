""" eight queens problem.
    finding a way to put 8 queens on a board without none of them
    threatening each other

by tau.

"""

from itertools import *

def threat(square1, square2):
    if vline(square1, square2):
        return True
    elif hline(square1, square2):
        return True
    elif right_diag(square1, square2):
        return True
    elif left_diag(square1, square2):
        return True
    else:
        return False

def vline(square1, square2):
    x_0, y_0 = square1
    x_1, y_1 = square2

    if x_0 == x_1:
        return True
    else:
        return False

def hline(square1, square2):
    x_0, y_0 = square1
    x_1, y_1 = square2

    if y_0 == y_1:
        return True
    else:
        return False

def right_diag(square1, square2):
    x_0, y_0 = square1
    x_1, y_1 = square2

    b = y_1 - y_0
    a = x_1 - x_0

    if b == a:
        return True
    else:
        return False

def left_diag(square1, square2):
    x_0, y_0 = square1
    x_1, y_1 = square2

    b = y_1 - y_0
    a = x_1 - x_0

    if a == -b:
        return True
    else:
        return False


def pred(board):
    """ this one i used to prove that it was correct cause i didn't
        find a program to put the queens on the table
        i have imagined them, but, i'm obsessed :P
    """

    space = combinations(board, 2)

    for i, j in space:
        if threat(i, j):
            return True
    else:
        return False

"""
def solve():
    board = [ (i, j) for i in range(1, 9) for j in range(1, 9) ]

    space = combinations(board, 8)

    for i in space:
        if not pred(i):
            print i
            break
"""

def solve():
    board = [ (i, j) for i in range(1, 9) for j in range(1, 9) ]
   
    mate(board, 8) 

def mate(board, nqueen):

    if nqueen == 0:
        return True

    if board == []:
        return False
    
    for i in board:
        if mate(options(board, i), nqueen - 1):
            print i
            return True
    
def reach(square):
    space = []

    x_0, y_0 = square

    for i in range(1, 9):
        if i != x_0:
            space.append((i, y_0))
    
    for i in range(1, 9):
        if i != y_0:
            space.append((x_0, i))

    space.extend(b_diag_right(square))
    space.extend(a_diag_right(square))
    space.extend(b_diag_left(square))
    space.extend(a_diag_left(square))
    return space

def b_diag_right(square):
    space = []
    
    x_0, y_0 = square

    while x_0 != 1 and y_0 != 1:
        x_0 -= 1
        y_0 -= 1
        space.append((x_0 , y_0))

    return space


def a_diag_right(square):
    space = []
    
    x_0, y_0 = square

    while x_0 != 8 and y_0 != 8:
        x_0 += 1
        y_0 += 1
        space.append((x_0 , y_0))

    return space


def b_diag_left(square):
    space = []
    
    x_0, y_0 = square

    while x_0 != 8 and y_0 != 1:
        x_0 += 1
        y_0 -= 1
        space.append((x_0 , y_0))

    return space



def a_diag_left(square):
    space = []
    
    x_0, y_0 = square

    while x_0 != 1 and y_0 != 8:
        x_0 -= 1
        y_0 += 1
        space.append((x_0 , y_0))
    return space

def options(board, square):
    m = reach(square)
    tmp = board[:]
    
    for i in m:
        try:
            ind = tmp.index(i)
            del tmp[ind]
        except:
            pass

    ind = tmp.index(square)
    del tmp[ind]

    return tmp

solve()

