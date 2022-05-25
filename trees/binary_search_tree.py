# Author : Sura Wankam

import sys
from time import time


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, arr):
        self.input: list = arr
        self.root = self.build_tree(self.input)

    def build_tree(self, arr):

        tree = None
        for data in arr:
            tree = self.insert_nodes(tree, data)

        return tree

    def insert_nodes(self, node, data):
        # plan : preorder traversal

        if node == None:
            return Node(data)
        else:
            temp = None
            if data <= node.data:
                temp = self.insert_nodes(node.left, data)
                node.left = temp
                temp.parent = node
            else:
                temp = self.insert_nodes(node.right, data)
                node.right = temp
                temp.parent = node

            return node

    def __str__(self):
        # inorder traversal
        node_list = self.inorder_tree_walk(self.root)
        return " ".join(list(map(str, node_list)))

    def inorder_tree_walk(self, root):
        # inorder tree walk using stack
        current = root
        stack = [current]
        current = current.left
        walk_result = []
        while True:
            if current == None and len(stack) != 0:
                pop = stack.pop()
                walk_result.append(pop.data)
                current = pop.right
            else:
                stack.append(current)
                current = current.left

            if current == None and len(stack) == 0:
                break

        return walk_result

    def search(self, target):
        result = self.tree_search(self.root, target)
        return f"{result.data} is found!" if result else f"{target.data} doesn't exist!"

    def tree_search(self, root, target):
        if root == None:
            return root

        if target == root.data:
            return root

        if target < root.data:
            return self.tree_search(root.left, target)
        return self.tree_search(root.right, target)

    def get_tree_minimum(self):
        return self.tree_minimum(self.root).data

    def get_tree_maximum(self):
        return self.tree_maximum(self.root).data

    def tree_minimum(self, root):
        current = root
        while current.left != None:
            current = current.left
        return current

    def tree_maximum(self, root):
        current = root
        while current.right != None:
            current = current.right
        return current

    def get_tree_successor(self, x):
        current = self.root
        while current is not None:
            if x < current.data:
                current = current.left
            elif x > current.data:
                current = current.right
            else:
                break
        successor = self.tree_successor(current)
        if successor:
            return f"Successor of {x} is {successor.data}"
        else:
            return f"There is no successor of {x}"

    def get_tree_predecessor(self, x):
        current = self.root
        while current is not None:
            if x < current.data:
                current = current.left
            elif x > current.data:
                current = current.right
            else:
                break
        predecessor = self.tree_predecessor(current)
        if predecessor:
            return f"Predecessor of {x} is {predecessor.data}"
        else:
            return f"There is no predecessor of {x}"

    def tree_successor(self, x: Node):
        # go to the leftmost of the right subtree,
        # it will be the successor
        if x.right is not None:
            return self.tree_minimum(x.right)
        successor = x.parent
        while successor is not None and x == successor.right:
            x = successor
            successor = successor.parent
        return successor

    def tree_predecessor(self, x: Node):
        # go to the rightmost of the left subtree
        # it will be the predecessor
        tree = self.inorder_tree_walk(self.root)
        predecessor = -sys.maxsize
        current = tree[0]
        for i in range(len(tree)):
            if current == x.data:
                break
            predecessor = current
            current = tree[i]

        predecessor_node = self.root
        if predecessor != -sys.maxsize:
            while predecessor_node.data != predecessor:
                if predecessor <= predecessor_node.data:
                    predecessor_node = predecessor_node.left
                else:
                    predecessor_node = predecessor_node.right
            return predecessor_node
        else:
            return None

    def insert(self, tree, z):
        y = None
        x = tree
        while x:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            tree = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def insert_recursive(self, tree, z, x, y=None):
        if not tree:
            return None

        if z.data < tree.data:
            self.insert_recursive(tree.left, z, tree.left, x)
            if not tree.left:
                tree.left = z
                return tree
        else:
            self.insert_recursive(tree.right, z, tree.right, x)
            if not tree.right:
                tree.right = z
                return tree
            
    def tree_insert(self, x):
        new_node = Node(x)
        self.insert_recursive(self.root, new_node, self.root)
        return " ".join(list(map(str, self.inorder_tree_walk(self.root))))

    def transplant(self, tree, u: Node, v: Node):
        if not u.parent:
            tree = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, z: Node):
        if not z.left:
            self.transplant(self.root, z, z.right)
        elif not z.right:
            self.transplant(self.root, z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent.data != z.data:
                self.transplant(self.root, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(self.root, z, y)
            y.left = z.left
            y.left.parent = y

    def tree_delete(self, x):
        # find x
        try:
            target = self.tree_search(self.root, x)
            self.delete(target)
            return " ".join(list(map(str, self.inorder_tree_walk(self.root))))
        except AttributeError:
            return f"{x} is not found!"

    def find_second_max(self):
        if self.root.right:
            current = self.root
            prev = None
            while current.right:
                prev = current
                current = current.right
                if not current.right and current.left:
                    if current.left.data > prev.data:
                        prev = current.left
                        current = prev

            return prev.data
        else:
            current = self.root.left
            prev = None
            while current:
                prev = current
                current = current.right
            return prev.data


if __name__ == "__main__":
    start = time()
    bt = BinarySearchTree([50, 10, 30, 43, 26, 33, 76, 66, 55, 12, 13, 16, 22, 11])
    print(bt.search(30))
    print(bt.get_tree_minimum())
    print(bt.get_tree_maximum())
    print(bt.get_tree_successor(55))
    print(bt.get_tree_predecessor(55))
    print(bt)
    print(bt.tree_delete(11))
    insert_list = [1,2,3,8,53,20,80,86,87]
    for i in insert_list:
        bt.tree_insert(i)
    print(bt)
    walks = bt.inorder_tree_walk(bt.root)
    print(walks)

    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
