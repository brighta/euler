import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

all_digits = set(range(1, input_value + 1))

def get_proper_divisor_pairs(number_to_check):
    proper_divisor_pairs = []
    for i in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % i == 0:
            proper_divisor_pairs.append([i, int(number_to_check / i)])
    return proper_divisor_pairs

pandigital_products = set()
for number in range(1, pow(10, floor(input_value / 2))):
    divisor_pairs = get_proper_divisor_pairs(number)
    for divisor_pair in divisor_pairs:
        all_digits_in_test = set(list(map(int, list(str(divisor_pair[0])))) + list(map(int, list(str(divisor_pair[1])))) + list(map(int, list(str(number)))))
        all_digits_string = str(divisor_pair[0]) + str(divisor_pair[1]) + str(number)
        if len(all_digits_in_test) == len(all_digits_string) and all_digits_in_test == all_digits:
            pandigital_products.add(number)

print(sum(pandigital_products))