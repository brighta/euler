import sys
from math import floor, sqrt
from itertools import combinations, permutations

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def is_prime(number_to_check):
    for divisor in range(floor(sqrt(number_to_check)), 1, -1):
        if number_to_check % divisor == 0:
            return False
    return True

def get_indexes(digits_to_check, number_to_check):
    return [index for index, digit_in_number in enumerate(digits_to_check) if digit_in_number == number_to_check]

def replace_digits(number_to_be_replaced, indexes_to_replace, number_to_set):
    number_to_be_replaced_list = list(str(number_to_be_replaced))
    for index in indexes_to_replace:
        number_to_be_replaced_list[index] = str(number_to_set)
    return int("".join(number_to_be_replaced_list))


number = 3
digits_required = set(range(0, 11 - input_value))
while True:
    digits = list(map(int, list(str(number))))
    if len(digits_required.intersection(set(digits))) > 0 and is_prime(number):
        for i in digits_required:
            indexes = get_indexes(digits, i)
            arrangements = set(combination for n in range(1, len(indexes) + 1) for combination in combinations(indexes, n))
            for arrangement in arrangements:
                number_of_primes = 0
                for n in range(0, 10):
                    replaced_number = replace_digits(number, arrangement, n)
                    if len(str(replaced_number)) == len(str(number)):
                        if is_prime(replace_digits(number, arrangement, n)):
                            number_of_primes += 1
                if number_of_primes == input_value:
                    print(number)
                    exit()
    number += 2