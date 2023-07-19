#!/usr/bin/python3
def number_keys(a_dictionary):
    nbr = 0
    list_k = list(a_dictionary.keys())

    for a in list_k:
        nbr += 1

    return (nbr)
