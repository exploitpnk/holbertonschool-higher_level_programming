#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if (ord(character) >= 97 and ord(character) < 123):
            updated_char = ord(character) - 32
            print(chr(updated_char), end="")
        else:
            print(character, end="")
    print()
