import sys

# credit - https://www.educative.io/answers/convergents-of-e-project-euler--sharp65

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

n = 2
previous_n = 1
continuous_fraction = 1
for k in range(2, input_value + 1):
    temporary_n = previous_n
    if k % 3 == 0:
        continuous_fraction = 2 * int(k / 3)
    else:
        continuous_fraction = 1
    previous_n = n
    n = continuous_fraction * previous_n + temporary_n
print(sum(map(int, list(str(n)))))
