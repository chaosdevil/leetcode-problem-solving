from ast import literal_eval
import heapq
from time import time

class MedianFinder:

    def __init__(self):
        # left is maxheap
        self.left = []
        # right is minheap
        self.right = []
        self.median = 0

    def get_signal(self, a, b):
        if a == b:
            return 0
        return -1 if a < b else 1

    def average(self, a, b):
        return (a+b) / 2
    
    def addNum(self, num: int) -> None:
        signal = self.get_signal(len(self.left), len(self.right))
        if signal == 0:
            if num < self.median:
                self.left.append(num)
                heapq._heapify_max(self.left)
                self.median = self.left[0]
            else:
                self.right.append(num)
                heapq.heapify(self.right)
                self.median = self.right[0]
        elif signal == 1:
            if num < self.median:
                self.right.append(self.left.pop(0))
                self.left.append(num)
                heapq.heapify(self.right)
                heapq._heapify_max(self.left)
            else:
                self.right.append(num)
                heapq.heapify(self.right)
            self.median = self.average(self.left[0], self.right[0])
        elif signal == -1:
            if num < self.median:
                self.left.append(num)
                heapq._heapify_max(self.left)
            else:
                self.left.append(self.right.pop(0))
                self.right.append(num)
                heapq._heapify_max(self.left)
                heapq.heapify(self.right)
            self.median = self.average(self.left[0], self.right[0])
            
    def findMedian(self) -> float:
        return self.median

commands = literal_eval(input())
stream_data = literal_eval(input())

result = []

start = time()
for i in range(len(commands)):
    if commands[i] == "addNum":
        medianFinder.addNum(stream_data[i][0])
        result.append(None)
    elif commands[i] == "findMedian":
        result.append(medianFinder.findMedian())
    else:
        medianFinder = MedianFinder()
        result.append(None)
print(result)

print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

