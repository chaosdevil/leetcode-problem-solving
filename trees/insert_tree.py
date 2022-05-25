class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insertion(self, root, prev, val):
        if not root:
            return Node(val)
        elif val < root.info:
            root.left = self.insertion(root.left, root, val)
        else:
            root.right = self.insertion(root.right, root, val)
        
        return root

    def insert(self, val):
        # Enter you code here.
        current = self.root
        prev = self.root
        self.root = self.insertion(current, prev, val)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
