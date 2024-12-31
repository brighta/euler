import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

range_to_input_value = range(1, input_value + 1)
sum_of_squares = 0
for i in range_to_input_value:
    sum_of_squares += pow(i, 2)

square_of_sums = pow(sum(list(range_to_input_value)), 2)

print(square_of_sums - sum_of_squares)