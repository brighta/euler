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
for i in range(2, input_value):
    if is_prime(i):
        count += i

print(count)