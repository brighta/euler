import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

maximum_digit_sum = 0
for a in range(1, input_value):
    for b in range(1, input_value):
        number = pow(a, b)
        digits = list(map(int, list(str(number))))
        digit_sum = sum(digits)
        if digit_sum > maximum_digit_sum:
            maximum_digit_sum = digit_sum
print(maximum_digit_sum)