story: str = ""
word: str = ""

while True:
    previous_word: str = word
    word = input("Please type in a word: ")
    if word == "end":
        break
    if word == previous_word:
        break
    story += word + " "
print(story)
