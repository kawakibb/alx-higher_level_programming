#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_k = list(a_dictionary.keys())

    for val_d in list_k:
        if value == a_dictionary.get(val_d):
            del a_dictionary[val_d]

    return (a_dictionary)
