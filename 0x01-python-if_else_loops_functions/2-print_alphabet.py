#!/usr/bin/python3

a = 122
while a >= 97:
    x = 0
    if a % 2 != 0:
        a = a - 32
        x = 1
    print("{:s}".format(chr(a)), end="")
    if x == 1:
        a = a + 32
    a = a - 1
