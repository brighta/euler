import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

numbers_processed = []

def get_proper_divisors(number_to_check):
    divisors = []
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.append(i)
            divisors.append(int(number_to_check / i))
    divisors.remove(number_to_check)
    return divisors

def get_amicable_numbers_for_number(number_to_check):
    if number_to_check in numbers_processed:
        return ()
    divisors = get_proper_divisors(number_to_check)
    divisors_sum = sum(divisors)
    other_divisors = get_proper_divisors(divisors_sum)
    if sum(other_divisors) == number_to_check and number_to_check != divisors_sum:
        numbers_processed.append(divisors_sum)
        return number_to_check, divisors_sum
    return ()

count = 0
for i in range(2, input_value):
    count += sum(get_amicable_numbers_for_number(i))
print(count)
