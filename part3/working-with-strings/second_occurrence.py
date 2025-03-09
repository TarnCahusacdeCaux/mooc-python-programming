string: str = input("Please type in a string: ")
substring: str = input("Please type in a substring: ")
index: int = 0
count: int = 0

while True:
    if len(string) < len(substring):
        print("The substring does not occur twice in the string.")
        break

    if string.find(substring) == 0:
        string = string[len(substring) :]
        count += 1
        if count == 2:
            print(f"The second occurrence of the substring is at index {index}.")
            break
        index += len(substring)

    else:
        string = string[1:]
        index += 1
