limit: int = int(input("Limit: "))
count: int = 0
sum: int = 0

while sum < limit:
    count += 1
    sum += count

print(sum)
