#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i != j and j > i:
            print("{}{}, ".format(i, j), end='')
print("89")
