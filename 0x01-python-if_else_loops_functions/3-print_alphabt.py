#!/usr/bin/python3

for k in range(ord('a'), ord('z') + 1):
    if chr(k) == 'e' or chr(k) == 'q':
        continue
    else:
        print("{:s}".format(chr(k)), end="")
