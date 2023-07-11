#!/usr/bin/python3

def uppercase(str):
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            x = chr(ord(k)-32)
        print('{}'.format(k), end='')
    print("")
