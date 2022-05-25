class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
    def __repr__(self):
        return "N({},{})".format(self.key, self.val)

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 100
        self.buf = [None] * self.cap

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        i = key % self.cap
        node = Node(key, value)

        if self.buf[i] is None: 
            self.buf[i] = node
            return
				
        head = self.buf[i] #collision occur
        while head:
            if head.key == key:
                head.val = value
                return
            prev = head
            head = head.next
        prev.next = node


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        i = key % self.cap

        if self.buf[i] is None:
            return -1

        head = self.buf[i]

        while head:
            if head.key == key:
                return head.val
            head = head.next

        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        i = key % self.cap

        if self.buf[i] is None:
            return

        head = self.buf[i]
        curr = head
        prev = None

        while curr:
            if curr.key == key:
                break
            prev = curr
            curr = curr.next

        if curr is None: # no such key in the list
            return

        if curr.key == head.key: #if first node is the node to be deleted
            self.buf[i] = head.next
        else:
            prev.next = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
