class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.color = "black"
        self.value = value
    
    def __str__(self):
        return f"{self.value}"


class RedBlackTree:
    def __init__(self) -> None:
        self.root = None

    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            y.left = x
            x.parent = y
    
    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
            y.right = x
            x.parent = y

            
    def insert_node(self, val):
        pass