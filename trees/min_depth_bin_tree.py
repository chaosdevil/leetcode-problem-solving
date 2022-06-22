# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        return self.bfs(root)
        
    def bfs(self, root):
        
        queue = [(root, 0)]
        result = []
        
        while queue:
            current, depth = queue.pop(0)
            
            if current:
                if depth < len(result):
                    result[depth].append(current.val)
                else:
                    result.append([current.val])

                queue.append((current.left, depth+1))
                queue.append((current.right, depth+1))
                
        return result


if __name__ == "__main__":
    pass

