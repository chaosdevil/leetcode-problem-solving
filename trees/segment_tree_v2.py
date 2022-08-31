# https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
from ast import literal_eval
import os


class SegmentTree:
	def __init__(self, arr):
		self.arr = arr
		self.tree = [0] * (len(arr)*4)

	def build_seg_tree(self, idx, low, high):
		if low == high:
			self.tree[idx] = self.arr[low]
			return

		mid = low + (high - low) // 2
		self.build_seg_tree(2*idx+1, low, mid)
		self.build_seg_tree(2*idx+2, mid+1, high)

		# merge build results
		self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]

	def query(self, idx, low, high, i, j):
		# query range
		if low > j or high < i:
			return 0

		if i <= low and j >= high:
			return self.tree[idx]

		mid = low + (high - low) // 2

		if i > mid:
			return self.query(2*idx+2, mid+1, high, i, j)
		elif j <= mid:
			return self.query(2*idx+1, low, mid, i, j)

		left_query = self.query(2*idx+1, low, mid, i, mid)
		right_query = self.query(2*idx+2, mid+1, high, mid+1, j)

		return left_query + right_query

	def update(self, idx, low, high, arrIdx, val):
		if low == high:
			self.tree[idx] = val
			return
		mid = low + (high - low) // 2
		if arrIdx > mid:
			self.update(2*idx+2, mid+1, high, arrIdx, val)
		else:
			self.update(2*idx+1, low, mid, arrIdx, val)

		self.tree[idx] = self.tree[2*idx+1] + self.tree[2*idx+2]

if __name__ == "__main__":
	with open(os.path.dirname(__file__) + "/segment_tree_testcase.txt", "r") as file:
		arr = literal_eval(file.readline().strip())
		n = len(arr)
	# arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]

	seg_tree = SegmentTree(arr)
	seg_tree.build_seg_tree(0, 0, n-1)

	# print sum of range 2 to 8
	print(seg_tree.query(0, 0, n-1, 2, 8))

	# update value at index 6 with 25
	seg_tree.update(0, 0, n-1, 6, 25)

	# print sum of range 2 to 8 again
	print(seg_tree.query(0, 0, n-1, 2, 8))