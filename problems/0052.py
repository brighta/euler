from collections import Counter

def get_counter(number_to_check):
    return Counter(list(str(number_to_check)))

number = 1
while True:
    if get_counter(number) == get_counter(2 * number) == get_counter(3 * number) == get_counter(4 * number) == get_counter(5 * number) == get_counter(6 * number):
        print(number)
        exit()
    number += 1