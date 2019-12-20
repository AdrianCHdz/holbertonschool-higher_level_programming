#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s_matrix = []
    for num in matrix:
        s_matrix.append(list(map(lambda x : x ** 2, num)))
    return (s_matrix)
