string: str = input("Please type in a string: ")
vowels: str = "aeo"
index: int = 0

while index < len(vowels):
    if vowels[index] in string:
        print(vowels[index] + " found")
    else:
        print(vowels[index] + " not found")
    index += 1
