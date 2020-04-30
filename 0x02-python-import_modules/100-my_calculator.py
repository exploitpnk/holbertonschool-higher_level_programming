#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv.pop(0)
    argvlength = len(argv)

    if (argvlength == 3):
        a = int(argv[0])
        b = int(argv[2])

        if (argv[1] == "+"):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif (argv[1] == "-"):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif (argv[1] == "*"):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif (argv[1] == "/"):
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
