count = 0
power = 1
while True:
    num_digits = 0
    for n in range(1, 10):
        power_of_n = n ** power

        num_digits = len(str(power_of_n))
        if num_digits == power:
            count += 1
    if num_digits < power:
        break
    power += 1
print(count)
