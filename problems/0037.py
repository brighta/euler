from math import floor, sqrt

def is_prime(number_to_check):
    divisors = set()
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.add(i)
            divisors.add(int(number_to_check / i))
    divisors.remove(number_to_check)
    return len(divisors) == 1

def is_truncatable_prime(number_to_check):
    number_to_check_string = str(number_to_check)
    if not is_prime(number_to_check):
        return False
    for i in range(1, len(number_to_check_string)):
        if not is_prime(int(number_to_check_string[:-i])):
            return False
        if not is_prime(int(number_to_check_string[i:])):
            return False
    return True

number = 12
truncatable_primes = []
while len(truncatable_primes) < 11:
    number += 1
    if is_truncatable_prime(number):
        truncatable_primes.append(number)

print(sum(truncatable_primes))
