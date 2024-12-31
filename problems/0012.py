import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def num_divisors(number_to_check):
    number_of_divisors = 0
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            number_of_divisors += 2
    return number_of_divisors

number = 0
index = 0
while True:
    index += 1
    number += index
    if num_divisors(number) > input_value:
        print(number)
        exit()