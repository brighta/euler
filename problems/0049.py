from math import floor, sqrt
from collections import Counter
def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 2, -1):
        if number_to_check % divisor == 0:
            return False
    return True

for i in range(1488, 3340):
    a = i
    b = i + 3330
    c = b + 3330
    if is_prime(a) and is_prime(b) and is_prime(c) and Counter(list(str(a))) == Counter(list(str(b))) ==  Counter(list(str(c))):
        print("{}{}{}".format(a, b, c))
        exit()