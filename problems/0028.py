import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

count = 1
for i in range(3, input_value + 1, 2):
    count += i * i * 4 - (i - 1) * 6

print(count)