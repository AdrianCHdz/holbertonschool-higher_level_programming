#!/usr/bin/python3
def fizzbuzz():
    str = ["Fizz", "Buzz", "FizzBuzz"]
    for num in range(1, 101):
        str1 = (str[2] if num % 15 == 0 else
                (str[0] if num % 3 == 0 else
                 (str[1] if num % 5 == 0 else num)))
        print("{}".format(str1), end=' ')
