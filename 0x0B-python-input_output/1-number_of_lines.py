#!/usr/bin/python3
""" returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open('my_file_0.txt', encoding='utf-8') as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
