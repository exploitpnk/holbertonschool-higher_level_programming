#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open('my_file_0.txt', encoding='uft-8') as f:
        print(f.read())
