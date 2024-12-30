import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input = int(sys.argv[1])

count = 0
for i in range(input):
    if i % 3 == 0 or i % 5 == 0:
        count += i

print(count)