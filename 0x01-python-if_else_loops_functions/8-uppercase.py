#!/usr/bin/python3
def uppercase(str):
    for n in str:
        up = ord(n)
        if 97 <= up <= 122:
            up -= 32
        print("{}".format(chr(up)), end='')
    print()
