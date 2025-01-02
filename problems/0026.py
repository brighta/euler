import sys
from decimal import Decimal, getcontext
from math import floor

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def get_recurring_cycle(number_to_check):
    for precision in [100, 1000, 10000]:
        getcontext().prec = precision
        number_string_without_decimal = str(number_to_check).split('.')[1]
        if len(number_string_without_decimal) < 20:
            return 0
        for i in range(len(number_string_without_decimal)):
            remaining_number = number_string_without_decimal[i:]
            number_half_length = floor(len(remaining_number) / 2)
            for j in range(1, number_half_length):
                if remaining_number[:j]*2 == remaining_number[j:j*3]:
                    return j
    return 0


number = 0
count = 0
for i in range(2, input_value):
    new_count = get_recurring_cycle(1/Decimal(i))
    if new_count > count:
        number = i
        count = new_count

print(number)