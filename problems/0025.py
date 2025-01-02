import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

previous_value = 1
current_value = 1
index = 2
while len(str(current_value)) < input_value:
    index += 1
    next_value = current_value + previous_value
    previous_value = current_value
    current_value = next_value

print(index)