from bisect import bisect_left

def lis(v):
	if len(v) == 1:
		return 1

	dp = [1 for _ in range(len(v))]

	for i in range(1, len(v)):
		for j in range(i):
			if v[j] < v[i]:
				dp[i] = max(dp[i], dp[j]+1)

	return max(dp)


def improved_lis(v):
	if len(v) == 0: # boundary case
		return 0

	tail = [0 for i in range(len(v) + 1)]
	length = 1 # always points empty slot in tail

	tail[0] = v[0]

	for i in range(1, len(v)):
		if v[i] > tail[length-1]:
			# v[i] extends the largest subsequence
			tail[length] = v[i]
			length += 1

		else:
			# v[i] will extend a subsequence and discard older subsequence

			# find the largest value just smaller than v[i] in tail

			# to find that value do binary search for the v[i] in
			# the range from begin to 0 + length

			# bisect function either returns index where element is found
			# or the appropriate index at which element should be placed

			# finally replace the existing subsequence with new end value
			tail[bisect_left(tail, v[i], 0, length-1)] = v[i]

	return length


# Driver program to test above function
v = [10,9,2,5,3,7,101,18]
print("Length of Longest Increasing Subsequence is ", lis(v))
print("Length of Longest Increasing Subsequence is ", improved_lis(v))

# This code is contributed by Serjeel Ranjan
