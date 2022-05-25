from time import time


class Node:
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth
        self.left = None
        self.right = None


def swap_nodes(root: Node, k):
    current = root
    queue = [current]

    while queue:
        front = queue.pop(0)

        if front.depth % k == 0:
            temp = front.left
            front.left = front.right
            front.right = temp
        
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)

def inorder_print(root: Node):
    current = root
    stack = []

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        top = stack.pop()
        print(top.data, end=" ")

        current = top.right

def print_nodes(root, k):
    swap_nodes(root, k)
    inorder_print(root)
    print()


if __name__ == "__main__":
    start = time()
    with open("trees\\testcases\\swap_nodes_input.txt", "r") as file:
        n = int(file.readline().strip())

        root = Node(1, 1)
        current = root
        queue = [current]

        while n > 0:
            current = queue.pop(0)
            left_data, right_data = list(map(int, file.readline().strip().split(" ")))

            if left_data != -1:
                current.left = Node(left_data, current.depth+1)
            if right_data != -1:
                current.right = Node(right_data, current.depth+1)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            n -= 1

        t = int(file.readline().strip())
        while t > 0:
            k = int(file.readline().strip())
            print_nodes(root, k)
            t -= 1

    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    # n = int(input().strip())
    # root = Node(1, 1)
    # current = root
    # # define queue
    # queue = [current]

    # while n > 0:
    #     current = queue.pop(0)

    #     # receive pair inputs
    #     left_data, right_data = list(map(int, input().split(" ")))

    #     if left_data != -1:
    #         current.left = Node(left_data, current.depth+1)
    #     if right_data != -1:
    #         current.right = Node(right_data, current.depth+1)

    #     if current.left:
    #         queue.append(current.left)
    #     if current.right:
    #         queue.append(current.right)
    #     n -= 1

    # t = int(input())
    # while t > 0:
    #     k = int(input())
    #     print_nodes(root, k)
    #     t -= 1
