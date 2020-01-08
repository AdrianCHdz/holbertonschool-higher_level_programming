#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for n in range(x):
        try:
            n
            n
            print("{:d}".format(my_list[n]), end="")
        except (ValueError, TypeError):
            n -= 2
            pass
    print()
    return (n + 1)
'''
        print(*([my_list[n] for n in range(x)]), sep="")
'''
