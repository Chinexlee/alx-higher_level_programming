#!/usr/bin/python3
def max_integer(my_list=[]):
    new = 0
    length = len(my_list)
    if length == 0:
        return(None)
    else:
        for i in my_list:
            if i > new:
               new = i
    return(new)
