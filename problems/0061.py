import sys
from itertools import combinations, permutations

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

def get_number_parts(number_to_split):
    number_string = str(number_to_split)
    return int(number_string[:2]), int(number_string[2:])

def set_figurate_number(figurate_number, number_to_set):
    if 1000 <= number_to_set < 10000:
        number_parts = get_number_parts(number_to_set)
        figurate_numbers[figurate_number][number_parts[0]] = number_parts[1]
    return number_to_set >= 10000

def cyclical_figurate_numbers(original_first_number, combination_to_check):
    first_number = original_first_number
    numbers = []
    for j in range(6):
        if not first_number in figurate_numbers[combination_to_check[j]].keys():
            return []
        second_number = figurate_numbers[combination_to_check[j]][first_number]
        numbers.append(int("{}{}".format(first_number, second_number)))
        if j == 5:
            if second_number != original_first_number:
                return []
            else:
                return numbers
        else:
            first_number = second_number

figurate_numbers = {
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {}
}
n = 1
numbers_complete = {
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False
}
while not all(numbers_complete.values()):
    if not numbers_complete[3]:
        numbers_complete[3] = set_figurate_number(3, int(n * (n + 1) / 2))
    if not numbers_complete[4]:
        numbers_complete[4] = set_figurate_number(4, int(n * n))
    if not numbers_complete[5]:
        numbers_complete[5] = set_figurate_number(5, int(n * (3 * n - 1) / 2))
    if not numbers_complete[6]:
        numbers_complete[6] = set_figurate_number(6, int(n * (2 * n - 1)))
    if not numbers_complete[7]:
        numbers_complete[7] = set_figurate_number(7, int(n * (5 * n - 3) / 2))
    if not numbers_complete[8]:
        numbers_complete[8] = set_figurate_number(8, int(n * (3 * n - 2)))
    n += 1

for i in range(10, 100):
    for combination in list(permutations([3, 4, 5, 6, 7, 8])):
        cyclic_figurate_numbers_list = cyclical_figurate_numbers(i, combination)
        if len(cyclic_figurate_numbers_list) != 0:
            print(sum(cyclic_figurate_numbers_list))
            exit()
