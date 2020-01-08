#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            a += 0
        except (ValueError, TypeError):
            continue
    print()
    return a
'''
        print(*([my_list[n] for n in range(x)]), sep="")
'''
