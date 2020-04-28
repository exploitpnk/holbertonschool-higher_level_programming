#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
elif number < 0:
    lastdigit = (number * -1) % 10 * (-1)

if lastdigit > 5:
    str = "and is greater than 5"
    print("Last digit of {:d} is {:d} {}".format(number, lastdigit, str))
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdigit))
elif lastdigit < 6:
    str = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} {}".format(number, lastdigit, str))
