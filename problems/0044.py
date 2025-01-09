from math import sqrt

# credit - https://raw.org/puzzle/project-euler/problem-44/

def is_pentagonal(number_to_check):
    return sqrt(1 + 24 * number_to_check) % 6 == 5

pentagonal_numbers = [1, 5, 12]
pentagonal_number_difference = 10
pentagonal_number = 22
while True:
    pentagonal_number_difference += 3
    pentagonal_number += pentagonal_number_difference
    pentagonal_numbers.append(pentagonal_number)
    for i in range(len(pentagonal_numbers)):
        b = pentagonal_numbers[i]
        a = pentagonal_number - b
        difference = abs(a - b)
        if is_pentagonal(a) and is_pentagonal(difference):
            print(difference)
            exit()
