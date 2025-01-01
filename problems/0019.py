day = 366

def sundays_on_first_in_year(year):
    global day
    count = 1 if day % 7 == 0 else 0
    for days in [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]:
        day += days
        if day % 7 == 0:
            count += 1
    day += 31
    return count

sundays_count = 0
for i in range(1901, 2001):
    sundays_count += sundays_on_first_in_year(i)

print(sundays_count)