from build_bst import BinarySearchTree

def lca(node, n1, n2):
    if not node:
        return None
    
    if node.info == n1 or node.info == n2:
        return node
    
    left= lca(node.left, n1, n2)
    right = lca(node.right, n1, n2)

    if left and right:
        return node

    return left if left else right


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
