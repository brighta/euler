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