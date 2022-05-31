#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of {0:d} is {1:d} and is {2:s}"
if (number >= 0):
    modulus = number % 10
elif (number < 0):
    modulus = -((-number) % 10)
if (modulus > 5):
    print(a.format(number, modulus, "greater than 5"))
elif (modulus == 0):
    print(a.format(number, modulus, "0"))
elif (modulus < 6 and (number % 10) != 0):
    print(a.format(number, modulus, "less than 6 and not 0"))
