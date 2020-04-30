#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sys.argv.pop(0)
    total = hex(0x00)
    for number in sys.argv:
        total += int(number)
    print("{}".format(total))
