"This is a testing code"

with open("line.txt", "r", encoding="utf8") as file:
    content = file.read()
    print(content)

assert content != ""
