limit: int = int(input("Limit: "))
count: int = 1
sum: int = 1
sum_str: str = "1"

while sum < limit:
    count += 1
    sum += count
    sum_str += " + " + str(count)

print(f"The consecutive sum: {sum_str} = {sum}")
