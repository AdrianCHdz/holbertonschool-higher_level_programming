#!/usr/bin/python3
"""
This is the matrix_divided module.
It has the function of modifyinf certain
aspects of bidimensional matrixes.
"""

def matrix_divided(matrix, div):
    """This function recieves a bidimensional matrix
    and a divisior, it returns the matrix with the values
    divided by the given divisor.
    """
    """new_l = [x[:] for x in matrix]"""
    T_error = "matrix must be a matrix (list of lists) of integers/floats"
    O_error = "Each row of the matrix must have the same size"

    if isinstance(matrix, list) is False or not matrix or\
       matrix is None:
        raise TypeError(T_error)

    for row in matrix:
        if isinstance(row, list) is False or not row or\
           all(isinstance(m, (int, float)) for m in row) is False:
            raise TypeError(T_error)

        if len(row) != len(matrix[0]):
            raise TypeError(O_error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False or div is None:
        raise TypeError("div must be a number")
    return ([[round(m / div, 2) for m in n] for n in matrix])
    """
    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            new_l[n][m] = "fuck"
    print(new_l)
    """
