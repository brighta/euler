import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

count = 0
for i in range(1, input_value + 1):
    count += pow(i, i)
print(str(count)[-10:])

print(input_value)