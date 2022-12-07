#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence) - 1
    char = sentence[0] if length > 0 else "None"
    new = (length, char)
    return(new)
