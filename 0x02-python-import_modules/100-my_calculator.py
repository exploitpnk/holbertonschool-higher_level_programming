#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == '__main__':
    sys.argv.pop(0)
    argvlength = len(sys.argv)

    if argvlength == 3:
        a = int(sys.argv[0])
        b = int(sys.argv[2])
        if (sys.argv[1] == "+"):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif (sys.argv[1] == "-"):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif (sys.argv[1] == "*"):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif (sys.argv[1] == "/"):
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
