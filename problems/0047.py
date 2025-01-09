import sys
from math import floor, sqrt

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

cache = {}

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 2, -1):
        if number_to_check % divisor == 0:
            return False
    return True

def get_distinct_prime_factors(number_to_check, primes_to_check):
    for i in range(len(primes_to_check)):
        distinct_prime_factors = set()
        number_remaining = number_to_check
        for j in range(i, len(primes_to_check)):
            prime = primes_to_check[j]
            while number_remaining % prime == 0:
                distinct_prime_factors.add(prime)
                number_remaining = int(number_remaining / prime)
                if number_remaining in cache:
                    distinct_prime_factors = distinct_prime_factors.union(cache[number_remaining])
                    number_remaining = 1
                if number_remaining == 1:
                    cache[number_to_check] = distinct_prime_factors
                    return len(distinct_prime_factors)
    return 0

candidate = 1
primes = [2, 3]
numbers_with_distinct_prime_factors = []
while candidate < 5000:
    while candidate > primes[-1]:
        next_prime_candidate = primes[-1] + 2
        while not is_prime(next_prime_candidate):
            next_prime_candidate += 2
        primes.append(next_prime_candidate)
    if get_distinct_prime_factors(candidate, primes[:-1]) == input_value:
        if len(numbers_with_distinct_prime_factors) == 0 or numbers_with_distinct_prime_factors[-1] == candidate - 1:
            numbers_with_distinct_prime_factors.append(candidate)
        else:
            numbers_with_distinct_prime_factors = [candidate]
        if len(numbers_with_distinct_prime_factors) == input_value:
            print(numbers_with_distinct_prime_factors[0])
            exit()
    candidate += 1

# ToDo: This code is not fast, and should be investigated to be improved. It's also unclear whether the cache actually brings any benefit.