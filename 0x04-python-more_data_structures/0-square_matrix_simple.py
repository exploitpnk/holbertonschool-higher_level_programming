#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for j in i:
            tmp = j**2
            new_matrix.append(tmp)
    return(new_matrix)
