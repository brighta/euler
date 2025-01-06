from math import factorial

def get_factorial_digit_sum(number_to_check):
    count = 0
    for digit in map(int, list(str(number_to_check))):
        count += factorial(digit)
    return count

count = 0
for i in range(3, 100000):
    if i == get_factorial_digit_sum(i):
        count += i

print(count)