import sys

from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_prime(number_to_check):
    for j in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % j == 0:
            return False
    return True

count = 0
number = 1
while count < input_value:
    number += 1
    if is_prime(number):
        count += 1

print(number)