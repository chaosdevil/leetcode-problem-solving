from typing import List
from time import time

import random
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # plan : max heap
        minheap = []
        for i in range(len(nums)):
            if len(minheap) < k:
               heapq.heappush(minheap, nums[i])
            else:
                heapq.heappushpop(minheap, nums[i])

        return minheap


start = time()
solution = Solution()
inp = [random.randint(-1e6, 1e6) for _ in range(1000)]
k = 300
print(solution.maxSubsequence(inp, k))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")        
