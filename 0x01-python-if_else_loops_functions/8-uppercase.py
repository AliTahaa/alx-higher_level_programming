#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')):
            z = ord(i) - 32
            y = y + "{:c}".format(z)
            print(y)
        else:
            print(i)
