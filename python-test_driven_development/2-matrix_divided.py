#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    A function expected 2 inputs, a matrix and a number (int or float),
    and it will divide all elements of the matrix on div (the number).
    The div should be a number (and not 0).

    Matrix must be a list of lists of integers or floats.
    Each row of the matrix must be of the same size.
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    notMatrix = 'matrix must be a matrix (list of lists) of integers/floats'
    lastRowLen = 0
    matrix_result = []
    tmp_list = []

    if isinstance(matrix, list):
        for row in matrix:
            if not isinstance(row, list):
                raise 
                TypeError('matrix must be a matrix (list of lists) of integers/floats')
            elif lastRowLen == 0:
                lastRowLen = len(row)
            elif len(row) is not lastRowLen:
                raise 
                TypeError('Each row of the matrix must have the same size')

            for col in row:
                if not isinstance(col, int) and not isinstance(col, float):
                    raise 
                    TypeError('matrix must be a matrix (list of lists) of integers/floats')
                else:
                    tmp_list.append(round((col / div), 2))
            matrix_result.append(tmp_list[:])
            tmp_list.clear()    
    else:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    return matrix_result
