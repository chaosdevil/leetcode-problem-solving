from ast import literal_eval
import os
import sys
from time import time
from typing import List

sys.setrecursionlimit(10**6)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # memoization
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        
        memo = dict()
        first = self.helper(n-1, cost, memo)
        second = self.helper(n-2, cost, memo)
        return min(first, second)
        
    def helper(self, n, cost, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]
        
        memo[n] = min(self.helper(n-1, cost, memo), self.helper(n-2, cost, memo)) + cost[n]
        
        return memo[n]
            

if __name__ == "__main__":

    with open(os.path.dirname(__file__) + "/min_cost_climbing_stairs_testcase.txt", "r") as file:
        cost = literal_eval(file.readline().strip())

    # cost = [1,100,1,1,1,100,1,1,100,1]
    
    start = time()
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
