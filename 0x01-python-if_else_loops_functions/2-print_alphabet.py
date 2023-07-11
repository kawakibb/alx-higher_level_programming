#!/usr/bin/python3

for a in range(122, 96, -1):
    if a % 2 == 0:
        x = chr(a)
    else:
        x = chr(a-32)
    print("{}".format(x), end="")
