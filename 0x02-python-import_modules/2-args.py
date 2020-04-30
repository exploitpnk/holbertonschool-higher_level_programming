#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    argvlength = len(sys.argv)

    if (argvlength == 0):
        print("0 arguments.")
    elif (argvlength == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(argvlength))
        number = 1
        for argument in sys.argv:
                print("{:d}: {}".format(number, argument))
                number += 1
