#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        tmp_matrix = []
        for n in i:
            tmp_matrix.append(n ** 2)
        new_matrix.append(tmp_matrix)
    return new_matrix
