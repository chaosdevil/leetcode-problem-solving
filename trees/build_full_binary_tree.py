# inputs must be binary tree that is traversed in preorder fashion
# nnnllll
# nlnll
# nlnnlll


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


def build_tree(inp):
    tree = None
    for i in range(len(inp)):
        tree = put_node(tree, inp[i])

    return tree

def put_node(root, data):
    if not root:
        root = Node(data)
        return root
    else:
        # search left
        current = root
        stack = [current]
        
        # find previous node
        while stack:
            
            current = stack.pop()

            if current.data == 'n' and (not current.left or not current.right):
                break
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        if not current.left:
            current.left = Node(data)
        elif not current.right:
            current.right = Node(data)

    return root

def preorder(root):
    if not root:
        return

    print(root, end=" ")

    preorder(root.left)
    preorder(root.right)


test = 'nlnll'
tree = build_tree(test)

preorder(tree)
