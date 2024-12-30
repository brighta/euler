import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input = int(sys.argv[1])

count = 0
previous_value = 1
current_value = 1
while current_value + previous_value < input:
    next_value = current_value + previous_value
    previous_value = current_value
    current_value = next_value
    if next_value % 2 == 0:
        count += next_value

print(count)