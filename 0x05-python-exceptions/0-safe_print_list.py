#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            a += 1
        except IndexError:
            break
    print()
    return(a)
'''
        print(*([my_list[n] for n in range(x)]), sep="")
'''
