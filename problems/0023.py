import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def get_proper_divisors(number_to_check):
    divisors = set()
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.add(i)
            divisors.add(int(number_to_check / i))
    divisors.remove(number_to_check)
    return divisors

def is_abundant_number(number_to_check):
    divisors = get_proper_divisors(number_to_check)
    return sum(divisors) > number_to_check

abundant_numbers = []
for i in range(12, input_value + 1):
    if is_abundant_number(i):
        abundant_numbers.append(i)

sum_of_abundant_numbers = set([])
for abundant_number_one in abundant_numbers:
    for abundant_number_two in abundant_numbers:
        ab_sum = abundant_number_one + abundant_number_two
        if ab_sum <= input_value:
            sum_of_abundant_numbers.add(ab_sum)

print(sum([number for number in range(input_value + 1) if number not in sum_of_abundant_numbers]))