#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')):
            z = ord(i) - 32
            print("{:c}".format(z), end='')
    print('')
