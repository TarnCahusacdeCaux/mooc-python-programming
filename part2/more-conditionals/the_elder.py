print("Person 1:")
name1: str = input("Name: ")
age1: int = int(input("Age: "))

print("Person 2:")
name2: str = input("Name: ")
age2: int = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age1 < age2:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")
