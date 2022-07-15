from ast import literal_eval
import heapq
import os
from time import time
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # plan : min heap
        total = 0
        pq = []
        for i in target:
            total += i
            heapq.heappush(pq, -i)
        
        flag = False
        while True:
            max_n = -1 * heapq.heappop(pq)
            total -= max_n
            if max_n == 1 or total == 1:
                flag = True
                break
            if max_n < total or total == 0 or max_n % total == 0:
                break
            max_n = max_n % total
            total += max_n
            heapq.heappush(pq, -max_n)
            
        return flag


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/construct_target_array_testcase.txt", "r") as file:
        target = literal_eval(file.readline().strip())

    # target = [13,3,4]

    solution = Solution()

    start = time()
    print(solution.isPossible(target))
    print(f"Time elaped : {(time() - start) * 1000} milliseconds")