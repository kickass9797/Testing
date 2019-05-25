import pprint
import matplotlib.pyplot as plt

def sum(j):
	S_n = 0
	n = 2**j
	for k in range(1,n+1):
		S_n += 1/(k**3)
	return S_n

def rev_sum(j):
	S_n = 0
	n = 2**j
	for k in reversed(range(1,n+1)):
		S_n += 1/(k**3)
	return S_n


S_n_arr = []
rev_S_n_arr = []

# for i in range(1,23):
# 	S_n_arr.append(sum(i))

for i in range(1,23):
 	rev_S_n_arr.append(rev_sum(i))
#
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(S_n_arr)
# pp.pprint(rev_S_n_arr)

S_inf = rev_S_n_arr[-1]

abweichung = []
for i in range(1,23):
	abw = abs(rev_S_n_arr[i-1] - S_inf)
	abweichung.append(abw)

x = []
for i in range(1,23):
	x.append(2**i)

plt.plot(x, abweichung, 'ro')
plt.yscale('log')
plt.xscale('log')
plt.show()

