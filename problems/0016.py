import sys
from math import pow

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

number = pow(2, input_value)
print(sum(map(int, list(str(int(number))))))
