#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of {0:d} is {1:d} and is {2:s}"
if ((number % 10) > 5):
    print(a.format(number, number % 10, "greater than 5"))
elif ((number % 10) == 0):
    print(a.format(number, number % 10, "and is 0"))
elif ((number % 10) < 6 and (number % 10) != 0):
    print(a.format(number, number % 10, "less than 6 and not 0"))
