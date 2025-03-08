limit: int = int(input("Upper limit: "))
base: int = int(input("Base: "))
count: int = 1

while count <= limit:
    print(count)
    count *= base
