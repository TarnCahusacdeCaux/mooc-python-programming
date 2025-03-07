year: int = int(input("Year: "))
next_leap_year: int = year

while True:
    next_leap_year += 1

    if next_leap_year % 4 == 0:
        if next_leap_year % 100 == 0 and not next_leap_year % 400 == 0:
            continue
        else:
            break
    else:
        continue

print(f"The next leap year after {year} is {next_leap_year}")
