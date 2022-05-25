import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    def get_signal(self, a, b):
        if a == b:
            return 0
        return -1 if a < b else 1
    
    def average(self, a, b):
        return (a + b) / 2
    
    def find_median(self, e: int, median: int, left: list, right: list):
        # left is maxheap
        # right is minheap
        signal = self.get_signal(len(left), len(right))
        if signal == 1:
            if e < median:
                right.append(left.pop(0))
                left.append(e)
                heapq.heapify(right)
                heapq._heapify_max(left)
            else:
                right.append(e)
                heapq.heapify(right)
            median = self.average(left[0], right[0])
        elif signal == 0:
            if e < median:
                left.append(e)
                heapq._heapify_max(left)
                median = left[0]
            else:
                right.append(e)
                heapq.heapify(right)
                median = right[0]
        elif signal == -1:
            if e < median:
                left.append(e)
                heapq._heapify_max(left)
            else:
                left.append(right.pop(0))
                right.append(e)
                heapq._heapify_max(left)
                heapq.heapify(right)
            median = self.average(left[0], right[0])
        return median
    
    def print_median(self, numbers, n):
        median = 0
        left = self.max_heap
        right = self.min_heap

        for i in range(n):
            median = self.find_median(numbers[i], median, left, right)
            print(median*1.0)

numbers = list(map(int, input().split(" ")))
finder = MedianFinder()
left, right = finder.max_heap, finder.min_heap
median = 0
for num in numbers:
    median = finder.find_median(num, median, left, right)
    print(median*1.0)

