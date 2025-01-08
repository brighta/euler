from math import prod

digits = "."
number = 1
while len(digits) < 1000001:
    digits += str(number)
    number += 1
wanted_digits = list(map(int, [digits[1], digits[10], digits[100], digits[1000], digits[10000], digits[100000], digits[1000000]]))
print(prod(wanted_digits))