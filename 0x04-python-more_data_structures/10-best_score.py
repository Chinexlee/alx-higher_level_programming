#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return(None)
    for keys, value in a_dictionary.items():
            maxi = max(a_dictionary.values())
            if value == maxi:
                return(keys)
