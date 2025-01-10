import sys
from math import factorial

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def generate_combinatorics(n_to_check, r_to_check):
    return int(factorial(n_to_check) / (factorial(r_to_check) * factorial(n_to_check - r_to_check)))

count = 0
for n in range(1, input_value + 1):
    for r in range(1, n + 1):
        if generate_combinatorics(n, r) > 1000000:
            count += 1
print(count)