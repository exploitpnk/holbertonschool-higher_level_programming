#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sys.argv.pop(0)
    total = 0
    for number in sys.argv:
        total += int(number)
    print("{}".format(total))
