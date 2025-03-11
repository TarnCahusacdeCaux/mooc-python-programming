num: int = int(input("Please type in a number: "))

left_side: int = 1
right_side: int = 1
result: int = left_side * right_side

while result <= num**2:
    print(f"{left_side} * {right_side} = {result}")
    left_side += 1
    right_side += 1
    result: int = left_side * right_side
