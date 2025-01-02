import sys
from math import pow

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def power_of_digit(digit_string):
    return pow(int(digit_string), input_value)

sum_of_powers = 0
for i in range(2, 1000000):
    if i == sum(map(power_of_digit, list(str(i)))):
        sum_of_powers += i

print(sum_of_powers)