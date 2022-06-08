#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append(i.copy())
    for row in range(len(new)):
        for j in range(len(new[row])):
            new[row][j] = new[row][j] ** 2
    return (new)
