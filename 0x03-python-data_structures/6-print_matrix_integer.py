#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = 1
        for j in i:
            if l == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            l = l + 1
        print()
