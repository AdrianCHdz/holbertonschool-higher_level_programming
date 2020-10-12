#!/usr/bin/python3
def mul(tup):
    return (tup[0] * tup[1])


def weight_average(my_list=[]):
    result = 0
    if my_list:
        result = sum([mul(x) for x in my_list]) / sum(x[1] for x in my_list)
    return result
