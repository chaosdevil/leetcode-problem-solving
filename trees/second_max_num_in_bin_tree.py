from binary_search_tree import BinarySearchTree

import random

# [1, 2, 3, 8, 10, 12, 13, 16, 20, 22, 26, 30, 33, 43, 50, 53, 55, 66, 76, 80, 86, 87]

# inp = list({random.randint(-1000, 1000) for _ in range(10)})
inp = [-953, -856, -823, 942, 752, 81, 117, 759, -610, 319]
print(inp)
bst = BinarySearchTree(inp)
print(bst.inorder_tree_walk(bst.root))
print(bst.find_second_max())