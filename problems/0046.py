from math import floor, sqrt

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 2, -1):
        if number_to_check % divisor == 0:
            return False
    return True

def meets_goldbach_other_conjecture(number_to_check, primes_to_check):
    for prime in primes_to_check:
        n = 1
        while prime + 2 * pow(n, 2) <= number_to_check:
            if prime + 2 * pow(n, 2) == number_to_check:
                return True
            n += 1
    return False

i = 9
primes = [3, 5, 7]
while True:
    while i > primes[-1]:
        next_prime_candidate = primes[-1] + 1
        while not is_prime(next_prime_candidate):
            next_prime_candidate += 1
        primes.append(next_prime_candidate)
    if not meets_goldbach_other_conjecture(i, primes[:-1]):
        print(i)
        exit()
    i += 2
    while is_prime(i):
        i += 2