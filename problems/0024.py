import sys
from itertools import permutations

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("".join(map(str, list(permutations(digits))[input_value - 1])))