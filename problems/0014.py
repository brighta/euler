import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

cache = {}

def get_next_number(current_number):
    if current_number in cache:
        return cache[current_number]
    if current_number == 1:
        return 1
    if current_number % 2 == 0:
        current_number = int(current_number / 2)
    else:
        current_number = current_number * 3 + 1
    answer = 1 + get_next_number(current_number)
    cache[current_number] = answer
    return answer

number = 0
length = 0
for i in range(2, input_value):
    answer = get_next_number(i)
    if answer > length:
        number = i
        length = answer

print(number)