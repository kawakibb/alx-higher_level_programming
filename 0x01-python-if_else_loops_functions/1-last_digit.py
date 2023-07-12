#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    k = -1 * (- number % 10)
else:
    k = number % 10

if k > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, k))
elif k == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, k))
elif k < 6 and k != 0:
    print("Last digit of {:d} is {:d}".format(number, k), end=" ")
    print("and is less than 6 and not 0")
