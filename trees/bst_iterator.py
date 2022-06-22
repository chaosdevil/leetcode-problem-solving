from time import time


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator:
    __stack = []
    def __init__(self, root):
        current = root
        while current:
            self.__stack.append(current)
            current = current.left
    
    def current(self):
        return self.__stack[-1]

    def next(self):
        current = self.__stack[-1].right
        self.__stack.pop()
        while current:
            self.__stack.append(current)
            current = current.left

    def hasNext(self):
        return True if self.__stack else False


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    start = time()

    iter = BSTIterator(root)

    while True:
        if not iter.hasNext():
            print()
            break
        print(iter.current().val, end=" ")
        iter.next()

    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")