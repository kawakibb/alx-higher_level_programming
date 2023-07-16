#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for c in a:
            print("{:d}".format(c), end=" " if c != a[-1] else "")
        print()
