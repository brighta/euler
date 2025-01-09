def get_triangular_number(n):
    return int(n * (n + 1) / 2)

def get_pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)

def get_hexagonal_number(n):
    return int(n * (2 * n - 1))

triangle_numbers = [1]
pentagonal_numbers = [1]
hexagonal_numbers = [1]

while True:
    hexagonal_numbers.append(get_hexagonal_number(len(hexagonal_numbers) + 1))
    while pentagonal_numbers[-1] < hexagonal_numbers[-1]:
        pentagonal_numbers.append(get_pentagonal_number(len(pentagonal_numbers) + 1))
    while triangle_numbers[-1] < hexagonal_numbers[-1]:
        triangle_numbers.append(get_triangular_number(len(triangle_numbers) + 1))
    if hexagonal_numbers[-1] == pentagonal_numbers[-1] == triangle_numbers[-1]:
        if hexagonal_numbers[-1] > 40755:
            print(hexagonal_numbers[-1])
            exit()