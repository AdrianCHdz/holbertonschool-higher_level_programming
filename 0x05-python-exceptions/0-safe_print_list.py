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
#    print(*(my_list[n] for n, m in zip(range(x), my_list)))
#    print(*([my_list[n] for n, m in zip(range(x), my_list)]), sep="")
#    return sum(1 for n in zip(range(x), my_list))
#    return sum(map(lambda x: 1, zip(range(x), my_list)))
