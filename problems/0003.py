import sys

from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_prime(number):
    for j in range(floor(sqrt(number)), 2, -1):
        if number % j == 0:
            return False
    return True

for i in range(floor(sqrt(input_value)), 1, -1):
    if input_value % i == 0 and is_prime(i):
        print(i)
        exit()
