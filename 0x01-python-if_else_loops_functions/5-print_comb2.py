#!/usr/bin/python3
for numbers in range(100):
    if (numbers == 99):
        print(f'{numbers:02}')
    else:
        print((f'{numbers:02}, '), end="")
