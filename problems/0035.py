import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_prime(number_to_check):
    divisors = set()
    for j in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % j == 0:
            divisors.add(j)
            divisors.add(int(number_to_check / j))
    divisors.remove(number_to_check)
    return len(divisors) == 1

def is_circular_prime(number_to_check):
    number_to_check_string = str(number_to_check)
    for _ in range(len(number_to_check_string)):
        number_to_check_string = number_to_check_string[-1] + number_to_check_string[:-1]
        if not is_prime(int(number_to_check_string)):
            return False
    return True

circular_primes = []
for i in range(2, input_value):
    if is_circular_prime(i):
        circular_primes.append(i)
print(len(circular_primes))