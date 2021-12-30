openFile = open("file.txt")
readFile = openFile.read()
text = readFile.lower()
unique = set(text.split())

for word in unique:
    print(f'{word}: {text.count(word)}')