import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % divisor == 0:
            return False
    return True

primes = [2, 3]
longest_list = 2
list_of_primes = [2, 3]
while sum(primes[-longest_list:]) < input_value:
    next_prime_candidate = primes[-1] + 2
    while not is_prime(next_prime_candidate):
        next_prime_candidate += 2
    primes.append(next_prime_candidate)
    for i in range(len(primes), longest_list, -1):
        sum_primes = sum(primes[-i:])
        if sum_primes < input_value and is_prime(sum_primes):
            longest_list = i
            list_of_primes = primes[-i:]
            break
print(sum(list_of_primes))