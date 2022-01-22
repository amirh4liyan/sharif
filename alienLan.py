lines = []
while True:
    data = input()
    if data != "<end_of_dic>":
        lines.append(data)
    else:
        # get text
        text = input()
        break

words = {}
for line in lines:
    line = line.split()
    words[line[0]] = line[1]

wordsList = list(words.keys())
wordsList.sort(key=len)

for word in wordsList:
    if word in text:
        text.replace(word, words[word])

print (text)
