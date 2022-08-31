class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TarjanOLCA:
    def __init__(self) -> None:
        self.rank = dict()
        self.parent = dict()
        self.ancestor = dict()
        self.children = dict()
        self.color = dict()

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def offline_lca(self, u: TreeNode, p, q, pairs):
        self.make_set(u.val)
        self.ancestor[u.val] = u.val
        children = []
        children.append(u.left)
        children.append(u.right)
        pairs.add(u.left)
        pairs.add(u.right)
        for v in children:
            if v:
                self.offline_lca(v, p, q, pairs)
                self.union(u.val, v.val)
                self.ancestor[self.find(u.val)] = u.val

        self.color[u.val] = "black"
        for v in pairs:
            if v and v.val in self.color and \
                self.color[v.val] == "black":
                print(f"Lowest Common Ancestor {u.val} and {v.val} is {self.ancestor[self.find(v.val)]}")
            
            
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = TarjanOLCA()
        global pairs
        pairs = set()
        lca.offline_lca(root, p, q, pairs)
        return 

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    solution = Solution()
    solution.lowestCommonAncestor(root, root.left, root.left.right.left)
        
                

