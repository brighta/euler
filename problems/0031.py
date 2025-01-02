import sys
from math import floor

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def make_value(coins_remaining, value):
    if value == 0 or len(coins_remaining) == 1:
        return 1
    count = 0
    for i in range(floor(value / coins_remaining[0]) + 1):
        count += make_value(coins_remaining[1:], value - i * coins_remaining[0])
    return count

print(make_value(coins, input_value))