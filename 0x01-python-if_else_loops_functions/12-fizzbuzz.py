#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 and i % 5:
            print("FizzBuzz ")
        elif i % 3:
            print("Fizz ")
        elif i % 5:
            print("Buzz ")
        else:
            print(i, end=' ')