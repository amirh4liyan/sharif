class Point:
    def __init__(self, A, B):
        self.A = A 
        self.B = B 

    def equation(self):
        y = (self.A[1] - self.B[1])
        x = (self.A[0] - self.B[0])
        a = y / x
        b = self.A[1] - a*self.A[0]
        return (int(a), int(b))

# input
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())


line = Point((x1, y1), (x2, y2))
e = line.equation()

print(e)
