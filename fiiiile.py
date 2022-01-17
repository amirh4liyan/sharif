rowColumn = input()
rowColumn = rowColumn.split()
n, m = rowColumn
n, m = int(n), int(m)


counter = 1
with open("csv.txt", "r") as f:
    for line in enumerate(f):
        if n == counter:
            data = line[1]
            data = data.strip().split(",")
            blockData = data[m-1]
            break
        else:
            counter += 1

with open("result.txt", "w") as f:
    f.write(blockData)
    f.write("\n")
