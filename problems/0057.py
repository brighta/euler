import sys

# credit - https://raw.org/puzzle/project-euler/problem-57/

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])
sys.setrecursionlimit(input_value + 100)

count = 0
numerator = denominator = 1
for _ in range(input_value):
    numerator, denominator = 2 * denominator + numerator, denominator + numerator
    if len(str(numerator)) > len(str(denominator)):
        count += 1
print(count)