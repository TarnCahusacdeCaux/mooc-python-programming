word: str = input("Word: ")
white_space: str = " " * ((28 - len(word)) // 2)

if len(word) % 2 == 0:
    print("*" * 30)
    print("*" + white_space + word + white_space + "*")
    print("*" * 30)
else:
    print("*" * 30)
    print("*" + white_space + word + white_space + " " + "*")
    print("*" * 30)
