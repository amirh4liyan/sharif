class Action:
    def __init__(self, n, matrix):
        self.n = n
        self.matrix = matrix

    def Clockwise(self):
        for i in range(self.n):
            for j in range(self.n):
                indexJ2 = (self.n-1) - i
                indexI2 = j
                self.matrix[i][j], self.matrix[indexI2][indexJ2] = self.matrix[indexI2][indexJ2], self.matrix[i][j]

    def Horizontal_symmetry(self):
        for i in range(int(self.n/2)):
            for j in range(self.n):
                indexI2 = (self.n-1) - i
                self.matrix[i][j], self.matrix[indexI2][j] = self.matrix[indexI2][j], self.matrix[i][j]

    def Vertical_symmetry(self):
        for i in range(self.n):
            for j in range(int(self.n/2)):
                indexJ2 = (self.n-1) - j
                self.matrix[i][j], self.matrix[i][indexJ2] = self.matrix[i][indexJ2], self.matrix[i][j]

    def pr(self):
        for i in range(self.n):
            print("".join(self.matrix[i]))


n = int(input())
matrix = []

for i in range(n):
    data = input()
    column = []
    for j in range(n):
        column.append(data[j])
    matrix.append(column)

m = Action(n, matrix)
q = int(input())

for i in range(q):
    data = input()
    if data == "H":
        m.Horizontal_symmetry()
    elif data == "V":
        m.Vertical_symmetry()
    elif data == "90":
        m.Clockwise()
    else:
        continue

m.pr()
