#!/usr/bin/python3
from sys import argv
sum = 0
if len(argv) == 1:
    print("{:d}".format(0))
else:
    for n in range(1, len(argv)):
        sum += int(argv[n])
    print("{}".format(sum))
