#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    nbr = 0
    de = 0
    for tu in my_list:
        nbr += tu[0] * tu[1]
        de += tu[1]

    return (nbr / de)
