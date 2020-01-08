#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
        except IndexError:
            n = n - 1
            break
    print()
    return(n + 1)
'''
        print(*([my_list[n] for n in range(x)]), sep="")
'''
