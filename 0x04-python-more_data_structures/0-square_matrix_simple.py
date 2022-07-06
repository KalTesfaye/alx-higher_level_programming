#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        temp_matrix = []
        for y in x:
            temp_matrix.append(y**2)
        new_matrix.append(temp_matrix)
    return new_matrix
