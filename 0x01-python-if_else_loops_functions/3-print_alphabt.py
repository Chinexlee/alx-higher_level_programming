#!/usr/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if i not in "qe":
        print("{}".format(i), end="")
