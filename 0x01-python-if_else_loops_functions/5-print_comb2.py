#!/usr/bin/python3
for n in range(100):
    print("{:02}".format(n), end='\n' if n == 99 else ', ')
