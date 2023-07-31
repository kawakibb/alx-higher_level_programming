#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                result += a ** b / x
        except:
            res = b + a
            break
    return (res)
