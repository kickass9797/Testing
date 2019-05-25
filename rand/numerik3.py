import numpy as np

k = 1
n = 10**k
L = np.eye(n)
L_T = np.eye(n)
for i in range(1,n):
  L[i-1][i] = -1
  L_T[i][i-1] = -1
print(L)
print(L_T)
