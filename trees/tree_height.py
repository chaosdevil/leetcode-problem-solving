from build_bst import *

def height_recursive(root):
    if not root:
        return -1
    
    return 1 + max(height_recursive(root.left), height_recursive(root.right))


def height_iterative(root):
    if not root:
        return 0
    
    height = 0
    queue = [root, None]
    
    while queue:
        front = queue[0]
        queue = queue[1:]

        if front:
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        else:
            if queue:
                height += 1
                queue.append(None)

    return height


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split(" ")))
    tree = BinarySearchTree()
    for i in range(n):
        tree.create(inputs[i])

    print(height_iterative(tree.root))
