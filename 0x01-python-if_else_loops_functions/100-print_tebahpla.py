#!/usr/bin/python3
for num in range(122, 96, -1):
    n = num if num % 2 == 0 else num - 32
    print("{}".format(chr(n)), end='')
