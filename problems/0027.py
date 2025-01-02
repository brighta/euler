from math import floor, sqrt

def is_prime(number_to_check):
    if number_to_check < 1:
        return False
    divisors = set()
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.add(i)
            divisors.add(int(number_to_check / i))
    divisors.remove(number_to_check)
    return len(divisors) == 1

product_of_coefficients = 0
count = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        number_of_primes = 0
        n = 0
        while is_prime(n * n + n * a + b):
            number_of_primes += 1
            n += 1
        if number_of_primes > count:
            count = number_of_primes
            product_of_coefficients = a * b

print(product_of_coefficients)