#!/usr/bin/python3
for ones_digit in range(10):
    for tens_digit in range(ones_digit + 1, 10):
        if ones_digit == 8 and tens_digit == 9:
            print("{}{}".format(ones_digit, tens_digit))
        else:
            print("{}{}".format(ones_digit, tens_digit), end=', ')
