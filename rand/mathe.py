import numpy as np
import matplotlib.pyplot as plt

def euklid_ggt(a,b):
	if a < b:
		print(f"Do ggT({b},{a})")
		return euklid_ggt(b,a)
	if b == 0:
		return a
	q = a // b
	r = a - q*b
	print((q,b,r))
	return euklid_ggt(b,r)

def euklid(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def solve_lgs():
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

	return x

def euler_phi(n):
    return [x for x in range(n+1) if euklid(x,n) == 1]

print(len(euler_phi(125)))

