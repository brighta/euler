import sys
# from itertools import permutations

# credit - https://www.educative.io/answers/project-euler-62-cubic-permutations

if len(sys.argv) != 2:
    sys.exit("Please enter the input value")

input_value = int(sys.argv[1])

# My Code - works but takes too long
# n = 1
# while True:
#     cubed = n**3
#     if n % 100000 == 0:
#         print(cubed)
#     cubed_len = str(cubed)
#     count = 0
#     for permutation in (set([int(''.join(p)) for p in permutations(str(cubed))])):
#         if len(str(permutation)) == cubed_len and round(permutation**(1/3), 10) % 1 == 0:
#             count += 1
#     if n == 41063625:
#         print(count)
#     if count == input_value:
#         print(cubed)
#         exit()
#     n += 1

cache = dict()

n = 1
while True:
    n_cube = n ** 3
    sorted_cube = ''.join(sorted(str(n_cube)))
    if sorted_cube in list(cache.keys()):
        cache[sorted_cube] = [cache[sorted_cube][0], cache[sorted_cube][1] + 1]
    else:
        cache.update({sorted_cube: [n_cube, 1]})
    if cache[sorted_cube][1] == input_value:
        print(cache[sorted_cube][0])
        exit()
    n += 1