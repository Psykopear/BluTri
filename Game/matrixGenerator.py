import math
import fpformat

def world_generator(size,sp,ap):
    matrix = [ [ 0 for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = [fpformat.fix(math.sqrt(math.fabs(pow((ap[0] - i),2) + pow((ap[1] - j), 2))),3)]
    matrix[ap[0]][ap[1]] = -2.22
    return matrix

def matrix_generator(size, sp, ap):
    matrix = [ [ 0 for i in range(size)] for j in range(size) ]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = "*"
    matrix[sp[0]][sp[1]] = "S"
    matrix[ap[0]][ap[1]] = "A"
    return matrix


def print_matrix(matrix):
    size = len(matrix[0])
    for j in range(size):
        for i in range(size):
            print "",matrix[i][j],
        print