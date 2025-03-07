password: str = input("Password: ")

while True:
    repeated_password: str = input("Repeat password: ")

    if repeated_password == password:
        break

    print("They do not match!")

print("User account created!")
