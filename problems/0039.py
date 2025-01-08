max_count = 0
p = 0
for i in range(1, 1001):
    valid_p_values = set()
    for c in range(1, i - 2):
        for b in range(1, i - c):
            a = i - c - b
            if a < b and pow(c, 2) == pow(b, 2) + pow(a, 2):
                valid_p_values.add(frozenset([a, b, c]))
    if len(valid_p_values) > max_count:
        max_count = len(valid_p_values)
        p = i
print(p)