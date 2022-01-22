
def dictionarize(listx):
    lines = []
    for i in range(len(listx)):
        lines.append(listx[i])
    diction = {}
    for item in lines:
        key = item[0]
        value = item[1]
        if key not in diction:
            diction[key] = [value]
        else:
            diction[key].append(value)
    print(diction)

lines = []
n = int(input())
for line in range(n):
    data = input()
    lines.append(data)

GUYS = []
for item in lines:
    key = item[:item.index(":")].strip()
    value = item[item.index(":")+1:].strip()
    GUYS.append((key, value))

dictionarize(GUYS)
