import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_multiple(test_number, range_max):
    for divisor in range(1, range_max + 1):
        if test_number % divisor != 0:
            return False
    return True

number = 0
while True:
    number += input_value
    if is_multiple(number, input_value):
        print(number)
        exit()
