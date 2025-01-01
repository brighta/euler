import sys

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

cache = {}

input_value = int(sys.argv[1])

def find_routes(size, x, y):
    if (x, y) in cache:
        return cache[x, y]
    if x == size:
        if y == size:
            return 1
        answer = find_routes(size, x, y + 1)
        cache[x, y] = answer
        return answer
    if y == size:
        answer = find_routes(size, x + 1, y)
        cache[x, y] = answer
        return answer
    answer = find_routes(size, x + 1, y) + find_routes(size, x, y + 1)
    cache[x, y] = answer
    return answer

print(find_routes(input_value, 0, 0))