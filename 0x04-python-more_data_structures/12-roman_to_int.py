#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string and isinstance(roman_string, str):
        for n in range(len(roman_string)):
            result += roman[roman_string[n]]
            if n - 1 >= 0 and roman[roman_string[n]]\
               > roman[roman_string[n - 1]]:
                result -= roman[roman_string[n - 1]] * 2
    return result
