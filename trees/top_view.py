from build_bst import *


def vertical_traversal(root: Node, depths: dict):
    # plan : breadth-first search
    level = 0

    # # to_visit queue
    to_visit = []

    # while to_visit:
    #     node, level = to_visit[0]
    #     to_visit = to_visit[1:]

    #     depths[level] = node.info
    #     if node.left and level-1 not in depths.keys():
    #         to_visit.append((node.left, level-1))
    #     if node.right and level+1 not in depths.keys():
    #         to_visit.append((node.right, level+1))


    depths[level] = [root.info]
    to_visit.extend([(root, level)])

    while to_visit:
        node, level = to_visit.pop(0)

        if node:
            if level in depths.keys():
                depths[level].append(node.info)
            else:
                depths[level] = [node.info]
            to_visit.extend([(node.left, level-1), (node.right, level+1)])



def top_view(root):
    # plan : vertical traversal
    depths = dict()
    vertical_traversal(root, depths)

    min_left, max_right = min(depths.keys()), max(depths.keys())

    for i in range(min_left, max_right+1):
        print(depths[i][0], end=" ")


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split(" ")))
    tree = BinarySearchTree()
    for i in range(n):
        tree.create(inputs[i])

    top_view(tree.root)
