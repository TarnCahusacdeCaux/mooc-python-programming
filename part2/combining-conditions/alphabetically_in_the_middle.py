letter1: str = input("1st letter: ")
letter2: str = input("2nd letter: ")
letter3: str = input("3rd letter: ")

if letter2 < letter1 < letter3:
    print(f"The letter in the middle is {letter1}")
elif letter2 > letter1 > letter3:
    print(f"The letter in the middle is {letter1}")

elif letter1 < letter2 < letter3:
    print(f"The letter in the middle is {letter2}")
elif letter1 > letter2 > letter3:
    print(f"The letter in the middle is {letter2}")

elif letter1 < letter3 < letter2:
    print(f"The letter in the middle is {letter3}")
elif letter1 > letter3 > letter2:
    print(f"The letter in the middle is {letter3}")
