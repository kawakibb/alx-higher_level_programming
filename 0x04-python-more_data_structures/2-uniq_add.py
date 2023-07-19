#!/usr/bin/python3

def uniq_add(my_list=[]):
    list = set(my_list)
    nbr = 0
    for i in list:
        nbr += i
    return (nbr)
