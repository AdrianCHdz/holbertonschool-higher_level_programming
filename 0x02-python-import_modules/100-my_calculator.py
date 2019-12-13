#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    op = {"+":add, "-":sub, "*":mul, "/":div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] in op:
        for n in op:
            if argv[2] == n:
                op = op[n]
                break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(argv[1], n, argv[3],
                                 op(int(argv[1]), int(argv[3]))))
