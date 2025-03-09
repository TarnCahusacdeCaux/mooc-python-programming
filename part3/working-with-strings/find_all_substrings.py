word: str = input("Please type in a word: ")
char: str = input("Please type in a character: ")

while word.find(char) != -1 and len(word) >= 3:
    index: int = word.find(char)
    if index + 3 <= len(word):
        print(word[index : index + 3])
    word = word[index + 1 :]
