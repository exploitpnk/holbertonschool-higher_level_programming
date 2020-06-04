#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints it to stdout """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, encoding='utf-8') as f:
        lines = 0
        for line in f:
            lines += 1
        return lines


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, encoding='utf-8') as f:
        total_lines = number_of_lines(f)
        if nb_lines <= 0 or nb_lines >= total_lines:
            print(f.read())
        else:
            printed_lines = 0
            for line in f:
                if printed_lines < nb_lines:
                    print(line, end='')
                    printed_lines = printed_lines + 1
