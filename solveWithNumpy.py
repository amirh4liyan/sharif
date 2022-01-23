import numpy as np

ex1 = input()
ex2 = input()

x1 = ex1[:ex1.find("x")]
y1 = ex1[ex1.find("+")+1:ex1.find("y")]

x2 = ex2[:ex2.find("x")]
y2 = ex2[ex2.find("+")+1:ex2.find("y")]

m1 = ex1[ex1.find("=")+1:]
m2 = ex2[ex2.find("=")+1:]

x1, x2 = int(x1) ,int(x2) 
y1, y2 = int(y1) ,int(y2) 
m1, m2 = int(m1) ,int(m2)

zaribs = np.array([[x1, y1], [x2, y2]])
answers = np.array([m1, m2])

final = np.linalg.solve(zaribs, answers)
a, b = final[0], final[1]

print("x = {:.6f} and y = {:.6f}".format(a, b))

