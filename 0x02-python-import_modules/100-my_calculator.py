#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    dic = {"+":add, "-":sub, "*":mul, "/":div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    for n in dic:
        if argv[2] in dic:
            if n == argv[2]:
                dic = dic[n]
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
    print("{}".format(dic(int(argv[1]), int(argv[3]))))
