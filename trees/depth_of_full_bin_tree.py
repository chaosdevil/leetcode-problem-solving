"""
inputs must be binary tree that is traversed in preorder fashion
nnnllll
nlnll
nlnnlll
"""

def findDepthRec(tree, n, index):
    # WRITE CODE HERE

    if index >= n or tree[index] == 'l':
        return 0

    # index += 1
    left = findDepthRec(tree, n, index+1)
    # index += 1
    right = findDepthRec(tree, n, index+2)

    return max(left, right) + 1


def findDepth(tree, n):
    index = 0
    return findDepthRec(tree, n, index)


if __name__ == '__main__':
    tree = str(input())
    n = len(tree)
    print(findDepth(tree, n))

