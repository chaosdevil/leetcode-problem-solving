from ast import literal_eval
import heapq
import os

from typing import List
from time import time


class Solution:
    def furthestBuildingV1(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(pq, diff)
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            if bricks < 0:
                return i - 1
        return len(heights) - 1

    def furthestBuildingV2(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if len(pq) < ladders:
                    heapq.heappush(pq, diff)
                else:
                    br = diff
                    if len(pq) > 0 and pq[0] < diff:
                        br = heapq.heappop(pq)
                        heapq.heappush(pq, diff)
                    if bricks-br >= 0:
                        bricks -= br
                    else:
                        return i - 1
        return len(heights) - 1

    def furthestBuildingV3(self, heights: List[int], bricks: int, ladders: int) -> int:
        # min-heap
        pq = []
        
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            
            # if diff is <=0, it is just a jump-down
            if diff > 0:
                if ladders > 0:
                    ladders -= 1
                    heapq.heappush(pq, diff)
                    continue
                
                if pq and pq[0] < diff:
                    heapq.heappush(pq, diff)
                    bricks -= heapq.heappop(pq)
                else:
                    bricks -= diff
                
                if bricks < 0:
                    return i - 1
            
        return i


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/furthest_building_testcase.txt", "r") as file:
        heights = literal_eval(file.readline().strip())
        bricks = int(file.readline().strip())
        ladders = int(file.readline().strip())

    solution = Solution()

    start = time()
    print(solution.furthestBuildingV1(heights, bricks, ladders))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    start = time()
    print(solution.furthestBuildingV2(heights, bricks, ladders))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    start = time()
    print(solution.furthestBuildingV3(heights, bricks, ladders))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")