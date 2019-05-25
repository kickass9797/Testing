import numpy as np

dim = int(input("Enter dimension: "))

A = np.zeros((dim,dim))
b = np.zeros(dim)

#input A
for i in range(0, dim):
	for j in range(0, dim):
		A[i][j] = float(input(f"Enter A[{i}][{j}]: "))

#input b
for i in range(0, dim):
	b[i] = float(input(f"Enter b[{i}]: "))

x = np.linalg.solve(A,b)

print(x)
