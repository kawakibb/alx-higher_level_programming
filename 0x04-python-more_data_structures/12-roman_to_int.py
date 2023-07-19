#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs_ter = [roman_dict[x] for x in roman_string]
    output = 0
    for a in range(len(decs_ter)):
        out_put += decs_ter[a]
        if decs_ter[a - 1] < decs_ter[a] and a != 0:
            out_put -= (decs_ter[a - 1] + decs_ter[a - 1])
    return out_put
