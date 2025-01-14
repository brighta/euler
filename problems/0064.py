import sys
from decimal import Context

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

context = Context(prec=500)

count = 0
for i in range(1, input_value + 1):
    square_root = context.sqrt(i)
    marker = int(square_root)
    if marker == square_root:
        continue
    reciprocal = context.divide(1, (context.subtract(square_root, marker)))
    continued_fractions = [int(reciprocal)]
    while continued_fractions[-1] != marker * 2:
        reciprocal = context.divide(1, context.subtract(reciprocal, continued_fractions[-1]))
        continued_fractions.append(int(reciprocal))
    if len(continued_fractions) % 2 != 0:
        count += 1
print(count)
