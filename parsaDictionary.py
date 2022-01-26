lines = set()
while True:
   line = input()
   if line == "<end>":
       break
   else:
       lines.add(line)
lines.discard('')

def addKeys(keyWord):
    strips = '.: "'
    keyWord = keyWord.strip(strips)
    keyWord = keyWord.lower()
    wordsDict.add(keyWord)

def swap(i):
    keyWords[i], keyWords[i-1] = keyWords[i-1], keyWords[i]

def sortByAlpha():
    a = len(keyWords)
    for j in range(a):
        for i in range(a-1, 0, -1):
            # if second was closer, return True, else will return False
            if compareAlpha(keyWords[i-1], keyWords[i]):
                swap(i)

def compareAlpha(x, y):
    a, b = x, y
    if len(x) > len(y):
        a, b = b, a
    answer = a
    for i in range(len(a)):
        ordX = ord(a[i])
        ordY = ord(b[i])
        if ordX == ordY:
            continue
        elif ordX < ordY:
            break
        elif ordX > ordY:
            answer = b
            break
    if answer == y:
        return True
    elif answer == x:
        return False


wordsDict = set()
for line in lines:
    line = line.split()
    for word in line:
        addKeys(word)

keyWords = list(wordsDict)
sortByAlpha()
for word in keyWords:
    print(word)
