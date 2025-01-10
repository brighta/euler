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

def reverse_and_add(number_to_process):
    return number_to_process + int("".join(reversed(list(str(number_to_process)))))

def is_lychrel_number(number_to_check):
    for _ in range(50):
        number_to_check = reverse_and_add(number_to_check)
        if is_palindromic_number(number_to_check):
            return False
    return True

count = 0
for i in range(input_value):
    if is_lychrel_number(i):
        count += 1
print(count)