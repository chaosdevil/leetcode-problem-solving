# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from time import time
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            heapq.heappush(self.pq, n)
            if len(self.pq) > self.k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    ops = ["KthLargest","add","add","add","add","add"]
    values = [[1,[]],[-3],[-2],[-4],[0],[4]]

    start = time()
    
    pq = None
    k = 0

    result = []

    for i in range(len(ops)):
        if ops[i] == "KthLargest":
            k = values[0][0]
            pq = values[0][1]
            for n in values[i][1]:
                heapq.heappush(pq, n)
                if len(pq) > k:
                    heapq.heappop(pq)
            result.append(None)
        else:
            heapq.heappush(pq, values[i][0])
            if len(pq) > k:
                heapq.heappop(pq)
            result.append(pq[0])
    
    print(result)
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")