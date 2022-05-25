from time import time

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        self.memoize_climbs(n, memo)
        return memo[n]

    def memoize_climbs(self, n, memo):
        if n <= 1:
            memo[n] = 1
            return memo[n]

        if n not in memo:
            memo[n] = self.memoize_climbs(n-1, memo) + self.memoize_climbs(n-2, memo)

        return memo[n]


start = time()
solution = Solution()
print(solution.climbStairs(10))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

