#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints it to stdout """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for i in lines:
                print(i, end='')
        else:
            for i in range(0, nb_lines):
                print(lines[i], end='')
