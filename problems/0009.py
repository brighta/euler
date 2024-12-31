import sys
from math import pow

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

for c in range(1, input_value - 1):
    for b in range(1, input_value - c):
        a = input_value - c - b
        if a < b < c:
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                print(a * b * c)
                exit()
