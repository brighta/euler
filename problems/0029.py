import sys
from math import pow

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

numbers = set()
for a in range(2, input_value + 1):
    for b in range(2, input_value + 1):
        numbers.add(pow(a, b))

print(len(numbers))