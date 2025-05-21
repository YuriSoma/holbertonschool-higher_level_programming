#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

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
