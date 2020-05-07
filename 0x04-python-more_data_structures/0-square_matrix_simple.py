#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for j in i:
            new_matrix.append(j**2)
    return(new_matrix)
