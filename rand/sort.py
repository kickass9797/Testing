import numpy as np

def insertsort(l):
	for i in range(1, len(l)):
		insert = l[i]
		j = i
		while j > 0 and l[j-1] > insert:
			l[j] = l[j-1]
			j -= 1
		l[j] = insert 
	return l

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)//2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

array = np.random.randint(0, high=2**10, size=1000)
print(array)

print(quicksort(array))

