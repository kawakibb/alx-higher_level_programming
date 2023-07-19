#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nv_list = []
    for element in my_list:
        if element == search:
            nv_list.append(replace)
        else:
            nv_list.append(element)
    return nv_list
