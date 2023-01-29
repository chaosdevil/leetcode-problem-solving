# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 04:12:12 2023

@author: yoksu
"""
from collections import defaultdict

class Node:
    def __init__(self, val, prev=None, after=None):
        self.val = val
        self.prev = prev
        self.next = after

class LinkedList:
    """Implementation of Doubly Linked List
        every operation takes only O(1)
    """
    def __init__(self):
        self.left = None
        self.right = None
        self.position_map = defaultdict(list)
        
    def append(self, val):
        # append to the last
        new_node = Node(val)
        if not self.left:
            self.left = new_node
            self.right = self.left
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = self.right.next
        self.position_map[val].append(new_node)
            
    def appendleft(self, val):
        # append to the first
        new_node = Node(val)
        if not self.left:
            self.left = new_node
            self.right = self.left
        else:
            self.left.prev = new_node
            new_node.next = self.left
            self.left = new_node
        self.position_map[val].append(new_node)
            
    def pop(self):
        # pop from the last
        val = self.right.prev.val
        temp = self.right.prev
        temp.next = None
        self.right = temp
        self.position_map.pop(val)
    
    def popleft(self):
        # pop the first
        val = self.left.next.val
        temp = self.left.next
        self.left = temp
        self.left.prev = None
        self.position_map.pop(val)
        
    def remove(self, val):
        # remove from anywhere
        node = self.position_map[val][0]
        if node.prev and node.next:
            left = node.prev
            right = node.next
            left.next = right
            right.prev = left
        else:
            if not node.prev:
                self.popleft()
            elif not node.next:
                self.pop()
            
    def get_last(self):
        return self.right.val
    
    def get_first(self):
        return self.left.val
    
    def traverse(self):
        curr = self.left
        print("Traverse from first to last :", end=" ")
        while curr:
            print(f"{curr.val:5d}", end=" ")
            curr = curr.next
        print()
        
        curr = self.right
        print("Traverse from last to first :", end=" ")
        while curr:
            print(f"{curr.val:5d}", end=" ")
            curr = curr.prev
        print()
        
    
ll = LinkedList()
ll.append(4)
ll.append(0)
ll.append(1)
ll.append(7)
ll.append(3)
ll.append(12)
ll.appendleft(11)
ll.append(13)
ll.append(15)
ll.appendleft(-10)
ll.append(3)

print("Popped")
ll.remove(1)
ll.remove(12)
ll.remove(-10)
ll.remove(3)
ll.pop()
print(ll.get_first())
print(ll.get_last())
ll.traverse()