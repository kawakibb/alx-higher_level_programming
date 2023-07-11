#!/usr/bin/python3

def uppercase(str):
    for x in range(len(str)):
        k = ord(str[k])
        if k >= 97 and k <= 122:
            k = k - 32
        print("{}".format(chr(k)), end="")
    print()
