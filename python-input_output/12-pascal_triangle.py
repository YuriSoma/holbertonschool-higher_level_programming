#!/usr/bin/python3
""" Pascal triangle function"""


def pascal_triangle(n=1):
    """ The function will receive n,
        then prints pascal triangle based on n.

        Args:
        n - the triangle depth (Default 1)

        Return:
        Nothing.
    """
    pascal = []
    for i in range(1, n+1):
        pascal.append([0]*i)
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(0, i//2):
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
            pascal[i][i-j-1] = pascal[i-1][j] + pascal[i-1][j+1]

    return pascal
