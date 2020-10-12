#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_list = []
    if value in a_dictionary.values():
        for x, y in a_dictionary.items():
            if y == value:
                a_list.append(x)
        for x in a_list:
            del a_dictionary[x]
    return a_dictionary
