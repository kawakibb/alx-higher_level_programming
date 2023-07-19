#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nv_dict = {}
    for k, val in a_dictionary.items():
        nv_dict.update({k: (val * 2)})
    return nv_dict
