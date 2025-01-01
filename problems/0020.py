import sys
from math import factorial

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

input_factorial = factorial(input_value)
input_factorial_string = str(input_factorial)
print(sum(map(int, list(input_factorial_string))))