#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_count = len(my_list)
    if idx < 0:
        return(my_list)
    elif idx > list_count:
        return(my_list)
    else:
        new = my_list.copy()
        new[idx] = element
        return(new)
