word: str = input("Please type in a word: ")
char: str = input("Please type in a character: ")

if word.find(char) + 3 <= len(word):
    print(word[word.find(char) : word.find(char) + 3])
