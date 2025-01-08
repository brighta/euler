from math import floor, sqrt

# from math import floor, sqrt
def get_proper_divisors(number_to_check):
    divisors = set()
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.add(i)
            divisors.add(int(number_to_check / i))
    divisors.remove(number_to_check)
    return divisors

# from math import floor, sqrt
def is_prime(number_to_check):
    divisors = set()
    for i in range(floor(sqrt(number_to_check)), 0, -1):
        if number_to_check % i == 0:
            divisors.add(i)
            divisors.add(int(number_to_check / i))
    divisors.remove(number_to_check)
    return len(divisors) == 1

# from math import floor
def is_palindromic_number(number):
    number_string = str(number)
    for k in range(int(floor(len(number_string)) / 2)):
        if number_string[k] != number_string[k * -1 - 1]:
            return False
    return True