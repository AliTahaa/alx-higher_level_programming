#!/usr/bin/python3
def uppercase(str):
    y = ''
    for i in str:
        if ord(i) in range(ord('a'), ord('z')+1):
            z = ord(i) - 32
            y = y + "{:c}".format(z)
        else:
            y = y + i
    print(y)
