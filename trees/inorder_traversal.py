from build_bst import *
from time import time

def inOrder(root):
    #Write your code here
    current = root
    prev = None
    
    if not current:
        return None
    
    while current:
        if not current.left:
            print(current.info, end=" ")
            current = current.right
        else:
            prev = current.left
            # find rightmost
            while prev.right and prev.right != current:
                prev = prev.right
                
            if not prev.right:
                prev.right = current
                current = current.left
            else:
                prev.right = None
                print(current.info, end=" ")
                current = current.right
    print()


def inorder_stack(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        top = stack.pop()
        print(top.info, end=" ")

        if top.left:
            stack.append(top.left)
        if top.right:
            stack.append(top.right)
        

if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split(" ")))
    tree = BinarySearchTree()
    for i in inputs:
        tree.create(i)
    
    start = time()
    inorder_stack(tree.root)
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
