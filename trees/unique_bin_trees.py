# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = [i for i in range(1, n+1)]
        return self.build_tree([], nums)
        
    def build_tree(self, result, nums):
        if not nums:
            return [None]
        
        for i in range(len(nums)):
            left = self.build_tree(result, nums[:i])
            right = self.build_tree(result, nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nums[i])
                    root.left = l
                    root.right = r
                    result.append(root)

        return result

    def print_trees(self, root):
        if not root:
            return

        print(root.val)

        self.print_trees(root.left)
        self.print_trees(root.right)


if __name__ == "__main__":

    n = 3

    solution = Solution()
    result = solution.generateTrees(3)
    print(result)
    for tree in result:
        solution.print_trees(tree)
            
        
    