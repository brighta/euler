from itertools import permutations

def is_pandigital(number_to_check):
    number_to_check_string = str(number_to_check)
    all_digits = set(map(str, range(1, len(number_to_check_string) + 1)))
    return len(number_to_check_string) == len(number_to_check_string) and set(number_to_check_string) == all_digits

def has_sub_string_divisibility(number_to_check):
    number_to_check_string = str(number_to_check)
    return (
        int("".join(number_to_check_string[1:4])) % 2  == 0 and
        int("".join(number_to_check_string[2:5])) % 3  == 0 and
        int("".join(number_to_check_string[3:6])) % 5  == 0 and
        int("".join(number_to_check_string[4:7])) % 7  == 0 and
        int("".join(number_to_check_string[5:8])) % 11 == 0 and
        int("".join(number_to_check_string[6:9])) % 13 == 0 and
        int("".join(number_to_check_string[7:]))  % 17 == 0
    )

pandigital_numbers_with_sub_string_divisibility = []
for permutation in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    number = int("".join(map(str, permutation)))
    if len(str(number)) == 10 and has_sub_string_divisibility(number):
        pandigital_numbers_with_sub_string_divisibility.append(number)
print(sum(pandigital_numbers_with_sub_string_divisibility))