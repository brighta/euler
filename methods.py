from math import floor, sqrt

# from math import floor, sqrt
def get_proper_divisors(number_to_check):
    divisors = set()
    for divisor in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % divisor == 0:
            divisors.add(divisor)
            divisors.add(int(number_to_check / divisor))
    divisors.remove(number_to_check)
    return divisors

# from math import floor, sqrt
def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % divisor == 0:
            return False
    return True

primes = []
def get_next_prime():
    global primes
    next_prime_candidate = primes[-1] + 2
    while not is_prime(next_prime_candidate):
        next_prime_candidate += 2
    primes.append(next_prime_candidate)

# from math import floor
def is_palindromic_number(number):
    number_string = str(number)
    for k in range(int(floor(len(number_string)) / 2)):
        if number_string[k] != number_string[k * -1 - 1]:
            return False
    return True

def is_pandigital(number_to_check):
    number_to_check_string = str(number_to_check)
    all_digits = set(map(str, range(1, len(number_to_check_string) + 1)))
    return len(number_to_check_string) == len(number_to_check_string) and set(number_to_check_string) == all_digits