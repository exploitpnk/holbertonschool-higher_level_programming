#!/usr/bin/python3
def uppercase(str):
    for character in str + "\n":
        if (ord(character) >= 97 and ord(character) < 123):
            print("{}".format(chr(ord(character) - 32)), end="")
        else:
            print("{}".format(character), end="")
