#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for keys, value in new.items():
        new[keys] = value * 2
    return(new)
