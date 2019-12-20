#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for lst in my_list:
        (n_list.append(replace)
        ) if lst == search else n_list.append(lst)
    return(n_list)
