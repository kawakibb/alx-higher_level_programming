#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_1 = matrix.copy()

    for i in range(len(matrix)):
        matrix_1[i] = list(map(lambda x: x**2, matrix[i]))

    return (matrix_1)
