#!/usr/bin/python3

for k in range(0, 9):
    for a in range(k + 1, 10):
        if k == 8 and a == 9:
            print("{:d}{:d}".format(k, a))
        else:
            print("{:d}{:d}".format(k, a), end=", ")
