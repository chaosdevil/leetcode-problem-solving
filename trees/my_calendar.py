class Node:
    def __init__(self, start, end, booked):
        self.start = start
        self.end = end
        self.booked = booked
        self.left = None
        self.right = None
        
class SegmentTree:
    def __init__(self, start, end):
        self.root = Node(start, end, False)
        self.current = self.root
    
    def modify(self, current, start, end, booked):
        if current.start == start and current.end == end:
            current.booked = booked
            return current.booked
        
        # if the duration is overlapping
        if start >= current.end or end <= current.start:
            return False
        
        mid = current.start + (current.end - current.start) // 2
        
        if not current.left:
            current.left = Node(current.start, mid, current.booked)
            current.right = Node(mid, current.end, current.booked)
            
        left_booked = self.modify(current.left, start, min(mid, end), booked)
        right_booked = self.modify(current.right, max(mid, start), end, booked)
        
        current.booked = left_booked or right_booked
        
        return left_booked or right_booked
    
    def query(self, current, start, end):
        if current.start == start and current.end == end:
            return not current.booked;
        
        if not current.left or not current.right:
            return not current.booked
        
        mid = current.start + (current.end-current.start) // 2
        
        if end <= mid:
            return self.query(current.left, start, end)
        if start >= mid:
            return self.query(current.right, start, end)
        
        return self.query(current.left, start, mid) & \
                self.query(current.right, mid, end)
        
class MyCalendar(object):
    def __init__(self):
        self.tree = SegmentTree(0, 1e9)

    def book(self, start, end):
        if self.tree.query(self.tree.current, start, end):
            return self.tree.modify(self.tree.current, start, end, True)
        return False
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)