# get lines
lines = []
while True:
    data = input()
    if data != "<end_of_dic>":
        lines.append(data)
    else:
        # get text
        text = input()
        break

# parsing words
words = {}
for line in lines:
    line = line.split()
    words[line[0]] = line[1]

# make a dictionary
wordsList = list(words.keys())
wordsList.sort(key=len, reverse=True)

# translate variable
translated = []
for i in range(len(text)):
    translated.append(-1)

# translating
for i in range(len(wordsList)):
    while True:
        a = text.find(wordsList[i])
        if a != -1:
            translated[a] = words[wordsList[i]]
            b = a + len(wordsList[i])
            text = text[:a] + " " + text[b:]
        else:
            break

# replace unknown with .
for i in range(len(text)):
    if text[i] != " ":
        translated[i] = "."
        text = text[:i] + " " + text[i+1:]

# remove extra blocks
for i in range(translated.count(-1)):
    translated.remove(-1)

# print translated string
newText = " ".join(translated)
print(newText)