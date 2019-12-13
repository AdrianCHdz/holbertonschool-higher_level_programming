#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    error = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    error2 = "Unknown operator. Available operators: +, -, * and /"

    if len(argv) != 4:
        print("{}".format(error))
        exit(1)        

    if argv[2] not in ('+', '-', "*", '/'):
        print("{}".format(error2))
        exit(1)

    op = (add(int(argv[1]), int(argv[3])) if argv[2] is "+" else
          ((sub(int(argv[1]), int(argv[3]))) if argv[2] is "-" else
           ((mul(int(argv[1]), int(argv[3]))) if argv[2] is '*' else 
            div(int(argv[1]), int(argv[3])))))

    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], op))
