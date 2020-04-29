#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for character in range(0, len(str)):
        if character != n:
            result = result + str[character]
    return result
