from math import prod
from fractions import Fraction

def get_digit_from_number(number, index):
    return int(str(number)[index])

non_trivial_fractions = []
for i in range(11, 100):
    for j in range(10, i):
        answer = j / i
        if sum([get_digit_from_number(j, 1), get_digit_from_number(i, 1)]) != 0:
            if (
                get_digit_from_number(i, 0) != 0 and (
                    (get_digit_from_number(j, 0) / get_digit_from_number(i, 0) == answer and get_digit_from_number(j, 1) == get_digit_from_number(i, 1)) or
                    (get_digit_from_number(j, 1) / get_digit_from_number(i, 0) == answer and get_digit_from_number(j, 0) == get_digit_from_number(i, 1))
                ) or
                get_digit_from_number(i, 1) != 0 and (
                    (get_digit_from_number(j, 0) / get_digit_from_number(i, 1) == answer and get_digit_from_number(j, 1) == get_digit_from_number(i, 0)) or
                    (get_digit_from_number(j, 1) / get_digit_from_number(i, 1) == answer and get_digit_from_number(j, 0) == get_digit_from_number(i, 0))
                )
            ):
                non_trivial_fractions.append((j, i))

numerator = prod([fraction[0] for fraction in non_trivial_fractions])
denominator = prod([fraction[1] for fraction in non_trivial_fractions])
print(Fraction(numerator, denominator).denominator)