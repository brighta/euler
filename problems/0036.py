import sys
from math import floor

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_palindromic_number(number):
    number_string = str(number)
    for k in range(int(floor(len(number_string)) / 2)):
        if number_string[k] != number_string[k * -1 - 1]:
            return False
    return True

def to_binary_number(number):
    return int(bin(number)[2:])

count = 0
for i in range(input_value):
    if is_palindromic_number(i) and is_palindromic_number(to_binary_number(i)):
        count += i

print(count)