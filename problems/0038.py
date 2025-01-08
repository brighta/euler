all_digits = set(map(str, range(1, 10)))

def create_multiple(number, max_n):
    new_number_string = ""
    for n in range(1, max_n + 1):
        new_number_string += str(n * number)
    return int(new_number_string)

def is_pandigital(number_to_check):
    number_to_check_string = str(number_to_check)
    return len(number_to_check_string) == 9 and set(number_to_check_string) == all_digits

pandigital_numbers = []
for i in range(10000):
    for maximum_n in range(1, 9):
        multiple = create_multiple(i, maximum_n)
        if is_pandigital(multiple):
            pandigital_numbers.append(multiple)
print(max(pandigital_numbers))