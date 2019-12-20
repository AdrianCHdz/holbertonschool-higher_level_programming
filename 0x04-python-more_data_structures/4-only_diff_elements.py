#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return ([a for a in set_1 if a not in set_2] +\
            [a for a in set_2 if a not in set_1])
