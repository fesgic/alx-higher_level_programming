#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return ([[y**2 for y in x] for x in matrix if len(matrix) != 0])
