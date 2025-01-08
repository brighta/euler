from math import floor, sqrt

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 2, -1):
        if number_to_check % divisor == 0:
            return False
    return True

def is_pandigital(number_to_check):
    number_to_check_string = str(number_to_check)
    all_digits = set(map(str, range(1, len(number_to_check_string) + 1)))
    return len(number_to_check_string) == len(number_to_check_string) and set(number_to_check_string) == all_digits

for i in range(7654321, 3, -2):
    if is_pandigital(i) and is_prime(i):
        print(i)
        exit()
