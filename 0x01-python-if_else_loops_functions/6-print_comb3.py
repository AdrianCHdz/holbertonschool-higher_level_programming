#!/usr/bin/python3
for n in range(100):
    a = n % 10
    b = n / 10
    if b >= a:
        continue
    print("{:02}".format(n), end = '\n' if n == 89 else ', ') 
