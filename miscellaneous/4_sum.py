# A hashing based Python program to find if there are
# four elements with given summ.

# The function finds four elements with given summ X
from collections import OrderedDict

def findFourElements(arr, n, X):

	# Store summs of all pairs in a hash table
	mp = {}
	for i in range(n - 1):
		for j in range(i + 1, n):
			mp[arr[i] + arr[j]] = [i, j]

	ans = []

	for i in range(n - 1):
		for j in range(i + 1, n):
			summ = arr[i] + arr[j]
			if (X - summ) in mp:
				p = mp[X - summ]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					ll = OrderedDict()
					ll.add(arr[i])
					ll.add(arr[j])
					ll.add(arr[p[0]])
					ll.add(arr[p[1]])
					if list(ll) not in ans:
						ans.append(list(ll))
	return ans

# Driver code
arr = [1,0,-1,0,-2,2]
n = len(arr)
X = 0

# Function call
ans = findFourElements(arr, n, X)
print(ans)

# This is code is contributed by shubhamsingh10
