#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_l = []
    for n in range(list_length):
        try:
            a = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            a = 0
            print("division by 0")
        except TypeError:
            a = 0
            print("wrong type")
        except IndexError:
            a = 0
            print("out of range")
        finally:
            n_l.append(a)
    return(n_l)
