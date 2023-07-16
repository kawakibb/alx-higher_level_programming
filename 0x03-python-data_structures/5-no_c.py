#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    for a in my_string:
        if a != 'c' and a != 'C':
            n_str += a
    return n_str
