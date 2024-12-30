import sys
from math import floor

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

max_value = int('9' * input_value)

def is_palindromic_number(number):
    number_string = str(number)
    for k in range(int(floor(len(number_string)) / 2)):
        if number_string[k] != number_string[k * -1 - 1]:
            return False
    return True

max_palindromic_number = 0
for i in range(max_value + 1):
    for j in range(max_value + 1):
        product = i * j
        if is_palindromic_number(product) and max_palindromic_number < product:
            max_palindromic_number = product

print(max_palindromic_number)