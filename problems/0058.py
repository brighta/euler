from math import floor, sqrt

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % divisor == 0:
            return False
    return True

primes = 0
non_primes = 1
n = 3
while True:
    non_primes += 1
    for i in range(1, 4):
        new_number = n * n - (i * (n - 1))
        if is_prime(new_number):
            primes += 1
        else:
            non_primes += 1
    if primes / (primes + non_primes) < 0.1:
        print(n)
        exit()
    n += 2