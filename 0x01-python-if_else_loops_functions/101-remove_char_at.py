#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for ctr in range(len(str)):
        if ctr == n:
            continue
        new += str[ctr]
    return (new)
