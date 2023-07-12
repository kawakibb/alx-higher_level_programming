#!/usr/bin/python3

def print_last_digit(number):
    x = 0
    if number < 0:
        number *= -1
    x = 1
    a = number % 10
    if number == 1:
        number *= -1
    print("{:d}".format(a), end="")
    return a
