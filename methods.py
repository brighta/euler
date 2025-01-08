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
    for divisor in range(floor(sqrt(number_to_check)), 2, -1):
        if number_to_check % divisor == 0:
            return False
    return True

# from math import floor
def is_palindromic_number(number):
    number_string = str(number)
    for k in range(int(floor(len(number_string)) / 2)):
        if number_string[k] != number_string[k * -1 - 1]:
            return False
    return True