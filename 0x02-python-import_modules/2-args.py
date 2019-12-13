#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    b = "arguments.:"

    print("{} {}".format(a - 1, (b[:8] + b[-1:]) if (a - 1) == 1 else
                         (b[:10] if (a - 1) == 0 else (b[0:9] + b[-1:]))))
    for c in range(1, a):
        print("{}: {}".format(c, argv[c]))
