#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    data = dir(hidden_4)
    for item in data:
        if (data[:2]) != '__':
            print("{}".format(item))
