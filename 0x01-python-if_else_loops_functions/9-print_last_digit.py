#!/usr/bin/python3
def print_last_digit(number):
    r=int(repr(number)[-1])
    print("{}".format(r), end="")
    return r
