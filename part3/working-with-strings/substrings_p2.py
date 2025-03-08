string: str = input("Please type in a string: ")
count: int = 0

while count > -len(string):
    count -= 1
    print(string[count:])
