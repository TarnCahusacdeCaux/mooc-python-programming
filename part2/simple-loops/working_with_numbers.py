number_of_nums: int = 0
sum: int = 0
positive_nums: int = 0
negative_nums: int = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num: int = int(input("Number: "))
    if num == 0:
        break
    if num > 0:
        positive_nums += 1
    else:
        negative_nums += 1
    number_of_nums += 1
    sum += num
print(f"Numbers typed in {number_of_nums}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / number_of_nums}")
print(f"Positive numbers {positive_nums}")
print(f"Negative numbers {negative_nums}")
