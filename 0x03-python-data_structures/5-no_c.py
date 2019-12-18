#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for n in range(len(my_string)):
        if my_string[n] is 'c' or my_string[n] is 'C':
            continue
        new += my_string[n]
    return(new)
