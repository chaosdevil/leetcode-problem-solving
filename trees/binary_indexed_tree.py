# Fenwick tree

class BinaryIndexedTree:
	def __init__(self, nums):
		self.nums = nums
		self.n = len(nums)
		self.bit = [0] * (self.n+1)
		for i in range(self.n):
			self.construct(i, self.nums[i])

	def construct(self, idx, val):
		idx += 1
		while idx <= self.n:
			self.bit[idx] += val
			idx += idx & (-idx)

	def update(self, idx, val):
		diff = val - self.nums[idx]
		self.nums[idx] = val
		self.construct(idx, diff)

	def query(self, idx):
		result = 0
		idx += 1
		while idx > 0:
			result += self.bit[idx]
			idx -= idx & (-idx)
		print(result)
		return result

	def sum_range(self, i, j):
		return self.query(j) - self.query(i-1)

if __name__ == "__main__":
	nums = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
	solution = BinaryIndexedTree(nums)
	print(solution.bit)
	print(solution.sum_range(2, 8))

	# update value at index 6 to 25
	solution.update(6, 25)
	print(solution.sum_range(2, 8))